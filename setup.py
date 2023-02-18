import re

from setuptools import setup, find_packages


def extract_version():
    return re.search(
        r"""__version__ = ['"]([\d.d\-]+)['"]""",
        open('src/potion/__init__.py', 'r', encoding='utf-8').read()).group(1)


if __name__ == '__main__':
    setup(
        name='notion-potion',
        version=extract_version(),
        description='A functional, easy to use Python wrapper of Notion Api.',
        long_description_content_type='text/markdown',
        url='https://github.com/sailist/potion',
        author='sailist',
        author_email='sailist@outlook.com',
        license='Apache License 2.0',
        include_package_data=True,
        install_requires=['dbrecord', 'requests'],
        # https://pypi.org/classifiers/
        classifiers=[
            'Programming Language :: Python :: 3',
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
