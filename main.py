import datetime
from nicegui import ui

with ui.column().classes("w-screen h-screen grid grid-rows-2"):
    with ui.row().classes("w-full h-full"):
        calendar = ui.date(value = datetime.date.today(), on_change=lambda e: result.set_text(e.value))
        calendar.classes("w-full h-full")
        calendar.props('first-day-of-week="1"')
        result = ui.label()
    with ui.row().classes("w-full h-full grid grid-cols-2"):
        with ui.column().classes("w-full h-full"):
            with ui.card().classes("w-full h-full"):
                ui.label("tekst 1")
        with ui.column().classes("w-full h-full"):
            with ui.card().classes("w-full h-full"):
                ui.label("tekst 2")
ui.run()
