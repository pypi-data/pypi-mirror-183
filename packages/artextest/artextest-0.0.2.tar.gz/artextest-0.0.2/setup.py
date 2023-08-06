from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='artextest',
    version='0.0.2',
    description='One function that gets the greatest common divisor between two numbers.',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Arwen Terpstra',
    author_email="arwenterpstra1@gmail.com",
    License='MIT',
    classifiers=classifiers,
    keywords='algorithm',
    packages=find_packages(),
    install_requires=['']
)