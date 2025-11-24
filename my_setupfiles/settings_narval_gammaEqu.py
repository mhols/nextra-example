"""
Global parameters for the datareduction pipeline
Normally you should not change these values in this file directly
Rather create a new setting_xxxx.py module in which you import

from nextra.setting_reference.py import kwargs as kwargs_xxxx

You then edit the keys of this dictionary for you specific project, e.g.

kwargs_xxxx['SETTING_ID'] = 'Moon'

Alternatively you may copy this module as a template and adapt it
"""
import os
import numpy as np
from dotenv import load_dotenv

import nextra.units as nu

load_dotenv()

comment = {}  ## this comments will be included into the .fits document


class SettingsReference:
    #:
    SETTING_ID = "NARVAL basic setting"
    """
    The setting ID for logging
    """
    # --------------------------------------------
    #    reference settings for Extractor_level_1
    # --------------------------------------------

    INSTRUMENT="NARVAL"
    OBS_LONG = 0.1333 * nu.DEG
    OBS_LAT = 42.9333 * nu.DEG
    OBS_ALT = 2869.4 * nu.M

    ADU_FACTOR = 1.35 * nu.ADU

 

    BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    REFFILES = os.path.abspath(os.path.join(BASEDIR, "assets/reffiles"))
    REFFITSFILE = os.path.abspath(
        os.path.join(REFFILES, "refthar/refthar_narval/276748c.fits")
    )
    STARPARAMFILES = os.path.abspath(os.path.join(BASEDIR, "assets/star_params"))

    # --------------------------------------------
    #    identifier for absolute sequence number and filenumber in sequence (1-4)
    # --------------------------------------------
    
    
    SEQIDENT = "A_IDENT"
    FILEINSEQ = "A_IDFILE"
    STOKENAME = "A_IDSEQ"
    NUMSEQ = "A_NUMSEQ"
    DATEOBS = "DATE"

    # ----------------------------------
    #   geometric constans of ccd
    # ---------------------------------
    NROWS = 4612
    comment["NROWS"] = "number of rows"
    NCOLS = 2098
    comment["NCOLS"] = "number of columns"
    NCROSS = 0
    comment["NCROSS"] = "number of rows/columns in central cross"
    REMOVECROSS = int(False)
    NROWSBLOCK = 2054  # number of rows in individual blocks
    NCOLSBLOCK = 2048  # number of cols in individual blocks
    # old moon
    ##HIGHEXP = 15
    ##LOWEXP = 4
    HIGHEXP = 60
    LOWEXP = 15
    CUTORDER = 35  # means that cutting flats is between 34 and 35
    UNIQUE_EXP = True  # no distinction high / low is made
    ABSORPTIONHALFW = 6  # central region beteween orders
    JUMP = 2.0
    comment["JUMP"] = "allowed jump for beam extraction"
    SMOOTHWIDTH_BEAM = 101
    comment["SMOOTHWIDTH_BEAM"] = "width of local polynomial fit"
    BACKGROUNDHW = 5
    VOIE1WIDTH = 15  # right of separator
    VOIE2WIDTH = 15  # left (redwards) of separator
    VOIE3WIDTH = 16
    FLUX_LIMIT = 250  * ADU_FACTOR # below, the beam extraction is discarded

    SHIFT_MASK_VOIE1 = list(range(1, VOIE1WIDTH + 2))
    SHIFT_MASK_VOIE2 = list(range(-VOIE2WIDTH - 1, 0)
    )  # realtive indices of extraction mask
    OFFSETRED = 16
    OFFSETBLUE = 16
    MEMORY_POSITION = 0.7  # memory of AR1 process for line following
    BLAZE_RANGE = list(
        range(-OFFSETRED, OFFSETBLUE + 1)
    )  # range for the blase function
    DEGREEBLAZE = 7  # polynomial degree for blaze funtion fit

    CENTRALROW = 2351  # arbitrarily selected central row
    USE_PICKED_CENTRAL_POSITIONS = (
        True  # if True use CENTRALPOSITIONS othterwise try matching
    )
    CENTRALPOSITION = {
        o : n
        for o, n in [
            [24, 151],
            [25, 182],
            [26, 213],
            [27, 244],
            [28, 276],
            [29, 309],
            [30, 342],
            [31, 376],
            [32, 411],
            [33, 447],
            [34, 483],
            [35, 521],
            [36, 560],
            [37, 600],
            [38, 641],
            [39, 683],
            [40, 726],
            [41, 771],
            [42, 818],
            [43, 865],
            [44, 914],
            [45, 965],
            [46, 1017],
            [47, 1070],
            [48, 1126],
            [49, 1183],
            [50, 1242],
            [51, 1302],
            [52, 1365],
            [53, 1430],
            [54, 1497],
            [55, 1565],
            [56, 1636],
            [57, 1709],
            [58, 1785],
            [59, 1863],
            [60, 1945],
            #[61, 2031],
        ]
    }

    ORDERS = list(range(24, 61))  ### 62 eigentlich...,
    #ORDERS = list(range(24, 61))  ### 62 eigentlich...,

    # -------------------------->--------------
    #    wave resolution for Extractor_level_1
    # ---------------------------------------
    LAMBDAFILE = os.path.join(REFFILES, "lambda_map_narval.csv")

    # snippets extraction
    # REF_SPECTRUM = os.path.join(REFFILES, 'thar_spec_MM201006.dat')

    ESTIMATE_BACKGROUND = "BACKGROUND_1D"

    # -------------------------------
    # __STORE__
    # -------------------------------

    STORE_PATH = os.path.join(BASEDIR, "assets/__STORE__")

    # ----------------------------------------
    #  atlas lines available
    # -------------------------------------------
    REF_ATLASLINES_REEDMAN = os.path.join(REFFILES, "Redman_table6.dat")
    REF_ATLASLINES_UVES = os.path.join(REFFILES, "thar_UVES_MM090311.dat")
    REF_ATLASLINES_CLICKED = os.path.join(REFFILES, "thar_clicked_uves.csv")

    # choice of catalog to use
    # TODO: use enum type
    ATLAS_FOR_SNIPPETS = 'CLICKED' #choose from 'UVES', 'REEDMAN', 'CLICKED'

    # zones not used (beware of Argon lines)
    EXCLUSION = os.path.join(REFFILES, "excluded_Narval.dat")

    WAVEMAP_IN_VACUUM_AIR = "AIR" #"AIR"  # 'VACUUM' # or AIR

    SEUIL = 0.2 * nu.ADU  # seuil en ADU
    SEUILR = 800.0
    VRANGE = 6.0 * nu.KM / nu.S  # vrange in km/s

    SNIPPETS_PIXEL_DELTA = (
        2 * nu.PIXEL
    )  # pixel interval around pixel mean for matching catalog
    VOIE_METHOD = "OPTIMAL_EXTRACT"##SUM_DIVIDE_CENTRALROW"# defines flux_123 in .fits

    #------- CONTINUUM PARAMS

    CONTINUUM_METHOD = "QQQ" #"CLASSICAL SPLINE" #
    CONTINUUM_POINTS = os.path.join(STARPARAMFILES, "vega/vega_narval_continuum.pickl")
    CONTINUUM_HALFVEL = 15 * nu.KM / nu.S

    # QQQ, QQQ = QQQ, POLYNOMIAL = 2nd order poly
    CONTINUUM_METHOD_ORDER = {
        o : n
        for o, n in [
            [24, 'QQQ'],
            [25, 'QQQ'],
            [26, 'QQQ'],
            [27, 'QQQ'],
            [28, 'QQQ'],
            [29, 'QQQ'],
            [30, 'QQQ'],
            [31, 'QQQ'],
            [32, 'QQQ'],
            [33, 'QQQ'],
            [34, 'QQQ'],
            [35, 'QQQ'],
            [36, 'QQQ'],
            [37, 'QQQ'],
            [38, 'QQQ'],
            [39, 'QQQ'],
            [40, 'QQQ'],
            [41, 'QQQ'],
            [42, 'QQQ'],
            [43, 'QQQ'],
            [44, 'QQQ'],
            [45, 'QQQ'],
            [46, 'QQQ'],
            [47, 'QQQ'],
            [48, 'QQQ'],
            [49, 'QQQ'],
            [50, 'QQQ'],
            [51, 'QQQ'],
            [52, 'QQQ'],
            [53, 'QQQ'],
            [54, 'QQQ'],
            [55, 'QQQ'],
            [56, 'QQQ'],
            [57, 'QQQ'],
            [58, 'QQQ'],
            [59, 'QQQ'],
            [60, 'QQQ'],
            #[61, 'P'],
        ]
    }





    # ------ spectrograph paramter

    n_bootstrap = 0  # number of bootstrap experiments
    profile = "igauss"  # fit profile for bootstrap estimate of centroid
    loss_function = "loss_3"  # weighted L2-loss for bootstrap estimate of centroid
    CLIPMETHOD = "threshold"
    CLIP_QUANTITY = "deltavr"
    CLIPTHRESHOLD = 1000 * nu.M / nu.S
    CLIP_MAX_VRAD = 1000 * nu.M / nu.S
    N_SIGMA_CLIPP = 1 # maximal number of clipping iterations per update 

    FITWEIGHT = "flux"  # weighted empirical risk
    USE_SIGMA_MIN = "True"  # do not use a minimal sigma in fitting
    sigma_min = 0.5 * nu.M / nu.S  # minimial sigma to avoid overfitting
    order_ol = 5  # order polynomial in ol
    order_o = 7   # order polynomial in o

    # ----------------------------
    #   plotting settings
    # ----------------------------------
    palette_order = "gist_rainbow"  # palette of orders


def get_kwargs():
    return {
        k: v for k, v in SettingsReference.__dict__.items() if not k.startswith("_")
    }


## the following parameters are included into the fits files header
PREFIX = "NEXTRA_"
HEADER_ITEMS = [k for k in comment.keys() if k[:2] != "__"]
