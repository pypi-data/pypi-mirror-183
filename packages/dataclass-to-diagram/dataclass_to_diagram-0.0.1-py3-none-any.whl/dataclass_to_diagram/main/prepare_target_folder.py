"""Подготовить целевую папку."""

import os
import shutil


def __ignore_files(directory: str, files: list[str]) -> list[str]:
    """Игнорировать файлы при копировании дерева папок."""
    return [f for f in files if os.path.isfile(os.path.join(directory, f))]


def prepare_target_folder(path_source: str, path_target: str) -> None:
    """Подготовить целевую папку."""
    # удаляем целевую папку
    shutil.rmtree(path=path_target, ignore_errors=True)
    # копируем структуру папок
    shutil.copytree(
        src=path_source,
        dst=path_target,
        ignore=__ignore_files,
    )
    # создаем файл пояснения
    with open(
        "{0}/__this_folder_is_automatically_generated__".format(path_target),
        "w",
    ) as desc_file:
        desc_file.write("")
