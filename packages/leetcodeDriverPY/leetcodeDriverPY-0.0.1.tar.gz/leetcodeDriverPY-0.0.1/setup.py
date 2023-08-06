from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='leetcodeDriverPY',
    version='0.0.1',
    description='A library to help people run Leetcode testcases without the Leetcode online IDE',
    long_description=open('BASIC_README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Duve3',
    author_email='',
    license='MIT',
    classifiers=classifiers,
    keywords='',
    packages=find_packages(),
    install_requires=['']
)
