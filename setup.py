import setuptools

with open('README.md', "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "MLOps Project1"
AUTHOR_USER_NAME = "mehmoodaman"
SRC_REPO = "MLOps Project1"


setuptools.setup(
    name=SRC_REPO
    version=__version__
    author=AUTHOR_USER_NAME
    description="an ML project"
)

