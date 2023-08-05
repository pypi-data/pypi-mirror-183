from setuptools import setup, find_packages


setup(
    name="cloopui",
    version="0.1",
    author="Francis B. Lavoie",
    author_email="francis.b.lavoie@usherbrooke.ca",
    description="CLoop UI",
    long_description="CLoop UI",
    long_description_content_type="text/markdown",
    url="https://catalyseur.ca",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={"cloopui": ["*.txt", "*.rst","*.pkl"]}

)