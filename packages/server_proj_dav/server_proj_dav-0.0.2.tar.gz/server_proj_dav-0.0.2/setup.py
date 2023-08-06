from setuptools import setup, find_packages

setup(name='server_proj_dav',
      version='0.0.2',
      description='Server packet',
      author='Konstantuan',
      author_email='dakope@tut.by',
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
