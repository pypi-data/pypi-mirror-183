import pathlib
import click


def __validate_metadata_yml(file_path):
    # assert False, "`title` not included in metadata"
    pass


def __validate_docker_compose_yml(file_path):
    pass


def __validate_english_md(file_path):
    pass


def validate_file_format(file_path):
    mapping = {
        "metadata.yml": __validate_metadata_yml,
        "docker-compose.yml": __validate_docker_compose_yml,
        "english.md": __validate_english_md,
    }
    validator_callable = mapping[file_path.name]
    validator_callable(file_path)


@click.group()
@click.version_option('0.1.0')
def content_tools():
    pass


@content_tools.command()
@click.argument(
    "path", type=click.Path(exists=True, path_type=pathlib.Path),
)
def validate_module_repo(path):
    ERROR_MSG = "Oh no! 💥 💔 💥"
    assert path.is_dir(), "Required a directory path"

    # check required files
    for file in ("metadata.yml", "docker-compose.yml", "english.md"):
        try:
            assert (path / file).exists(), f"`{file}` not found"
        except AssertionError as exc:
            click.echo(f"{ERROR_MSG} {str(exc)}")
            exit(1)
        else:
            click.echo(f"✅ {file} exists")

        try:
            validate_file_format(path / file)
        except AssertionError as exc:
            click.echo(f"{ERROR_MSG} {str(exc)}")
            exit(1)
        else:
            click.echo(f"✅ {file} has a valid format")

    click.echo("All done! ✨ 🍰 ✨")


if __name__ == "__main__":
    content_tools()
