from brownie import Crud, accounts

def test_deploy():
    '''test'''
    #Arrange
    account = accounts[0]
    
    #act
    crud = Crud.deploy({"from" :account})
    starting_value = crud.retrieve()
    expected = 0
    
    #Assert
    assert starting_value == expected


def test_updating():
    #Arrange
    account = accounts[0]

    #Act
    crud = Crud.deploy({'from' :account})
    expected = 15
    crud.store(expected, {'from' : account})
    
    #Assert
    assert expected == crud.retrieve()
