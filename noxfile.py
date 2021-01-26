import tempfile

import nox
from nox.sessions import Session
import nox_poetry.patch  # noqa: F401

nox.options.sessions = "lint", "safety", "tests", "bdd"
nox.options.reuse_existing_virtualenvs = False
locations = "minisculus", "tests", "noxfile.py"


@nox.session(python="3.8")
def lint(session: Session) -> None:
    """Lints the code."""
    args = session.posargs or locations
    session.install(
        "darglint",
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
        "flake8-mypy",
    )
    session.run("flake8", *args)


@nox.session(python=["3.8", "3.9"])
def tests(session: Session) -> None:
    """Runs the test harness."""
    session.install(".")
    session.install("pytest", "coverage[toml]", "hypothesis", "pytest-cov")
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")


@nox.session(python=["3.8"])
def bdd(session: Session) -> None:
    """Runs the bdd features."""
    session.install(".")
    session.install("behave")
    session.install("pyhamcrest")
    session.run("behave")


@nox.session(python="3.8")
def black(session: Session) -> None:
    """Reformats code to be in black."""
    args = session.posargs or locations
    session.install("black", "blackdoc")
    session.run("black", *args)
    session.run("blackdoc", *args)


@nox.session(python="3.8")
def safety(session: Session) -> None:
    """Checks libraries for known vulnerabilities."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python="3.8")
def docs(session: Session) -> None:
    """Build the documentation."""
    session.install(".")
    session.install(
        "auto-behave",
        "sphinx",
        "sphinx-autodoc-typehints",
        "sphinx-rtd-theme",
        "sphinxcontrib.mermaid",
        "six",
    )
    session.run("sphinx-build", "docs", "docs/_build")
