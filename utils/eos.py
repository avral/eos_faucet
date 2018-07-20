import os

from eosiopy import eosio_config
from eosiopy.nodenetwork import NodeNetwork


eosio_config.url = os.getenv('EOS_NODE_URL', 'https://eost.travelchain.io')
eosio_config.port = os.getenv('EOS_NODE_PORT', '443')


def account_exists(account_name):
    return 'account_name' in NodeNetwork.get_account({
        'account_name': account_name
    })
