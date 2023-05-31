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
        ui.table(columns=self.columns, rows=self.rows, row_key='name', pagination=4).style('width: 800px')
    def update_table(self, date = None, table = None):
        content = open('calendar.json')
        events = json.load(content)
        self.dates=events['dates']
        rows = []
        try:
            events = self.dates[0][date]['events']
            for event in events:
                rows.append({
                    'time':event['from'] + '-' + event['to'], 'events':event['description']
                })
        except:
            self.add_date(date)
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
    def add_date(self, date):
        content = open('calendar.json')
        events = json.load(content)
        content.close()
        events['dates'][0][date] = {"events": []}
        outfile = open("calendar.json", "w")
        json.dump(events, outfile)
        outfile.close()
        content = open('calendar.json')
        events = json.load(content)
        self.dates = events["dates"]
        content.close()



