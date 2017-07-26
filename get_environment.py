#!/usr/bin/env python

# This napalm script when executed will connect to a network device given to it
# as an argument and return the environmental status of the device in JSON
# format.

import sys
import json
from getpass import getpass
from napalm import get_network_driver

def get_input(prompt=''):
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)
    return line

def get_credentials():
    """Prompt and return a username and password."""
    username = get_input('Enter username: ')
    password = None
    while not password:
        password = getpass()
        password_verify = getpass('Retype your password: ')
        if password != password_verify:
            print ('Passwords do not match. Try again.')
            password = None
    return username, password

# Main entry in to the program
try:
    driver = sys.argv[1]
    hostname = sys.argv[2]
except:
    print 'Syntax: ios-get_environment.py <driver type> <ip address>'
    sys.exit(1)  # abort

netdriver = get_network_driver(driver)
username, password = get_credentials()
device = netdriver(hostname, username, password)
device.open()
env_status = device.get_environment()
device.close()
print (json.dumps(env_status, sort_keys=True, indent=4))
