def show(location, weather):
    print()
    print('Location : {}'.format(location.address))
    print('Weather  : {}'.format(weather.summary))
    print('Currently: {}\xb0C'.format(int(weather.temperature)))
    print('Forecast : {}'.format(weather.forecast))
    print('icon     : {}'.format(weather.icon))
