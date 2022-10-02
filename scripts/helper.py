from brownie import network, config, accounts

FORKED_LOCAL_ENVIRONMETNS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMETNS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def get_verify_status():
    return config["networks"][network.show_active()].get("verify")
