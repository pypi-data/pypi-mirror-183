# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['enkanetworkcard', 'enkanetworkcard.src.utils']

package_data = \
{'': ['*'],
 'enkanetworkcard': ['src/assets/*',
                     'src/assets/InfoCharter/*',
                     'src/assets/constant/*',
                     'src/assets/elementColor/*',
                     'src/assets/font/*',
                     'src/assets/icon/*',
                     'src/assets/stars/*',
                     'src/assets/teapmleOne/artifact/*',
                     'src/assets/teapmleOne/background/*',
                     'src/assets/teapmleOne/charterInfo/*',
                     'src/assets/teapmleOne/maska/*',
                     'src/assets/teapmleOne/stats/*',
                     'src/assets/teapmleOne/talants/*',
                     'src/assets/teapmleOne/weapons/*',
                     'src/assets/teapmleTree/artifact/*',
                     'src/assets/teapmleTree/background/*',
                     'src/assets/teapmleTree/constant/closed/*',
                     'src/assets/teapmleTree/constant/open/*',
                     'src/assets/teapmleTree/maska/*',
                     'src/assets/teapmleTree/name/*',
                     'src/assets/teapmleTree/talants/*',
                     'src/assets/teapmleTree/weapon/*',
                     'src/assets/teapmleTwo/artifact/*',
                     'src/assets/teapmleTwo/background/*',
                     'src/assets/teapmleTwo/charterInfo/*',
                     'src/assets/teapmleTwo/charter_element/*',
                     'src/assets/teapmleTwo/infoUser/*',
                     'src/assets/teapmleTwo/maska/*',
                     'src/assets/teapmleTwo/stats/*',
                     'src/assets/teapmleTwo/talants/*',
                     'src/assets/teapmleTwo/weapon/*']}

install_requires = \
['Pillow>=9.3.0,<10.0.0',
 'asyncache>=0.3.1,<0.4.0',
 'cachetools>=5.2.0,<6.0.0',
 'enkanetwork.py>=1.3.2,<2.0.0']

