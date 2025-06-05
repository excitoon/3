import os

import setuptools


with open(f"{os.path.dirname(os.path.abspath(__file__))}/requirements.txt") as requirements:
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/README.md") as readme:
        setuptools.setup(
            name="3-py",
            version="2.0.1",
            description="`.gitignore`-aware tree tool written in Python",
            long_description=readme.read(),
            long_description_content_type="text/markdown",
            author="Vladimir Chebotarev",
            author_email="vladimir.chebotarev@gmail.com",
            license="MIT",
            classifiers=[
                "Development Status :: 5 - Production/Stable",
                "Environment :: Console",
                "Intended Audience :: Developers",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
                "Programming Language :: Python :: 3 :: Only",
                "Programming Language :: Python :: 3.7",
                "Programming Language :: Python :: 3.8",
                "Programming Language :: Python :: 3.9",
                "Programming Language :: Python :: 3.10",
                "Programming Language :: Python :: 3.11",
                "Programming Language :: Python :: 3.12",
                "Topic :: Software Development",
                "Topic :: Terminals",
                "Topic :: Utilities",
            ],
            keywords=["git", "gitignore", "tree"],
            project_urls={
                "Documentation": "https://github.com/excitoon/3/blob/master/README.md",
                "Source": "https://github.com/excitoon/3",
                "Tracker": "https://github.com/excitoon/3/issues",
            },
            url="https://github.com/excitoon/3",
            packages=[],
            scripts=["3", "3.cmd"],
            install_requires=requirements.read().splitlines(),
        )
