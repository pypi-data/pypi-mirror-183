from setuptools import setup, find_packages


setup(
    name='ez box',
    version='1.0',
    license='MIT',
    author="Batte",
    author_email='BatteTarte@protonmail.com',
    packages=find_packages('ezbox'),
    package_dir={'ezbox': 'ezbox'},
    url=None,
    keywords='Ez package',
    install_requires=[
          'scikit-learn',
      ],

)
