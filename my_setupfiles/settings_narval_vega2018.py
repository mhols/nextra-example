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
    FLUX_LIMIT = 250 * ADU_FACTOR  # below, the beam extraction is discarded

    SHIFT_MASK_VOIE1 = list(range(1, VOIE1WIDTH + 2))
    SHIFT_MASK_VOIE2 = list(range(-VOIE2WIDTH -1, 0) #voie2 from -VOIE2WIDTH-1 : -2
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
        False # if True use CENTRALPOSITIONS othterwise try matching
    )

    LAMBDA_UNIT_OF_INPUT_FITSFILES=nu.ANGSTROM 
    LAMBDA_UNIT_OF_OUTPUT=nu.NM              # nanometer 

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

    ORDERS = list(range(60, 23, -1))     # enumeration from low to high freqs

    # ----------------------------------------
    #    wave resolution for Extractor_level_1
    # ---------------------------------------
    # LAMBDAFILE = os.path.join(REFFILES, "lambda_map_narval.csv")

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

    SEUIL = 0.2 * nu.ADU  # seuil en ADU
    SEUILR = 800.0
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
            CONTINUUM_POINTS_FILE = os.path.join(STARPARAMFILES, "vega/vega_narval_continuum.pickl"),
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
    CLIPTHRESHOLD = 1000 * nu.M / nu.S
    CLIP_MAX_VRAD = 1000 * nu.M / nu.S
    N_SIGMA_CLIPP = 1 # maximal number of clipping iterations per update

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
    from nextra import settings_narval
    tmp = settings_narval.get_kwargs()
    tmp.update({
        k: v for k, v in SettingsReference.__dict__.items() if not k.startswith("_")
    })
    return tmp


## the following parameters are included into the fits files header
PREFIX = "NEXTRA_"
HEADER_ITEMS = [k for k in comment.keys() if k[:2] != "__"]
