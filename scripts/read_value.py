from brownie import Crud, accounts, config


def read_contract():
    crud = Crud[-1]
    print(crud.retrieve())


def main():
    read_contract()

