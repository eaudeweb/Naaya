''' destinet.extra installer '''
from setuptools import setup, find_packages

setup(name='destinet.extra',
      version='1.3.51',
      author='Eau de Web',
      author_email='office@eaudeweb.ro',
      url='http://naaya.eaudeweb.ro',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Naaya >= 5.0.25',
          'naaya.content.bfile >= 1.4.27',
          'Products.NaayaContent.NyPublication >= 1.1.4',
          'naaya.envirowindows',
          'naayabundles-destinet',
      ]
      )
