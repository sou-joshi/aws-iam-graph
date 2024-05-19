from setuptools import setup, find_packages

setup(
    name='aws_iam_graph',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'neo4j',
        'pyyaml',
    ],
)
