#!/usr/bin/env python
"""
Provides all account functions
"""
import json
from time import sleep
import requests
from .environment import BASE_TIMEOUT, LIMIT_TIMEOUT, SLEEP_TIME, OFFSET, RETRYING_TIME, LIMIT_RETRYING_TIMES

def get_account_list(self, content_range="0-999"):
    """
    Get a list of all accounts.

    :return: string list of account (stake address: stake1...  bech32 format) IDs.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            custom_headers = {"Range": str(content_range)}
            address_list = requests.get(self.ACCOUNT_LIST_URL, headers = custom_headers, timeout=timeout)
            address_list = json.loads(address_list.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return address_list


def get_account_info(self, *args):
    """
    Get the account information for given stake addresses (accounts).

    :param str args: staking address/es in bech32 format (stake1...).
    :return: list with all address data.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            get_format = {"_stake_addresses": [args] }
            accounts_info = requests.post(self.ACCOUNT_INFO_URL, json= get_format , timeout=timeout)
            accounts_info = json.loads(accounts_info.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return accounts_info


def get_account_info_cached(self, *args):
    """
    Get the account information for given stake addresses (accounts).

    :param str args: staking address/es in bech32 format (stake1...).
    :return: list with all address data.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            get_format = {"_stake_addresses": [args] }
            accounts_info = requests.post(self.ACCOUNT_INFO_URL_CACHED, json= get_format , timeout=timeout)
            accounts_info = json.loads(accounts_info.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return accounts_info


def get_account_rewards(self, *args):
    """
    Get the full rewards history (including MIR) for given stake addresses (accounts).

    :param str args: Cardano staking address (reward account) in bech32 format (stake1...)
    :param int args: Epoch Number, has to be last parameter (optional).
    return: list with all account rewards.
    :rtype: list.
    """
    epoch = args[len(args)-1]
    timeout = BASE_TIMEOUT

    while True:
        try:
            if not isinstance(epoch, int):
                get_format = {"_stake_addresses": [args] }
                rewards = requests.post(self.ACCOUNT_REWARDS_URL, json= get_format , timeout=timeout)
                rewards = json.loads(rewards.content)
            else:
                get_format = {"_stake_addresses": [args], "_epoch_no": epoch}
                rewards = requests.post(self.ACCOUNT_REWARDS_URL, json= get_format , timeout=timeout)
                rewards = json.loads(rewards.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return rewards


def get_account_updates(self, *args):
    """
    Get the account updates (registration, deregistration, delegation and withdrawals) for given \
    stake addresses (accounts)

    :param str args: staking address/es in bech32 format (stake1...)
    :return: list with all account updates.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT
    while True:
        try:
            get_format = {"_stake_addresses": [args]}
            updates = requests.post(self.ACCOUNT_UPDATES_URL, json= get_format, timeout=timeout)
            updates = json.loads(updates.content)
            break
        
        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return updates


def get_account_addresses(self, *args):
    """
    Get all addresses associated with given staking accounts.
    :param str args: staking address/es in bech32 format (stake1...)
    :return: list with all account addresses.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT
    while True:
        try:
            get_format = {"_stake_addresses": [args]}
            addresses = requests.post(self.ACCOUNT_ADDRESSES_URL, json=get_format, timeout=timeout)
            addresses = json.loads(addresses.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return addresses


def get_account_assets(self, *args):
    """
    Get the native asset balance of given accounts.
    :param str args: staking address/es in bech32 format (stake1...)
    :return: list with all account assets.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT
    retriyng_time = RETRYING_TIME

    while True:
        try:
            get_format = {"_stake_addresses": [args]}
            assets = requests.post(self.ACCOUNT_ASSETS_URL, json= get_format, timeout=timeout)
            assets = json.loads(assets.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

        except json.decoder.JSONDecodeError as decode_error:
            print(f"Exception Decode: Payload too heavy. {decode_error}")
            sleep(SLEEP_TIME)
            retriyng_time += 1
            print(f"Retriyng one more time...({retriyng_time} times)")
            if retriyng_time >= LIMIT_RETRYING_TIMES:
                print("Reached limit of attempts")
                break

    return assets

## Alternative to Paginate all list automately
def get_account_assets_2(self, *args):
    """
    Get the native asset balance of given accounts.
    :param str args: staking address/es in bech32 format (stake1...)
    :return: list with all account assets.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT
    offset= OFFSET
    retriyng_time = RETRYING_TIME
    total_assets= []

    while True:
        while True:
            try:
                get_format = {"_stake_addresses": [args]}
                assets = requests.post(self.ACCOUNT_ASSETS_URL + str(offset), json= get_format, timeout=timeout)
                assets = json.loads(assets.content)
                break

            except requests.exceptions.ReadTimeout as timeout_error:
                print(f"Exception: {timeout_error}")
                if timeout < LIMIT_TIMEOUT:
                    timeout= timeout + 10
                else:
                    print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                    break
                print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

            except json.decoder.JSONDecodeError as decode_error:
                print(f"Exception Decode: Payload too heavy. {decode_error}")
                sleep(SLEEP_TIME)
                retriyng_time += 1
                print(f"Retriyng one more time...({retriyng_time} times)")
                if retriyng_time >= LIMIT_RETRYING_TIMES:
                    print("Reached limit of attempts")
                    break

        total_assets += assets
        if len(total_assets) < 1000:
            break
        offset += len(total_assets)

    return total_assets


def get_account_history(self, *args):
    """
    Get the staking history of given stake addresses (accounts).

    :param str address: staking address in bech32 format (stake1...)
    return: list with all account history.
    :rtype: list.
    """
    epoch = args[len(args)-1]
    timeout = BASE_TIMEOUT

    while True:
        try:
            if not isinstance(epoch, int):
                get_format = {"_stake_addresses": [args] }
                history = requests.post(self.ACCOUNT_HISTORY_URL, json= get_format , timeout=timeout)
                history = json.loads(history.content)
            else:
                get_format = {"_stake_addresses": [args], "_epoch_no": epoch}
                history = requests.post(self.ACCOUNT_HISTORY_URL, json= get_format , timeout=timeout)
                history = json.loads(history.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return history
