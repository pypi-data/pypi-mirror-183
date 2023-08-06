from setuptools import setup

# python setup.py sdist bdist_wheel
# twine upload --repository testpypi dist/* (TEST)
# twine upload dist/*

setup(
    name='extratyping',
    version='1.0.0',
    packages=['extratyping'],
    url='https://github.com/DWolfNineteen/extratyping',
    license='MIT License',
    author='DWolf_19',
    description='Mini Python module for type annotations of primitive immutable or mutable types.'
)
