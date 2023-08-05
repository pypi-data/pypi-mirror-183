# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dataclass_to_diagram',
 'dataclass_to_diagram.dia',
 'dataclass_to_diagram.dia.c4',
 'dataclass_to_diagram.dia.c4.sprite_lib',
 'dataclass_to_diagram.dia.c4.sprite_lib.tupadr3_lib',
 'dataclass_to_diagram.dia.mermaid_er',
 'dataclass_to_diagram.dia.mermaid_state',
 'dataclass_to_diagram.exporters',
 'dataclass_to_diagram.exporters.erd_to_dbml',
 'dataclass_to_diagram.main',
 'dataclass_to_diagram.models',
 'dataclass_to_diagram.models.erd',
 'dataclass_to_diagram.service']

package_data = \
{'': ['*']}

install_requires = \
['requests']

entry_points = \
{'console_scripts': ['dataclass_to_diagram = '
                     'dataclass_to_diagram.__main__:start']}

setup_kwargs = {
    'name': 'dataclass-to-diagram',
    'version': '0.0.1',
    'description': 'Создание диаграмм из датаклассов python',
    'long_description': '[![PyPI version](https://badge.fury.io/py/dataclass-to-diagram.svg)](https://badge.fury.io/py/dataclass-to-diagram)\n\n# dataclass_to_diagram\n\nСоздание диаграмм из датаклассов python\n\n\n\nСостоит из пакетов:\n\n- main - основной пакет для запуска\n- models - модели на основе dataclass для различных диаграмм\n- exporters - экспорт моделей в текстовый формат\n- converters - конвертирование текстового формата в изображение (svg, png, pdf, ...)\n\n\n\n### exporters\n\n#### dbml\n\nЭкспорт моделей БД (ERD) в формат [dbml](https://www.dbml.org/home/)\n\n\n\n### converters\n\n#### dbml-renderer\n\nКонвертирует файл с разметкой dbml в svg-изображение.\n\nУстановка:\n\n```bash\nnpm install -g @softwaretechnik/dbml-renderer\n```\n\n\n\n\n\n\n\nБиблиотека для генерации диаграмм из текстового описания.\n\nДиаграммы описываются объектами python. Далее геренируются изображения с помощью https://kroki.io.\n\n\n\n\n\n## Как использовать\n\n1. Создать две папки:\n\n   - dia_src - папка с исходным описанием\n   - dia_dist - папка со сгенерированными изображениями\n\n2. В папке dia_src создаются py-файлы. Названия файлов - произвольные. Можно создавать подкаталоги - структура каталогов будет скопирована в целевую папку dia_dist. Примеры создания можно посмотреть в тестовых диаграммах [пакета](https://github.com/Konstantin-Dudersky/konstantin_docs/tree/main/test).\n\n3. Для генерации можно создать задачу poetepoet. Прописать в файле pyproject.toml:\n\n   ```toml\n   [tool.poetry.dependencies]\n   konstantin_docs = "*"\n   poethepoet = "*"\n\n   [tool.poe.tasks]\n   docs = {script = "konstantin_docs.main:generate_images(\'dia_src\', \'dia_dist\')"}\n   ```\n\n4. Запустить командой:\n\n   ```sh\n   poetry run poe docs\n   ```\n\n5. Дополнительно можно создать задачу в vscode. Для этого в файле .vscode/tasks.json:\n\n   ```json\n   {\n     "version": "2.0.0",\n     "tasks": [\n       {\n         "label": "docs",\n         "type": "shell",\n         "command": "poetry run poe docs"\n       }\n     ]\n   }\n   ```\n\n   Запускать командой F1 -> Task: Run task -> docs\n\nERD\n\n```bash\nnpm install -g @softwaretechnik/dbml-renderer\n```\n\n\n\n## Разработка\n\n```bash\npoetry build && poetry publish\n```\n\n\n\n',
    'author': 'konstantin-dudersky',
    'author_email': 'konstantin.dudersky@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Konstantin-Dudersky/dataclass_to_diagram.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
