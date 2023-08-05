# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deployment_tools']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=6.0,<7.0', 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'deployment-tools',
    'version': '0.1.0',
    'description': 'Simple to use command running tools and file transformation/move tools.',
    'long_description': '# DEPLOYMENT-TOOLS\n### Description:\nSmall package simplifying deployment scripts by:\n* easy shell command running, with or without success checks;\n* easy file editing (such as configs, settings, text, etc ...);\n* easy file transfers, directory manipulation, and file reading;\n### Content:\n#### class Command => runs shell command from as list[str], example ["ls", "-la"]\n* raise_on_failure() => raises ShellCommand exception on cmd failure;\n* set_success(check:[str], on_line[int] = None) => check if string is present in outputs, could be specified specific line, where it should be (normal python indexing applies);\n* set_failure(check:[str], on_line[int] = None) => check stderr for string, could be specified specific line, where it should be (normal python indexing applies);\n#### class [File]Builder:\n* invoked by create_file_builder(path: str, type_: str | None = None, blanked=False) => path - location of the file, type_ - if None, the function will decide based on extension, otherwise supported are json, toml, yaml/yml, or it will default to txt; blanked - will void the data in the file;\n* attribute self.base_data, holds all the file information;\n* [+]/[-] operand can be used to either add or remove from the files (including nesting of dicts in cases of nested configs);\n* txt files support self.replace_line(patten, new_line) if pattern in existing line, it will be replaced by new_line;\n* self.replace_string_in_lines(old, new), it will replace old:str with new:str in all occurances in the files;\n#### class WorkingDirectory (singleton):\n* slicing: [file_name] -> returns file content as dict(json, yml/yaml, toml) or list;\n* setting: [file_name] = payload: str|list -> create file with provided data;\n* [+]/[/]/[self.go_to(path)] - operands are used to transfer exectusion to another location;\n* self.back() - return to previous location;\n* self.go_to_home() - return to initial location;\n* self.transfer_with_files(*args) => move execution to a location with all files in current location;\n* self.transfer_and_copy_files(*args) => move execution to a location copy all files in current location;',
    'author': 'Daniel Nikolaev',
    'author_email': 'toolsproed@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
