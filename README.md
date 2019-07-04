# AirBnB_clone (The Holberton B&B) :octocat:

## Description :star:
This project was created as part of the 2nd trimester curriculum at [Holberton School](https://www.holbertonschool.com/), San Francisco. We won't be covering the entire process of creating a clone of AirBnB's website. Instead we will do it step by step.

In **this Repository** we will go over the  1st part of the project: Creating the **console**.

## The Console :collision:
If you know what a shell is and how to create one using the C programming language, then you should know what the console is. If not, then here's a quick review: Shell is a user interface command-line interpreter. The shell is a program that takes commands from the keyboard and gives them to the operating system to perform.

In our case, the reason need to create a shell is because we want to be able to manage the objects of our project. We need to create custom commands that allows us to manage our objects.

Our console will be created in `Python3` (version 3.4.3). We used the module `cmd` in order to create our console/shell. And for practical reasons, our code should not be executed when imported.

### Starting the Console :dizzy:
In order to use the console and start it. Follow the example below:
```
$
$ ./console.py
(hbnb)
```
Make sure the `console.py` file is an executable file. It should be by default but if a bug happens, please double check permissions for executable.

## Console Commands :smiley_cat:
Here are the commands we have created for the console:
* **quit** - use to exit the program.
```
$ ./console.py
(hbnb) quit
$
```
* **help** - use to get the doumentation for the command.
```
$ ./console.py
(hbnb) help quit
Quit command to exit the program
$
```
* **EOF** - use to exit the program and print an empty line before exiting.
```
$ ./console.py
(hbnb) EOF

$
```
* **create** - used to create a new instanc of a class then saves it (to the JSON file) and also prints the instance atrribute `id` to stdout. 
```
(hbnb) create BaseModel
5ad82155-9278-4934-9573-0741caf52b72
(hbnb)
```
* **show** - use to print the string representation of an instance based on the class name and `id`. Ex: `$ show BaseModel 1234-1234-1234`.
```
(hbnb) show BaseModel 5ad82155-9278-4934-9573-0741caf52b72
[BaseModel] (5ad82155-9278-4934-9573-0741caf52b72) {'id': '5ad82155-9278-4934-9573-0741caf52b72', 'created_at': datetime.datetime(2019, 7, 4, 0, 52, 22, 456228), 'updated_at': datetime.datetime(2019, 7, 4, 0, 52, 22, 456283)}
(hbnb)
```
* **destroy** - use to delete an instance based on the class name and `id` (save the change into the JSON file). Ex: `$ destroy BaseModel 1234-1234-1234`.
```
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
```
* **all** - use to print all string representation of all instances based or not on the class name. Ex: `$ all BaseModel or $ all`.
```
(hbnb) create BaseModel
59e8277e-4283-42c5-bf4f-71725e036bec
(hbnb) create User
d99383df-4213-4f77-bf20-25a2d072f733
(hbnb) all
["[User] (d99383df-4213-4f77-bf20-25a2d072f733) {'id': 'd99383df-4213-4f77-bf20-25a2d072f733', 'updated_at': datetime.datetime(2019, 7, 4, 6, 18, 34, 454928), 'created_at': datetime.datetime(2019, 7, 4, 6, 18, 34, 454886)}", "[BaseModel] (59e8277e-4283-42c5-bf4f-71725e036bec) {'id': '59e8277e-4283-42c5-bf4f-71725e036bec', 'updated_at': datetime.datetime(2019, 7, 4, 6, 18, 24, 583479), 'created_at': datetime.datetime(2019, 7, 4, 6, 18, 24, 583414)}"]
(hbnb) all User
["[User] (d99383df-4213-4f77-bf20-25a2d072f733) {'id': 'd99383df-4213-4f77-bf20-25a2d072f733', 'updated_at': datetime.datetime(2019, 7, 4, 6, 18, 34, 454928), 'created_at': datetime.datetime(2019, 7, 4, 6, 18, 34, 454886)}"]
(hbnb)
```
* **update** - use to update an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"`.
```
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```
Pressing `ENTER` with an empty line shouldn’t execute anything.
```
(hbnb)
(hbnb)
(hbnb)
```
Note: All commands are case sensitive. If the command is not recognized, please check the spelling.

## Data Diagram
![Image of the Data Diagram](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/289/AirBnb_DB_diagramm.jpg)

### Classes Created :snowflake:
1. **BaseModel** - class with attributes/methods that is inherited by all other classes listed in the data diagram.
   * Public instance attributes:
     * `id`: string - assign with an uuid when an instance is created.
     * `created_at`: datetime - assign with the current datetime (`utcnow()`) when an instance is created.
     * `updated_at`: datetime - assign with the current datetime (`utcnow()`) when an instance is created and it will be updated every time you change your object.
1. **FileStorage** - class with attributes/methods that can serialize instances to a JSON file and then deserializes the JSON file back to an instance.
   * Private class attributes:
     * `__file_path1`: string - the file path to the JSON file (ex: `"file.json"`)
     * `__objects`: dictionary - empty but will store all objects by `<class name>.id` (ex: to store a `BaseModel` object with `id=68778655`, the dictionary key will be `BaseModel.68778655`)
1. **User** - class that inherits from BaseModel
   * Public class attributes:
     * `email`: string - empty string.
     * `password`: string - empty string.
     * `first_name`: string - empty string.
     * `last_name`: string - empty string.
1. **State** - class that inherits from BaseModel
   * Public class attributes:
     * `name`: string - empty string.
1. **City** - class that inherits from BaseModel
   * Public class attributes:
     * `state_id`: string - empty string: it will be seen as the `State.id`.
     * `name`: string - empty string.
1. **Amenity** - class that inherits from BaseModel
   * Public class attributes:
     * `name`: string - empty string.
1. **Place** - class that inherits from BaseModel
   * Public class attributes:
     * `city_id`: string - empty string: it will be seen as the `City.id`.
     * `user_id`: string - empty string: it will be seen as the `User.id`.
     * `name`: string - empty string.
     * `description`: string - empty string.
     * `number_rooms`: integer - 0.
     * `number_bathrooms`: integer - 0.
     * `max_guest`: integer - 0.
     * `price_by_night`: integer - 0.
     * `latitude`: float - 0.0.
     * `longitude`: float - 0.0.
     * `amenity_ids`: list of string - empty list: it will be the list of `Amenity.id` later.
1. **Review** - class that inherits from BaseModel
   * Public class attributes:
     * `place_id`: string - empty string: it will be seen as the `Place.id`.
     * `user_id`: string - empty string: it will be senn as the `User.id`.
     * `text`: string - empty string.

## Execution :hatching_chick:
Our command interpreter (i.e. Shell) will be executed like in the example below.

Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Files :stars:
Files in Home | Description
--- | ---
[AUTHORS](https://github.com/billhong6981/AirBnB_clone/blob/master/AUTHORS) | File containing the list of contributors for this project.
[models](https://github.com/billhong6981/AirBnB_clone/tree/master/models) | Directory containing the files for the classes.
[tests](https://github.com/billhong6981/AirBnB_clone/tree/master/tests) | Directory containing the files used for unittesting.
[console.py](https://github.com/billhong6981/AirBnB_clone/blob/master/console.py) | File containing the source code for the console.

Files in Model | Description
--- | ---
[AUTHORS](https://github.com/ethanpasta/simple_shell/blob/master/AUTHORS) | This file store the contact info of all individuals who contributed to the branches of our shell code.
[base_model.py](https://github.com/billhong6981/AirBnB_clone/blob/Dev/models/base_model.py) | Contains the base-class called `BaseModel` that defines all common attributes/methods for other classes. And to be inherited by other classes created in the repo.
[__init__.py](https://github.com/billhong6981/AirBnB_clone/blob/Dev/models/__init__.py) | Create variable called `storage` in order to link our `BaseModel` class  to the `FileStorage` class. And calls the method `reload()` when variable is used.
[amenity.py](https://github.com/billhong6981/AirBnB_clone/blob/master/models/amenity.py) | File containing  the `Amenity` class.
[city.py](https://github.com/billhong6981/AirBnB_clone/blob/master/models/city.py) | File containing the `City` class.
[place.py](https://github.com/billhong6981/AirBnB_clone/blob/master/models/place.py) | File containing the `Place` class.
[review.py](https://github.com/billhong6981/AirBnB_clone/blob/master/models/review.py) | File containing the `Review` class.
[state.py](https://github.com/billhong6981/AirBnB_clone/blob/master/models/state.py) | File containing the `State` class.
[user.py](https://github.com/billhong6981/AirBnB_clone/blob/master/models/user.py) | File containing the `User` class.

Files in engine | Description
--- | ---
[file_storage.py](https://github.com/billhong6981/AirBnB_clone/blob/master/models/engine/file_storage.py) |File containing the source code for the storage engine.

## Final Product
![Screenshot of the Final AirBnB page](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/8-index.png)

## Testing :poop:
To perform unittesting for the console, please use the following commands:
```
python3 -m unittest discover tests
```
You can also test file by file by using this command:
```
python3 -m unittest tests/test_models/test_base_model.py
```

## Bugs :bug:
We have not implemented all the known unit tests often found in similiar AirBnB clone projects.

### About :frog:
All files were created and compiled on `Ubuntu 14.04.4 LTS` using `GCC 4.8.4`

## Authors :koala:
- **Bill Huang** - [billhong6981](https://github.com/billhong6981) :cat:
- **Jun Zhu** - [VieetBubbles](https://github.com/VieetBubbles) :hamster:

## Acknowledgments :turtle:
- **David Kwan** - [dwkwan](https://github.com/dwkwan) :goat: