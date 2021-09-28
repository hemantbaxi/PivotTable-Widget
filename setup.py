import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ptwidget",
    version="0.1.0",
    author="Hemant Baxi",
    author_email="baxihemant@gmail.com",
    description="Pivot Table Widget",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hemantbaxi/PivotTable-Widget",
    project_urls={
        "Bug Tracker": "https://github.com/hemantbaxi/PivotTable-Widget/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #package_dir={"": "src"},
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    install_requires=[
    'pivottablejs',
    'ipyiframe',
    'ipywidgets',
    'pandas']

)
