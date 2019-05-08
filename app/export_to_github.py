from github import Github
from datetime import datetime
from config import Config
# First create a Github instance:


def get_repos():
    # using an access token
    g = Github(Config.ACCESS_TOKEN)

    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
        print(repo.name)


def update_create_file(repo, filename, content, message):
    try:
        contents = repo.get_contents(filename)
    except:
        contents = None

    # Erstelle File falls nicht existent
    if not contents:
        repo.create_file(path=filename, message=message, content=content, branch="master")
    else:
        contents = repo.get_contents(filename)
        repo.update_file(path=filename, message=message, content=content, sha=contents.sha)


def upload_files(filenames, content):
    g = Github(Config.ACCESS_TOKEN)
    repo = g.get_user().get_repo(name=Config.TARGET_REPO)
    message = "AutoCommit per " + datetime.ctime(datetime.utcnow())
    for file, filename in zip(content, filenames):
        update_create_file(
            repo=repo,
            filename="Projekte/" + filename + ".md",
            content=file,
            message=message)
