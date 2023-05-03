from nicegui import ui
import datetime

class Planner:
    dates = []
    table = None
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    columns = [
            {'name': 'time', 'label': 'Time', 'field': 'time', 'required': True, 'align': 'left'},
            {'name': 'events', 'label': 'Events', 'field': 'events', 'sortable': True},
        ]
    rows = []
    def __init__(self, planner_data):
        self.dates = planner_data['dates']
    @ui.refreshable
    def create_table(self):
        ui.table(columns=self.columns, rows=self.rows, row_key='name')

    def update_table(self, date = None, table = None):
        events = self.dates[0][date]['events']
        rows = []
        for event in events:
            rows.append({
                'time':event['from'] + '-' + event['to'], 'events':event['description']
            })
        self.rows = rows
        self.create_table.refresh()
