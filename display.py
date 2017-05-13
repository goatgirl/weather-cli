def show(location, weather):
    # print(weather.day[0])
    print('\nNow:', weather.now['summary'], "{}\xb0C".format(
        int(weather.now['temperature'])))
    print('\nToday:', weather.day[0]['summary'])
    print('\nTomorrow:', weather.day[1]['summary'])
