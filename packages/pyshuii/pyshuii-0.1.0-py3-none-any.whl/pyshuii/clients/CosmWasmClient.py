# https://github.com/cosmos/chain-registry
from cosmpy.aerial.client import LedgerClient, NetworkConfig
from cosmpy.aerial.contract import LedgerContract

configs = {
    'JUNO-1': {
        "url": "rest+https://lcd-juno.itastakers.com",
        "fee_minimum_gas_price": 0.0025,
        "fee_denomination": "ujuno",
        "staking_denomination": "ujuno",
    },
    'STARGAZE-1': {
        "url": "rest+https://rest.stargaze-apis.com/",
        "fee_minimum_gas_price": 0.0025,
        "fee_denomination": "ustars",
        "staking_denomination": "ustars",
    },
    'OSMOSIS-1': {
        "url": "rest+https://rest-osmosis.ecostake.com",
        "fee_minimum_gas_price": 0.0001,
        "fee_denomination": "uosmo",
        "staking_denomination": "uosmo",
    }
}


class CosmWasmClient:
    def __init__(self, chain_id):
        config = configs[chain_id.upper()]
        self.ledger = LedgerClient(
            NetworkConfig(
                chain_id=chain_id.lower(),
                url=config['url'],
                fee_minimum_gas_price=config['url'],
                fee_denomination=config['fee_denomination'],
                staking_denomination=config['staking_denomination'],
            )
        )
        self.contract = None

    def getCollectionMetadata(self, address):
        try:
            self.contract = LedgerContract(
                path=None, client=self.ledger, address=address)

            contract_info = self.contract.query({
                'contract_info': {},
            })

            token = self.contract.query({
                'all_tokens': {
                    'limit': 1
                }
            })['tokens'][0]

            total_supply = self.contract.query({
                'num_tokens': {}
            })

            token_metadata = self.contract.query({
                'nft_info': {
                    'token_id': token
                }
            })

            token_url = token_metadata['token_uri']
            token_uri = self.standardize_uri(token_url)

            return {
                'address': address,
                'name': contract_info['name'],
                'symbol': contract_info['symbol'],
                'token_uri': token_uri,
                'starting_index': int(token[-1]),
                'total_supply': int(total_supply['count']),
                'suffix': (token_url and token_url[len(token_url) - 5:] == '.json') and '.json' or None
            }
        except Exception as e:
            print(e)
            raise Exception(
                "CosmWasmClient: Unable to get collection metadata.")

    def standardize_uri(self, uri):
        if uri:
            uri = uri.split('/')
            uri = '/'.join(uri[:-1])
        return uri

    @staticmethod
    async def retrieve(contract, job_id, job, retry_limit, results, **kwargs):
        error_message = None
        for _ in range(retry_limit):
            try:
                token_id = contract.query({
                    'all_tokens': {
                        'start_after': job,
                        'limit': 1,
                    }
                })['tokens'][0]
                token = contract.query({
                    'nft_info': {
                        'token_id': token_id
                    }
                })
                results[job_id] = token
                return
            except Exception as e:
                error_message = e
                continue

        print(
            f'Error: CosmWasmClient.retrieve: {job_id} - {job}:\n{error_message}')
