from setuptools import setup, find_packages

setup(
    name='celestis',
    version='1.3',
    description='A simple backend framework built using python',
    author="Aryaan Hegde",
    author_email="aryhegde@gmail.com",
    packages=find_packages(),
    py_modules=['celestis', 'command', 'create_files', 'error', 'render', 'requests'],
    include_package_data=True,
    install_requires=['requests', 'click'],
    entry_points={
        'console_scripts': [
            'celestis=command:celestis',
        ],
    },
)