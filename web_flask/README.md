# 0x04. AirBnB clone - Web framework
---

![HBnB](https://i.imgur.com/ETx1Gtf.png)

## Description

This is a repository for the first segment of the AirBnB clone we will be creating for the next four months.
This project will consist of six parts:
* The console
* Web static
* MySQL storage
* Web framework - templating
* RESTful API
* Web Dynamic

This repo contains the first part: the console. The console is the storage system that will hold all the future objects that we will implement in the later parts of the project.

![the diagram](https://i.imgur.com/buXwT8d.png)
---
## Files
---
File|Task
---|---
console.py | Main console file
amenity.py | Amenity class
base_model.py | BaseModel class template
city.py | City class
place.py | Place class
review.py | Review class
state.py | State class
user.py | User class
file_storage.py | FileStorage class
test_console.py | Unittest module for console
test_amenity.py | Unittest module for amenity
test_base_model.py | Unittest module for base model
test_city.py | Unittest module for city
test_place.py | Unittest module for place
test_review.py | Unittest module for review
test_state.py | Unittest module for state
test_user.py | Unittest module for user
test_file_storage.py | Unittest module for file storage

Directory Name | Description
---|---
models | Contains all the classes
models/engine | Contains JSON conversion files
tests/test_models | Contains unittest files
tests/test_models/test_engine | Contains unittest file for the engine

## Authors
Damon Nyhan [@anovacap](https://twitter.com/anovacap)  
Leo Byeon [@byeon_cat](https://twitter.com/byeon_cat)