from setuptools import setup
import uuid


setup(
    name='mediafire',
    version='0.6.1',
    author='Roman Yepishev',
    author_email='rye@keypressure.com',
    packages=['mediafire', 'mediafire.media'],
    license='BSD',
    description='Python MediaFire client library',
    long_description=open('README.rst').read(),
    install_requires=[
        'requests',
        'requests_toolbelt',
        'six',
    ],
    keywords="mediafire cloud files sdk storage api upload",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: BSD License'
    ]
)
