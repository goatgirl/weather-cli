# Visit https://darksky.net/dev/ for an API key and add to weather key and uncomment

config = {
    'location-url': 'https://maps.googleapis.com/maps/api/geocode/json?address={loc}',
    'save-file': 'weather.sav',
    'weather-url': 'https://api.darksky.net/forecast/{key}/{lat},{lng}?units=uk2',
    # 'weather-key': KEY HERE
}
