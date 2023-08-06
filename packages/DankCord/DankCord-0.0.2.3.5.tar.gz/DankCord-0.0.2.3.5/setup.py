from distutils.core import setup

setup(
    name='DankCord',
    version='0.0.2.3.5',
    description='The first python library for Dank Memer selfbots. Incredibly fast, secure, strong, and reliable.',
    author='Sxvxge',
    author_email='sxvxge69@gmail.com',
    url='https://www.github.com/Sxvxgee/DankCord',
    license='MIT',
    packages=['DankCord'],
    install_requires=['rich', 'typing-extensions', 'orjson', 'requests'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    project_urls={
        "Documentation": "https://github.com/Sxvxgee/DankCord/blob/master/README.md",
        "Github": "https://www.github.com/Sxvxgee/DankCord",
        "Changelog": "https://github.com/Sxvxgee/DankCord/blob/master/Changelog.md"
    }
)