
from setuptools import setup, find_packages


setup(
    name='phillipshuepython',
    version='0.1',
    license='MIT',
    author="Carl Johann Felix Stempel",
    author_email='carljohann@robotik.ag',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Gandalf123456789/pythonhue',
    keywords='phillips python hue',
    install_requires=[
          'requests',
      ],

)