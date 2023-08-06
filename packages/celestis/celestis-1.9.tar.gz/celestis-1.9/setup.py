from setuptools import setup

README_FILE = open('README.md', 'r').read()

setup(
    name='celestis',
    version='1.9',
    description='A simple backend framework built using python',
    long_description_content_type="text/markdown",
    long_description=README_FILE,
    author="Aryaan Hegde",
    author_email="aryhegde@gmail.com",
    packages=["celestis.controller", "celestis.view"],
    package_dir={"celestis.controller": "controller", "celestis.view": "view"},
    py_modules=['celestis', 'command', 'create_files', 'error', 'render', 'requests'],
    include_package_data=True,
    install_requires=['requests', 'click'],
    entry_points={
        'console_scripts': [
            'celestis=command:celestis',
        ],
    },
)