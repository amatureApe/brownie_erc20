from brownie import network, accounts, OurToken
from scripts.helper import (
    get_account,
    get_verify_status,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from web3 import Web3

INITIAL_SUPPLY = Web3.toWei(10000, "ether")


def deploy():
    account = get_account()
    token = OurToken.deploy(
        INITIAL_SUPPLY, {"from": account}, publish_source=get_verify_status()
    )
    print(f"Token launched at {token.address}")


def main():
    deploy()
