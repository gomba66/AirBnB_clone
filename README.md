# AirBnB clone - The console 👨‍💻

![simple_shell]()
## Table of Contents

- [Description](#Description)
- [Environment](#Environment)
- [Authors](#Authors)
- [Requirements](#Requirements)
- [File Contents](#FileContents)
- [Usage and Installation](#UsageandInstallation)
- [Compilation](#Compilation)
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
|[path.c](./path.c) | finds the directory a command is located at |
|[strings1.c](./strings1.c) | functions strings 1 |
|[strings2.c](./strings2.c) | functions strings 2 |
|[token.c](./token.c) | parses strings into tokens |




### Usage and Installation 🛠️
Clone the repository, compile with compilation flags, listed below, then run the executable.
```
$ git clone https://github.com/------/simple_shell.git
```
### Compilation 🔧
This code was compiled this way:
` $ gcc -Wall -Werror -Wextra -pedantic *.c -o hsh `


###### Example usage

```
vagrant@vagrant-ubuntu-trusty-64:~/holbertonschool-low_level_programming/shelll$ ./hsh
$ ls
#README.md#  _getline.c~  build_ins.c	 holberton.h  no_file.c		     test_results
README.md    _llops.c	    build_ins.c~  hsh	            path_handler.c        tokensplit.c
_freeops.c   _realloc.c   builtins.c	   main.c       preparation_functions
_getenv.c    _strops.c	    ctrl.c	    man_shell    shelltest
_getline.c   atoi.c	      executeprog.c  man_shell~   test_2
$
```
```
vagrant:simple_shell$ ./hsh
$ pwd
/home/vagrant/simple_shell
$
```
```
vagrant@vagrant-ubuntu-trusty-64:~/holbertonschool-low_level_programming/shelll$ ./hsh
$ env
XDG_SESSION_ID=2
TERM=cygwin
SHELL=/bin/bash
SSH_CLIENT=10.0.2.2 60471 22
SSH_TTY=/dev/pts/0
USER=vagrant
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arj=01;31:*.taz=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lz=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.axa=00;36:*.oga=00;36:*.spx=00;36:*.xspf=00;36:
MAIL=/var/mail/vagrant
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
PWD=/home/vagrant/simple_shell
LANG=en_US.UTF-8
SHLVL=1
HOME=/home/vagrant
LOGNAME=vagrant
SSH_CONNECTION=10.0.2.2 60471 10.0.2.15 22
LESSOPEN=| /usr/bin/lesspipe %s
XDG_RUNTIME_DIR=/run/user/1000
LESSCLOSE=/usr/bin/lesspipe %s %s
OLDPWD=/home/vagrant
_=./hsh
$
```
### Version 📌
simple_shell - version 9.6

### Acknowledgements 🎁
All the peers that contributed with their knowledge

### Authors  ✒️
Laura Peralta, Julian Gaitan
