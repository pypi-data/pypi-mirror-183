import warnings
import numpy as np

PX_PER_CM = 28.45274


class plot:
    def __init__(self):
        # Initialize the settings.
        self.xlist = []         # list of x-axis vectors
        self.ylist = []         # list of y-axis vectors
        self.colors = []        # list of colors
        self.opacities = []     # list of opacities
        self.width = 8.636      # 3.4 in
        self.height = 5.337     # 2.10 in
        self.xpad = False       # use padding on x axis
        self.ypad = True        # use padding on y axis
        self.xmin = None        # x-axis minimum
        self.xmax = None        # x-axis maximum
        self.ymin = None        # y-axis minimum
        self.ymax = None        # y-axis maximum
        self.fontsize = 9.0     # font size [pt]
        self.xlabel = None      # x-axis label
        self.ylabel = None      # y-axis label
        self.xaxis = True       # flag to show x axis
        self.yaxis = True       # flag to show y axis
        self.xgrid = True       # flag to show x grid
        self.ygrid = True       # flag to show y grid
        self.xsubgrid = True    # flag to show x sub-grid
        self.ysubgrid = True    # flag to show y sub-grid
        self.xtick = True       # flag to show x ticks
        self.ytick = True       # flag to show y ticks
        self.simp = True        # flag to simplify curve
        self.xlog = False       # flag to use log scaling on x axis
        self.ylog = False       # flag to use log scaling on y axis

    def add(self, x, y, color=0x000000, opacity=1.0):
        # Check the inputs.
        if not isinstance(x, np.ndarray):
            raise TypeError("Input x must be an np.ndarray!")
        if not isinstance(y, np.ndarray):
            raise TypeError("Input y must be an np.ndarray!")
        if x.shape[0] != y.shape[0]:
            raise ValueError("Inputs x and y must be the same length!")
        if x.ndim == 2 and y.ndim == 2:
            if x.shape[1] != y.shape[1]:
                raise ValueError("Inputs x and y must have " +
                        "the same number of columns!")
        if x.ndim > 2 or y.ndim > 2:
            raise TypeError("Inputs x and y must be vectors or matrices!")

        # Append the data set to the lists.
        self.xlist.append(x)
        self.ylist.append(y)
        self.colors.append(color)
        self.opacities.append(opacity)

    def render(self, file_name, standalone=True):
        if not self.xlist or not self.ylist:
            raise ValueError("No x and y data has been provided!")

        # ---------------
        # Scale the data.
        # ---------------

        # Get the number of curves.
        J = len(self.xlist)

        # Initialize the minimums and maximums.
        x_min = np.inf
        x_max = -np.inf
        y_min = np.inf
        y_max = -np.inf
        for j in range(J):
            # Get extrema of this path, ignoring NaNs.
            xa = np.nanmin(self.xlist[j])
            xb = np.nanmax(self.xlist[j])
            ya = np.nanmin(self.ylist[j])
            yb = np.nanmax(self.ylist[j])

            # Enlarge minimums and maximums.
            if xa < x_min:
                x_min = xa
            if xb > x_max:
                x_max = xb
            if ya < y_min:
                y_min = ya
            if yb > y_max:
                y_max = yb

        # Override minimums and maximums.
        do_clip = False
        if self.xmin is not None:
            if self.xmin > x_min:
                do_clip = True
            x_min = self.xmin
        if self.xmax is not None:
            if self.xmax < x_max:
                do_clip = True
            x_max = self.xmax
        if self.ymin is not None:
            if self.ymin > y_min:
                do_clip = True
            y_min = self.ymin
        if self.ymax is not None:
            if self.ymax < y_max:
                do_clip = True
            y_max = self.ymax
        # Past this point, x and y values can be in logarithmic scaling.

        # Determine where the grid lines will be.
        if self.xlog:
            x_min = np.log10(x_min)
            x_max = np.log10(x_max)
            x_grids, x_sub_grids, x_min_pad, x_max_pad = \
                    grid_logarithmic(x_min, x_max)
        else:
            x_grids, x_sub_grids, x_min_pad, x_max_pad = \
                    grid_linear(x_min, x_max)
        if self.ylog:
            y_min = np.log10(y_min)
            y_max = np.log10(y_max)
            y_grids, y_sub_grids, y_min_pad, y_max_pad = \
                    grid_logarithmic(y_min, y_max)
        else:
            y_grids, y_sub_grids, y_min_pad, y_max_pad = \
                    grid_linear(y_min, y_max)

        # Add requested padding.
        if self.xpad:
            x_min = x_min_pad
            x_max = x_max_pad
        if self.ypad:
            y_min = y_min_pad
            y_max = y_max_pad

        # Define the box width and height.
        W_box = self.width
        H_box = self.height

        # Get the length for text.
        L_text = (self.fontsize*1.6)/PX_PER_CM

        # Subtract from box for labels.
        if self.xlabel is not None:
            H_box -= L_text # space for bottom x label
        if self.ylabel is not None:
            W_box -= L_text # space for left-side y label
        if self.xtick:
            W_box -= L_text*0.4 # space for right-side numbers

        # Get the arrow-head length.
        head_len = 0.013*self.fontsize

        # Subtract from box for arrow heads.
        if self.xaxis:
            H_box -= 2*head_len
        if self.yaxis:
            W_box -= 2*head_len

        # Get the data scaling factors.
        x_range = x_max - x_min
        x_scale = W_box/x_range
        y_range = y_max - y_min
        y_scale = H_box/y_range

        # Determine where the x and y axes will be.
        if self.xaxis:
            if self.ylog:
                Y_axis = 0.0
            else:
                Y_axis = (0 - y_min)*y_scale
                Y_axis = 0 if Y_axis < 0 else \
                        H_box if Y_axis > H_box else Y_axis
        if self.yaxis:
            if self.xlog:
                X_axis = 0.0
            else:
                X_axis = (0 - x_min)*x_scale
                X_axis = 0 if X_axis < 0 else \
                        W_box if X_axis > W_box else X_axis

        # -----------------------
        # Write the data to file.
        # -----------------------

        # Open the output file.
        fid = open(file_name, "w")

        # Open the standalone TikZ script.
        if standalone:
            tikz_open(fid)

        # Define the font size.
        tikz_fontsize(fid, self.fontsize)

        # Define the colors.
        tikz_colors(fid, self.colors)

        # Draw the grids.
        if self.xsubgrid:
            if self.xgrid:
                x_sub_grids = np.delete(x_sub_grids,
                        np.in1d(x_sub_grids, x_grids))
            X = (x_sub_grids - x_min)*x_scale
            tikz_xgrid(fid, X, H_box, sub=True)
        if self.ysubgrid:
            if self.ygrid:
                y_sub_grids = np.delete(y_sub_grids,
                        np.in1d(y_sub_grids, y_grids))
            Y = (y_sub_grids - y_min)*y_scale
            tikz_ygrid(fid, Y, W_box, sub=True)
        if self.xgrid:
            X = (x_grids - x_min)*x_scale
            if self.yaxis:
                X = np.delete(X, np.where(X == X_axis)[0])
            tikz_xgrid(fid, X, H_box)
        if self.ygrid:
            Y = (y_grids - y_min)*y_scale
            if self.xaxis:
                Y = np.delete(Y, np.where(Y == Y_axis)[0])
            tikz_ygrid(fid, Y, W_box)

        # Draw the paths.
        points = 0
        if do_clip:
            tikz_begin_clip(fid, W_box, H_box)
        for j in range(J):
            X = (self.xlist[j] - x_min)*x_scale
            Y = (self.ylist[j] - y_min)*y_scale
            if self.simp:
                X, Y = xchunk(X, Y, W_box)
            if self.opacities[j] == 1:
                fmt = f"C{j}"
            else:
                op = self.opacities[j]
                fmt = f"C{j}, opacity={op:0.3g}"
            points += tikz_path(fid, X, Y, fmt)
        if do_clip:
            tikz_end_clip(fid)
        if points > 35000:
            warnings.warn("This many points might exceed TeX capacity.")

        # Draw the axes.
        if self.xaxis:
            tikz_line(fid, -head_len, Y_axis, W_box + head_len, Y_axis, "->")
        if self.yaxis:
            tikz_line(fid, X_axis, -head_len, X_axis, H_box + head_len, "->")

        # Write the ticks.
        if self.xtick and self.xaxis:
            X = (x_grids - x_min)*x_scale
            if Y_axis > L_text:
                fmt = "below, draw opacity=0.5"
            else:
                fmt = "above, draw opacity=0.5"
            for n in range(len(X)):
                if self.yaxis and np.abs(X[n] - X_axis) < W_box*1e-6:
                    continue
                tikz_line(fid, X[n], Y_axis - 0.005*W_box,
                        X[n], Y_axis + 0.005*W_box)
                txt = f"\\contour{{white}}{{{x_grids[n]:g}}}"
                tikz_text(fid, X[n], Y_axis, txt, fmt)
        if self.ytick and self.yaxis:
            Y = (y_grids - y_min)*y_scale
            if X_axis > L_text:
                fmt = "left, draw opacity=0.5"
            else:
                fmt = "right, draw opacity=0.5"
            for n in range(len(Y)):
                if self.xaxis and np.abs(Y[n] - Y_axis) < H_box*1e-6:
                    continue
                tikz_line(fid, X_axis - 0.005*W_box, Y[n],
                        X_axis + 0.005*W_box, Y[n])
                txt = f"\\contour{{white}}{{{y_grids[n]:g}}}"
                tikz_text(fid, X_axis, Y[n], txt, fmt)

        # Write the labels.
        if self.xlabel is not None:
            Y = -L_text - head_len if self.yaxis else -L_text
            tikz_text(fid, W_box/2, Y, self.xlabel, "above")
        if self.ylabel is not None:
            X = -L_text - head_len if self.xaxis else -L_text
            tikz_text(fid, X, H_box/2, self.ylabel, "below, rotate=90")

        # Close the standalone TikZ script.
        if standalone:
            tikz_close(fid)

        # Close the output file.
        fid.close()


