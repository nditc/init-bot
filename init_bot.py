import click
import datetime
import json
import os
from pyfiglet import Figlet

def findEventWithId(id):
    events = json.load(open(eventspath))
    for i in range(len(events)):
        if(events[i]["event"]==id): return events[i]["name"]

def show0(schedule):
    ln = len(schedule)
    print('\nFRIDAY\n')
    for i in range(ln):
        day = schedule[i]["day"]
        if(day is 0): print(schedule[i]["time"], '===>' , findEventWithId(schedule[i]["event"]), '\n', '-'*50)
        

def show1(schedule):
    ln = len(schedule)
    print('\nSATURDAY\n')
    for i in range(ln):
        day = schedule[i]["day"]
        if(day is 1): print(schedule[i]["time"], '===>' , findEventWithId(schedule[i]["event"]), '\n', '-'*50)

schedulepath = 'schedule.json'
eventspath = 'events.json'

f = Figlet(font='ogre')

@click.group()
def cli():
    print(f.renderText('nditc_init_2018'))
    pass

@cli.command('schedule', help='Get schedule of the entire event')
def schedule():
    schedule = json.load(open(schedulepath))
    show0(schedule)
    show1(schedule)

@cli.command('eventid', help='Get IDs of all events')
def eventids():
    events = json.load(open(eventspath))
    ln = len(events)
    for i in range(ln):
        print(events[i]["event"], events[i]["name"])

@cli.command('event', help='Get event description with ID')
@click.argument('id')
def event(id):
    events = json.load(open(eventspath))
    ln = len(events)
    for i in range(ln):
        if(events[i]["event"]==int(id)):
            print('\n\n', '\t'*4, events[i]["name"], '\n'*3, events[i]["desc"])
