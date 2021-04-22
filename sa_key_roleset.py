#!/usr/bin/python
import sys


def login_auth_github(vault_addr, vault_ca, github_pat):
     addr = vault_addr + '/v1/auth/github/FRA-CES-IAC/login'
     response = requests.post(
           addr, verify=vault_ca,
           data=json.dumps({"token": github_pat})
     )
     response_body = response.json()
     vault_token = response_body["auth"]["client_token"]
     return vault_token


def get-sa-key(vault_addr, vault_ca, github_pat):	
     vault_token = login_auth_github(vault_addr, vault_ca, github_pat)
     addr = vault_addr + '/v1/gcp/key/my-key-roleset'
     response = requests.get(
           addr, verify=vault_ca,
           headers={'X-Vault-Token': vault_token},
     )
     response_body = response.json()
     sa_key = response_body["data"]["private_key_data"]
     return sa_key

if __name__ == '__main__':
    return get-sa-key(*sys.argv[1:])
