import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="varyzhoutest01",
    version="0.0.1",
    author="varyzhou",
    author_email="zhouxiaolie@163.com",
    description="test package01",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="",
    #project_urls={},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
