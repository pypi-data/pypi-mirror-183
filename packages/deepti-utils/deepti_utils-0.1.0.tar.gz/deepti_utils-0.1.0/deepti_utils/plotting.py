import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

# Plotting parameters
# PRL Font preference: computer modern roman (cmr), medium weight (m), normal shape
cm_in_inch = 2.54
# column size is 8.6 cm
prl_col_size = 8.6 / cm_in_inch
pnas_col_size = 8.7 / cm_in_inch
slide_width = 11.5
half_slide_width = 5.67
aspect_ratio = 5/7

params_dict = {}
params_dict['prl'] = {
    'backend': 'pdf',
    'savefig.format': 'pdf',
    'text.usetex': True,
    'font.size': 7,

    'figure.figsize': [1.0 * prl_col_size, aspect_ratio * 1.0 * prl_col_size],
    'figure.facecolor': 'white',

    'axes.grid': False,
    'axes.edgecolor': 'black',
    'axes.facecolor': 'white',

    'axes.titlesize': 8.0,
    'axes.titlepad': 5,
    'axes.labelsize': 8,
    'legend.fontsize': 6.5,
    'xtick.labelsize': 6.5,
    'ytick.labelsize': 6.5,
    'axes.linewidth': 0.75,

    'xtick.top': False,
    'xtick.bottom': True,
    'xtick.direction': 'out',
    'xtick.minor.size': 2,
    'xtick.minor.width': 0.5,
    'xtick.major.pad': 2,
    'xtick.major.size': 4,
    'xtick.major.width': 1,

    'ytick.left': True,
    'ytick.right': False,
    'ytick.direction': 'out',
    'ytick.minor.size': 2,
    'ytick.minor.width': 0.5,
    'ytick.major.pad': 2,
    'ytick.major.size': 4,
    'ytick.major.width': 1,

    'lines.linewidth': 1
}
params_dict['pnas'] = {
    'backend': 'pdf',
    'savefig.format': 'pdf',
    'text.usetex': True,
    'font.size': 8,

    'figure.figsize': [1.0 * pnas_col_size, aspect_ratio * 1.0 * pnas_col_size],
    'figure.facecolor': 'white',

    'axes.grid': False,
    'axes.edgecolor': 'black',
    'axes.facecolor': 'white',

    'axes.titlesize': 8.0,
    'axes.labelsize': 8,
    'legend.fontsize': 6.5,
    'xtick.labelsize': 6.5,
    'ytick.labelsize': 6.5,
    'axes.linewidth': 0.8,

    'xtick.top': False,
    'xtick.bottom': True,
    'xtick.direction': 'in',
    'xtick.minor.size': 1.5,
    'xtick.minor.width': 0.6,
    'xtick.major.pad': 2,
    'xtick.major.size': 3,
    'xtick.major.width': 0.8,

    'ytick.left': True,
    'ytick.right': False,
    'ytick.direction': 'in',
    'ytick.minor.size': 1.5,
    'ytick.minor.width': 0.6,
    'ytick.major.pad': 2,
    'ytick.major.size': 3,
    'ytick.major.width': 0.8,

    'lines.linewidth': 1.6
}
params_dict['poster'] = {'axes.edgecolor': 'black',
                 'axes.facecolor': 'white',
                 'axes.grid': False,
                 'axes.titlesize': 24,
                 'axes.titlepad': 12,
                 'axes.labelsize': 24,
                 'legend.fontsize': 20,
                 'text.usetex': True,
                 'xtick.labelsize': 20,
                 'ytick.labelsize': 20,
                 'figure.figsize': [12.6 / cm_in_inch, 12.6 / cm_in_inch],
                 'font.family': 'serif',
                 # 'font.serif' : ["Latin Modern Roman"],
                 'mathtext.fontset': 'cm',
                 'xtick.bottom': True,
                 'xtick.top': False,
                 'xtick.direction': 'out',
                 'xtick.major.pad': 3,
                 'xtick.major.size': 4,
                 'xtick.minor.bottom': False,
                 'xtick.major.width': 1.0,
                 'ytick.left': True,
                 'ytick.right': False,
                 'ytick.direction': 'out',
                 'ytick.major.pad': 3,
                 'ytick.major.size': 4,
                 'ytick.major.width': 1.0,
                 'ytick.minor.right': False,
                 'ytick.minor.left': False,
                 'lines.linewidth': 2}

