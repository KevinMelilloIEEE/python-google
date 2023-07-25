#!/usr/bin/env python3
import os.path
from ldap3 import Server, Connection, SAFE_SYNC, ObjectDef, AttrDef, Reader, Writer, ALL

# Global Variables
basedn = ''
staffbasedn = ''
memberbasedn = ''

# Creates a connection with LDAP, reading the connection info from the credentials file
# include needed: from ldap import connectLDAP
# conn = connectLDAP()
def connectLDAP():
    global basedn,staffbasedn,memberbasedn
    ldapInfo = os.path.expanduser('~/python-google-data/ldap-creds')
    with open(ldapInfo) as f:
      for line in f:
        head, sep, tail = line.partition(':')
        if head == 'uid':
          uid = 'uid=' + tail.strip()
        if head == 'password':
          pWord = tail.strip()
        if head == 'server':
          ldapServer = tail.strip()
        if head == 'staffbasedn':
          staffbasedn = tail.strip()
        if head == 'memberbasedn':
          memberbasedn = tail.strip()
    conn = Connection(ldapServer, uid, pWord, client_strategy=SAFE_SYNC, auto_bind=True)
    return conn

# Searches LDAP for specified fields using mailalias
# include needed: from ldap import ldapSearch
# ldapRecord = ldapSearch(mailalias)
def ldapSearch(mailalias):
  conn = connectLDAP()
  ldapRecord = conn.search(staffbasedn, '(mailalias=' + mailalias + ')', attributes=['sn', 'givenName', 'manager', 'gaid', 'telephoneNumber'])
  return ldapRecord

def ldapInfo(mailalias):
  conn = connectLDAP()
  ldapRecord = conn.search(staffbasedn, '(mailalias=' + mailalias + ')', attributes=['manager', 'title', 'department', 'division'])
  return ldapRecord

def ldapEmployeeType(email):
  conn = connectLDAP()
  ldapRecord = conn.search(staffbasedn, '(mail=' + email + ')', attributes=['employeeType'])
  return ldapRecord

# Searches LDAP for specified fields using dn
# include needed: from ldap import ldapDN
# ldapRecord = ldapDN(dn)
def ldapDN(dn):
  conn = connectLDAP()
  ldapRecord = conn.search(basedn, '(distinguishedname' + dn + ')', attributes=['sn', 'givenName', 'manager', 'gaid', 'telephoneNumber'])
  return ldapRecord

def ldapNumber(siebcustid):
  conn = connectLDAP()
  ldapRecord = conn.search(memberbasedn, '(siebcustid=' + siebcustid + ')', attributes=['sn', 'givenName', 'gaid', 'ReservedMailAliases', 'MailAliasCreateDate', 'MailAliasStatus', 'MailAliasUpdateDate'])
  return ldapRecord
