import sys
from pathlib import Path

PROJECT_NAME = sys.argv[1] if len(sys.argv) > 1 else "my_project"

def create_repo():
    base = Path(PROJECT_NAME)

    # ----------------------------
    # Folders
    # ----------------------------
    folders = [
        f"src/{PROJECT_NAME}",
        "tests",
        "notebooks",
        "data",
        "outputs",
    ]

    for folder in folders:
        (base / folder).mkdir(parents=True, exist_ok=True)

    # ----------------------------
    # Files
    # ----------------------------
    files = {
        "README.md": f"# {PROJECT_NAME}\n\nMinimal Python project.\n",

        ".gitignore": """
__pycache__/
*.pyc
.venv
.ipynb_checkpoints/

# keep structure but ignore contents
data/*
!data/.gitkeep

outputs/*
!outputs/.gitkeep
""",

        "pyproject.toml": f"""
[project]
name = "{PROJECT_NAME}"
version = "0.1.0"
description = "Minimal Python project"
authors = [{{name = "Your Name"}}]
dependencies = []

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
""",

        f"src/{PROJECT_NAME}/__init__.py": "",

        f"src/{PROJECT_NAME}/main.py": """from pathlib import Path

def main():
    output_file = Path("outputs/result.txt")
    output_file.parent.mkdir(exist_ok=True)

    with open(output_file, "w") as f:
        f.write("Hello from the project!")

    print("Execution finished. Output saved.")

if __name__ == "__main__":
    main()
""",

        f"src/{PROJECT_NAME}/utils.py": """def add(a, b):
    return a + b
""",

        "tests/test_basic.py": """from my_project.utils import add

def test_add():
    assert add(2, 3) == 5
""",

        "data/.gitkeep": "",
        "outputs/.gitkeep": "",

        "notebooks/exploration.ipynb": """{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
""",
    }

    # ----------------------------
    # Create files
    # ----------------------------
    for path, content in files.items():
        file_path = base / path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content.strip(), encoding="utf-8")

    print(f"✅ Repository '{PROJECT_NAME}' created successfully.")

if __name__ == "__main__":
    create_repo()