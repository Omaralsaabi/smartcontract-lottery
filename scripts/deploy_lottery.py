from brownie import Lottery, accounts, config, network
from scripts.helpful_scripts import get_account, get_contract


def deploy_lottery():
    account = get_account()
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
    )


def main():
    deploy_lottery()
