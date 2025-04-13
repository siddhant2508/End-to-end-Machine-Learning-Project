import setuptools
with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()
__version__ = "0.0.0"
REPO_NAME = "End-to-end-Machine-Learning-Project- Implementation"

AUTHOR_USER_NAME = "siddhant2508"
SCR_REPO = "mlProject"
AUTHOR_EMAIL = "siddhantdhatrak32@gmail.com"

setuptools.setup(
    name=SCR_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A sma;; python package for ml app",
    long_description = long_description,
    project_url = f"https://github.com/siddhant2508/End-to-end-Machine-Learning-Project.git",
    package_dir={"":"src"},
    package=setuptools.find_packages(where="src")
)
