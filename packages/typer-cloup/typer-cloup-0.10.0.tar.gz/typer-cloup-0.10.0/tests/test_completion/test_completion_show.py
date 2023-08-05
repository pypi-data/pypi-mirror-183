import os
import subprocess

from docs_src.commands.index import tutorial001 as mod


def test_completion_show_no_shell():
    result = subprocess.run(
        ["coverage", "run", mod.__file__, "--show-completion"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        env={
            **os.environ,
            "_TYPER_COMPLETE_TESTING": "True",
            "_TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION": "True",
        },
    )
    assert "Error: Option '--show-completion' requires an argument" in result.stderr


def test_completion_show_bash():
    result = subprocess.run(
        ["coverage", "run", mod.__file__, "--show-completion", "bash"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        env={
            **os.environ,
            "_TYPER_COMPLETE_TESTING": "True",
            "_TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION": "True",
        },
    )
    assert (
        "complete -o nosort -F _tutorial001py_completion tutorial001.py"
        in result.stdout
    )


def test_completion_source_zsh():
    result = subprocess.run(
        ["coverage", "run", mod.__file__, "--show-completion", "zsh"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        env={
            **os.environ,
            "_TYPER_COMPLETE_TESTING": "True",
            "_TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION": "True",
        },
    )
    assert "compdef _tutorial001py_completion tutorial001.py" in result.stdout


def test_completion_source_fish():
    result = subprocess.run(
        ["coverage", "run", mod.__file__, "--show-completion", "fish"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        env={
            **os.environ,
            "_TYPER_COMPLETE_TESTING": "True",
            "_TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION": "True",
        },
    )
    assert "complete --no-files --command tutorial001.py" in result.stdout
