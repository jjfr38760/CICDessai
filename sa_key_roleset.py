#!/usr/bin/python
import sys
import requests
import json



def login_auth_github(vault_addr, vault_ca, github_pat):
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
   with open('vault_ca.txt','r') as file:
     vault_ca = file.read()
   vault_token = login_auth_github(sys.argv[1], vault_ca, sys.argv[3])
   print(vault_token)


