from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='array-helpers',
    author='Liam Edwards',
    author_email='me@liamedwards.dev',
    description='Add useful helper functions for lists with a wrapper class',
    keywords='array, list, helpers, human friendly, python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/liam-edwards/python-array-helpers',
    project_urls={
        'Documentation': 'https://github.com/liam-edwards/python-array-helpers',
        'Source': 'https://github.com/liam-edwards/python-array-helpers',
        'Tracker': 'https://github.com/liam-edwards/python-array-helpers/issues',
    },
    packages=['array_helpers'],
    license='LICENSE.txt',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3 :: Only',
        
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        
        'Typing :: Typed',
    ],
    python_requires='>=3.7'
)