def tikz_open(fid):
    fid.write("\\documentclass{standalone}")
    fid.write("\n\\usepackage{xcolor}")
    fid.write("\n\\usepackage{tikz}")
    fid.write("\n\\usepackage[pdftex, outline]{contour}")
    fid.write("\n\\contourlength{0.8pt}")
    fid.write("\n\\begin{document}")
    fid.write("\n\\begin{tikzpicture}")


def tikz_fontsize(fid, fs):
    if fs != 10:
        fsplus = round(fs*1.2, 1)
        fid.write(f"\n\\fontsize{{{fs}}}{{{fsplus}}}\\selectfont")


def tikz_colors(fid, colors):
    for n in range(len(colors)):
        C = int(colors[n])
        rd = ((C & 0xff0000) >> 16)
        gn = ((C & 0x00ff00) >> 8)
        bl = (C & 0x0000ff)
        fid.write(f"\n\definecolor{{C{n}}}{{RGB}}{{{rd},{gn},{bl}}}")
    fid.write("\n")


def tikz_xgrid(fid, x_list, y_max, sub=False):
    if sub:
        fid.write("\n\\draw[very thin, lightgray!15]")
    else:
        fid.write("\n\\draw[very thin, lightgray!45]")
    for x in x_list:
        fid.write(f"\n    ({x:0.3f},0) -- ({x:0.3f},{y_max:0.3f})")
    fid.write(";")


