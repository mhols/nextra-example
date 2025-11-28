import os
import numpy as np
from dotenv import load_dotenv

import nextra.units as nu
import nextra.continuum as continuum

__doc__ = """ Global parameters for the datareduction pipeline.
This specific module is adapted for the NEO Narval instrument.

Normally you should not change these values in this file directly
Rather create a new setting_xxxx.py module in which you import

.. code-block:: python

    from nextra import settings_reference
    mykwargs = settings_reference.get_kwargs()
    ## now use mykwargs by updating the paramters
    mykwargs['SETTING_ID'] = 'Moon'
    ...

Alternatively you may copy this module as a template and adapt it
"""
load_dotenv()

comment = {}  ## this comments will be included into the .fits document


class SettingsReference:
    SETTING_ID = "neonarval_reference"
    """
    The setting ID for logging
    """
    # --------------------------------------------
    #    reference settings for Extractor_level_1
    # --------------------------------------------

    INSTRUMENT="NEONARVAL"
    OBS_LONG = 0.1333 * nu.DEG
    OBS_LAT = 42.9333 * nu.DEG
    OBS_ALT = 2869.4 * nu.M
    
    ADU_FACTOR = 3.0 * nu.ADU


    USER_BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    # uncomment if necessary
    # REFFILES = os.path.abspath(os.path.join(BASEDIR, "reffiles"))
    STARPARAMFILES = os.path.abspath(os.path.join(USER_BASEDIR, "star_params"))
