#!/usr/bin/python
import sys
import requests
import json



def login_auth_github(vault_addr, vault_ca, github_pat):
     print("vault_addr ", vault_addr)
     print("vault_ca ", vault_ca)
     print("github_pat ", github_pat)
     addr = vault_addr + '/v1/auth/github/FRA-CES-IAC/login'
     response = requests.post(
           addr, verify=vault_ca,
           data=json.dumps({"token": github_pat})
     )
     response_body = response.json()
     #print(response_body)
     #global vault_token
     vault_token = response_body["auth"]["client_token"]
     #print(vault_token)
     return vault_token


def get_sa_key(vault_addr, vault_ca, github_pat):
     vault_token = login_auth_github(vault_addr, vault_ca, github_pat)
     addr = vault_addr + 'v1/gcp/key/my-key-roleset'
     response = requests.get(
           addr, verify=vault_ca,
           headers={'X-Vault-Token': vault_token},
     )
     response_body = response.json()
     sa_key = response_body["data"]["private_key_data"]
     print(sa_key)
     return sa_key


if __name__ == '__main__':
#   get_sa_key(*sys.argv[1:])
     global vault_ca     
     vault_ca="-----BEGIN CERTIFICATE-----
MIIDHjCCAgagAwIBAgIQZ7daAePFpCN+/IluVIeGczANBgkqhkiG9w0BAQsFADAp
MRQwEgYDVQQKEwtBdG9zIEFnYXJpazERMA8GA1UEAxMIYXRvcy5uZXQwHhcNMjEw
NDIxMTQwOTUxWhcNMjIwNDIxMTQwOTUxWjApMRQwEgYDVQQKEwtBdG9zIEFnYXJp
azERMA8GA1UEAxMIYXRvcy5uZXQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
AoIBAQCrKMapXRQxxlo1HNJUl18W3QF7sdVlHXIMz47QfdIu6kdfgH8Hr9odPDKa
2sZCl1uqevbWshn4ewdqV1IvFmJoEidYLzvgNNH9r/Is9EwM4/DQjhWQdFkSFKUU
KXJGKl6QunA19FmnyhbJfP/96ikfWPLCsoJPbCDYLv1rQnf9bX+7LnjohlJqVCzp
k0Waw+CRSJ4GTuFMOlwnLGHPV8rbhTjsSVaEjATEm0IkZ8ASgrWWkr0s55UDFEnp
BqLjwR8bEuC0/7j2osBSjABQoeL7lqyx7V8VQIoonZ+Elhx2Fhet7NrOLPzUoQn/
3cTIg+bwkw45iBrOKa7YJcJIeWHxAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwICpDAP
BgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBToPm13S6mDt6ZGRA/w0CD/5HKHWTAN
BgkqhkiG9w0BAQsFAAOCAQEAZYg+IJ9LAjs24btMhDZttvVQD/DOU7F1K9yXER+S
nUccoqO/GkLcnGBS/sANksewQgZP/1/PSKZRSc/7IK1gdk7qhJXJ6JIPTf5Qka46
DE2KREfmsPqaEAHUvOX2/cY28JKGJWCGqwkC4rne4fNvzpaA7RT/TEOkSCaQkQRE
RIzTXiFl1KeDBGgKwPhZGrzjs00Si8GmB11j7NOqN95jXNLsZrMfHqL6U93QpxyD
DefT2Rv4QgQON0xT4SBngUVhvzT3w0f08G3MyrERP3Y9o6cwEMPQWZzdrtJGXz14
NsA4gl/uPGdU8pb6ZBOKJ2VXNKxS/+/CpblCOx3BQPg5AQ==
-----END CERTIFICATE-----"
   #get_sa_key(sys.argv[1], sys.argv[2], sys.argv[3])
   get_sa_key(sys.argv[1], vault_ca, sys.argv[3])


