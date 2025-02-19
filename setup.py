from setuptools import setup, find_packages

setup(name='citrination-client',
      version='5.3.0',
      url='http://github.com/CitrineInformatics/python-citrination-client',
      description='Python client for accessing the Citrination api',
      packages=find_packages(exclude=('docs')),
      install_requires=[
          'requests>=2.20.0,<3',
          'pypif',
          'six<2',
          'pyyaml'
      ],
      extras_require={
        "dev": [
          'sphinx_rtd_theme',
          'sphinx',
        ],
        "test": [
          'requests_mock',
          'pytest',
        ]
      })
