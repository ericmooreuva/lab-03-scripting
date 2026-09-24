#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

# get the events from the user from the url and load them as a list
def retrieve_events(url):
	response = requests.get(url)
	text = response.text
	events = json.loads(text)
	return events

# prints the first n events
def print_events(events, n=5):
	for x in events[:n]:
		event = x['type'] + ' :: ' + x['repo']['name']
		print(event)

# Print the Github user and url and then get their events
def main():
	print(GHUSER)
	print(url)
	events = retrieve_events(url)
	print_events(events)

if __name__ =='__main__':
	main()
		

[A[A[B
