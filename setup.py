import setuptools


setuptools.setup(
    name="3-py",
    version="1.0.1",
    author="Vladimir Chebotarev",
    description="`.gitignore`-aware tree tool written in Python",
    packages=[],
    scripts=["3"],
    install_requires=["gitignore-parser"],
)
