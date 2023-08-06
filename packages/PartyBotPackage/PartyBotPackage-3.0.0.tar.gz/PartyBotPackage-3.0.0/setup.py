import setuptools
import os

for directory in [f.path.split('\\')[-1] for f in os.scandir(os.getcwd()) if f.is_dir()]:
    if directory.startswith('PartyBot') and 'egg' not in directory:
        name = directory.split('.')[0]

with open(f'{name}/__init__.py', encoding="utf8") as f:
    version = f.read().split("__version__ = '")[1].split("'")[0]

with open(r'C:\Users\Oli\Documents\GitHub\PartyBotPackage\requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name=name,
    version=version,
    author="xMistt",
    author_email="oli@partybot.net",
    description="Developer build of PartyBotPackage." if name == "PartyBotDev" else
    "PartyBot in a PyPi package form to easily be ran on repl.",
    long_description_content_type="text/markdown",
    url="https://partybot.net",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=[name],
    python_requires=">=3.5.3",
    install_requires=requirements
)
