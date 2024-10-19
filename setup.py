from setuptools import setup, find_packages

setup(
    name='cli-pdf',
    version='1.0.0',
    description='A PDF CLI tool.',
    author='Bichler Bastian',
    author_email='bichlerbastian@gmail.com',
    packages=find_packages(),  # Automatically finds all packages including mymodule.lib
    entry_points={
        'console_scripts': [
            'pdftool=mymodule.main:main',  # Entry point for the command-line tool
        ],
    },
    install_requires=[
        'pycryptodome',
    ],
    python_requires='>=3.6',
     classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
