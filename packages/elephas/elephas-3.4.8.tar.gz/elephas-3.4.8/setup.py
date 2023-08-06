from setuptools import setup
from setuptools import find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="UTF-8")
version='3.4.8'
setup(name='elephas',
      version=version,
      description='Deep learning on Spark with Keras',
      long_description=long_description,
      long_description_content_type='text/markdown',
    url='http://github.com/danielenricocahall/elephas',
      download_url=f'https://github.com/danielenricocahall/elephas/tarball/{version}',
      author='Daniel Cahall',
      author_email='danielenricocahall@gmail.com',
      install_requires=['cython',
                        'tensorflow>=2,!=2.2.*,<=2.10',
                        'flask',
                        'h5py==3.3.0',
                        'pyspark<3.4'],
      extras_require={
        'tests': ['pytest', 'pytest-pep8', 'pytest-cov', 'pytest-spark', 'mock']
    },
      packages=find_packages(),
      license='MIT',
      zip_safe=False,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ])
