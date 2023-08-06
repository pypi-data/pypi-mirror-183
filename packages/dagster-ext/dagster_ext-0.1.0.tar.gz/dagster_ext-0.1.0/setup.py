# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dagster_ext',
 'files_dagster_ext',
 'files_dagster_ext.dagster.{{ cookiecutter.project_name }}',
 'meltano',
 'meltano.edk']

package_data = \
{'': ['*'], 'files_dagster_ext': ['dagster/*', 'github/*']}

install_requires = \
['PyYAML>=6.0.0,<7.0.0',
 'click>=8.1.3,<9.0.0',
 'cookiecutter>=2.1.1,<3.0.0',
 'dagit>=1.0',
 'dagster-dbt>=0.16',
 'dagster-meltano>=1.0.0',
 'dagster>=1.0',
 'devtools>=0.9.0,<0.10.0',
 'pydantic>=1.9.0,<2.0.0',
 'rich>=12.5.1,<13.0.0',
 'structlog>=21.2.0,<22.0.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['cloud_invoker = '
                     'dagster_ext.pass_through:pass_through_cli_cloud',
                     'dagit_invoker = '
                     'dagster_ext.pass_through:pass_through_cli_dagit',
                     'dagster_extension = dagster_ext.main:app',
                     'dagster_invoker = '
                     'dagster_ext.pass_through:pass_through_cli_dagster']}

setup_kwargs = {
    'name': 'dagster-ext',
    'version': '0.1.0',
    'description': '`dagster-ext` is a Meltano utility extension.',
    'long_description': '# Meltano Dagster Extention\n\n[![PyPI version](https://badge.fury.io/py/dagster-ext.svg)](https://badge.fury.io/py/dagster-ext)\n\nThis project is still a work in progress. Please create an issue if you find any bugs.\n\n## Features\n\n- Load all Meltano jobs as Dagster jobs.\n- Add all correspondig schedules to these jobs.\n- (todo) Load all DBT models as Dagster assets.\n- (todo) Load all Singer tap streams as Dagster assets.\n- (todo) Ops to perform all Meltano actions.\n- (todo) Extract Singer metrics from logs and store them using Dagster.\n\n## Installation\n\n```sh\n# Add the dagster-ext to your Meltano project\nmeltano add utility dagster\n\n# Initialize your Dagster project\nmeltano invoke dagster:initialize\n\n# Start Dagit\nmeltano invoke dagster:start\n```\n\n## Commands\n\n```sh\nmeltano invoke dagster:initialize\n```\n\nSetup a new Dagster project and automatically load jobs and assets from your Meltano project.\n\n```sh\nmeltano invoke dagster:start\n```\n\nStart Dagit to serve your local Dagster deployment.\n\n## Code Examples\n\nBelow are some code examples how to use the `dagster-meltano` package.\n\n### Automatically load all jobs and schedules from your Meltano project.\n\n```python\nfrom dagster import repository\n\nfrom dagster_meltano import load_jobs_from_meltano_project\n\nmeltano_jobs = load_jobs_from_meltano_project("<path-to-meltano-root>")\n\n@repository\ndef repository():\n    return [meltano_jobs]\n```\n\n### Install all Meltano plugins\n\n```python\nfrom dagster import repository, job\n\nfrom dagster_meltano import meltano_resource, meltano_install_op\n\n@job(resource_defs={"meltano": meltano_resource})\ndef install_job():\n    meltano_install_op()\n\n@repository()\ndef repository():\n    return [install_job]\n```\n\n### Create an arbitrary Meltano run command\n\n```python\nfrom dagster import repository, job\n\nfrom dagster_meltano import meltano_resource, meltano_run_op\n\n@job(resource_defs={"meltano": meltano_resource})\ndef meltano_run_job():\n    tap_done = meltano_run_op("tap-1 target-1")()\n    meltano_run_op("tap-2 target-2")(tap_done)\n\n@repository()\ndef repository():\n    return [meltano_run_job]\n```\n',
    'author': 'Jules Huisman',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
