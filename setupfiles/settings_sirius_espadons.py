import os
import numpy as np

import nextra as nx
from dotenv import load_dotenv

import nextra.units as nu
import nextra.continuum as continuum



comment = {}  ## this comments will be included into the .fits document


class SettingsSiriusEspadons(nx.settings_espadons.SettingsReferenceEspadons):
    IS_REFERENCE = False
    VOIE_METHOD = "OPTIMAL_EXTRACT" #SUM_DIVIDE_CENTRALROW"
    BIG_PSEUDO_FLAT = False

    ORDERS = list(range(24, 57))

    CONTINUUM_METHOD_CLASS = continuum.SigmaClippingContinuum
    

def get_kwargs():
    tmp = nx.settings_espadons.get_kwargs()
    tmp.update({
        k: v for k, v in SettingsSiriusEspadons.__dict__.items() if not k.startswith("_")
    })
    return tmp


## the following parameters are included into the fits files header
PREFIX = "NEXTRA_"
HEADER_ITEMS = [k for k in comment.keys() if k[:2] != "__"]
