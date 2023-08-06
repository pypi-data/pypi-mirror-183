"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(

    name='pyBCabs', 
    version='0.0.1',
    description='Outputs shape information for fractal aggregates based on mass, mixing state, and mass absorption cross-section.',
    long_description=' - See `documentation <http://pyBCabs.readthedocs.io/>`_ for update notes.',
    #long_description_content_type='text/markdown',
    url='https://github.com/beelerpayton/pyBCabs',
    author='Payton Beeler',
    author_email='beelerpayton@wustl.edu',

    classifiers=[
      'Intended Audience :: Science/Research',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License'
    ],
    
    keywords='fractal absorption morphology',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=['numpy','matplotlib','scipy'],
)
