#!/usr/bin/env python3
import sys
sys.dont_write_bytecode = True
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Global Variables
lCreds = os.path.expanduser('~/python-google-data/ldap-creds')
gCreds = os.path.expanduser('~/python-google-data/credentials.json')
gToken = os.path.expanduser('~/python-google-data/token.json')
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user', 'https://www.googleapis.com/auth/admin.directory.group', 'https://www.googleapis.com/auth/gmail.settings.sharing']

# Create connection to Google through scopes and OAuth2
# include needed: from googleLib import getCredentials
# service = getCredentials()
def getCredentials():
  creds = None
  if os.path.exists(gToken):
    creds = Credentials.from_authorized_user_file(gToken, SCOPES)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(gCreds, SCOPES)
      creds = flow.run_local_server(port=0)
    with open(gToken, 'w') as token:
      token.write(creds.to_json())
  service = build('admin', 'directory_v1', credentials=creds)
  return service

# Get groups for a specific email address, returns as dictionary
# include needed: from googleLib import groupList
# groupDump = groupList(email)
def groupList(email):
    service = getCredentials()
    groupList = service.groups().list(userKey=email).execute()
    group = groupList['groups']
    return group

# Get user information for a specific email address, returns as dictionary
# include needed: from googleLib import getUser
# userDump = getUser(email)
def getUserInfo(email):
  service = getCredentials()
  userDump = service.users().get(userKey=email, projection='full', viewType='admin_view').execute()
  return userDump

# Get group information for a specific group email address, returns as dictionary
# include needed: from googleLib import getGroup
# groupDump = getGroup(email)
def getGroup(email):
  service = getCredentials()
  groupDump = service.groups().get(groupKey=email).execute()
  return groupDump

# Get all members for a specific group email address, returns as dictionary
# include needed: from googleLib import getMembers
# membersDump = getMembers(email)
def getMembers(email):
  service = getCredentials()
  membersDump = service.members().list(groupKey=email).execute()
  return membersDump

# This will add a specific email address to a specific group, returns as the result code
# include needed: from googleLib import addToGroup
# groupAdd = addToGroup(group, email)
def addToGroup(group,email):
  print(group, email)
  service = getCredentials()
  groupKey = {"email": email, "kind": "admin#directory#member", "role": "MEMBER"}
  groupDump = service.members().insert(groupKey=group, body=groupKey).execute()
  return groupDump

# Create a user based on the userRecord
# include needed: from googleLib import createUser
# status = createUser(userRecord)
# userRecord is a dictionary with the following mandatory items
# userRecord = {'primaryEmail': <email address>, 'password': <password>, 'name': { 'givenName': <firstName>, 'familyName': <lastName> }, 'orgUnitPath': <orgUnit>}
def createUser(userRecord):
  service = getCredentials()
  status = service.users().insert(body=userRecord).execute()
  return status

# Add an alias to a user account using the email address as the userKey, and the aliasRecord which is a JSON
# include needed: from googleLib import addAlias
# status = addAlias(emailAddress, aliasRecord)
# aliasRecord is a JSON with the following mandatory items
# aliasRecord = { 'alias': 'emailalias@ieee.org', 'alias': 'emailtwo@ieee.org }
def addAlias(emailAddress, aliasRecord):
  service = getCredentials()
  status = service.users().aliases().insert(userKey=emailAddress, body=aliasRecord).execute()
  return status
