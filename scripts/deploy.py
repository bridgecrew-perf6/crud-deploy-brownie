'''deploying contract'''
from brownie import accounts
def deploy_crud():
    '''deploy function'''
    account = accounts[0]
    print(account)

def main():
    '''calling the deploy function'''
    deploy_crud()
