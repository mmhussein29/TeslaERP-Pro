from pathlib import Path

folders = [
    "src",
    "src/core",
    "src/database",
    "src/models",
    "src/repositories",
    "src/services",
    "src/resources",
    "src/ui",

    "src/modules",
    "src/modules/auth",
    "src/modules/dashboard",
    "src/modules/customers",
    "src/modules/suppliers",
    "src/modules/products",
    "src/modules/inventory",
    "src/modules/sales",
    "src/modules/purchases",
    "src/modules/accounting",
    "src/modules/hr",
    "src/modules/projects",
    "src/modules/reports",
    "src/modules/settings",

    "tests",
    "docs",
    "scripts",
    "config",
    "logs",
    "exports",
    "backups",
    "migrations",
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)
    Path(folder, "__init__.py").touch(exist_ok=True)

print("Project structure created successfully.")