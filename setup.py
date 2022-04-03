from setuptools import setup, find_packages

from potion import __version__

"""
python3 setup.py sdist bdist_wheel; 
python3 setup.py sdist bdist_wheel; pip3 install dist/$(python3 install.py);
python3 setup.py sdist bdist_wheel; pip install dist/$(python3 install.py) --user
python3 setup.py sdist bdist_wheel; pip install dist/$(python3 install.py) 
python3 setup.py sdist bdist_wheel; pip3 install dist/$(python3 install.py) 
sudo pip install dist/$(python3 install.py);
pip install dist/$(python3 install.py) --user
"""

from scripts import list_apis

list_apis.main()

setup(
    name='notion-potion',
    version=__version__,
    description='A functional, easy to use Python wrapper of Notion Api.',
    url='https://github.com/sailist/potion',
    author='sailist',
    author_email='sailist@outlook.com',
    license='Apache License 2.0',
    include_package_data=True,
    install_requires=['dbrecord', 'requests'],
    # https://pypi.org/classifiers/
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    keywords='potion notion',
    packages=find_packages('.', exclude=('tests', 'scripts', 'examples')),
    entry_points={},
)
