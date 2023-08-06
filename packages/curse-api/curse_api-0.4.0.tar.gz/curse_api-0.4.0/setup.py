# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['curse_api']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.1,<0.24.0', 'pydantic>=1.10.4,<2.0.0']

setup_kwargs = {
    'name': 'curse-api',
    'version': '0.4.0',
    'description': 'A simple curseforge api wrapper',
    'long_description': '# curse-api\n\n----\n\n## A simple python Curseforge api wrapper using pydantic\n\nBuilt to serve CF endpoints while providing methods and functions to assist in finding the right mod.\n\n- [Features](#features)\n- [Quick Start](#quick-start)\n- [Examples](#examples)\n\n----\n\n## Some backstory\n\nA while back when I was starting to learn python further then the basics I created a small tool to download Minecraft mods from a pack manifest.\nSoon after I wrote it the new API changes came and broke it. Now once more I want to return to that project idea and expand further. After first rewriting the project using [chili](https://pypi.org/project/chili/) it felt off, so returned to rewrite once more using [pydantic](https://pypi.org/project/pydantic/) for data validation and ease of access\n\n----\n\n## Features\n\nMain Dependencies:\n\n- [Pydantic](https://pypi.org/project/pydantic/)\n- [HTTPX](https://pypi.org/project/httpx/)\n\nCurrently implemented:\n\n- Important endpoint support\n- Full CurseForge model\n- Mediocre error handling\n- Shortcuts to download mods\n- Pluggable API factory\n- Serialization and deserialization of models\n- Python 3.8 & 3.9 support\n\nTo Do:\n\n- Fix to be usable with pydantic based ORM\'s\n- Async Rewrite\n- Address all TODO\'s\n- Fully expose needed httpx args\n- Write more download handling code\n- Test other games too\n- Write docs\n- Update and fix error handling\n\nCI/CD:\n\n- Type checking\n- Version testing\n- Tests\n\n----\n\n## Examples\n\n### Quick start\n\nRequires an api from CF to use the API. You can get one [here](https://docs.curseforge.com/#authentication).\nThis example runs through most of the basics\n\n```python\nfrom curse_api import CurseAPI\n\napi = CurseAPI(API_KEY)\n\n\n"Mods"\na = api.search_mods(searchFilter="JEI", slug="jei")\n# applies the search filters to the standard of CF docs\n\nmod = api.get_mod(250398)                   # returns a singular Mod\nmod_list = api.get_mods([285109, 238222])   # returns a list of Mods\n\n\n"files"\n"See examples/download.py"\n# TODO finish file support\nfiles = api.get_files([3940240])        # returns a list of Files matching their id\nmod_files = api.get_mod_files(238222)   # returns all the Files of on a give Mod\n\n\n"Version details - large data"\n"See examples/modloader.py"\nmc = api.minecraft_versions()  # returns all of minecraft version data\nml = api.modloader_versions()  # returns **ALL** modloader versions on curseforge\n\nmc_112 = api.get_specific_minecraft_version("1.12.2")           # returns minecraft version related information\nforge = api.get_specific_minecraft_modloader("forge-36.2.39")   # returns forge related version information\n```\n\n### Downloading to a file\n\nThis example opens a properly named file in the current working directory and writes to it.\n\n```python\nfrom curse_api import CurseAPI\n\napi = CurseAPI(API_KEY)\n\nmod_l, page_data = api.search_mods(slug="jei")\nlatest = mod_l[0].latestFiles[0] # gets the first mod matching the slug "jei" and latest file from the mod\n\nwith open(latest.fileName, "wb") as f:\n    f.write(latest.download()) # download returns bytes while kwargs is passed to the get method\n\n```\n\n----\nSub project / extension ideas:\n\n- Modloader download and installation\n- Minecraft Version type / parser\n- MC pack installation\n- DB cache extension\n',
    'author': 'Stinky-c',
    'author_email': '60587749+Stinky-c@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Stinky-c/curse-api',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
