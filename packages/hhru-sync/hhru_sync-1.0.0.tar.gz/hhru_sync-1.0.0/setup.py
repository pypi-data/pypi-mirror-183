from distutils.core import setup

import re


with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open("hhru_sync/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()


setup(
    name = "hhru_sync",
    packages = ["hhru_sync"],
    version = version,
    license = "MIT",
    description = "Элегантная библиотека для взаимодействия с сайтом hh.ru",
    author = "Dmitriy Yablokov",
    author_email = "dimon4ik_228@bk.ru",
    url = "https://github.com/Dangeres/hhru_sync",
    download_url = "https://github.com/Dangeres/hhru_sync/releases/latest",
    keywords = "hhru hh.ru headhunter.ru api library python",
    install_requires = requires,
    long_description = readme,
    long_description_content_type = "text/markdown",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    zip_safe = False,
)