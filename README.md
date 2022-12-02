# python-google
These are the scripts we use to automate some of our procedures that deal with Google and LDAP

## Step 1: Python 3
You need to make sure you have Python 3 installed. 
([Python Downloads](https://www.python.org/downloads/))

## Step 2: PIP
You need PIP (or PIP3) installed.  On a Mac, this should already be installed with Python3, and is called pip3

## Step 3: Google Client Libraries
You need the Google Client Libraries (which are installed with PIP\PIP3)
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
or
```
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Step 4: Create Google Project
You will need to create a project in the Google Developer Console, allow APIs, and create credentials.
([Python Quickstart](https://developers.google.com/admin-sdk/directory/v1/quickstart/python)))

You are ready to start coding with Python and the Google Client Libraries.
