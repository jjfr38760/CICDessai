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
     global vault_token
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
   get_sa_key(*sys.argv[1:])

