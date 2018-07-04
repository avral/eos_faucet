import os
import logging

from apistar import App, Route

from eosiopy import eosio_config
from eosiopy.eosioparams import EosioParams
from eosiopy.nodenetwork import NodeNetwork
from eosiopy.rawinputparams import RawinputParams

from apistar import types, validators

logging.basicConfig(
    level=logging.WARN,
    format="%(asctime)s [%(threadName)s] [%(levelname)s]  %(message)s",
    handlers=[
        # logging.FileHandler("{0}/{1}.log".format(logPath, fileName)),
        logging.StreamHandler()
    ])

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


REGISTRATOR_NAME = os.getenv('REGISTRATOR_NAME')
REGISTRATOR_WIF = os.getenv('REGISTRATOR_WIF')


class EosPubKeyValidator(types.Type):
    # TODO Add validation
    name = validators.String(max_length=12)
    owner_pub = validators.String(max_length=54)
    active_pub = validators.String(max_length=54)


eosio_config.url = os.getenv('EOS_NODE_URL', 'https://eost.travelchain.io')
eosio_config.port = os.getenv('EOS_NODE_PORT', '443')


def create_account(account: EosPubKeyValidator):
    raw = RawinputParams('newaccount', {
            'creator': REGISTRATOR_NAME,
            'name': account.name,
            'owner': account.owner_pub,
            'active': account.active_pub
        }, REGISTRATOR_NAME, f'{REGISTRATOR_NAME}@active')

    eosiop_arams = EosioParams(raw.params_actions_list, REGISTRATOR_WIF)
    r = NodeNetwork.push_transaction(eosiop_arams.trx_json)

    if 'transaction_id' in r:
        logger.info(f'account created: {account.name}')

    return r


routes = [
    Route('/account', method='POST', handler=create_account),
]

app = App(routes=routes)


if __name__ == '__main__':
    if not all([REGISTRATOR_NAME, REGISTRATOR_WIF]):
        logger.critical(
            'REGISTRATOR_NAME & REGISTRATOR_WIF required env variables!'
        )

        raise SystemExit

    host = os.getenv('HOST', '127.0.0.1')
    app.serve(host, 5000, debug=True)
