import os
import numpy as np
from dotenv import load_dotenv

import nextra.units as nu
import nextra.continuum as continuum
from nextra import settings_narval

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


class SettingsNarvalSirius2011(settings_narval.SettingsReference):
    SETTING_ID = "NARVAL Sirius setting"
    """
    The setting ID for logging
    """
    IS_REFERENCE = False
    USER_BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    STARPARAMFILES = os.path.abspath(os.path.join(USER_BASEDIR, "star_params"))

    CENTRALPOSITION = {
        o : n
        for o, n in [
            #[24, 151],
            #[25, 182],
            #[26, 213],
            #[27, 244],
            #[28, 276],
            #[29, 309],
            #[30, 342],
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
    
    CENTRALPOSITION = {o: n + 9 for o, n in CENTRALPOSITION.items()}

    ORDERS = list(range(60, 30, -1))     # enumeration from low to high freqs

    CONTINUUM_METHOD_CLASS = continuum.PointBasedContinuum  ### set this if you want to use the same continuum estimator for all orders

    ### add here any extra paramters your continuum method may need
    CONTINUUM_METHOD_EXTRA_KWARGS = dict (
            CONTINUUM_POINTS_FILE = os.path.join(STARPARAMFILES, "vega/vega_narval_continuum_A.pickl"),
            CONTINUUM_HALFVEL = 15 * nu.KM / nu.S
        )
 
    # ------ spectrograph paramter



def get_kwargs():
    return SettingsNarvalSirius2011().get_kwargs()

## the following parameters are included into the fits files header
PREFIX = "NEXTRA_"
HEADER_ITEMS = [k for k in comment.keys() if k[:2] != "__"]

