import click
import os

@click.command()
@click.argument("alias")
def main(alias):
    git = dict(
        g='git',
        gi="git init",
        gaa='git add --all',
        gst='git status',
        gp='git push'
    )
    os.system(git.get(alias))

if __name__ == "__main__":
    main()