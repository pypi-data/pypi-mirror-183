import importlib
import json
import os
from pkgutil import iter_modules
from pydoc import locate
from inspect import getmembers, isfunction
from sequoia.core.helpers.cache import Cache


async def get_modules():

    cache = Cache()
    await cache.remove_all("module:")
    await cache.remove_all("tasks:")

    async def listasks(module: str):
        """
        List module di folder tasks
        """
        curr = os.path.dirname(__file__)
        package_dir = os.path.dirname(curr) + f"/modules/{module}/tasks"
        for (_, module_name, _) in iter_modules([package_dir]):
            pkg = importlib.import_module(
                f'sequoia.modules.{module}.tasks.__init__')

            # list modules
            method_list = [
                method for method in dir(pkg)
                if method.startswith('__') is False
            ]
            for mdl in method_list:

                kelas = locate(f"sequoia.modules.{module}.tasks.{mdl}")

                ts = getmembers(kelas, isfunction)
                for t in ts:

                    # print('asasa', module_name, t)
                    if t[0].startswith("_") is False:

                        ff = locate(
                            f"sequoia.modules.{module}.tasks.{mdl}.{t[0]}")
                        key = f"tasks:{d.name}:{module_name}:{t[0]}"

                        dat = {
                            "key": key,
                            "module": module,
                            "classfile": module_name,
                            "class": mdl,
                            "class_doc": str(kelas.__doc__).strip(),
                            "func": t[0],
                            "func_doc": str(ff.__doc__).strip()
                        }
                        await cache.set(key, json.dumps(dat))

    # list modules
    drs = os.scandir(os.path.dirname(os.path.dirname(__file__)) + "/modules")
    for d in drs:
        if d.is_dir():
            await cache.set(f"module:{d.name}", d.name)
            await listasks(d.name)
