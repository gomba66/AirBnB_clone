# AirBnB clone - The console 👨‍💻

![simple_shell]()
## Table of Contents

- [Description](#Description)
- [Environment](#Environment)
- [Authors](#Authors)
- [Requirements](#Requirements)
- [File Contents](#FileContents)
- [Usage and Installation](#UsageandInstallation)
- [Console](#Console)
- [Example usage](#Exampleusage)
- [Built With](#built-with)
- [Acknowledgments](#acknowledgments)

### Description 📄
With this project console (AirBnB clone - The console), we want to be able to manage the objects of our project:

 - Create a new object (ex: a new User or a new Place)
 - Retrieve an object from a file, a database etc…
 - Do operations on objects (count, compute stats, etc…)
 - Update attributes of an object
 - Destroy an object

### Environment 💻
AirBnB clone - The console  was developed on Ubuntu 18.04 LTS and Python3

## Further information 🚀
For further information please refer to [Authors](./AUTHORS)

## Requirements 📋
Basic knowledge about Python programming language Basic knowledge about shell and linux A text editor software

## Built with ⚙️
Python3 programming language

## File Contents
The repository contains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[man_1_simple_shell](./man_1_simple_shell) | Man page for the created shell |
|[main.c](./main.c) | The main function |
|[builtins.c](./builtins.c) | Handles exit, env built-in commands |
|[command.c](./command.c)| Actions executes given input into the shell |
|[shell.h](./shell.h)| Header file containing all function prototypes and struct declarations |
|[error_msg.c](./error_msg.c) | Containing function, that prints error messages |
|[findpath.c](./findpath.c) | searches the environment for PATH |
|[fix_token.c](./fix_token.c) | concatenates 2 strings adding a backslash and null byte |
|[getline_func.c](./getline_func.c) | reads input from user |



### Usage and Installation 🛠️
Clone the repository
```
root@ubuntu:~$ git clone https://github.com/JulianDavidG07/AirBnB_clone.git
```

### Console 🔧
To test the console just run:
```
root@ubuntu:~/AirBnB$ ./console.py `
```

###### Example usage

```
root@ubuntu:~/AirBnB$ ./console.py `
```
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb) create
** class name missing **
(hbnb) create Amenity
aacbe2ca-daaa-49f3-b01f-99ab7eaacc77
(hbnb) destroy
** class name missing **
(hbnb) destroy Amenity
** instance id missing **
(hbnb) show Amenity
** instance id missing **
(hbnb) show Amenity aacbe2ca-daaa-49f3-b01f-99ab7eaacc77
[Amenity] (aacbe2ca-daaa-49f3-b01f-99ab7eaacc77) {'updated_at': datetime.datetime(2018, 6, 14, 12, 10, 16, 276535), 'created_at': datetime.datetime(2018, 6, 14, 12, 10, 16, 276466), 'id': 'aacbe2ca-daaa-49f3-b01f-99ab7eaacc77'}
(hbnb) destroy Amenity aacbe2ca-daaa-49f3-b01f-99ab7eaacc77
(hbnb) show Amenity aacbe2ca-daaa-49f3-b01f-99ab7eaacc77
** no instance found **
(hbnb)
(hbnb) help quit
Quit command to exit the program
(hbnb)
(hbnb) show User
** instance id missing **
(hbnb) show User (24ed1cb3-8f8a-4081-878e-60fdce47a42d)
** no instance found **
(hbnb) show User 24ed1cb3-8f8a-4081-878e-60fdce47a42d
[User] (24ed1cb3-8f8a-4081-878e-60fdce47a42d) {'password': 'root', 'last_name': 'Holberton', 'created_at': datetime.datetime(2018, 6, 12, 13, 7, 27, 53126), 'updated_at': datetime.datetime(2018, 6, 12, 13, 7, 27, 53158), 'email': 'airbnb@holbertonshool.com', 'id': '24ed1cb3-8f8a-4081-878e-60fdce47a42d', 'first_name': 'Betty'}
(hbnb)
(hbnb) User.show(24ed1cb3-8f8a-4081-878e-60fdce47a42d)
[User] (24ed1cb3-8f8a-4081-878e-60fdce47a42d) {'password': 'root', 'last_name': 'Holberton', 'created_at': datetime.datetime(2018, 6, 12, 13, 7, 27, 53126), 'updated_at': datetime.datetime(2018, 6, 12, 13, 7, 27, 53158), 'email': 'airbnb@holbertonshool.com', 'id': '24ed1cb3-8f8a-4081-878e-60fdce47a42d', 'first_name': 'Betty'}
(hbnb)
(hbnb) User.count()
12
(hbnb) Amenity.show()
** instance id missing **
(hbnb) Amenity.show(58ceeeb9-7a28-4554-af76-f5dff402be70)
[Amenity] (58ceeeb9-7a28-4554-af76-f5dff402be70) {'id': '58ceeeb9-7a28-4554-af76-f5dff402be70', 'created_at': datetime.datetime(2018, 6, 13, 13, 57, 34, 149032), 'updated_at': datetime.datetime(2018, 6, 13, 13, 57, 34, 149117)}
(hbnb) User.show(deaf744b-c904-4b56-8823-71acc18a529c)
[User] (deaf744b-c904-4b56-8823-71acc18a529c) {'created_at': datetime.datetime(2018, 6, 13, 9, 16, 53, 138370), 'updated_at': datetime.datetime(2018, 6, 13, 9, 16, 53, 138489), 'id': 'deaf744b-c904-4b56-8823-71acc18a529c', 'first_name': 'Ben'}
(hbnb) User.update("deaf744b-c904-4b56-8823-71acc18a529c", 'first_name', "Bimpe")
(hbnb) User.show(deaf744b-c904-4b56-8823-71acc18a529c)
[User] (deaf744b-c904-4b56-8823-71acc18a529c) {'created_at': datetime.datetime(2018, 6, 13, 9, 16, 53, 138370), 'updated_at': datetime.datetime(2018, 6, 13, 9, 16, 53, 138489), 'id': 'deaf744b-c904-4b56-8823-71acc18a529c', 'first_name': 'Bimpe'}
(hbnb)
```
```
(hbnb) quit
```
```
or
```
```
(hbnb) EOF
```
```
root@ubuntu:~/AirBnB$
```
### Version 📌
(AirBnB clone - The console) --version 1.0

### Acknowledgements 🎁
All the peers that contributed with their knowledge

### Authors  ✒️
Daniel Ramirez, Julian Gaitan
