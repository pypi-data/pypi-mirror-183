import logging
import os

from .module_info import ModuleInfo

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def scan_source_folder_for_modules(
    path_source: str,
    path_target: str,
) -> list[ModuleInfo]:
    """Сканируем файлы в папке и создаем список потенциальных модулей."""
    log.debug("Начинаем сканировать папку и искать модули")
    modules: list[ModuleInfo] = []
    for dirpath, _, filenames in os.walk(path_source):
        log.debug("Сканирование папки, dirpath: %s", dirpath)
        for module in filenames:
            if module[-3:] != ".py":
                continue
            if module == "main.py":
                continue
            log.debug("Найден модуль {0}".format(module))
            modules.append(
                ModuleInfo(
                    path_module=dirpath,
                    filename=module[:-3],
                    path_source=path_source,
                    path_target=path_target,
                ),
            )
    return modules
