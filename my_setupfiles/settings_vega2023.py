import os
import numpy as np
from dotenv import load_dotenv

import nextra
import nextra.units as nu
import nextra.continuum as continuum

from nextra.settings_neonarval import SettingsReferenceNeoNarval

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


class SettingsNeoNarvalVega2023(SettingsReferenceNeoNarval):
    IS_REFERENCE = False

    SETTING_ID = "Vega 2023"
    """
    The setting ID for logging
    """

    VOIE_METHOD = "OPTIMAL_EXTRACT"##SUM_DIVIDE_CENTRALROW" ##OPTIMAL_EXTRACT"  # defines flux_123 in .fits

    #------- CONTINUUM PARAMS

    USER_BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

    print(USER_BASEDIR)

    # uncomment if necessary
    STARPARAMFILES = os.path.abspath(os.path.join(USER_BASEDIR, "star_params/"))
    print(STARPARAMFILES)
    
    # CONTINUUM_METHOD_CLASS = continuum.PointBasedContinuum
    CONTINUUM_METHOD_CLASS = continuum.SigmaClippingContinuum


    CONTINUUM_METHOD_EXTRA_KWARGS = {
        'CONTINUUM_POINTS_FILE': os.path.join(STARPARAMFILES, 'vega/vega_neonarval_continuum.pickl'),
        'CONTINUUM_HALFVEL' :15 * nu.KM / nu.S
    }



    # CONTINUUM_CLICKED, QQQ = qqq, POLYNOMIAL = 2nd order poly
    
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
 
    # --------------------------------------------
    #    reference settings for Extractor_level_1
    # --------------------------------------------

def get_kwargs():
    tmp = nextra.settings_neonarval.get_kwargs()
    tmp.update({
        k: v for k, v in SettingsNeoNarvalVega2023.__dict__.items() if not k.startswith("_")
    })
    return tmp

