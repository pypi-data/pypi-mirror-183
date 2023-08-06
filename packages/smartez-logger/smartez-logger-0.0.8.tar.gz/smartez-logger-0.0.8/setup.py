from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="smartez-logger",
    version="0.0.8",
    author="Rune Lykke-Kjeldsen",
    author_email="rune@lykke-kjeldsen.dk",
    description="Logger package used for smartez",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    install_requires=['python-dotenv'],
    url="https://github.com/BispensGipsGebis/smartez-logger",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    project_urls={
        "Bug Tracker": "https://github.com/BispensGipsGebis/smartez-logger/issues",
    }
)
