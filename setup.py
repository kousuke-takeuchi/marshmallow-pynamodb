from setuptools import setup, find_packages

setup(
    name="marshmallow-pynamodb",
    version="0.9.0",
    packages=find_packages(exclude=('*test*',)),
    package_dir={'marshmallow-pynamodb': 'marshmallow_pynamodb'},
    description='PynamoDB integration with the marshmallow (de)serialization library',
    author='Kousuke Takeuchi',
    author_email='u651601f@gmail.com',
    long_description=open('README.rst').read(),
    install_requires=[
        "marshmallow>=2.0.0",
        "pynamodb>=6.0.0",
    ]
)
