"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Notion Paperpile."""


if __name__ == "__main__":
    main(prog_name="notion_paperpile_")  # pragma: no cover
