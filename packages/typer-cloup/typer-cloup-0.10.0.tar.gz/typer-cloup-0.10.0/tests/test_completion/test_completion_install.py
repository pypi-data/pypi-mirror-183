import os
import subprocess
from pathlib import Path

import typer_cloup as typer
from docs_src.commands.index import tutorial001 as mod
from typer_cloup.testing import CliRunner

runner = CliRunner()
app = typer.Typer()
app.command()(mod.main)


def test_completion_install_no_shell():
    result = subprocess.run(
        ["coverage", "run", mod.__file__, "--install-completion"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        env={
            **os.environ,
            "_TYPER_COMPLETE_TESTING": "True",
            "_TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION": "True",
        },
    )
    assert "Error: Option '--install-completion' requires an argument" in result.stderr


def test_completion_install_bash():
    bash_completion_path: Path = Path.home() / ".bashrc"
    text = ""
    if bash_completion_path.is_file():
        text = bash_completion_path.read_text()
    result = subprocess.run(
        ["coverage", "run", mod.__file__, "--install-completion", "bash"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        env={
            **os.environ,
            "_TYPER_COMPLETE_TESTING": "True",
            "_TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION": "True",
        },
    )
    new_text = bash_completion_path.read_text()
    bash_completion_path.write_text(text)
    install_source = ".bash_completions/tutorial001.py.sh"
    assert install_source not in text
    assert install_source in new_text
    assert "completion installed at" in result.stdout
    assert "Completion will take effect once you restart the terminal" in result.stdout
    install_source_path = Path.home() / install_source
    assert install_source_path.is_file()
    install_content = install_source_path.read_text()
    install_source_path.unlink()
    assert (
        "complete -o nosort -F _tutorial001py_completion tutorial001.py"
        in install_content
    )


def test_completion_install_zsh():
    completion_path: Path = Path.home() / ".zshrc"
    text = ""
    if not completion_path.is_file():  # pragma: no cover
        completion_path.write_text('echo "custom .zshrc"')
    if completion_path.is_file():
        text = completion_path.read_text()
    result = subprocess.run(
        ["coverage", "run", mod.__file__, "--install-completion", "zsh"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        env={
            **os.environ,
            "_TYPER_COMPLETE_TESTING": "True",
            "_TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION": "True",
        },
    )
    new_text = completion_path.read_text()
    completion_path.write_text(text)
    zfunc_fragment = "fpath+=~/.zfunc"
    assert zfunc_fragment in new_text
    assert "completion installed at" in result.stdout
    assert "Completion will take effect once you restart the terminal" in result.stdout
    install_source_path = Path.home() / ".zfunc/_tutorial001.py"
    assert install_source_path.is_file()
    install_content = install_source_path.read_text()
    install_source_path.unlink()
    assert "compdef _tutorial001py_completion tutorial001.py" in install_content


def test_completion_install_fish():
    script_path = Path(mod.__file__)
    completion_path: Path = (
        Path.home() / f".config/fish/completions/{script_path.name}.fish"
    )
    result = subprocess.run(
        ["coverage", "run", mod.__file__, "--install-completion", "fish"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        env={
            **os.environ,
            "_TYPER_COMPLETE_TESTING": "True",
            "_TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION": "True",
        },
    )
    new_text = completion_path.read_text()
    completion_path.unlink()
    assert "complete --no-files --command tutorial001.py" in new_text
    assert "completion installed at" in result.stdout
    assert "Completion will take effect once you restart the terminal" in result.stdout


runner = CliRunner()
app = typer.Typer()
app.command()(mod.main)
