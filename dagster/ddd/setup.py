from setuptools import find_packages, setup

setup(
    name="ddd",
    packages=find_packages(exclude=["ddd_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
