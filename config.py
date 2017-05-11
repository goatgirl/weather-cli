import file
import shutil
import sys

if file.exists('settings.py'):
    from settings import config

    save_file = config['save-file']
    location_url = config['location-url']
    weather_url = config['weather-url']
    weather_key = config['weather-key']


else:
    shutil.copy('blank-settings.py', 'settings.py')
    print("creating settings file")
    print("please visit https://darksky.net/dev/ for an API key")
    print("and add this to weather-key in settings.py file")
    sys.exit()
