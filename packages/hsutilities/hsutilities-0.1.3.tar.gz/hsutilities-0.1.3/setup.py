from setuptools import find_packages, setup  # type: ignore

with open("README.md") as f:
    long_description = f.read()

setup(
    name="hsutilities",
    description="Useful functions for hosting with Hostsharing eG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tpokorra/hsutilities",
    author="Timotheus Pokorra",
    author_email="timotheus.pokorra@solidcharity.com",
    version='0.1.3',
    license="New BSD License",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
    ],
)

