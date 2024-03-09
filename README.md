# AirBnB Clone Project

Welcome to the AirBnB clone project! This README provides essential information about the project, including background context, requirements, learning objectives, and execution instructions.

## Background Context

This project involves building an AirBnB clone, starting with developing a command interpreter in Python. The command interpreter will manage various AirBnB objects, including User, State, City, Place, etc. The primary objectives of this project include creating a parent class for object initialization, implementing serialization/deserialization flows, developing storage engines, and conducting unit tests.

### What's a Command Interpreter?

Similar to a Shell, a command interpreter in this context is limited to managing specific objects within the AirBnB project. It allows users to create, retrieve, update, and destroy objects, as well as perform operations and computations on them.

## Learning Objectives

Upon completing this project, you're expected to grasp several key concepts, including:

- Creating a Python package
- Developing a command interpreter using the cmd module
- Implementing Unit testing in a large project
- Serializing and deserializing a Class
- Reading and writing JSON files
- Managing datetime
- Understanding UUIDs
- Using *args and **kwargs
- Handling named arguments in a function

## Requirements

### Python Scripts

- Editors: vi, vim, emacs
- Ubuntu 20.04 LTS with Python 3.8.5
- Scripts end with a newline
- First line of all files: `#!/usr/bin/python3`
- Mandatory README.md file at the root
- Code should adhere to pycodestyle (version 2.8.*)
- All files must be executable
- File length tested using wc
- Documentation for modules, classes, and functions
- Unit tests using the unittest module
- Test files organized within a `tests` folder
- Tests executed using `python3 -m unittest discover tests`

### GitHub

- One project repository per group
- Avoid cloning/forking repositories with the same name before the second deadline to prevent a 0% score

## Execution

The shell should work both in interactive and non-interactive mode:

- Interactive mode:

```bash
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

- Non-interactive mode:

```bash
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

All tests should pass in non-interactive mode using the command: 

```bash
$ echo "python3 -m unittest discover tests" | bash
```

## Conclusion

This README provides a comprehensive overview of the AirBnB clone project, including its objectives, requirements, and execution instructions. It serves as a guide for developers participating in the project.
