from setuptools import setup, find_packages

setup(
    name='cosmic-framework',
    version='1.0',
    description='A simple backend framework built using python',
    author="Aryaan Hegde",
    author_email="aryhegde@gmail.com",
    packages=find_packages(),
    py_modules=['celestial', 'command', 'create_files', 'error'],
    include_package_data=True,
    install_requires=['requests', 'click'],
    entry_points={
        'console_scripts': [
            'celestial=command:celestial',
        ],
    },
)