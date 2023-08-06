from setuptools import setup, find_packages

setup(name='client_proj_dav',
      version='0.0.1',
      description='Client packet',
      author='Konstantuan',
      author_email='dakope@tut.by',
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
