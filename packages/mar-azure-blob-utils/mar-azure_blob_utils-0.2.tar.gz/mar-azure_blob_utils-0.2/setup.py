from setuptools import setup

long_description = open('README.md').read()


setup(
    name='mar-azure_blob_utils',  
    version='0.2',
    description="A wrapper libray for Azure Blob Storage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maradder/azure_blob_utils",
    author="Marcus Radder",
    author_email="marcusradder@gmail.com",
    license='MIT',
    packages=['azure_blob_utils'],
    install_requires=[
        'azure-storage-blob'
    ],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )