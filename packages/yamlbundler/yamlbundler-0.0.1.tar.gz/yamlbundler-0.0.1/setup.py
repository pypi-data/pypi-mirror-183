# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yamlbundler']

package_data = \
{'': ['*']}

install_requires = \
['jsonpath-ng>=1.5.3,<2.0.0', 'pyyaml>=6.0,<7.0']

entry_points = \
{'console_scripts': ['yamlbundler = yamlbundler.command:run']}

setup_kwargs = {
    'name': 'yamlbundler',
    'version': '0.0.1',
    'description': '',
    'long_description': '# YAML Bundler\n`yamlbundler` is a useful command that bundles multiple YAML files into a single file.\nIt finds `!include` tag in a YAML file and replaces it with the contents of another YAML file.\n\n## Install\n\n```bash\npip install yamlbundler\n```\n\n## Quick start\nSave these files in your working directory.\n\n```yaml\n# ./main.yaml\n\n# include entire file\na: !include ./sub1.yaml  # relative path from the parent directory of main.yaml \nb: !include\n  filepath: ./sub2.yaml \n\n# include specific value using jsonpath\nc: !include\n  filepath: ./sub1.yaml\n  jsonpath: $.foo\n\n# include multiple files\n# Array elements are flattened.\nd: !include\n- filepath: ./sub1.yaml\n- filepath: ./sub2.yaml\n\n# include multiple files\n# If all of them are map elements, they are merged into a single map.\ne: !include\n- filepath: ./sub1.yaml\n- filepath: ./sub3.yaml\n```\n```yaml\n# ./sub1.yaml\nfoo: bar\n```\n\n```yaml\n# ./sub2.yaml\n- one\n- two\n```\n\n```yaml\n# ./sub3.yaml\nhoge: !include\n  # relative path from the parent directory of sub3.yaml (not main.yaml)\n  filepath: ./sub2.yaml\n  jsonpath: $[0]\n```\n\nThen, run this command.\nThe result is shown in your terminal as STDOUT.\nComments in original YAML are removed.\n\n```bash\nyamlbundler ./main.yaml\n\n# a:\n#   foo: bar\n# b:\n# - one\n# - two\n# c: bar\n# d:\n# - foo: bar\n# - one\n# - two\n# e:\n#   foo: bar\n#   hoge: one\n```\n\nYou can save the result as a new file using `--output` parameter.\nIf you want to overwrite the original file, use `--inplace` parameter.\n\n```bash\nyamlbundler --output ./result.yaml ./main.yaml\nyamlbundler --inplace ./main.yaml\n```\n\n# Feedback\nIf you find any bugs, please feel free to create an issue.\n',
    'author': 'dr666m1',
    'author_email': 'skndr666m1@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
