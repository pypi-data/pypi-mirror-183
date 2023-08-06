from setuptools import setup, find_packages

setup(
    name='celestis',
    version='1.6',
    description='A simple backend framework built using python',
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