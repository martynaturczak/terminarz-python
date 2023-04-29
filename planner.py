from nicegui import ui

class Planner:
    dates = []
    table = None
    def __init__(self, planner_data):
        self.dates = planner_data['dates']

    def create_table(self):
        columns = [
            {'name': 'time', 'label': 'Time', 'field': 'time', 'required': True, 'align': 'left'},
            {'name': 'events', 'label': 'Events', 'field': 'events', 'sortable': True},
        ]
        rows = [
            {'time': '12:00', 'events': 'text'},
            {'time': '13:00', 'events': 'text'},
            {'time': '14:00', 'events': 'text'},
            {'time': '15:00', 'events': 'text'},
        ]
        self.table = ui.table(columns=columns, rows=rows, row_key='name')

    def update_table(self, date = None, table = None):
        return 0
