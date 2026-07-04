import importlib


class ModuleManager:

    MODULES = [
        "dashboard",
        "crm",
        "sales",
        "inventory",
        "accounting",
        "hr",
        "reports",
        "settings",
    ]

    def load_modules(self):

        loaded = {}

        for module in self.MODULES:

            mod = importlib.import_module(
                f"src.modules.{module}.module"
            )

            loaded[module] = mod

        return loaded