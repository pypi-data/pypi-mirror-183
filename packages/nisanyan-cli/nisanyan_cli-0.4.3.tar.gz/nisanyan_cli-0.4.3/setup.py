# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nisanyan_cli']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata>=5.2.0,<6.0.0', 'rich>=13.0.0,<14.0.0']

entry_points = \
{'console_scripts': ['nis = nisanyan_cli.__main__:cli']}

setup_kwargs = {
    'name': 'nisanyan-cli',
    'version': '0.4.3',
    'description': 'CLI tool for Turkish etymological dictionary, nisanyansozluk.com (nis <word>)',
    'long_description': '![screenshot](https://user-images.githubusercontent.com/16024979/162843362-4050c114-dc82-49eb-ac43-dd6cef79382a.png)\n\n<div align="center">\n<a href="https://github.com/agmmnn/nisanyan-cli">\n<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/agmmnn/nisanyan-cli"></a>\n<a href="https://pypi.org/project/nisanyan-cli/">\n<img alt="PyPI" src="https://img.shields.io/pypi/v/nisanyan-cli"></a>\n\nCLI tool for Turkish etymological dictionary, [nisanyansozluk.com](https://www.nisanyansozluk.com/).\n\n</div>\n\n## Install\n\n```\npip install nisanyan-cli\n```\n\n## Usege\n\n```\n$ nis yakamoz\n```\n\n![nisanyan-cli](https://user-images.githubusercontent.com/16024979/162844886-7831aebc-8efe-4018-9df5-b26babcc1ca3.png)\n\n### Etymology Tree (`--tree`, `-t`):\n\n```\n$ nis çikolata --tree\nçikolata (Günümüz Türkçesi)\n└── cioccolata (İtalyanca): kakao yağı ve şekerle imal edilen yiyecek maddesi.\n    └── chocolate (İspanyolca): ~.\n        └── xocolatl (Aztekçe): kakaodan yapılan içecek.\n            ├── xocolli (Aztekçe): acı.\n            └── atl (Aztekçe): su.\n```\n\n![Etymology Tree](https://user-images.githubusercontent.com/16024979/164780578-0d51d1b1-31b6-48a4-a09e-b42aa6b6c515.png)\n\n### Random Word (`--random`, `-r`):\n\n```\n$ nis -r -t\nmenekşe (Günümüz Türkçesi)\n└── banafşe ‹بنفشه› (Farsça): aynı anlam.\n    └── vanavşag (Orta Farsça 1300—1500): aynı anlam.\n        └── *vana-vaxşa- (Avestaca MÖ.2000): orman otu.\n            └── vaxşaiti, vaxş- (Avestaca MÖ.2000): yetişmek, bitmek (bitki).\n```\n\n### Adlar (`-ad`):\n\n```\n$ nis gökçe -ad\n```\n\n<img src="https://user-images.githubusercontent.com/16024979/208524422-115cf48b-b2db-4e3e-880f-d43784ed48c6.png" alt="NisanyanAdlar" width="540"/>\n\nAlso you can use `--random`, `-r` argument with `-ad` argument: `nis -ad -r`\n\n## Arguments\n\n```\npositional arguments:\n    <word>\n\noptions:\n    -h, --help     show this help message and exit\n    -t, --tree     show result as etymology tree\n    -r, --random   selects a random word and brings the result\n    -p, --plain    plain text output\n    -ad            show result from nisanyanadlar\n    -v, --version  show program\'s version number and exit\n```\n\n## TODO\n\n- [ ] Köken metninin sitedeki gibi görünmesi için Api\'dan dönen sonucun işlenmesi.\n- [ ] Ek açıklama metnindeki kısaltmaların normal hallerine çevrilmesi.\n- [ ] Decode işlemini python koduna uyarlama.[\\*](https://github.com/agmmnn/Radyal-api/blob/master/api/nisanyan-decrypt.js) (crypto-js/aes, crypto-js/enc-utf8)\n\n## Dependencies\n\n- [rich](https://pypi.org/project/rich/)\n',
    'author': 'Gökçe',
    'author_email': 'agmmnn@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/agmmnn/nisanyan-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
