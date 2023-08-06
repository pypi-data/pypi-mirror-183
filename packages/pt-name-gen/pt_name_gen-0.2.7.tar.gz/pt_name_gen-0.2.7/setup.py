from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pt_name_gen',
    version='0.2.7',
    description='A name generator in Portuguese. Um gerador de nomes em português.',
    author='Victor Figueredo',
    packages=['pt_name_gen'],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['unidecode'],
    entry_points={
        'console_scripts': [
            'pt_name_gen=pt_name_gen.__main__:main'
        ]
    }
)
