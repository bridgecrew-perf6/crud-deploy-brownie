#! /usr/bin/python3
'''deploying contract'''
#import os
from brownie import Crud, accounts, network, config

def get_network():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])
def deploy_crud():
    '''deploy function'''
    #using ganache
    account = get_network()

    #using brownie to password encrypt the key
    #account = accounts.load("KEY")

    #using .env file
    #account =accounts.add(os.getenv("KEY"))

    #using special .yaml config
    #account = accounts.add(config['wallets']['from_key'])
    print('Deploying contract...')
    crud = Crud.deploy({
        'from': account
        })
    print('Getting the stores valus...')
    store_value = crud.retrieve()
    print(store_value)


    transaction = crud.store(15, {'from':account})
    transaction.wait(1)
    updated_crud = crud.retrieve()
    print(updated_crud)

def main():
    '''calling the deploy function'''
    deploy_crud()
