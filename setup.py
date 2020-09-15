import setuptools
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('c19mlp/__init__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setuptools.setup(
    name='covid_19',
    version='1.0.0',
    author='my_fahras@hotmail.fr',
    description='Covid_19 - a packaged machine learning algorithm to predict on Covid_19',
    packages=setuptools.find_packages(),
    install_requires=[
        "scikit-learn==0.22.1",
        "pandas==1.0.1"
    ],
)
