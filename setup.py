from setuptools import setup, find_packages

setup(
    name="dj_affiliate",  
    version="0.1.0",  
    author="Eyob",
    author_email="eyobabdellasharo@gmail.com",
    description="A simple Django Affiliate module",
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown",  
    url="https://github.com/EyobAbdella/dj_affiliate",  
    packages=find_packages(where='.'),  
    include_package_data=True,  
    install_requires=[
        "Django>=3.2",  
    ],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7", 
)
