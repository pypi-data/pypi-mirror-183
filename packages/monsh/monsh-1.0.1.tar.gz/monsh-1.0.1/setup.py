from setuptools import setup

with open('PYPI_README.md') as pypi_readme:
    long_description=pypi_readme.read()

setup(
    name='monsh',
    version='1.0.1',
    description='This package contains the client side script for mon.sh which allows you to sync your command output to the cloud.',
    # package_data={'': ['PYPI_README.md']},
    # include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ameer Ayoub',
    author_email='ameer.ayoub@gmail.com',
    url='https://www.mon.sh/',
    entry_points={
        'console_scripts': [
            'mon=mon:run',
            'monsh=mon:run'
        ]
    },
    install_requires=['requests'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Logging",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
        "Topic :: Utilities"
    ]
)