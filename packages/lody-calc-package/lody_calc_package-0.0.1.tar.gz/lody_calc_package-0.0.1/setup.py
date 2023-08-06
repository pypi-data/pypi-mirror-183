import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "lody_calc_package",
    version = "0.0.1",
    author = "lodyne",
    author_email = "lodgmtui@gmail.com",
    description = "A calculator package",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/lodyne/lody_calc_package",
    project_urls = {
        "Package builder": "https://github.com/lodyne/lody_calc_package",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)