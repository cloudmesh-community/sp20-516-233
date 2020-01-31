# Virtual Environment on Windows 10 EDU - Holly Zhang sp20-516-233

## How to get to the home directory?

By default, Command Prompt starts out in the home directory. However if the 
current directory is not the home directory, then the following command can be 
used.

```bash
$ cd %HOMEPATH%
```

## How to create a python environment?

The command below creates a python environment in a directory called ENV3.

```bash
$ python -m venv ENV3
```

## How to activate the environment?

The following code is used to activate the environment. 

```bash
$ ENV3\Scripts\activate
```

## How to deactivate the environment?

To deactivate the python environment, type the command below in Command Prompt.

```bash
(ENV3)$ deactivate
```