def tikz_ygrid(fid, y_list, x_max, sub=False):
    if sub:
        fid.write("\n\\draw[very thin, lightgray!15]")
    else:
        fid.write("\n\\draw[very thin, lightgray!45]")
    for y in y_list:
        fid.write(f"\n    (0,{y:0.3f}) -- ({x_max:0.3f},{y:0.3f})")
    fid.write(";")


def tikz_begin_clip(fid, x_max, y_max):
    fid.write("\n\\begin{scope}")
    fid.write(f"\n\\clip (0,0) rectangle ({x_max:0.3f},{y_max:0.3f});")


def tikz_end_clip(fid):
    fid.write("\n\\end{scope}")


def tikz_line(fid, xa, ya, xb, yb, fmt=None):
    # Draw the line.
    fid.write("\n\\draw")
    if fmt is not None:
        fid.write(f"[{fmt}]")
    fid.write(f" ({xa:0.4f},{ya:0.4f}) --")
    fid.write(f" ({xb:0.4f},{yb:0.4f});")


def tikz_path(fid, x, y, fmt=None):

    def path1d(fid, x, y, fmt=None):
        # Begin the drawing command.
        fid.write("\n\\draw")
        fid.write(f"[line cap=round, line join=round")
        if fmt is not None:
            fid.write(f", {fmt}")
        fid.write("]")

        # Write the coordinates.
        is_start = True
        points = 0
        for n in range(len(x)):
            if np.isnan(x[n]) or np.isnan(y[n]):
                is_start = True
                continue
            if points % 4 == 0:
                fid.write("\n   ")
            if is_start:
                fid.write(f" ({x[n]:0.4f},{y[n]:0.4f})")
                is_start = False
            else:
                fid.write(f" -- ({x[n]:0.4f},{y[n]:0.4f})")
            points += 1

        # End the drawing command.
        fid.write(";")

        return points

    # Draw each column as a separate path.
    points = 0
    if x.ndim == 2 and y.ndim == 2:
        for c in range(x.shape[1]):
            points += path1d(fid, x[:, c], y[:, c], fmt)
    elif x.ndim == 1 and y.ndim == 2:
        for c in range(y.shape[1]):
            points += path1d(fid, x, y[:, c], fmt)
    elif x.ndim == 2 and y.ndim == 1:
        for c in range(x.shape[1]):
            points += path1d(fid, x[:, c], y, fmt)
    else:
        points = path1d(fid, x, y, fmt)

    return points


