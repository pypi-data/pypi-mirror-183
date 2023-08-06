import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Crypto-Graphics",
    version="0.0.1",
    author="Javier Marin",
    author_email="jmarinordov@alumni.unav.com",
    description="Crypto Visaulization data App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmarinMBDS/Crypto_Graphics",
    install_requires=[
        "pandas == 1.5.2",
        "requests == 2.28.1",
        "datetime == 4.9",
        "streamlit == 1.16.0",
        "plotly == 5.11.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)