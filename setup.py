import setuptools


setuptools.setup(
    name="3-py",
    version="1.0.6",
    description="`.gitignore`-aware tree tool written in Python",
    long_description="`.gitignore`-aware tree tool written in Python.",
    long_description_content_type="text/markdown",
    author="Vladimir Chebotarev",
    author_email="vladimir.chebotarev@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="git gitignore tree",
    project_urls={
        "Documentation": "https://github.com/excitoon/3/blob/master/README.md",
        "Source": "https://github.com/excitoon/3",
        "Tracker": "https://github.com/excitoon/3/issues",
    },
    packages=[],
    scripts=["3"],
    install_requires=["gitignore-parser"],
)
