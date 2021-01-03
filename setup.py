import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="keep-your-data",
    version="0.0.1",
    author="Ilyas Kuhlemann",
    author_email="ilyasp.ku@gmail.com",
    description="Keep track of anything, on your own sever.",
    long_description=long_description,
    long_description_content_type="text/rst",
    url="https://github.com/ilyasku/keep-your-data",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3"
    ],
    python_requires=">=3.7"
)
