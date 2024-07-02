from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name="numbering",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python-docx>=1.1.2",
        "python-dotenv>=1.0.1",
    ],
    author="Madung2",
    author_email="tuliphan91@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Madung2/Numbering", 
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
