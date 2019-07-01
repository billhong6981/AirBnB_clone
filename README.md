# AirBnB_clone (The Holberton B&B)
![Image of Hol AirBnB Logo](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20190701%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190701T223807Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=048d405fe03edc6999b7369405a2f967b665a67ff06e099a0a4378cea4737dc0)

## Description
This project was created as part of the 2nd trimester curriculum at [Holberton School](https://www.holbertonschool.com/), San Francisco. We won't be covering the entire process of creating a clone of AirBnB's website. Instead we will do it step by step.

In **this Repository** we will go over the  1st part of the prject: Creating the **console**.

### The Console
If you know what a shell is and how to create one using the C programming language, then you should know what the console is. In our case, we want to be able to manage the objects of our project.

### Data Diagram
![Image of the Data Diagram](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/289/AirBnb_DB_diagramm.jpg)

### Execution
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

### Files
Files in `Model` | Description
--- | ---
[AUTHORS](https://github.com/ethanpasta/simple_shell/blob/master/AUTHORS) | This file store the contact info of all individuals who contributed to the branches of our shell code.
[base_model.py](https://github.com/billhong6981/AirBnB_clone/blob/Dev/models/base_model.py) | Contains the base-class called `BaseModel` that defines all common attributes/methods for other classes. And to be inherited by other classes created in the repo.
[__init__.py](https://github.com/billhong6981/AirBnB_clone/blob/Dev/models/__init__.py) | Create variable called `storage` in order to link our `BaseModel` class  to the `FileStorage` class.

## Final Product
![Screenshot of the Final AirBnB page](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/8-index.png)

### About
All files were created and compiled on `Ubuntu 14.04.4 LTS` using `GCC 4.8.4`

### Authors
- **Bill Huang** [billhong6981](https://github.com/billhong6981)
- **Jun Zhu** - [VieetBubbles](https://github.com/VieetBubbles)

### Acknowledgments
- **David Kwan** [dwkwan](https://github.com/dwkwan)