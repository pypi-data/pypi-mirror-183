# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bittrade_kraken_rest',
 'bittrade_kraken_rest.connection',
 'bittrade_kraken_rest.endpoints',
 'bittrade_kraken_rest.endpoints.private',
 'bittrade_kraken_rest.endpoints.public',
 'bittrade_kraken_rest.exceptions',
 'bittrade_kraken_rest.models',
 'bittrade_kraken_rest.models.private',
 'bittrade_kraken_rest.models.public',
 'bittrade_kraken_rest.models.websocket']

package_data = \
{'': ['*']}

install_requires = \
['orjson>=3.8.3,<4.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'bittrade-kraken-rest',
    'version': '0.10.0',
    'description': 'Kraken REST library',
    'long_description': "ELM Bittrade's Kraken REST package & optional CLI\n====\n\nInstall\n---\n\n`pip install bittrade-kraken-rest` or `poetry add bittrade-kraken-rest`\n\nNot all Kraken endpoints are implemented yet.\n\nPublic endpoints\n------\n\nFor all public endpoints, simply use `get_<endpoint>`.\n\nBring Your Own ~~Credentials~~ Signature (Private endpoints)\n---\n\nTLDR; Don't pass your API secret but sign the requests yourself, with your own code. It's safer.\n\nThis library doesn't want to ever access your Kraken secret keys.\n\nMost libraries expect you to provide your api key and secret. I'm not comfortable doing that with third-party code, even open sourced.\n\nHere instead, the library prepares the request, which you then sign using your own code and the library finishes the job. It has NO access to your secret.\n\nThankfully this is quite straightforward: you need to implement a `sign(request: RequestWithResponse) -> None` method which sets the correct headers and then follow a two step process:\n\n```python\nprep: RequestWithResponse\nwith get_websockets_token() as prep:\n    sign(prep)  # copy `sign` from readme below or implement your own method.\n# Once you exit the `with` context, the response object is available.\nresult: GetWebsocketsTokenResult = prep.response.get_result()\n```\n\nAnd here is a sample code for `sign` implementation. Feel free to copy it or implement your own signature function:\n\n```python\nfrom os import getenv\nimport urllib, hmac, base64, hashlib\n\n# Taken (with a minor change on non_null_data) from https://docs.kraken.com/rest/#section/Authentication/Headers-and-Signature\ndef generate_kraken_signature(urlpath, data, secret):\n    non_null_data = {k: v for k, v in data.items() if v is not None}\n    post_data = urllib.parse.urlencode(non_null_data)\n    encoded = (str(data['nonce']) + post_data).encode()\n    message = urlpath.encode() + hashlib.sha256(encoded).digest()\n    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)\n    signature_digest = base64.b64encode(mac.digest())\n    return signature_digest.decode()\n\n\ndef sign(request):\n    request.headers['API-Key'] = getenv('KRAKEN_API_KEY')  # this is just one example of how to read the API key/secret; alternatives include docker secrets and config files\n    request.headers['API-Sign'] = generate_kraken_signature(request.url, request.data, getenv('KRAKEN_API_SECRET'))\n```\n\n\nWhen using the CLI, simply put the above code (or your own) inside a file called `sign.py` at the root of the library (same level as `kraken.py`).\n\n\nCLI\n---\n\nTo use the CLI, clone/fork this repo then:\n\n`python kraken.py <command>`\n\nList of commands `python kraken.py --help`\n\nAuto complete can be achieved using [Google Fire's commands](https://google.github.io/python-fire/using-cli/#-completion-generating-a-completion-script)\n\n### Authenticated Websocket\n\n`python kraken.py authenticated_websocket`\n\nYou will need to have set up the `sign.py` file as described ",
    'author': 'Matt Kho',
    'author_email': 'matt@techspace.asia',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/TechSpaceAsia/bittrade-kraken-rest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
