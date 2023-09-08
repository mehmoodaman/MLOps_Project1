import setuptools

with open('README.md', "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "MLOps_Project1"
AUTHOR_USER_NAME = "mehmoodaman"
SRC_REPO = "MLOps_Project1"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="an ML project",
    Long_description=long_description,
    Long_description_content="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

