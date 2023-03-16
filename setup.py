from setuptools import setup, find_packages

print(find_packages())

setup(
    name='ilikepaintings',
    version='0.0.1',
    author='Olivier RISSER-MAROIX, Nicolas BIZZOZZERO',
    author_email='orissermaroix@gmail.com',
    description='A package for predicting painting appreciation from images using a linear regressor on top of a frozen CLIP model',
    url='https://github.com/VieVie31/i-like-painings',
    packages=find_packages(),
    install_requires=[
        'torch'
    ],
    package_data={
        "ilikepaintings": ["weights/*/*.pth"]
    },
    license_files=["LICENSE"]
)
