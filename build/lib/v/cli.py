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
        gp='git push',
        gl='git pull',
        glo='git log --oneline',
        ghh='git help',
        gcpa='git cherry-pick --abort',
        gcpc='git cherry-pick --continue',
    
    )
    os.system(git.get(alias))

def start():
    main(obj={})




if __name__ == "__main__":
    start()
