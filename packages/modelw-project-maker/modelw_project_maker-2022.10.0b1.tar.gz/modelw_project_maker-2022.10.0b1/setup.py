# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['project_maker',
 'project_maker.maker',
 'project_maker.template.api',
 'project_maker.template.api.___project_name__snake___.cms',
 'project_maker.template.api.___project_name__snake___.cms.migrations',
 'project_maker.template.api.___project_name__snake___.core',
 'project_maker.template.api.___project_name__snake___.core.migrations',
 'project_maker.template.api.___project_name__snake___.django',
 'project_maker.template.api.___project_name__snake___.people',
 'project_maker.template.api.___project_name__snake___.people.migrations']

package_data = \
{'': ['*'],
 'project_maker': ['template/*',
                   'template/front/*',
                   'template/front/components/*',
                   'template/front/components/blocks/*',
                   'template/front/pages/*'],
 'project_maker.template.api.___project_name__snake___.cms': ['templates/*',
                                                              'templates/cms/*']}

install_requires = \
['Unidecode>=1.3.4,<2.0.0',
 'black>=22.8.0,<23.0.0',
 'isort>=5.10.1,<6.0.0',
 'monoformat>=0.1.0b3,<0.2.0',
 'node-edge>=0.1.0b2,<0.2.0',
 'pathspec>=0.10.2,<0.11.0',
 'rich>=12.5.1,<13.0.0',
 'tomlkit>=0.11.4,<0.12.0']

entry_points = \
{'console_scripts': ['project_maker = model_w.project_maker.__main__:__main__']}

setup_kwargs = {
    'name': 'modelw-project-maker',
    'version': '2022.10.0b1',
    'description': 'A tool to create Model-W-compliant projects',
    'long_description': 'None',
    'author': 'Rémy Sanchez',
    'author_email': 'remy.sanchez@hyperthese.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
