import setuptools

# Print project readme description when published as PyPI package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
    
"""
The setup.py file is a Python script commonly used in Python projects to define metadata about the project 
and specify how the project should be packaged and distributed. 
"""


__version__ = "0.0.0"

REPO_NAME = "kidney-disease-classification"
AUTHOR_USER_NAME = "PySciJ"
SRC_REPO = "cnnClassifier" # Defined as local package dir
AUTHOR_EMAIL = "ho.jiajun@outlook.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"}, 
    packages=setuptools.find_packages(where="src") # A list of package names to include in the distribution. 
)

"""
When you call find_packages(where="src"), it scans the "src" directory for Python packages,
by looking for directories containing an __init__.py file, which is a marker that indicates the directory is a Python package,
and it includes all packages found in the search. Each package may contain multiple modules, and find_packages() will include all modules within those packages in the list of packages it returns.
"""