#    REFFITSFILE = os.path.abspath(
#        os.path.join(REFFILES, "refthar/NEO_20220903_191404_th0.fits")
#    )
    
    # --------------------------------------------
    #    identifier for absolute sequence number and filenumber in sequence (1-4)
    # --------------------------------------------
    SEQIDENT = "A_IDSEQ"
    FILEINSEQ = "STOKESEQ"
    STOKENAME = "STOKNAME"
    NUMSEQ = ""
    DATEOBS = "DATE-FIT"

    # ----------------------------------
    #   geometric constans of ccd
    # ---------------------------------
    NROWS = 4208
    comment["NROWS"] = "number of rows"
    NCOLS = 4196
    comment["NCOLS"] = "number of columns"
    NCROSS = 100
    comment["NCROSS"] = "number of rows/columns in central cross"
    REMOVECROSS = int(True)
    NROWSBLOCK = 2054  # number of rows in individual blocks
    NCOLSBLOCK = 2048  # number of cols in individual blocks
    # old moon
    ##HIGHEXP = 15
    ##LOWEXP = 4
    HIGHEXP = 60
    LOWEXP = 15
    CUTORDER = 35  # means that cutting flats is between 34 and 35
    ABSORPTIONHALFW = 6  # central region beteween orders
    JUMP = 2.0
    comment["JUMP"] = "allowed jump for beam extraction"
    SMOOTHWIDTH_BEAM = 101
    comment["SMOOTHWIDTH_BEAM"] = "width of local polynomial fit"
    BACKGROUNDHW = 5
    VOIE1WIDTH = 13  # right of separator
    VOIE2WIDTH = 11  # left (redwards) of separator
    VOIE3WIDTH = 13
    FLUX_LIMIT = 500  * ADU_FACTOR # below, the beam extraction is discarded

    SHIFT_MASK_VOIE1 = list(range(2, VOIE1WIDTH + 1)) #voie1 from 2 : VOIEWIDTH1
    SHIFT_MASK_VOIE2 = list(range(-VOIE2WIDTH -1, -1) #voie2 from -VOIE2WIDTH-1 : -2
    )  # realtive indices of extraction mask
    OFFSETRED = 13
    OFFSETBLUE = 13
    MEMORY_POSITION = 0.7  # memory of AR1 process for line following
    BLAZE_RANGE = list(
        range(-OFFSETRED, OFFSETBLUE + 1)
    )  # range for the blase function
    DEGREEBLAZE = 7  # polynomial degree for blaze funtion fit

    CENTRALROW = 2161  # arbitrarily selected central row
    USE_PICKED_CENTRAL_POSITIONS = (
        False # if True use CENTRALPOSITIONS othterwise try matching
    )
    CENTRALPOSITIONSHIFT = 0  #shift of reference CENTRALPOSITION to observed CENTRALPOSITION
    
    CENTRALPOSITION = {
        21: 824,
        22: 866,
        23: 907,
        24: 948,
        25: 990,
        26: 1032,
        27: 1074,
        28: 1117,
        29: 1161,
        30: 1206,
        31: 1252,
        32: 1299,
        33: 1347,
        34: 1398,
        35: 1449,
        36: 1501,
        37: 1555,
        38: 1611,
        39: 1669,
        40: 1728,
        41: 1789,
        42: 1852,
        43: 1918,
        44: 1985,
        45: 2054,
        46: 2126,
        47: 2200,
        48: 2276,
        49: 2355,
        50: 2436,
        51: 2520,
        52: 2606,
        53: 2697,
        54: 2789,
        55: 2885,
        56: 2984,
        57: 3086,
    }
    # 58:3192,} TODO make snipets not to break ...
    # 59:3302}  TODO make robust for empty beams

    ORDERS = list(range(57, 20, -1))     # enumeration from low to high freqs

    # ----------------------------------------
    #    wave resolution for Extractor_level_1
    # ---------------------------------------
    # LAMBDAFILE = os.path.join(REFFILES, "NEXTRA_base_lambda_map.txt")

    ESTIMATE_BACKGROUND = "BACKGROUND_1D"

    # -------------------------------
    # __STORE__
    # -------------------------------

    STORE_PATH = os.path.join(USER_BASEDIR, "__STORE__")

    # snippets extraction
    # REF_SPECTRUM = os.path.join(REFFILES, 'thar_spec_MM201006.dat')

    # ----------------------------------------
    #  atlas lines available
    # -------------------------------------------
    #REF_ATLASLINES_REEDMAN = os.path.join(REFFILES, "Redman_table6.dat")
    #REF_ATLASLINES_UVES = os.path.join(REFFILES, "thar_UVES_MM090311.dat")
    #REF_ATLASLINES_CLICKED = os.path.join(REFFILES, "thar_clicked_uves.csv")

    # choice of catalog to use
    # TODO: use enum type

    #ATLAS_FOR_SNIPPETS = (
    #    "CLICKED"  #'CLICKED'   # choose from 'UVES', 'REEDMAN', 'CLICKED'
    #)

    # zones not used (beware of Argon lines)
    # EXCLUSION = os.path.join(REFFILES, "excluded.dat") TODO: check if out

    WAVEMAP_IN_VACUUM_AIR = "AIR"   #"VACUUM"  # "VACUUM" # 'VACUUM' # or AIR

    VRANGE = 6.0 * nu.KM / nu.S  # vrange in km/s

    SNIPPETS_PIXEL_DELTA = (
        2 * nu.PIXEL
    )  # pixel interval around pixel mean for matching catalog
    VOIE_METHOD = "OPTIMAL_EXTRACT"##SUM_DIVIDE_CENTRALROW" ##OPTIMAL_EXTRACT"  # defines flux_123 in .fits

    #------- CONTINUUM PARAMS

    #CONTINUUM_METHOD_CLASS = continuum.QQQContinuum        ### set this if you want to use the same continuum estimator for all orders
    CONTINUUM_METHOD_CLASS = continuum.PointBasedContinuum  ### set this if you want to use the same continuum estimator for all orders

    ### add here any extra paramters your continuum method may need
    CONTINUUM_METHOD_EXTRA_KWARGS = dict (
            CONTINUUM_POINTS_FILE = os.path.join(STARPARAMFILES, "vega/vega_continuum.pickl"),
            CONTINUUM_HALFVEL = 15 * nu.KM / nu.S
        )
    



    ### the following settings should be removed....
    """
    CONTINUUM_HALFVEL = 15 * nu.KM / nu.S
    CONTINUUM_METHOD = "CONTINUUM_CLICKED" 
    CONTINUUM_POINTS = os.path.join(STARPARAMFILES, 'vega/vega_continuum.pickl')
    CONTINUUM_METHOD_ORDER = {
        o : n
        for o, n in [
            [21, 'CONTINUUM_CLICKED'],
            [22, 'CONTINUUM_CLICKED'],
            [23, 'CONTINUUM_CLICKED'],
            [24, 'CONTINUUM_CLICKED'],
            [25, 'CONTINUUM_CLICKED'],
            [26, 'CONTINUUM_CLICKED'],
            [27, 'CONTINUUM_CLICKED'],
            [28, 'CONTINUUM_CLICKED'],
            [29, 'CONTINUUM_CLICKED'],
            [30, 'CONTINUUM_CLICKED'],
            [31, 'CONTINUUM_CLICKED'],
            [32, 'CONTINUUM_CLICKED'],
            [33, 'CONTINUUM_CLICKED'],
            [34, 'CONTINUUM_CLICKED'],
            [35, 'CONTINUUM_CLICKED'],
            [36, 'CONTINUUM_CLICKED'],
            [37, 'CONTINUUM_CLICKED'],
            [38, 'CONTINUUM_CLICKED'],
            [39, 'CONTINUUM_CLICKED'],
            [40, 'CONTINUUM_CLICKED'],
            [41, 'CONTINUUM_CLICKED'],
            [42, 'CONTINUUM_CLICKED'],
            [43, 'CONTINUUM_CLICKED'],
            [44, 'CONTINUUM_CLICKED'],
            [45, 'CONTINUUM_CLICKED'],
            [46, 'CONTINUUM_CLICKED'],
            [47, 'CONTINUUM_CLICKED'],
            [48, 'CONTINUUM_CLICKED'],
            [49, 'CONTINUUM_CLICKED'],
            [50, 'CONTINUUM_CLICKED'],
            [51, 'CONTINUUM_CLICKED'],
            [52, 'CONTINUUM_CLICKED'],
            [53, 'CONTINUUM_CLICKED'],
            [54, 'CONTINUUM_CLICKED'],
            [55, 'CONTINUUM_CLICKED'],
            [56, 'CONTINUUM_CLICKED'],
            [57, 'CONTINUUM_CLICKED'],
            #[61, 'P'],
        ]
    }
    """



    # ------ spectrograph paramter

    n_bootstrap = 0  # number of bootstrap experiments
    profile = "igauss"  # fit profile for bootstrap estimate of centroid
    loss_function = "loss_3"  # weighted L2-loss for bootstrap estimate of centroid
    CLIPMETHOD = "threshold"
    CLIP_QUANTITY = "deltavr"
    CLIPTHRESHOLD = 2000 * nu.M / nu.S
    CLIP_MAX_VRAD = 2000 * nu.M / nu.S
    N_SIGMA_CLIPP = 10 # maximal number of clipping iterations per update 

    FITWEIGHT = "flux"  # weighted empirical risk
    USE_SIGMA_MIN = "True"  # do not use a minimal sigma in fitting
    sigma_min = 0.5 * nu.M / nu.S  # minimial sigma to avoid overfitting
    order_ol = 5  # order polynomial in ol
    order_o = 7  # order polynomial in o

    # ----------------------------
    #   plotting settings
    # ----------------------------------
    palette_order = "gist_rainbow"  # palette of orders


def get_kwargs():
    from nextra import settings_reference
    tmp = settings_reference.get_kwargs()
    tmp.update({
        k: v for k, v in SettingsReference.__dict__.items() if not k.startswith("_")
    })
    return tmp


## the following parameters are included into the fits files header
PREFIX = "NEXTRA_"
HEADER_ITEMS = [k for k in comment.keys() if k[:2] != "__"]
