from setuptools import setup

setup(
    name='dmlestudioapy',
    version='0.0.1',
    url='https://github.com/ravishan16/QuikRestApy',
    license='NIELSEN',
    author='Ravishankar Sivasubramaniam',
    author_email='ravishankar.sivasubramaniam@nielsen.com',
    description='dmlestudioapy REST API using Python Flask/SQLAlchemy/SQLite',
    packages=['dmlestudioapy'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.12',
        'SQLAlchemy>=1.1.6',
        'flask-restplus>=0.10.1',
        'Flask-SQLAlchemy>=2.2',
        'CherryPy>=10.2.1',
        'Paste>=2.0.3',
        'pylint',
        'nose'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
