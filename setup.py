from setuptools import setup, find_packages

setup(
    name='mkdocs-obsidian-plugin',
    version='0.2.0',
    description='An MkDocs plugin',
    long_description='An MkDocs plugin to use obsidian features with MkDocs',
    keywords='mkdocs',
    url= 'https://github.com/aarkue/mkdocs-obsidian-plugin',
    author='aarkue',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs>=1.0.4',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'obsidian = mkdocs_obsidian_plugin.plugin:ObsidianPlugin',
        ]
    }
)
