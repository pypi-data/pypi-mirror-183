import setuptools


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='cameo_pg2gsheet',
    version='1.2.0',
    description='PostgreSQL table to Google sheet',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bohachu/pg2gsheet',
    author='Yi-Hao Su',
    author_email='elantievs@gmail.com',
    license='BSD 2-clause',
    install_requires=[
        'psycopg2-binary>=2.9.5',
        'python-dotenv>=0.21.0',
        'gspread>=5.7.2',
        'pandas>=1.5.2'
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.9',
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)
