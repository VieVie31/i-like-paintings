from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='ilikepaintings',
    version='0.0.1',
    author='Nicolas BIZZOZZERO, Ihab BENDIDI, Olivier RISSER-MAROIX',
    author_email='orissermaroix@gmail.com',
    description='A package for predicting painting appreciation from images using a linear regressor on top of a frozen CLIP model',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/VieVie31/i-like-painings',
    packages=find_packages(),
    install_requires=[
        'torch',
        'numpy'
    ],
    package_data={
        "ilikepaintings": ["weights/*/*.pth"]
    },
    license_files=["LICENSE"]
)
