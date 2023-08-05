import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="english-detector",
    version="0.1.0",
    author="apinanyogaratnam",
    author_email="apinanapinan@icloud.com",
    description="A python package to detect english text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apinanyogaratnam/english-detector",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10.4",
    install_requires=[
        'pycld2==0.41',
    ],
)
