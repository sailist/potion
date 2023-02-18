from setuptools import setup, find_packages

from potion import __version__

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
    package_dir={"": "src"},
    packages=find_packages('src'),
    # packages=find_packages('.', exclude=('tests', 'scripts', 'examples')),
    entry_points={},
)
