from invoke import task

@task
def start(ctx):
    ctx.run("python src/index.py", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src/")

@task
def test(ctx):
    ctx.run("pytest")
