import json
from setuptools import setup
import pathlib


with open('package.json') as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")


here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    long_description=long_description,
    long_description_content_type='text/markdown', 
    packages=[package_name],
    include_package_data=True,
    license=package['license'],
    description=package.get('description', package_name),
    install_requires=[],
    classifiers = [
        'Framework :: Dash',
    ],    
)
