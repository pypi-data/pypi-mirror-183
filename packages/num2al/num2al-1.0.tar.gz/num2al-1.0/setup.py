from setuptools import setup

setup(
    name="num2al",
    version="1.0",
    packages=["num2al"],
    entry_points={"console_scripts": ["words=num2al:words"]},
)
