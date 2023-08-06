from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='mathfin',
    version='0.0.3',
    license='MIT License',
    author='Naoki Yokoyama',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='naokity@msn.com',
    keywords='math fin',
    description=u'Lib com funções de matematica financeira',
    packages=['mathfin'],
    install_requires=['pandas'],)