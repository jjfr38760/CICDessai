#!/usr/bin/python
import sys


def login_auth_github(vault_addr, vault_ca, github_pat):
     vault_token = vault_addr + vault_ca + github_pat
     return vault_token


def get-sa-key(vault_addr, vault_ca, github_pat):	
     vault_token = login_auth_github(vault_addr, vault_ca, github_pat)
     sa_key = vault_token + "good job"
     return sa_key

if __name__ == '__main__':
    return get-sa-key(*sys.argv[1:])
