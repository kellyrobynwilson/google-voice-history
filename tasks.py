# type: ignore
import os

from invoke import task

FILES = "src tests *.py"

os.environ["INVOKE_RUN_ECHO"] = "1"


@task
def format(c):
    """Format Python files with isort and black."""
    c.run(f"isort {FILES}")
    c.run(f"black {FILES}")


@task
def check(c):
    """Check Python files for code style and type errors."""
    c.run(f"isort --check {FILES}")
    c.run(f"black --check {FILES}")
    c.run(f"flake8 {FILES}")
    c.run(f"mypy {FILES}")
