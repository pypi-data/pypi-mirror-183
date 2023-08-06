from setuptools import setup

setup(
    name="yamdgen",
    description="For generating dbt yaml and md files",
    author="Muizz Lateef",
    author_email="lateefmuizz@gmail.com",
    url="https://github.com/Muizzkolapo/yamdgenerator",
    entry_points={
        'console_scripts': [
            'yamdgen = yamdgen:generate',
        ]
    }
)