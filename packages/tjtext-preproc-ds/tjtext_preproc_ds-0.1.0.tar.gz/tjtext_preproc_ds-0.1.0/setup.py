from setuptools import setup, find_packages


setup(
    name='tjtext_preproc_ds',
    version='0.1.0',
    license='MIT',
    author="Tariq Jamil",
    author_email='tariqjamil.bwp@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/pypi_projects/tj_nlp/',
    keywords='tjtext_preproc_ds',
    install_requires=[
          'unidecode',
          'nltk',
          'autocorrect',
          'bs4',
          'pandas',
          'numpy',
          'tqdm',
      ],
)