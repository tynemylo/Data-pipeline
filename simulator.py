import random #Random module for generating random numbers
import urllib.request #Module for handling URL requests
import json #Module for working with JSON data
from datetime import datetime, timedelta #Modules for handling date and time

def get_message(): # Creates a randomized message with a unique location
    units_completed = random.randint(0, 5)# Adjusted to ensure units are non-negtive
    locations = ['New York', 'Sydney', None, 'Luxemborg', 'Toronto', 'San Francisco']
    location = random.choice(locations)
    date = datetime.now().isoformat() # Convert datetime to ISO 8601 string
    return {  'units': units_completed, 'location': location, 'date': date }

def daemon():
    message = get_message() # Generate a message
    body = json.dumps(message).encode('utf-8') # Convert message to JSON and encode to bytes
    post("http://localhost:8080", body)# Send the message to the server

    
def set_interval(func, interval): # Function to set an interval for executing a function
        while True:
            func()
            datetime_now = datetime.now()
            datetime_next = datetime_now + timedelta(milliseconds=interval)
            while datetime.now() < datetime_next:
                datetime_now = datetime.now()

# Define a function to simulate posting data using urllib
def post(url, data):
    try:
        req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                print("Data sent successfully")
            else:
                print(f"Failed to send data. Status code: {response.getcode()}")
    except urllib.error.URLError as e:
        print(f"Error sending data: {e}")

# Start the daemon with an interval of 4000 milliseconds (4 seconds)
set_interval(daemon, 4000)        