def tikz_text(fid, x, y, txt, fmt=None):
    if fmt is None:
        fid.write(f"\n\\node at ({x:0.3f},{y:0.3f}) {{{txt}}};")
    else:
        fid.write(f"\n\\node[{fmt}] at ({x:0.3f},{y:0.3f}) {{{txt}}};")


def tikz_close(fid):
    fid.write("\n\\end{tikzpicture}")
    fid.write("\n\\end{document}")


def grid_linear(x_min, x_max, fewer=None):

    # Default fewer.
    if fewer is None:
        fewer = False
    if fewer:
        cnt_min = 4
    else:
        cnt_min = 6

    # Get the normalized range.  Every range will map to [1,10).
    x_range = x_max - x_min
    if x_range == 0:
        grids = [x_min - 1e-15, x_max + 1e-15]
        sub_grids = []
        return grids, sub_grids
    base = 10**np.floor(np.log10(x_range))
    normalized_range = x_range/base # [1, 10)

    # Choose a nice step and sub-step based on the normalized range.
    step_sizes =     [2.0, 1.5, 1.0, 0.8, 0.5, 0.4, 0.30, 0.20]
    sub_step_sizes = [0.5, 0.5, 0.2, 0.2, 0.1, 0.1, 0.10, 0.05]
    for n_step in range(len(step_sizes)):
        grid_cnt = normalized_range/step_sizes[n_step] + 1
        if grid_cnt >= cnt_min:
            step_size = step_sizes[n_step]*base
            sub_step_size = sub_step_sizes[n_step]*base
            break

    # Get the nice extrema.  The major grid lines may go to the very edge of the
    # minimum and maximum.  The minor grid lines may not.
    if np.mod(x_min, step_size) == 0:
        grid_min = x_min
    else:
        grid_min = (np.floor(x_min/step_size) + 1)*step_size
    if np.mod(x_max, step_size) == 0:
        grid_max = x_max
    else:
        grid_max =  (np.ceil(x_max/step_size) - 1)*step_size
    sub_grid_min = (np.floor(x_min/sub_step_size) + 1)*sub_step_size
    sub_grid_max =  (np.ceil(x_max/sub_step_size) - 1)*sub_step_size

    # Build the grids arrays.
    N = round((grid_max - grid_min)/step_size) + 1
    grids = np.arange(N)*step_size + grid_min
    N = round((sub_grid_max - sub_grid_min)/sub_step_size) + 1
    sub_grids = np.arange(N)*sub_step_size + sub_grid_min

    # Make sure the grid arrays do not have numerical residuals.
    base = 10**(np.floor(np.log10(grid_max - grid_min)) - 3)
    grids = np.round(grids/base)*base
    sub_base = 10**(np.floor(np.log10(sub_grid_max - sub_grid_min)) - 3)
    sub_grids = np.round(sub_grids/sub_base)*sub_base

    # Get padded min and max.
    if sub_grids[0] > x_min:
        x_min_pad = sub_grids[0] - sub_step_size
    else:
        x_min_pad = x_min
    if sub_grids[-1] < x_max:
        x_max_pad = sub_grids[-1] + sub_step_size
    else:
        x_max_pad = x_max

    return grids, sub_grids, x_min_pad, x_max_pad


