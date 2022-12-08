# python-google
These are the scripts I developed to automate some of my procedures procedures that deal with Google and LDAP

### Step 1: Python 3
You need to make sure you have Python 3 installed. 
([Python Downloads](https://www.python.org/downloads/))

### Step 2: PIP
You need PIP (or PIP3) installed.  On a Mac, this should already be installed with Python3, and is called pip3

### Step 3: Google Client Libraries
You need the Google Client Libraries (which are installed with PIP\PIP3)
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
or
```
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### Step 4: Create Google Project
You will need to create a project in the Google Developer Console, allow APIs, and create credentials.
([Python Quickstart](https://developers.google.com/admin-sdk/directory/v1/quickstart/python))

You are ready to start coding with Python and the Google Client Libraries.

## Notes
All of my scripts (which will be included in this repository) are in 
```
~/python-google
```
All of my private data (to NOT be included in this repository) is in
```
~/python-google-data
```
This includes any connection details and data files that you must create on your end.  When necessary, I will outline the format of these files, so the code can be used on your end, without releasing any private information.

## googleLib.py
This is a bunch of functions I have developed.  Each function is documented within the code. Here is a small summary of what is included.
```
getCredentials - creates a connection to Google through scopes, and authentication
groupList - grab and return a list of all groups for a specific email address.
getUserInfo - grab and return all user info for a specific email address.
createUser - creates a user based on a specified user record
addAlias - add an alias to an account based on a specific email address
```
### ~/python-google-data/credentials.json
This file is created (and downloaded) from the Google Developer Console for your project. ([Python Quickstart](https://developers.google.com/admin-sdk/directory/v1/quickstart/python))
### ~/python-google-data/token.json
This file is created the first time you run your project.  If you change any of the scopes, you must delete this file, and it will be recreated.
