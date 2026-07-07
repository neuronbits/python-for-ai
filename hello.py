import os

# app.py
from dotenv import load_dotenv
import requests

print("hello")

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.environ.get("OPENAI_API_KEY")

if not API_KEY:
    print("Please set OPENAI_API_KEY in .env file")
    exit(1)

# Use the API
headers = {"Authorization": f"Bearer {API_KEY}"}
# Make your API calls...
headers


# Read from environment
api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE_NAME", "default.db")

print(f"Using api key: {api_key}")
print(f"Using database: {database}")


# Method 2: Check if exists
if "API_KEY1" in os.environ:
    api_key = os.environ["API_KEY1"]
    print(api_key)
else:
    print("No API key found")


from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Now use your variables
api_key = os.environ.get("API_KEY")
debug = os.environ.get("DEBUG")

print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")


import requests


# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200


def greet(name):
    if name:
        print(f"Hello {name}!")
    else:
        print("Hello")


greet("Mr")

# Good
x = 1 + 2
numbers = [1, 2, 3, 4]

# Bad
x = 1 + 2
numbers = [1, 2, 3, 4]


def first_function():
    pass


def second_function():
    pass


# Good - readable
long_string = "This is a very long string that spans multiple lines for readability"

# Bad - too long
long_string = "This is a very long string that spans multiple lines for readability but keeps going and going"

print(long_string)
long_string

print(type(42))

# Addition and subtraction
total = 10 + 5  # 15
change = 20 - 7  # 13

# Multiplication and division
area = 6 * 4  # 24
half = 10 / 2  # 5.0 (always returns float)

# Powers
squared = 5**2  # 25
cubed = 2**3  # 8

# Single quotes
first = "Python"

# Double quotes
second = "Python"

# Triple quotes for multiple lines
paragraph = """This is
a multi-line
string"""

# Use double quotes when your text contains apostrophes: "It's Python!"


first_name = "John"
last_name = "Doe"

# Concatenation
full_name = first_name + " " + last_name
print(full_name)  # John Doe

# Repetition
stars = "*" * 5
print(stars)  # *****

messy = "  hello world  "
print(messy.strip())  # "hello world" (removes whitespace)

price = "$19.99"
print(price.strip("$"))  # "19.99"

message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)  # True
print(message.startswith("I"))  # True
print(message.endswith("Python"))  # True

# Find position
print(message.find("Python"))  # 7 (first occurrence)
print(message.count("Python"))  # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"

age = 25
has_license = True

# Both must be True
if age >= 18 and has_license:
    print("You can drive!")

# At least one must be True
if weekend or holiday:
    print("No work today!")

# Reverse the condition
if not raining:
    print("Let's go outside!")

for i in range(5):
    print("Hello!")

# Count from 1 to 5
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# Count by 2s
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8

name = "Python"
for letter in name:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n

colors = ["red", "blue", "green"]
for color in colors:
    print(f"I like {color}")

# Output:
# I like red
# I like blue
# I like green

# Empty list
my_list = []

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]  # Different types OK!

my_list

fruits = ["apple", "banana", "orange"]

# Get items
print(fruits[0])  # "apple" (first item)
print(fruits[1])  # "banana"
print(fruits[-1])  # "orange" (last item)
print(fruits[-2])  # "banana" (second to last)

# Slicing
print(fruits[0:2])  # ["apple", "banana"]
print(fruits[1:])  # ["banana", "orange"]

fruits = ["apple", "banana", "orange"]

# Change an item
fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "orange"]

# Add items
fruits.append("grape")  # Add to end
fruits.insert(1, "kiwi")  # Insert at position

# Remove items
fruits.remove("banana")  # Remove by value
last = fruits.pop()  # Remove and return last
del fruits[0]  # Remove by index

fruits

numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers))  # 6 (length)
print(numbers.count(1))  # 2 (count occurrences)
print(numbers.index(4))  # 2 (find position)

# Sorting
numbers.sort()  # Sort in place
print(numbers)  # [1, 1, 3, 4, 5, 9]

numbers.reverse()  # Reverse order
print(numbers)  # [9, 5, 4, 3, 1, 1]

# Copy
new_list = numbers.copy()  # Create a copy

# Empty dictionary
my_dict = {}

# Dictionary with data
person = {"name": "Alice", "age": 30, "city": "New York"}

# Different ways to create
scores = dict(math=95, english=87, science=92)

person = {"name": "Alice", "age": 30, "city": "New York"}

# Get values by key
print(person["name"])  # "Alice"
print(person["age"])  # 30

# Safer with get()
print(person.get("job"))  # None (no error)
print(person.get("job", "Unknown"))  # "Unknown" (default)


person = {"name": "Alice", "age": 30}

# Add or update
person["email"] = "alice@email.com"  # Add new
person["age"] = 31  # Update existing

# Remove items
del person["email"]  # Remove by key
age = person.pop("age")  # Remove and return
person.clear()  # Remove all items

person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys, values, or items
print(person.keys())  # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())  # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"},
}

# Access nested data
print(students["alice"]["grade"])  # "A"

# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}

colors = {"red", "blue"}

# Add items
colors.add("green")
print(colors)  # {'red', 'blue', 'green'}

# Remove items
colors.remove("blue")  # Error if not found
colors.discard("yellow")  # No error if not found

# Check membership
if "red" in colors:
    print("Red is available")

colors


names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(unique_names)  # ['Alice', 'Bob', 'Charlie']

allowed_users = {"alice", "bob", "charlie"}

if "alice" in allowed_users:  # Very fast!
    print("Access granted")

counter = 0  # Global variable


def increment():
    global counter  # Declare we want to modify the global variable
    counter += 1


increment()
increment()
print(counter)  # 2


def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")


# Positional arguments (order matters)
create_profile("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(city="NYC", age=25, name="Alice")
create_profile(name="Bob", city="LA", age=30)


def get_min_max(numbers):
    return min(numbers), max(numbers)


# Get both values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Or as a tuple
result = get_min_max([5, 2, 8, 1, 9])
print(result)  # (1, 9)


# Import entire module
import random

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])
choice


# Date and time
import datetime

today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os

current_dir = os.getcwd()
print(current_dir)

# JSON data
import json

data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
json_string


# Web requests
import requests

response = requests.get("https://www.google.com")
data = response.json()
data
# Data analysis
import pandas as pd

# Create a simple DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["NYC", "LA", "Chicago"],
}
df = pd.DataFrame(data)
print(df)

import requests

# We need coordinates to get weather data
latitude = 48.85  # Paris latitude
longitude = 2.35  # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)

data

temperature = data["current"]["temperature_2m"]
print(f"Temperature in Paris: {temperature}°C")
# Output: Temperature in Paris: 20.0°C
