import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Arduino_Master",
    version="0.0.1",
    author="Sayad Pervez",
    author_email="pervez2504@gmail.com",
    description="Data Science enabled Data extraction and control library for Arduino with easy Data Visualizations !.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SayadPervez/Arduino_Master",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
