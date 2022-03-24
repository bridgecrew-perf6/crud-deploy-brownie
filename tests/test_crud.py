from brownie import Crud, accounts

def test_deploy():
    #Arrange
    account = accounts[0]
    
    #act
    crud = Crud.deploy({"from" :account})
    starting_value = crud.retrieve()
    expected = 0
    #Assert

    assert starting_value == expected
