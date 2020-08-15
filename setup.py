import setuptools

setuptools.setup(
    name='covid_19',
    version='1.0.0',
    author='my_fahras@hotmail.fr',
    description='Covid_19 - a packaged machine learning algorithm to predict on Covid_19',
    packages=setuptools.find_packages(),
    install_requires=[
        "scikit-learn==0.22.1",
        "pandas==1.0.1"
    ]
)
