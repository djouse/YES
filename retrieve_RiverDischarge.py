
#
#   Credentials:
#   UID 264981
#   API Keye427c56b-030d-4004-ac3f-821f07e9150d
#

import cdsapi

c = cdsapi.Client()

c.retrieve(
    'efas-seasonal-reforecast',
    {
        'format': 'grib.zip',
        'leadtime_hour': '24',
        'hmonth': '12',
        'hyear': '2019',
        'model_levels': 'surface_level',
        'variable': 'river_discharge_in_the_last_24_hours',
    },
    'download.grib.zip')