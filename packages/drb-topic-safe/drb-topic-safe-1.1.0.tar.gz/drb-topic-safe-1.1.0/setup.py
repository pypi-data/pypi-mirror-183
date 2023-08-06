import versioneer
from setuptools import setup, find_namespace_packages


with open('requirements.txt', 'r') as file:
    REQUIREMENTS = file.readlines()

with open('README.md', 'r') as file:
    long_description = file.read()


setup(
    name='drb-topic-safe',
    description='Safe topic for DRB Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='GAEL Systems',
    author_email='drb-python@gael.fr',
    url='https://gitlab.com/drb-python/topics/safe',
    python_requires='>=3.8',
    install_requires=REQUIREMENTS,
    packages=find_namespace_packages(include=['drb.*']),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
    ],
    package_data={'drb.topics.safe': ['cortex.yml']},
    data_files=[('.', ['requirements.txt'])],
    entry_points={'drb.topic': ['safe=drb.topics.safe']},
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass()
)
