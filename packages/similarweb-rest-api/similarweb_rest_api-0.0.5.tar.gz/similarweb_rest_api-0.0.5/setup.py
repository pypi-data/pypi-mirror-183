from setuptools import setup

setup(
    name='similarweb_rest_api',
    version='1.5',
    description='A library to simplify the access to the REST API of similarweb.',
    author='Damien Frigewski',
    author_email='dfrigewski@gmail.com',
    url='https://github.com/DamienDrash/similarweb_rest_api',
    packages=['similarweb_rest_api'],
    include_package_data=True,
    package_data={'similarweb_rest_api': ['similarweb_endpoints.json']},
    install_requires=['pandas', 'requests', 'lxml', 'pyyaml'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
)
