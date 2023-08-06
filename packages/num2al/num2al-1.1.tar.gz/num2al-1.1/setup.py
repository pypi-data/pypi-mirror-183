from setuptools import setup

setup(
    name="num2al",
    version="1.1",
    packages=["num2al"],
    entry_points={"console_scripts": ["words=num2al:words"]},
    description="A package for converting numbers to Albanian words",
    long_description="This package provides a function for converting numbers to their corresponding words in Albanian. It supports numbers up to one trillion and includes special handling for numbers between 10 and 19.",
)
