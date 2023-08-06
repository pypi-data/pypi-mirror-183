from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name = 'GoldenSectionSearch',
    version = '0.0.6',
    author="Vishal Pandey",
    author_email="vishalp316253@gmail.com",
    description = "This package is to print and plot Golden Section Algorithm", 
    # url="https://github.com/Vishalpandey1247/HashTable",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules = ['goldensectionsearch'],
    # package_dir = {'': 'src'},
    packages=find_packages(),
    install_requires=['numpy','matplotlib','IPython','time'], 
    # extras_require = {
    #    "dev":[
    #    "pytest>=3.7",
    #    ]
    # },
    classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Natural Language :: English",
       "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)

