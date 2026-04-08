import settings_narval_vega2018

class SettingsSirius(settings_narval_vega2018.SettingsNarval2018):


    ### add or owerwrite your properties here 
    STARNAME_MAP_FOR_BERV = {
        'SIRIUSA': 'SIRIUS',
        'ALDEBARAN_QUATSCH': 'ALDEBARAN'   
    }

   
def get_kwargs():
    """
    a convenience shorcut
    """
    return SettingsSirius.get_kwargs()   ### use your classname
 