setup_kwargs = {
    'name': 'enkanetworkcard',
    'version': '0.2.9',
    'description': 'Wrapper module for enkanetwork.py for creating character cards.',
    'long_description': '<p align="center">\n  <img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/banner.jpg" alt="Баннер"/>\n</p>\n\n**<p align="center"> <a href="https://github.com/DEViantUA/EnkaNetworkCard/wiki/EnkaNetworkCard-RU">Русская версия</a> | <a href="https://github.com/DEViantUA/EnkaNetworkCard/tree/main/Example">Example</a> | <a href = "https://discord.gg/SJ3d9x4e"> Discord <a> </p>**\n\n# EnkaNetworkCard\nWrapper for [EnkaNetwork.py](https://github.com/mrwan200/EnkaNetwork.py) to create character cards in Python.\n\n## Full Documentation:\n\nEn: [Documentation EN](https://deviantua.github.io/EnkaNetworkCard-Documentation/) \n\n## Navigation\n* Installation\n* Dependencies\n* Launch\n* Running Async\n* Fix bug with async\n* Get a character showcase\n* Description of arguments\n* Languages Supported\n* Sample Results\n\n## Installation:\n\n```\npip install enkanetworkcard\n```\nOr you can copy the given repository.\n\n### Dependencies:\n  Dependencies that must be installed for the library to work:\n  * Pillow\n  * requests\n  * io\n  * math\n  * threading\n  * datetime\n  * random\n  * enkanetwork\n  * logging\n\n## Launch:\n``` python\nfrom enkanetworkcard import encbanner\n\nENC = encbanner.EnkaGenshinGeneration() \n\nresult = ENC.start(uids = 724281429)\n\nprint(result)\n\n```\n## Running Async:\n\n``` python\nfrom enkanetworkcard import aioenkbanner\nimport asyncio\n\nasync def card():\n    ENC = aioenkbanner.EnkaGenshinGeneration()\n    return await ENC.start(uids = 724281429)\n\nresult = asyncio.run(card()) \n\nprint(result)\n```\n_Thank you for this example and advice: [Gaurav Mandal](https://github.com/GauravM512)_\n\n## Fix bug with async:\nWindows users may experience an error: ```RuntimeError: Event loop is closed``` if this occurs, then you must set the variable ```FIX_ASYNCIO_WIN = True```\n\n### Example\n``` python \nfrom enkanetworkcard import encbanner\n\nENC = encbanner.EnkaGenshinGeneration() \nENC.FIX_ASYNCIO_WIN = True\n```\n\n## Get a character showcase:\n```profile``` - A useful feature for bot developers. Get information about the characters from the showcase, for their further use.\n\n### Example\n``` python\nfrom enkanetworkcard import encbanner\n\nENC = encbanner.EnkaGenshinGeneration()\nresultProfile = ENC.profile(uid = 724281429, image = False)\nresult = ENC.start(uids = 724281429, name = resultProfile["charactersArg"])\n\nprint(result)\n```\nFunction: ```profile``` returns: ```characters```, ```charactersArg```, ```img```\n- ```characters``` - Information about each character.\n- ```charactersArg``` - List of character names to quickly pass to ```start()```\n- ```img``` - Showcase generated image.\n\n\n## Description of arguments:\nMain class: <code>EnkaGenshinGeneration</code> Contains the following arguments <code>lang</code>,<code>img</code>,<code>charterImg</code>,<code>name</code>,<code>adapt</code>,<code>randomImg</code>,<code>hide</code>,<code>dowload</code>,<code>namecard</code>,<code>splash</code>\n\n### Class argument description::\n* <code>lang</code> - Takes one value to define the language. Supported languages are listed below in the documentation. The default is Russian.\n* Values: str\n* Example str: ```EnkaGenshinGeneration(lang = "en")```\n-----\n* <code>img</code> - If you want to use your image on the card, then pass this argument.\n* Values str: Image link or the path to the file.\n* Values PIL.ImageFile: Image opened with Image.open()\n* Values list: Image link, the path to the file or PIL.ImageFile\n* Example str the path to the file: ```EnkaGenshinGeneration(img = "img.png")```\n* Example str image link: ```EnkaGenshinGeneration(img = "https//...image.png")```\n* Example PIL.ImageFile: ```EnkaGenshinGeneration(img = Image.open("img.png"))```\n* Example list: ```EnkaGenshinGeneration(img = [Image.open("img.png"), "img.png", "https//...image.png"])``` - list only works with the argument: ```randomImg```.\n-----\n* <code>charterImg</code> - Give each character a custom image.\n* Values dict: Can take all values from the img argument except list.\n* Example dict: ```EnkaGenshinGeneration(charterImg = {"Klee": Image.open("img.png"), "Albedo": "img.png", "Xiao": "https//...image.png"})```\n-----\n* <code>name</code> - Needed if you want to get certain characters.\n* Values: str\n* Example str one character: ```EnkaGenshinGeneration(name = "Klee")```\n* Example str two or more characters: ```EnkaGenshinGeneration(name = "Klee, Albedo, ...")```\n-----\n* <code>adapt</code> - Adapt background to custom image.\n* Values: bool\n* Example bool: ```EnkaGenshinGeneration(img = "img.png", adapt = True)```\n-----\n* <code>randomImg</code> - Random selection of custom images from the list.\n* Values: bool\n* Example bool: ```EnkaGenshinGeneration(img = [Image.open("img.png"), "img.png"], randomImg = True)``` - If img is not a list, then randomImg is ignored.\n-----\n* <code>hide</code> - Hide the UID on the character card.\n* Values: bool\n* Example bool: ```EnkaGenshinGeneration(hide = True)```\n-----\n* <code>dowload</code> - Will return ready images for further work with them. (If not specified, then the finished results will be saved in the directory of the executable file in the folder and return None: ```EnkaImg```)\n* Values: bool\n* Example bool: ```EnkaGenshinGeneration(dowload = True)```\n-----\n* ```namecard``` - Replaces the background of the player card image with character images. (Used only for the second template.)\n* Values: bool\n* Example bool: ```EnkaGenshinGeneration(namecard = True)```\n-----\n* <code>splash</code> - Displays splashes of characters in costumes\n* Values: bool\n* Example bool: ```EnkaGenshinGeneration(splash= True)```\n-----\n\nThe main function of the class: <code>start</code> takes ```template```, ```uids```, ```name```  argument\n### Function argument description::\n* ```uids``` - Game UID in the game Genshin Impact.\n* Values: int, str\n* Example int: ```EnkaGenshinGeneration().start(uids = 757562748)```\n* Example str one UID: ```EnkaGenshinGeneration().start(uids = "757562748")```\n* Example str two or more UID: ```EnkaGenshinGeneration().start(uids = "757562748,544523587,874385763")```\n-----\n* ```template``` - Changes the character card template.\n* Values: int\n* Example int: ```EnkaGenshinGeneration().start(uids = "757562748", template = 2)```\n-----\n* <code>name</code> - Needed if you want to get certain characters.\n* Values: str\n* Example str one character: ```EnkaGenshinGeneration(uids = "757562748", name = "Klee")```\n* Example str two or more characters: ```EnkaGenshinGeneration.start(uids = "757562748", name = "Klee, Albedo, ...")```\n-----\n\nAdditional class function: <code>profile</code> takes ```uid```, ```image```  argument\n* ```uid``` - Game UID in the game Genshin Impact.\n* Values: int\n* Example int: ```EnkaGenshinGeneration().profile(uids = 757562748)```\n-----\n* ```image``` - Generate a showcase image. (Default True)\n* Values: bool\n* Example bool: ```EnkaGenshinGeneration().profile(uid = 757562748б, image = False)```\n\n\n## Languages Supported\n| Languege    |  Code   | Languege    |  Code   |\n|-------------|---------|-------------|---------|\n|  English    |     en  |  русский    |     ru  |\n|  Tiếng Việt |     vi  |  ไทย        |     th  |\n|  português  |     pt  | 한국어      |     kr  |\n|  日本語      |     jp  | 中文        |     zh  |\n|  中文        |     zh  | Indonesian |     id  |\n|  français   |     fr  | español    |     es  |\n|  deutsch    |     de  | Taiwan     |    cht  |\n|  Chinese    |    chs  |      |      |\n\n## Sample Results:\n\n\n### The result of a custom images and adaptation (template= 1).\n<img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example1.png" width=\'300\' alt="Example1"/> <img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example2.png" width=\'300\' alt="Example2"/> \n\n### Usual result (template= 1).\n<img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example3.png" width=\'300\' alt="Example3"/> <img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example4.png" width=\'300\' alt="Example4"/> \n\n### The result of a custom images and adaptation (template= 2).\n<img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example5.png.png" width=\'300\' alt="namecard = True"/> <img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example6.png.png" width=\'300\' alt="namecard = False"/> \n\n### Usual result (template= 2).\n<img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example8.png.png" width=\'300\' alt="namecard = True"/> <img src="https://raw.githubusercontent.com/DEViantUA/EnkaNetworkCard/main/img/Example7.png.png" width=\'300\' alt="namecard = False"/> ',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/DEViantUA/EnkaNetworkCard/wiki/Dokumentation-enkanetworkcard',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
