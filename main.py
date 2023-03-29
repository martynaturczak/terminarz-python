from nicegui import Client, ui

@ui.page('/')
async def main_page(client: Client):
    await client.connected()
    await ui.run_javascript('document.getElementById("3").style.padding = "0px"')
    with ui.column().classes("w-screen h-screen grid grid-rows-2 bg-[#9A5F86]"):
        with ui.row().classes("w-full h-full"):
            calendar = ui.date()
            calendar.classes("w-full h-full")
            calendar.props('first-day-of-week="1" color=teal-10')
            calendar.run_method('setToday')
        with ui.row().classes("w-full h-full grid grid-cols-2"):
            with ui.column().classes("w-full h-full"):
                with ui.card().classes("w-full h-full").classes("bg-[#FFFCFE]"):
                    ui.label("tekst 1")
            with ui.column().classes("w-full h-full"):
                with ui.card().classes("w-full h-full").classes("bg-[#FFFCFE]"):
                    ui.label("tekst 2")
ui.run(port=1234)