def grid_logarithmic(e_min, e_max):
    """
    Returns values in logarithmic scaling.
    """

    # Get the first log grid line after x_min.
    e_min_base = np.floor(e_min)

    # Get the last log grid line before x_max.
    e_max_base = np.floor(e_max)

    # Build grid lines array.
    if e_min_base == e_min:
        e_min_grid = int(e_min_base)
    else:
        e_min_grid = int(e_min_base + 1)
    e_max_grid = int(e_max_base + 1)
    grids = np.arange(e_min_grid, e_max_grid)

    # Get inner sub-grid limits.
    rel_sub_grid = np.ceil(10.0*(e_min - e_min_base))/10.0
    e_min_subgrid = round(rel_sub_grid + e_min_base, 1)
    rel_sub_grid = np.floor(10.0*(e_max - e_max_base))/10.0
    e_max_subgrid = round(rel_sub_grid + e_max_base, 1)

    # Build sub-grid lines array.
    N_subs = int((e_max_subgrid - e_min_subgrid)*10) + 1
    sub_grids = (np.arange(N_subs) + round(e_min*10))*0.1

    # Get padded min and max.
    if sub_grids[0] > e_min:
        rel_sub_grid = np.floor(10.0*(e_min - e_min_base))/10.0
        e_min_pad = round(rel_sub_grid + e_min_base, 1)
    else:
        e_min_pad = e_min
    if sub_grids[-1] < e_max:
        rel_sub_grid = np.ceil(10.0*(e_max - e_max_base))/10.0
        e_max_pad = round(rel_sub_grid + e_max_base, 1)
    else:
        e_max_pad = e_max

    return grids, sub_grids, e_min_pad, e_max_pad


def xchunk(x, y, width):
    """
    Simplify the x and y data set by uniform index chunking along the x axis.
    """

    def xchunk1d(x, y, nn):
        # Allocate memory for new path.
        chunks = len(nn) - 1
        xc = np.zeros(2*chunks)
        yc = np.zeros(2*chunks)

        # For each chunk, store the min and max.
        for n_chunk in range(chunks):
            na = nn[n_chunk]
            nb = nn[n_chunk + 1]
            n_min = np.argmin(y[na:nb]) + na
            n_max = np.argmax(y[na:nb]) + na
            if n_min < n_max:
                xc[2*n_chunk] = x[n_min]
                yc[2*n_chunk] = y[n_min]
                xc[2*n_chunk + 1] = x[n_max]
                yc[2*n_chunk + 1] = y[n_max]
            else:
                xc[2*n_chunk] = x[n_max]
                yc[2*n_chunk] = y[n_max]
                xc[2*n_chunk + 1] = x[n_min]
                yc[2*n_chunk + 1] = y[n_min]

        return xc, yc

    # Get the number of points.
    K = x.shape[0]

    # Get the number of chunks.
    chunks = min(K, round(width*120))
    if chunks < round(width*120):
        return x, y

    # Get the array of chunk indices.
    nn = np.round(np.arange(chunks + 1)/chunks*K).astype(int)

    # Initialize the new arrays.
    if x.ndim == 2 and y.ndim == 2:
        cols = x.shape[1]
        xc = np.zeros((2*chunks, cols))
        yc = np.zeros((2*chunks, cols))
        for c in range(cols):
            xc[:, c], yc[:, c] = xchunk1d(x[:, c], y[:, c], nn)
    elif x.ndim == 1 and y.ndim == 2:
        cols = y.shape[1]
        xc = np.zeros((2*chunks, cols))
        yc = np.zeros((2*chunks, cols))
        for c in range(cols):
            xc[:, c], yc[:, c] = xchunk1d(x, y[:, c], nn)
    elif x.ndim == 2 and y.ndim == 1:
        cols = x.shape[1]
        xc = np.zeros((2*chunks, cols))
        yc = np.zeros((2*chunks, cols))
        for c in range(cols):
            xc[:, c], yc[:, c] = xchunk1d(x[:, c], y, nn)
    else:
        xc = np.zeros(2*chunks)
        yc = np.zeros(2*chunks)
        xc, yc = xchunk1d(x, y, nn)

    return xc, yc
