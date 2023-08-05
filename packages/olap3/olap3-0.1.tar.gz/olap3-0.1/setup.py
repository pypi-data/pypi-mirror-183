# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(name='olap3',
      version='0.1',
      description='Interface to OLAP DBs',
      author='Leonid Kolesnichenko',
      author_email='xperience439@gmail.com',
      packages=find_packages(),
      namespace_packages=['olap'],
      package_dir={'olap': 'olap'},
      package_data={'olap.xmla': ['*.wsdl'],
                    'olap': ['*.g']},
      install_requires=["setuptools~=60.2.0", "zope.component", "cornice", "webob", "venusian", "zeep==3.4.0"],
      url="https://github.com/robert-werner/olap3",
      license='Apache Software License 2.0',
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries :: Python Modules"
      ]
      )
