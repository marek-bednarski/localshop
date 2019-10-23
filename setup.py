from setuptools import find_packages, setup

readme = []
with open('README.rst', 'r') as fh:
    readme = fh.readlines()

tests_require = [
    'django-webtest==1.9.2',
    'factory-boy==2.9.2',
    'mock==2.0.0',
    'pytest-cache==1.0',
    'pytest-cov>=1.7.0',
    'pytest-django>=2.8.0',
    'pytest>=2.6.0',
    'requests-mock==1.3.0',
    'requests-toolbelt==0.9.1',
]

setup(
    name='localshop',
    version='2.0.0-alpha.1',
    author='Michael van Tellingen',
    author_email='michaelvantellingen@gmail.com',
    url='http://github.com/mvantellingen/localshop',
    description='A private pypi server including auto-mirroring of pypi.',
    long_description='\n'.join(readme),
    zip_safe=False,
    install_requires=[
        'boto3==1.4.7',
        'celery==4.1.0',
        'django-braces==1.11.0',
        'django-celery-beat==1.1.0',
        'django-celery-results==1.0.1',
        'django-environ==0.4.4',
        'django-model-utils==3.0.0',
        'django-storages==1.6.5',
        'django-widget-tweaks==1.4.1',
        'Django==1.11.7',
        'docutils==0.12',
        'kombu==4.1.0',
        'netaddr==0.7.12',
        'Pillow==6.2.0',
        'psycopg2==2.7.3.2',
        'redis==2.10.6',
        'requests==2.18.4',
        'social-auth-app-django==1.2.0',
        'sqlparse==0.1.15',
        'Versio==0.3.0',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
    license='BSD',
    include_package_data=True,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'localshop = localshop.runner:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: System',
        'Topic :: System :: Software Distribution',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
