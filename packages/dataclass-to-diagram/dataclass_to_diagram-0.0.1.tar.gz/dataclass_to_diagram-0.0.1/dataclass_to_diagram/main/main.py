"""Точка входа для генерации схем."""

import logging
from types import ModuleType

from ..models.base_model import BaseModel

from .import_modules import import_modules
from .module_info import ModuleInfo
from .prepare_target_folder import prepare_target_folder
from .scan_source_folder_for_modules import scan_source_folder_for_modules

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def __dia_from_module(module: ModuleType) -> tuple[BaseModel]:
    """Список диаграмм из модуля."""
    dias: list[BaseModel] = []
    for item in module.__dict__.values():
        if isinstance(item, BaseModel):
            dias.append(item)
    return tuple(dias)


def generate_images(path_source: str, path_target: str) -> None:
    """Основная функция для генерации изображений.

    Parameters
    ----------
    path_source: str
        путь к папке с текстовым описанием диаграмм
    path_target: str
        путь к папке, куда будут сохраняться изображения
    """
    prepare_target_folder(
        path_source=path_source,
        path_target=path_target,
    )
    potential_modules: list[ModuleInfo] = scan_source_folder_for_modules(
        path_source=path_source,
        path_target=path_target,
    )
    imported_modules: list[ModuleInfo] = import_modules(
        potential_modules=potential_modules,
    )
    # генерируем диаграммы
    for mod, _path in [
        (mod.imported, mod.path_image) for mod in imported_modules
    ]:
        if mod is None:
            continue
        dias_in_module = __dia_from_module(mod)
        log.debug(
            "В модуле %s найдено диаграмм: %s",
            mod,
            len(dias_in_module),
        )
        for dia in dias_in_module:
            for dia_format in dia.get_images():
                with open(_path + "/" + dia_format.filename, "wb") as stream:
                    stream.write(dia_format.content)
