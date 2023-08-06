# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smc_movement_models']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'jupyter>=1.0.0,<2.0.0',
 'llvmlite==0.39.1',
 'matplotlib>=3.6.2,<4.0.0',
 'notebook>=6.5.2,<7.0.0',
 'numpy==1.23.5',
 'pandas>=1.5.2,<2.0.0',
 'particles>=0.3,<0.4',
 'plotly>=5.11.0,<6.0.0',
 'scipy>=1.8,<1.9',
 'seaborn>=0.12.1,<0.13.0',
 'statsmodels>=0.13.5,<0.14.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'smc-movement-models',
    'version': '1.0.0',
    'description': "Projet pour le cours Hidden Markov models and Sequential Monte-Carlo methods de l'ENSAE.",
    'long_description': '# Estimating behavioral parameters in animal movement models using a state-augmented particle filter\n\nProjet pour le cours **Hidden Markov models and Sequential Monte-Carlo methods** de l\'ENSAE.\n\n* Gabriel Watkinson\n* Gabriel Guaquiere\n* Jérémie Stym-Popper\n* Benjamin Maurel\n\n## Introduction\n\nDans ce projet, nous implementons le modèle décrit dans le papier [Estimating behavioral parameters in animal movement models using a state-augmented particle filter](https://dalspace.library.dal.ca/bitstream/handle/10222/33464/Dowd_et_al-2011-Ecology.pdf), et l\'approfondissons avec des méthodes plus récentes.\n\nNotre rapport est disponible [ici](https://github.com/gwatkinson/smc_movement_models/blob/main/SMC_Movement_Model_Ecology.pdf) à la racine du projet.\n\n### Le package `smc_movement_models`\n\nLes fonctions sont définies dans le package `smc_movement_models`.\n\nLes modules `models.py` et `models_SMC2.py` contiennent les modèles de mouvement et l\'algorithme du papier et une version SMC2 respectivement.\n\nLe module `plot.py` contient des fonctions utilitaires pour génerer des graphes.\n\nLe module `process_data.py` contient des fonctions utilitaires pour traiter les données brutes et une CLI.\n\n### Les notebooks\n\nLes notebooks sont dans le dossier `notebooks` et permettent de lancer les expériences et de visualiser les résultats.\n\nLe notebook `notebooks/simulation_papier.ipynb` contient les expériences avec l\'algorithme du papier.\n\nLe notebook `notebooks/implementation_smc2.ipynb` contient les expériences avec la version SMC2.\n\n### Le reste\n\nLe dossier `data` contient les données brutes et les données traitées.\n\nLe dossier `images` contient les images utilisées dans le rapport.\n\nLe dossier `paper` contient les papiers liés au projet.\n\nLe dossier `r_code` contient le code R original du papier (pas utilisé par notre groupe).\n\nLes fichiers `poetry.lock` et `pyproject.toml` sont utilisés par [poetry](https://python-poetry.org/) pour gérer les dépendances.\n\nLe fichier `requirements.txt` est utilisé par `pip` pour gérer les dépendances et est généré par poetry.\n\nLe dossier `latex` contient le LaTeX utilisé pour le rapport.\n\n## Installation\n\nNous utilisons Python pour simuler les données et mettre en place les modèles, notamment la librairie [particles](https://github.com/nchopin/particles).\n\nAvant toutes choses, il faut se déplacer dans le dossier `smc_movement_models`:\n\n```bash\ncd /path/to/smc_movement_models\n```\n\n### Avec [`poetry`](https://python-poetry.org/)\n\n```bash\n# Creation d\'un environement virtuel et installation des packages\npoetry install\n\n# Activation de l\'environement\npoetry shell  # sub shell\n# OU source $(poetry env info --path)/bin/activate  # activer l\'environement dans le shell actuel\n```\n\n### Avec `pip`\n\n```bash\n# Creation d\'un environement virtuel\npython -m venv .venv\n\n# Activation de l\'environement\n.venv/Script/activate  # pour Windows\n# OU source .venv/bin/activate  # pour Linux / MacOS\n\n# Installation des packages\npip install -r requirements.txt\n```\n\n### Processing des données\n\nPour générer les données à partir du fichier brut, il faut lancer le script `process_data.py` :\n\n```python\npython smc_movement_models/process_data.py\n# Pour plus d\'informations\n# python smc_movement_models/process_data.py --help\n```\n\n### `pre-commit`\n\nPour activer les pre-commit qui formattent le code avant chaque commit :\n\n```bash\npre-commit install\npre-commit run --all-files  # Pour installer les modules et lancer les tests\n```\n\n![Exemple de pre-commit](images/pre-commit-exemple.png)\n\nPour forcer un commit sans vérifier :\n\n```bash\ngit commit -m "..." --no-verify\n```\n',
    'author': 'Gabriel Watkinson',
    'author_email': 'gabriel.watkinson@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.8,<3.11',
}


setup(**setup_kwargs)
