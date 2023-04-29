from nicegui import ui
import datetime

class Weather:
    img = ""
    message = ""
    index = 0
    time = []
    hours = []
    temperature = []
    cloudcover = []
    humidity = []
    windspeed = []
    precipitation_probability = []
    now = datetime.datetime.now()
    hour = now.strftime("%H")
    minutes = now.strftime("%M")
    day = now.strftime("%A")
    def __init__(self, weather_data):
        self.time = weather_data['hourly']['time']
        self.temperature = weather_data['hourly']['temperature_2m']
        self.cloudcover = weather_data['hourly']['cloudcover']
        self.humidity = weather_data['hourly']['relativehumidity_2m']
        self.windspeed = weather_data['hourly']['windspeed_10m']
        self.precipitation_probability = weather_data['hourly']['precipitation_probability']
        self.set_index()
        self.set_weather_info()

    def set_index(self):
        now = datetime.datetime.now()
        hour = now.strftime("%H")
        minutes = now.strftime("%M")
        day = now.strftime("%A")
        date = now.strftime("%Y-%m-%dT%H:00")
        self.index = self.time.index(date)

    def set_weather_info(self):
        if self.precipitation_probability[self.index] > 60:
            self.img = "img/przelotny_deszczyk.png"
            self.message = "Passing rain"
        if self.precipitation_probability[self.index] > 80 and self.cloudcover[self.index] > 80 and self.humidity > 50:
            self.img = "img/deszczyk.png"
            self.message = "Rainy"
        if self.temperature[self.index] > 20 and self.cloudcover[self.index] < 50:
            self.img = "img/sloneczka.png"
            self.message = "Sunny"
        if self.temperature[self.index] > 15 and self.cloudcover[self.index] > 20:
            self.img = "img/chmurki_za_sloneczkiem.png"
            self.message = "Partially sunny"
        if self.windspeed[self.index] > 10 and self.humidity[self.index] > 90 and self.precipitation_probability[self.index] > 90:
            self.img = "img/burza.png"
            self.message = "Thunderstorm"
        else:
            self.img = "img/chmurka.png"
            self.message = "Cloudy"

    def create_temperature_chart(self):
        hours = []
        temperature = []
        for i in range(0, 24, 3):
            hours.append((self.time[self.index + 1 + i])[-5:])
            temperature.append(self.temperature[self.index + i])
        ui.chart({
                    'title': False,
                    'chart': {'type': 'column'},
                    'xAxis': {'categories': hours},
                    'series': [
                            {'name': 'Temperature', 'data': temperature}
                    ],
                }).classes('w-full h-48')

