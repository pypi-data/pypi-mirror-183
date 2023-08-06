#!/usr/bin/env python
# coding: utf-8
import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

# Package meta-data.
NAME = 'nonebot_plugin_animalVoice_main'
DESCRIPTION = '基于 腾讯云合成图的 以图绘图 NoneBot2插件'
URL = 'https://github.com/ANGJustinl/nonebot_plugin_animalVoice_main'
EMAIL = 'angjustin@163.com'
AUTHOR = 'ANGJustinl'
VERSION = '0.0.1'

setuptools.setup(
    name="nonebot_plugin_animalVoice",
    version="0.0.1",
    author="ANGJustinl",
    author_email="angjustin@163.com",
    keywords=["pip", "nonebot2", "nonebot", "nonebot_plugin"],
    description="""_✨Nonebot兽语译者插件✨_""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ANGJustinl/nonebot_plugin_animalVoice_main",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=[
        'nonebot2>=2.0.0rc2',
        'nonebot-adapter-onebot>=2.1.5'               
    ],
    python_requires=">=3.7"
)
