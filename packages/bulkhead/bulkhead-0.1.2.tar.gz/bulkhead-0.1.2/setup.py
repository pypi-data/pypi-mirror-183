from setuptools import setup, find_packages

setup(
    name="bulkhead",
    version="0.1.2",
    packages=find_packages(),
    author="Julian M. Kleber",
    author_email="julian.m.kleber@gmail.com",
    description="package providing objects for API interaction",
    include_package_data=True,
    python_requires=">3.9",
    install_requires=["python-dotenv"],
)
