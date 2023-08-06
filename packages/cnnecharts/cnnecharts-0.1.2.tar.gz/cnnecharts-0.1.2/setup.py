#!/usr/bin/env python
"""The setup script."""

from setuptools import setup, find_packages
import cnnecharts as cecharts

with open("README.md", encoding="utf8") as readme_file:
    readme = readme_file.read()

requirements = ["pandas", "jinja2"]

test_requirements = [
    "pytest>=3",
]

setup(
    author="carson_jia",
    author_email="568166495@qq.com",
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="...",
    entry_points={
        # 'console_scripts': [
        #     'test_prj=test_prj.cli:main',
        # ],
    },
    install_requires=requirements,
    license="MIT license",
    # long_description=readme,
    include_package_data=True,
    keywords=["cnnecharts", "cnnechart", "echarts", "BI", "report"],
    name="cnnecharts",
    packages=find_packages(include=["cnnecharts", "cnnecharts.*"]),
    # data_files=[('template', [
    #     'cechart/template/index.html',
    #     'pybiland/template/plotly-2.9.0.min.js'
    # ])],
    test_suite="__tests",
    tests_require=test_requirements,
    url="",
    version=cecharts.__version__,
    zip_safe=False,
)
