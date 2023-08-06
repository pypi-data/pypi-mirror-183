# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dask_deltalake']

package_data = \
{'': ['*']}

install_requires = \
['bokeh<3.0',
 'dask[dataframe]>=2022.11.1,<2023.0.0',
 'deltalake>=0.6.4,<0.7.0',
 'distributed>=2022.11.1,<2023.0.0',
 's3fs>=2022.10.0']

setup_kwargs = {
    'name': 'dask-deltalake',
    'version': '0.0.1',
    'description': 'Dask + Deltalake',
    'long_description': '## Dask Deltalake\nReads and write to deltalake from Dask leveraging delta-rs\n\n## Dask Deltalake Reader\n\nReads data from Deltalake with Dask\n\nTo Try out the package:\n\n```\npip install dask_deltalake\n```\n\n### Features:\n1. Reads the parquet files based on delta logs parallely using dask engine\n2. Supports all three filesystem like s3, azurefs, gcsfs\n3. Supports some delta features like\n   - Time Travel\n   - Schema evolution\n   - parquet filters\n     - row filter\n     - partition filter\n4. Query Delta commit info - History\n5. vacuum the old/ unused parquet files\n6. load different versions of data using datetime.\n\n### Usage:\n\n```\nimport dask_deltalake as ddl\n\n# read delta table\nddl.read_delta("delta_path")\n\n# read delta table for specific version\nddl.read_delta("delta_path",version=3)\n\n# read delta table for specific datetime\nddl.read_delta("delta_path",datetime="2018-12-19T16:39:57-08:00")\n\n\n# read delta complete history\nddl.read_delta_history("delta_path")\n\n# read delta history upto given limit\nddl.read_delta_history("delta_path",limit=5)\n\n# read delta history to delete the files\nddl.vacuum("delta_path",dry_run=False)\n\n# Can read from S3,azure,gcfs etc.\nddl.read_delta("s3://bucket_name/delta_path",version=3)\n# please ensure the credentials are properly configured as environment variable or\n# configured as in ~/.aws/credential\n\n# can connect with AWS Glue catalog and read the complete delta table (currently only AWS catalog available)\n# will take expilicit AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY from environment\n# variables if available otherwise fallback to ~/.aws/credential\nddl.read_delta(catalog=glue,database_name="science",table_name="physics")\n\n```\n',
    'author': 'Greg Hayes',
    'author_email': 'hayesgb@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4',
}


setup(**setup_kwargs)
