import os
import json
import subprocess


REGISTRATOR_NAME = os.getenv('REGISTRATOR_NAME')
REGISTRATOR_WIF = os.getenv('REGISTRATOR_WIF')


def create_account(name, owner_pub, active_pub):
    command = [
        "node",
        "faucet/new_account.js",
        name, owner_pub, active_pub
    ]

    r = subprocess.run(command, stdout=subprocess.PIPE).stdout
    return json.loads(r.decode("utf-8"))


# from eosiopy import eosio_config
# from eosiopy.eosioparams import EosioParams
# from eosiopy.nodenetwork import NodeNetwork
# from eosiopy.rawinputparams import RawinputParams
# def create_account(name, owner_pub, active_pub):
#     eosio_config.url = os.getenv('EOS_NODE_URL', 'https://eost.travelchain.io')
#     eosio_config.port = os.getenv('EOS_NODE_PORT', '443')
#
#
#     print(name)
#     raw = RawinputParams('newaccount', {
#             'creator': REGISTRATOR_NAME,
#             'name': name,
#             'memo': '',
#             'owner': owner_pub,
#             'active': active_pub
#         }, 'eosio', f'{REGISTRATOR_NAME}@active')
# 
#     eosiop_arams = EosioParams(raw.params_actions_list, REGISTRATOR_WIF)
#     r = NodeNetwork.push_transaction(eosiop_arams.trx_json)
#     print(eosiop_arams.trx_json)
# 
#     return r
