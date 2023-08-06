# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyshuii',
 'pyshuii.clients',
 'pyshuii.indexers',
 'pyshuii.retrievers',
 'pyshuii.utils']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp==3.8.1',
 'asyncio==3.4.3',
 'cosmpy==0.5.1',
 'tqdm==4.64.0',
 'web3==5.30.0']

setup_kwargs = {
    'name': 'pyshuii',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Rarity Scanner\n\neth: **_0xbA842b7DA417Ba762D75e8F99e11c2980a8F8051_**\nens: **_prathik.xyz_**\n\nAggregate metadata info on NFT collections\n\nAccuracy on par w/ legitimate tools afaik (May now have changed with the release of OpenRarity)\n\n# Notice(s)\n1. Using [poetry](https://python-poetry.org/docs/) for package management.\n3. Using [SmartProxy](https://smartproxy.com/) for proxies.\n\n#### description\n\nGathering info on collection, weighing rarities, and spitting into json file\n_Currently supports collections on Ethereum and Cosmos_\n_Currently supports on-chain metadata, single-file metadata, multi-file metadata_\n\n#### how-to\n\n##### sample\n\n```py\nimport json\nfrom pyshuii.retrievers import erc721, cw721\n\ncreds = {}\ncreds[\'ALCHEMY_API_KEY\'] = \'\'\n\nclient_mappings = {\n    \'EVM\': erc721,\n    \'CW\': cw721\n}\n\nproxies = open(\'proxies.txt\', \'r\').read()\n\n\ndef main(event):\n    try:\n        if (event[\'network\'] == \'EVM\'):\n            cli = client_mappings[event[\'network\']](\n                alchemy_api_key=creds.get(\'ALCHEMY_API_KEY\'),\n                max_retries=100,\n                proxies=proxies\n            )\n        elif (event[\'network\'] == \'CW\'):\n            cli = client_mappings[event[\'network\']](\n                max_retries=100,\n                proxies=proxies\n            )\n\n        results = cli.run(event[\'chain\'], event[\'address\'])\n\n        with open("%s.json" % (results[\'project_name\'].lower().replace(" ", "_")), "w") as dumped:\n            dumped.write(json.dumps(results))\n\n        return \'{}s\'.format(results[\'time_to_sync\'])\n    except Exception as e:\n        print(e)\n        raise e\n\n# main(\n#     event={\n#         "network": "CW",\n#         "chain": "JUNO-1",\n#         "address": "juno1za0uemnhzwkjrqwguy34w45mqdlzfm9hl4s5gp5jtc0e4xvkrwjs6s2rt4"\n#     })\n# main(\n#     event={\n#         "network": "CW",\n#         "chain": "JUNO-1",\n#         "address": "juno1e229el8t4lu4rx7xeekc77zspxa2gz732ld0e6a5q0sr0l3gm78stuvc5g"\n#     })\n# main(\n#     event={\n#         "network": "CW",\n#         "chain": "STARGAZE-1",\n#         "address": "stars1rz8jkes33jxqf79t707s68yary3969faqfz59lvwnxjy4j65q7es62j098"\n#     })\nmain(\n    event={\n        "network": "EVM",\n        "chain": "ETH",\n        "address": "0x0e32cee0445413e118b14d02e0409303d338487a"\n    })\n```\n\n### whats left\n\n- _containerize_\n  - poetry shell alternative\n- improve efficiency\n  - work around brute force retry method\n  - CW single threaded\n- more chains?\n- better docs\n\n```sh\npython3 setup.py install\n```\n\n```sh\npython3 -m twine upload --repository pypi dist/*\n```\n\n### to do\n\ngithub workflow for package publishing & layer uploading\n',
    'author': 'prathik',
    'author_email': '37804760+prmali@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
