from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements=f.read().splitlines ()

    setup(
        name='cli-pdf',
        version='1.0.0',
        description='A PDF CLI tool.',
        author='Bichler Bastian',
        author_email='bichlerbastian@gmail.com',
        packages=find_packages(), 
        install_requires=requirements,
        entry_points={
            'console_scripts': [
                'pdftool=mymodule.main:main',  # Entry point for the command-line tool
            ],
        },
        python_requires='>=3.6',
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
    )