params_dict['pres'] = {'axes.edgecolor': 'black',
                  'axes.facecolor':'white',
                  'axes.grid': False,
                  'axes.linewidth': 0.5,
                  'backend': 'ps',
                  'savefig.format': 'pdf',
                  'axes.titlesize': 24,
                  'axes.labelsize': 20,
                  'legend.fontsize': 20,
                  'xtick.labelsize': 18,
                  'ytick.labelsize': 18,
                  'text.usetex': True,
                  'figure.figsize': [half_slide_width, half_slide_width * aspect_ratio],
                  'font.family': 'sans-serif',
                  #'mathtext.fontset': 'cm',
                  'xtick.bottom':True,
                  'xtick.top': False,
                  'xtick.direction': 'out',
                  'xtick.major.pad': 3,
                  'xtick.major.size': 3,
                  'xtick.minor.bottom': False,
                  'xtick.major.width': 0.2,

                  'ytick.left':True,
                  'ytick.right':False,
                  'ytick.direction':'out',
                  'ytick.major.pad': 3,
                  'ytick.major.size': 3,
                  'ytick.major.width': 0.2,
                  'ytick.minor.right':False,
                  'lines.linewidth':2}

params_dict['default'] = {'axes.edgecolor': 'black',
                  'axes.facecolor':'white',
                  'axes.grid': False,
                  'axes.linewidth': 0.5,
                  'backend': 'ps',
                  'savefig.format': 'ps',
                  'axes.titlesize': 11,
                  'axes.labelsize': 9,
                  'legend.fontsize': 9,
                  'xtick.labelsize': 8,
                  'ytick.labelsize': 8,
                  'text.usetex': True,
                  'figure.figsize': [7, 5],
                  'font.family': 'sans-serif',
                  #'mathtext.fontset': 'cm',
                  'xtick.bottom':True,
                  'xtick.top': False,
                  'xtick.direction': 'out',
                  'xtick.major.pad': 3,
                  'xtick.major.size': 3,
                  'xtick.minor.bottom': False,
                  'xtick.major.width': 0.2,

                  'ytick.left':True,
                  'ytick.right':False,
                  'ytick.direction':'out',
                  'ytick.major.pad': 3,
                  'ytick.major.size': 3,
                  'ytick.major.width': 0.2,
                  'ytick.minor.right':False,
                  'lines.linewidth':2}

def update_plotting_params(style):
    """ Update matplotlib's rcParams to one of the following styles: 'PRL', 'PNAS', 'pres'
    or 'poster'. """
    if style in params_dict.keys():
        plt.rcParams.update(params_dict[style])
    else:
        plt.rcParams.update(params_dict['default'])

def draw_power_law_triangle(alpha, x0, width, orientation, base=10,
                            x0_logscale=True, label=None,
                            label_padding=0.1, text_args={}, ax=None,
                            **kwargs):
    """Draw a triangle showing the best-fit power-law on a log-log scale.

    Parameters
    ----------
    alpha : float
        the power-law slope being demonstrated
    x0 : (2,) array_like
        the "left tip" of the power law triangle, where the hypotenuse starts
        (in log units)
    width : float
        horizontal size in number of major log ticks (default base-10)
    orientation : string
        'up' or 'down', control which way the triangle's right angle "points"
    base : float
        scale "width" for non-base 10
    ax : mpl.axes.Axes, optional

    Returns
    -------
    corner : (2,) np.array
        coordinates of the right-angled corhow to get text outline of the
        triangle
    """
    if x0_logscale:
        x0, y0 = [base**x for x in x0]
    else:
        x0, y0 = x0
    if ax is None:
        ax = plt.gca()
    x1 = x0*base**width
    y1 = y0*(x1/x0)**alpha
    ax.plot([x0, x1], [y0, y1], 'k')
    if (alpha >= 0 and orientation == 'up') \
            or (alpha < 0 and orientation == 'down'):
        ax.plot([x0, x1], [y1, y1], 'k')
        ax.plot([x0, x0], [y0, y1], 'k')
        # plt.plot lines have nice rounded caps
        # plt.hlines(y1, x0, x1, **kwargs)
        # plt.vlines(x0, y0, y1, **kwargs)
        corner = [x0, y1]
    elif (alpha >= 0 and orientation == 'down') \
            or (alpha < 0 and orientation == 'up'):
        ax.plot([x0, x1], [y0, y0], 'k')
        ax.plot([x1, x1], [y0, y1], 'k')
        # plt.hlines(y0, x0, x1, **kwargs)
        # plt.vlines(x1, y0, y1, **kwargs)
        corner = [x1, y0]
    else:
        raise ValueError(r"Need $\alpha\in\mathbb{R} and orientation\in{'up', "
                         r"'down'}")
    if label is not None:
        xlabel = x0*base**(width/2)
        if orientation == 'up':
            ylabel = y1*base**label_padding
        else:
            ylabel = y0*base**(-label_padding)
        ax.text(xlabel, ylabel, label, horizontalalignment='center',
                verticalalignment='center', **text_args)
    return corner



