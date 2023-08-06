from setuptools import setup

with open("README.md", "r") as readme_bf:
    readme_content = readme_bf.read()

setup(
    name="bigjpg",
    version="1.0.1",
    license="MIT License",
    author="Marcuth",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    author_email="marcuth2006@gmail.com",
    keywords="bigjpg wrapper api",
    description=f"Wrappper for https://bigjpg.com/",
    packages=["bigjpg"],
    install_requires=["httpx", "pydantic", "rich"],
)