import setuptools

setuptools.setup(
    name="jbg_util",
    version="0.0.5",
    description="A general util package",
    packages=setuptools.find_packages('src'),
    package_dir={'':'src'}
)