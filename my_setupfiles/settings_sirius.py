import settings_narval_vega2018

_PARENT_POS = settings_narval_vega2018.SettingsNarval2018.CENTRALPOSITION

class SettingsSirius(settings_narval_vega2018.SettingsNarval2018):


    ### add or owerwrite your properties here 
    STARNAME_MAP_FOR_BERV = {
        'SIRIUSA': 'SIRIUS',
        'ALDEBARAN_QUATSCH': 'ALDEBARAN'   
    }
    FLUX_LIMIT = 250 * settings_narval_vega2018.SettingsNarval2018.ADU_FACTOR
    CONTINUUM_METHOD_CLASS = settings_narval_vega2018.continuum.QQQContinuum

    CENTRALPOSITION = {o: n + 9 for o, n in _PARENT_POS.items()}

   
def get_kwargs():
    """
    a convenience shorcut
    """
    return SettingsSirius().get_kwargs()   ### use your classname
 
