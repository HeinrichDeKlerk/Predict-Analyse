from setuptools import setup, find_packages

setup(
    name='predictModuleT27',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Analyse predict function package',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/HeinrichDeKlerk/predictModuleT27',
    author='Heinrich de Klerk, Armaan Maharaj, Sibusiso Luthuli, Abednego',
    author_email='heinrich.deklerk9@gmial.com')
