| Problem Statement:                                           |
| ------------------------------------------------------------ |
| A  command line interface project that has following features |
|                                                              |
| This  will give following menu                               |
| 1. List Friends                                              |
| 2. Create Friends                                            |
| 3. Delete Friends                                            |
|                                                              |
| User  Input: ??                                              |
|                                                              |
| If user enters 1, they list  all the friends                 |
| If user enters 2, they can  create a friend from command line with friend information |
| If user enters 3, they can put  in a number of the friend from the list and delete it |
|                                                              |
| Requirements                                                 |
| A friend  will have the first name, lastname and a phone number |
| Store the information in file                                |
| ID should be auto generated                                  |
| Use the OOPS concept to build  (classmethods, staticmethods, etc) |
| Data Validation                                              |
| Create log file at each run                                  |
| Unit Testing                                                 |
|                                                              |
| Submission                                                   |
| Push the code to public git  repository and share the link   |
| Create requirements.txt to  install all the python libraries used |
| Create readme file and mention  all the steps to run the application code |
|                                                              |

**How does it work?**

You need to have Python installed on your computer.

Create a folder on your local computer and copy the files from the repository.

Usually you create a virtual environment here.

In this folder you must run the command : `pip install -r requirements.txt`

To run the application you must run: python Friends.py with line arguments:

First argument (the option) is mandatory

*1* is for list friends

*2* is for adding a friend

*3* is for deleting a friend

depending on the option you must provide one or more optional arguments:

*-File*  represents the file name which contains the friends (to be listed)

*-Name* represents the name of the friend (to be added)

*-Last* represents the last name of the friend (to be added)

*-Phone* represents the phone of the friend (to be added)

*-Id* represents the id of the friend (to be deleted)

Example:

`python Friends.py 1 -File Friends.db` will list friends from file Friends.db

`python Friends.py 2 -Name Jane -Last Doe -Phone 555-888` will add a new friend to the file (if not exist before)

`python Friends.py 3 -Id 4`  will delete friend with Id=4

**Ways to improve:**

validation of data based on regexp

multiple data formats (add csv)

accept list of phones for a friend

...

