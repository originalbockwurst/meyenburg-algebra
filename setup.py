from setuptools import setup, find_packages

setup(
    name='meyenburg_algebra',
    version='0.1.1',
    description='Algebra where 0 is replaced by i for consistent and complex-safe arithmetic.',
    author='Till Meyenburg',
    packages=find_packages(),
    python_requires='>=3.6',
)
