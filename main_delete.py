#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.place import Place
from models.state import State

fs = FileStorage()

# All States
print("All States: {}".format(fs.all(State)))

# Create a new State
new_state = State()
new_state.name = "Texas"
fs.new(new_state)

new_place = Place()
new_place.name = "California"
fs.new(new_place)
fs.save()

# All States
print("All States: {}".format(fs.all(State)))
