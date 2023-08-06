import versioneer
from setuptools import setup, find_namespace_packages

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='drb-driver-s3',
    packages=find_namespace_packages(include=['drb.*']),
    description='DRB aws3 implementation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='GAEL Systems',
    author_email='drb-python@gael.fr',
    url='https://gitlab.com/drb-python/impl/aws3',
    install_requires=REQUIREMENTS,
    test_suite='tests',
    data_files=[('.', ['requirements.txt'])],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.8',
    entry_points={
        'drb.driver': 'aws3 = drb.drivers.aws3:S3NodeFactory',
        'drb.topic': 'aws3 = drb.topics.aws3'
    },
    package_data={
        'drb.topics.aws3': ['cortex.yml']
    },
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    project_urls={
        'Documentation': 'https://drb-python.gitlab.io/impl/aws3/',
        'Source': 'https://gitlab.com/drb-python/impl/aws3',
    }

)
