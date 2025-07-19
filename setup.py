import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "krish922"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "kc880303@gmail.com"



setuptools.setup(
    name='TextS',
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
},
    Package_dir={'': 'TextS'},
    packages=setuptools.find_packages(where="TextS"),
)