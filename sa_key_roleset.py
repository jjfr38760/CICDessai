#!/usr/bin/python
import sys


def login_auth_github(vault_addr, vault_ca, github_pat):
     vault_token = vault_addr + vault_ca + github_pat
     print(vault_token)
     return vault_token


def get_sa_key(vault_addr, vault_ca, github_pat):	
     vault_token = login_auth_github(vault_addr, vault_ca, github_pat)
     sa_key = vault_token + "good job"
     print(sa_key)
     return sa_key

if __name__ == '__main__':
    get_sa_key(*sys.argv[1:])
