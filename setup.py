
import setuptools


classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities"
]


setuptools.setup(
    name="marcus-pypi-test",
    version="12.0.0",
    description="PyPI Test",
    author="Marcus Ottosson",
    author_email="marcus@abstractfactory.com",
    url="www.google.com",
    license="LGPLv3",
    zip_safe=False,
    classifiers=classifiers,
    py_modules=["pypi_test"],

)
