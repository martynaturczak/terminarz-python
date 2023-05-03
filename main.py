from nicegui import Client, ui, app
from weather import Weather
from planner import Planner
import datetime
import requests
import json 

url = "https://api.open-meteo.com/v1/forecast?latitude=51.10&longitude=17.03&hourly=temperature_2m&hourly=relativehumidity_2m&hourly=cloudcover&hourly=windspeed_10m&hourly=precipitation_probability&&forecast_days=2"
response = requests.get(url).json()

weather = Weather(response)
index = weather.index

now = datetime.datetime.now()
hour = now.strftime("%H")
minutes = now.strftime("%M")
day = now.strftime("%A")
app.add_static_files('/img', 'img')

content = open('calendar.json')
events = json.load(content)

planner = Planner(events)

@ui.page('/')
async def main_page(client: Client):
    await client.connected()
    await ui.run_javascript('document.getElementById("3").style.padding = "0px"')
    with ui.column().classes("w-screen h-screen grid grid-rows-2 bg-[#9A5F86] font-mono"):
        with ui.row().classes("w-full h-full"):
            calendar = ui.date(on_change=lambda e: planner.update_table(date = e.value))
            calendar.classes("w-full h-full")
            calendar.props('first-day-of-week="1" color=teal-10')
            calendar.run_method('setToday')
        with ui.row().classes("w-full h-full grid grid-cols-2"):
            with ui.column().classes("w-full h-full"):
                with ui.card().classes("w-full h-full bg-[#FFFCFE]"):
                    planner.create_table()
            with ui.column().classes("w-full h-full"):
                with ui.card().classes("w-full h-full grid grid-rows-2 bg-[#FFFCFE]"):
                    with ui.row().classes("w-full h-full grid grid-cols-5"):
                        with ui.column().classes("w-full h-full grid grid-cols-3 col-span-4 gap-0"):
                            with ui.column().classes("w-full h-full"):
                                ui.image(weather.img).classes("w-[96px] h-[96px] mt-4 ml-11")
                            with ui.column().classes("w-full h-full text-5xl flex content-center"):
                                ui.label(str(weather.temperature[index]) + "°C").classes("pt-8 pr-20")
                            with ui.column().classes("w-full h-full"):
                                ui.label("Precipitation probability: " + str(weather.precipitation_probability[index]) + "%")
                                ui.label("Humidity: " + str(weather.humidity[index]) + "%")
                                ui.label("Wind speed: " + str(weather.windspeed[index]) + " km/h")
                        with ui.column().classes("w-full h-full"):
                            with ui.row().classes("w-full h-3.5"):
                                ui.label("Weather").classes("w-full text-right text-2xl font-bold")
                            with ui.row().classes("w-full h-1"):
                                ui.label(day + ", " + hour + ":" + minutes).classes("w-full text-right")
                            with ui.row().classes("w-full"):
                                ui.label(weather.message).classes("w-full text-right")
                    with ui.row().classes("w-full h-full"):
                        weather.create_temperature_chart()
ui.run(port=1237)