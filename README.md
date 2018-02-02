# GMAIL REST API

## Requirements

You need to install several things before starting:
* pip for python 3
* google cloud api for python

```
sudo apt install python3-pip
pip3 install --upgrade google-api-python-client
```

## Informations

For this course we will use a specific mail adress created for the occasion.

**EMAIL** : onfaitlescours@gmail.com

**PASS**  : bioinformatique

## Initialization

Clone the git repository :

```
git clone https://github.com/Zarete/CoursInverseREST
```

First you need to set up the credentials by running the unmodified script **main.py**

```
python3 main.py
```

A pop-up window will appear and you add to use the email and password given previously.

If everything is fine you should have a new page notifying that the connection is allowed.

## Exercises

You have 3 tasks (try to code the first one at list).

Each function have to be filled up with your own code.

Prototypes have been given in order to speed up the process.

### Exercise 1

Goal : get all the labels existing for the mailbox

### Exercise 2

Goal : Display all the messages contained into the 'INBOX' folder

### Exercise 3 (for the glory)

Goal : Display only the messages coming FROM a given mail address