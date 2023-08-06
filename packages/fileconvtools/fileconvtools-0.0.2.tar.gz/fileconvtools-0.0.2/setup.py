from setuptools import setup


from setuptools import setup, find_packages

setup(
    name             = 'fileconvtools',
    version          = '0.0.2',
    description      = 'Test package for Convert tool',
    author           = 'Ddangkwon',
    author_email     = 'semi109502@gmail.com',
    url              = '',
    download_url     = '',
    install_requires = ['tkinter', 'pandas', 'tqdm'],
	include_package_data=True,
	packages=find_packages(),
    keywords         = ['FILECONVTOOLS', 'fileconvtools'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)

