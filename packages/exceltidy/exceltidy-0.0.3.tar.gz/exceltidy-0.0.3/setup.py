import setuptools
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="exceltidy",
    version="0.0.3",
    author="cmacckk",
    author_email="emailforgty@163.com",
    description="Based on openpyxl and xlwings to facilitate Excel processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cmacckk/exceltidy",
    packages=setuptools.find_packages(),
    install_requires=[
        'xlwings',
        'openpyxl'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3) ",
    ],
    python_requires='>=3.6',    #对python的最低版本要求
)