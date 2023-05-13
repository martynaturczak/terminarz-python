from nicegui import ui
import datetime
import json 

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
        content = open('calendar.json')
        events = json.load(content)
        self.dates=events['dates']
        events = self.dates[0][date]['events']
        rows = []
        for event in events:
            rows.append({
                'time':event['from'] + '-' + event['to'], 'events':event['description']
            })
        self.rows = rows
        self.create_table.refresh()
    def add_event(self, date, from1 = None, to = None, description = None):
        content = open('calendar.json')
        events = json.load(content)
        content.close()
        new_events = [
            {"from": from1, "to": to, "description": description},
        ]
        events2 = self.dates[0][date]['events']
        if len(events2) > 0:
            events['dates'][0][date]['events'].append(new_events[0])
        else:
            events["dates"][0][date] = {"events": new_events}
        with open("calendar.json", "w") as outfile:
            json.dump(events, outfile)
        self.update_table(date)
         



