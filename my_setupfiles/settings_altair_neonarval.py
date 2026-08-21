import os
import numpy as np

import nextra as nx
from dotenv import load_dotenv

import nextra.units as nu
import nextra.continuum as continuum



comment = {}  ## this comments will be included into the .fits document


class SettingsAltairNeoNarval(nx.settings_neonarval.SettingsReferenceNeoNarval):
    IS_REFERENCE = False
    VOIE_METHOD = "OPTIMAL_EXTRACT" #SUM_DIVIDE_CENTRALROW"
    BIG_PSEUDO_FLAT = False
    CENTRALPOSITION={o:n+25 for o,n in nx.settings_neonarval.SettingsReferenceNeoNarval.CENTRALPOSITION.items()}




def get_kwargs():
    tmp = nx.settings_neonarval.get_kwargs()
    tmp.update({
        k: v for k, v in SettingsAltairNeoNarval.__dict__.items() if not k.startswith("_")
    })
    return tmp


## the following parameters are included into the fits files header
PREFIX = "NEXTRA_"
HEADER_ITEMS = [k for k in comment.keys() if k[:2] != "__"]
