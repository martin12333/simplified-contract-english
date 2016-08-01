from setuptools import setup, find_packages

setup(
    name='sce',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'markdown',
        'nltk'
    ],
    entry_points='''
        [console_scripts]
        sce=sce.Tools.sce:cli
    ''',
)
