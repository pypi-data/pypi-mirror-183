import setuptools


setuptools.setup(
    name="cloop",
    version="0.1",
    author="Francis B. Lavoie",
    author_email="francis.b.lavoie@usherbrooke.ca",
    description="CLoop",
    long_description="CLoop",
    long_description_content_type="text/markdown",
    url="https://catalyseur.ca",
    packages=setuptools.find_packages(),
    install_requires = ["mariadb","pyodbc"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)