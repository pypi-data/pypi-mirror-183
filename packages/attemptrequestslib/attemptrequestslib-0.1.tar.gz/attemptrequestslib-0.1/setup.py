import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="attemptrequestslib",
    version="0.1",
    author="Euardo Soares   ",
    author_email="eduardolimasoares@gmail.com",
    description="Small lib with custom functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/nappsolutionsdev/napplib.git",
    packages=setuptools.find_packages(),
    license='Proprietary',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
        "azure-storage-blob==2.1.0", 
        "tinydb", 
        "pandas", 
        "patool==1.12",
        "google-api-core==1.25.1",
        "google-api-python-client==1.12.8",
        "google-auth==1.25.0",
        "google-auth-httplib2==0.0.4",
        "google-auth-oauthlib==0.4.2",
        "googleapis-common-protos==1.52.0",
        "gspread==3.7.0",
        "lxml==4.6.3",
        "xmltodict==0.12.0",
        "loguru==0.5.3",
        "google-cloud-storage"
    ],
    package_data={},
)
