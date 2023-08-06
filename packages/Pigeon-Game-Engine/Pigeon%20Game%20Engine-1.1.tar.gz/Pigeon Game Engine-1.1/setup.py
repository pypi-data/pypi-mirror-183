from setuptools import find_packages, setup

setup(
    name='Pigeon Game Engine',
    packages=find_packages(include=['pgengine']),
    version='1.1',
    description='Game Engine for Python called "Pigeon Game Engine"',
    author='Demandes',
    license='MIT',
    install_requires=['keyboard', 'PIL'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)