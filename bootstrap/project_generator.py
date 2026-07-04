from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DIRECTORIES = [
    "src",
    "src/core",
    "src/core/application",
    "src/core/database",
    "src/core/security",
    "src/core/utils",
    "src/models",
    "src/services",
    "src/repositories",
    "src/modules",
    "src/ui",
    "src/ui/widgets",
    "src/ui/dialogs",
    "src/ui/windows",
    "src/resources",
    "src/resources/icons",
    "src/resources/images",
    "src/resources/themes",
    "config",
    "logs",
    "exports",
    "backups",
    "tests",
    "docs",
]

FILES = [
    "app.py",
    "src/__init__.py",
    "src/app.py",
    "src/config.py",
    "src/settings.py",
    "src/constants.py",
]


def create_directory(path):
    path.mkdir(parents=True, exist_ok=True)


def create_file(path):
    if not path.exists():
        path.write_text("", encoding="utf-8")


def main():

    print("=" * 60)
    print("TeslaERP Project Generator")
    print("=" * 60)

    for directory in DIRECTORIES:
        create_directory(ROOT / directory)
        print("DIR :", directory)

    for file in FILES:
        create_file(ROOT / file)
        print("FILE:", file)

    print()
    print("Project Generated Successfully.")


if __name__ == "__main__":
    main()