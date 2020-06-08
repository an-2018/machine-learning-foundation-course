# Basic Python Project Setup

## Virtual Environement

Its a convention to work eith python as virtual environements to avoid conflict with the diferent packages from the python package index ([PyPi](https://pypi.org/)) for example.
Also using this method is possible to use **pip** to install the packages used in the projet.

To setup a virtual environement we can follow these comands

```bash
# create a virtual environement
$ python -3 -m venv .venv_name

# activate the virtual environement
$ .ven_name\scripts\activate

# for windows sometimes requires the following comand if the previous one gives a error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# install packages with pip install
$ python -m pip install numpy

# list packages used in the environement
$ pip list

# export package to requirements.txt
$ pip freeze > requirements.txt
$ cat requirements.txt 
```

With this, the projet can be exported to a git repository management and use the requirements.txt file to install the packages.

```bash
# install the packages usin pip
$ pip install -r requirements.txt
```
