from setuptools import setup, find_packages

setup(
    name="mocha",
    version="1.0.2",
    packages=find_packages(),
    install_requires=[
        "click",
        "rich",
        "colorama",
        "InquirerPy",
    ],
    entry_points={
        "console_scripts": [
            "mocha=mocha.mocha:cli",
        ],
    },
)
