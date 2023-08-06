#!/usr/bin/env python
# coding: utf-8
import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

# Package meta-data.
NAME = 'nonebot_plugin_HttpCat'
DESCRIPTION = '_✨Nonebot猫猫http状态码插件✨_'
URL = 'https://github.com/ANGJustinl/nonebot_plugin_HttpCat'
EMAIL = 'angjustin@163.com'
AUTHOR = 'ANGJustinl'
VERSION = '0.0.1'

setuptools.setup(
    name="nonebot_plugin_HttpCat",
    version="0.0.1",
    author="ANGJustinl",
    author_email="angjustin@163.com",
    keywords=["pip", "nonebot2", "nonebot", "nonebot_plugin"],
    description="""_✨Nonebot猫猫http状态码插件✨_""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ANGJustinl/nonebot_plugin_HttpCat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=[
        'nonebot2>=2.0.0rc2',
        'nonebot-adapter-onebot>=2.1.5',
        'https>=0.23.0',     
        'BeautifulSoup4>=4.11.1'          
    ],
    python_requires=">=3.7"
)
