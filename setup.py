from setuptools import setup, find_packages

setup(
        name="TestCreationPackage",
        version="0.0.1",
        author="kcinnay23",
        author_email="yatadegnon2002@gmail.com",
        url="",
        description="Un package pour créer des réseaux de neurones denses",
        packages=find_packages(),
        readme = "README.md",
        install_requires = ["numpy >= 1.26.3"],
        python_requires=">=3.11",
        classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
)