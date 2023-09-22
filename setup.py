import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    long_description = fh.read()
setuptools.setup(
    name="Sunscreen_Api_Test",
    version="0.0.7",
    author="yuanjunling",
    author_email = "261412489@qq.com",
    description = "接口自动化测试框架",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuanjunling/AutomationApiTest.git",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"

)