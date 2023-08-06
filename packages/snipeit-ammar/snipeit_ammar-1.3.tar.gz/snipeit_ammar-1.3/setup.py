from setuptools import setup

with open("README.rst","r") as fh:
	long_description = fh.read()
	
setup(name='snipeit_ammar',
      version='1.3',
	  long_description=long_description,
      long_description_content_type="text/markdown",
      description=("Python library to access the SnipeIT API-forked"),
      url='https://github.com/ammar0466/SnipeIT-PythonAPI',
      author='Ammar Ibrahim',
      author_email='ammar@webkaido.com',
      license='MIT',
      packages=['snipeit_ammar'],
      install_requires=['requests','simplejson'],
      zip_safe=False)
