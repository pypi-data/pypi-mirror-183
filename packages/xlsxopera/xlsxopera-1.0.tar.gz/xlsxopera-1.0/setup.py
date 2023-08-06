from setuptools import setup, find_packages


setup(
    name="xlsxopera",
    version="1.0",
    author="voidayan",
    author_email="jan.emil.wojda@gmail.com",
    url='https://github.com/voidayan/xlsxopera',
    description="Work on xlsx file.",
    long_description_content_type="text/markdown",
    long_description="Convert to list, dict. Get headers, cell values, cell info, positions and more.",
    packages=find_packages(),
    install_requires=['openpyxl'],
    keywords=['python', 'xlsx', 'xls', 'excel', 'microsoft excel', 'cell'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
