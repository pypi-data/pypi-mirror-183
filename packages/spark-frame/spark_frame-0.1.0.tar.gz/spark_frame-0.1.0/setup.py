# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spark_frame',
 'spark_frame.examples',
 'spark_frame.fp',
 'spark_frame.graph_impl',
 'spark_frame.nested_functions_impl',
 'spark_frame.nested_impl',
 'spark_frame.transformations_impl']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'spark-frame',
    'version': '0.1.0',
    'description': 'A library containing various utility functions for playing with PySpark DataFrames',
    'long_description': "# Spark-frame\n\n[![PyPI version](https://badge.fury.io/py/spark-frame.svg)](https://badge.fury.io/py/spark-frame)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/spark-frame.svg)](https://pypi.org/project/spark-frame/)\n[![GitHub Build](https://img.shields.io/github/actions/workflow/status/FurcyPin/spark-frame/build_and_validate.yml?branch=main)](https://github.com/FurcyPin/spark-frame/actions)\n[![SonarCloud Coverage](https://sonarcloud.io/api/project_badges/measure?project=FurcyPin_spark-frame&metric=coverage)](https://sonarcloud.io/component_measures?id=FurcyPin_spark-frame&metric=coverage&view=list)\n[![SonarCloud Bugs](https://sonarcloud.io/api/project_badges/measure?project=FurcyPin_spark-frame&metric=bugs)](https://sonarcloud.io/component_measures?metric=reliability_rating&view=list&id=FurcyPin_spark-frame)\n[![SonarCloud Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=FurcyPin_spark-frame&metric=vulnerabilities)](https://sonarcloud.io/component_measures?metric=security_rating&view=list&id=FurcyPin_spark-frame)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/spark-frame)](https://pypi.org/project/spark-frame/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n\n## What is it ?\n\n[Spark-frame](https://furcypin.github.io/spark-frame/) is a library that brings several utility methods and \ntransformation functions for PySpark DataFrames.\nThese methods were initially part of the [karadoc](https://github.com/FurcyPin/karadoc) project \nused at [Younited](https://medium.com/younited-tech-blog), but they don't rely on karadoc, \nso it makes more sense to keep them as standalone library.\n\nSeveral of these methods were my initial inspiration to make the cousin project \n[bigquery-frame](https://github.com/FurcyPin/bigquery-frame), which is why you will find similar \nmethods in `transformations` and `data_diff` for both `spark_frame` and `bigquery_frame`, except\nthe former runs on PySpark while the latter runs on BigQuery (obviously).\n\n## Getting Started\n\nVisit the official Spark-frame website [documentation](https://furcypin.github.io/spark-frame/) \nfor [use cases examples](https://furcypin.github.io/spark-frame/use_cases/intro/) \nand [reference](https://furcypin.github.io/spark-frame/reference/functions/).\n\n## Installation\n\n[spark-frame is available on PyPi](https://pypi.org/project/spark-frame/).\n\n```bash\npip install spark-frame\n```\n\n## Compatibilities and requirements\n\nThis library does not depend on any other library.\nPyspark must be installed separately to use it.\nIt is compatible with the following versions:\n\n- Python: requires 3.8.1 or higher (tested against Python 3.9, 3.10 and 3.11)\n- pyspark: requires 3.3.0 or higher\n\nThis library is tested against Mac and Linux.\n\n# Release notes\n\n# v0.1.0\n\n- Added a new _amazing_ module called `spark_frame.nested`, \n  which makes manipulation of nested data structure much easier!\n  Make sure to check out the [reference](https://furcypin.github.io/spark-frame/reference/nested/)\n  and the [use-cases](https://furcypin.github.io/spark-frame/use_cases/working_with_nested_data/).\n\n- Also added a new module called `spark_frame.nested_functions`,\n  which contains aggregation methods for nested data structures\n  ([See Reference](https://furcypin.github.io/spark-frame/reference/nested_functions/)).\n\n- New [transformations](https://furcypin.github.io/spark-frame/reference/transformations/):\n  - `spark_frame.transformations.transform_all_field_names`\n  - `spark_frame.transformations.transform_all_fields`\n  - `spark_frame.transformations.unnest_field`\n  - `spark_frame.transformations.unnest_all_fields`\n  - `spark_frame.transformations.union_dataframes`\n\n# v0.0.3\n\n- New transformation: `spark_frame.transformations.convert_all_maps_to_arrays`.\n- New transformation: `spark_frame.transformations.sort_all_arrays`.\n- New transformation: `spark_frame.transformations.harmonize_dataframes`.\n",
    'author': 'FurcyPin',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/FurcyPin/spark-frame',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8.1,<3.11',
}


setup(**setup_kwargs)
