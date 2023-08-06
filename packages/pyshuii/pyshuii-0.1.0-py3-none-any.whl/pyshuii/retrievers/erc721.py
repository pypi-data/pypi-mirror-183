# EthereumRC721 Standard
import asyncio
import aiohttp
import ssl
import time
import tqdm

from functools import cmp_to_key

from pyshuii.utils import traceCast

from pyshuii.clients import EthereumClient
from pyshuii.indexers import MultiDocument

from pyshuii.retrievers.Main import Main


class erc721(Main):
    def __init__(self, alchemy_api_key, max_retries=500, proxies=''):
        super().__init__()

        self.client = EthereumClient(alchemy_api_key)
        self.indexer = MultiDocument(max_retries, proxies=proxies)
        self.address = None

    async def count(self, token_id, metadata):
        attributes = metadata["attributes"]
        await self.prep(token_id, attributes)

    async def execute(self):
        t0 = time.time()
        collection_metadata = self.client.getCollectionMetadata(self.address)

        token_uri = collection_metadata['token_uri'].replace(
            "ipfs://", "https://gateway.ipfs.io/ipfs/")
        suffix = collection_metadata['suffix']

        await traceCast(
            desc="Initialize jobs",
            fn=self.indexer.create_job,
            tasks=[{
                'job_id': token_id,
                'job': "%s/%s%s" % (token_uri, token_id, suffix)
            } for token_id in range(
                collection_metadata['starting_index'],
                collection_metadata['starting_index'] +
                collection_metadata['total_supply']
            )]
        )

        await self.indexer.execute_jobs(fn=None, params={})

        await traceCast(
            desc="Count results",
            fn=self.count,
            tasks=[{
                'token_id': token_id,
                'metadata': metadata
            } for token_id, metadata in self.indexer.results.items()]
        )

        for attributes in self.aggregate.values():
            for attribute in attributes.values():
                self.composed.append(attribute)

        await traceCast(
            desc="Weigh collection",
            fn=self.assign_weight,
            tasks=[{
                'attribute': attribute,
                'limit': collection_metadata['total_supply']
            } for attribute in self.composed]
        )

        print("*** SORTING ***")
        print("Sorting assets by weight")
        self.weights.sort(key=cmp_to_key(self.compare), reverse=True)

        print("*** RANKING ***")
        print("Assigning ranks to assets")
        self.rank()

        t1 = time.time()
        finalized_time = t1 - t0

        print("*** DONE ***")
        print(f'*** {finalized_time} SECONDS ***')
        print(
            f'*** {collection_metadata["total_supply"] - len(self.weights)} DROPPED ***')

        return {
            'network': "ETH",
            'address': collection_metadata['address'],
            'project_name': collection_metadata['name'],
            'project_symbol': collection_metadata['symbol'],
            'token_uri': token_uri,
            'total_supply': collection_metadata['total_supply'],
            'suffix': collection_metadata['suffix'],
            'starting_index': collection_metadata['starting_index'],
            'time_started': t0,
            'time_finalized': t1,
            'time_to_sync': finalized_time,
            'aggregate': self.aggregate,
            'weights': self.weights,
        }

    def run(self, chain, address):
        super().refresh()
        self.indexer.clear_results()
        self.address = address

        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(self.execute())
        loop.close()

        return result
