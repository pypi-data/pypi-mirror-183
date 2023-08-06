import os
from setuptools import setup, find_packages

# with open('requirements.txt') as f:
#     required = f.read().splitlines()
# required = ['torch==1.12.0', 'torchvision==0.13.0', 'pyyaml==5.4.1', 'timm==0.6.5', 'scikit-learn', 'matplotlib', 'opencv-python']
required = ['pyyaml==5.4.1', 'scikit-learn==1.1.3', 'matplotlib==3.6.2']
# required = ['opencv-python==4.6.0.66']

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

exec(open('cvnets/__version__.py').read())
setup(
    name="cvnets",
    version=__version__,
    author="Jihoon Lucas Kim",
    description="Library for Computer Vision Deep Learning Networks",
    packages=find_packages(),
    package_data={'cvnets': ['**/*.yaml']},
    install_requires=required,
    include_package_data=True,
)