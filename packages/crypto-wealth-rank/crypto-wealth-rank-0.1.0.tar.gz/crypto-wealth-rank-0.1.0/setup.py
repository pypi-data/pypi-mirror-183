import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="crypto-wealth-rank",
    version="0.1.0",
    author="apinanyogaratnam",
    author_email="apinanapinan@icloud.com",
    description="A python package to get wealth rank depending on number of bitcoin/ethereum",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apinanyogaratnam/crypto-wealth-rank",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10.4",
    install_requires=[],
)
