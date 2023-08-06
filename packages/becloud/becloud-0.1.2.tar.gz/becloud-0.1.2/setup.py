from setuptools import setup

setup(name='becloud',
      version='0.1.2',
      description='Backend Cloud Package',
      packages=['becloud', 'becloud/datastore'],
      install_requires=['requests'],
      zip_safe=False,
      )
