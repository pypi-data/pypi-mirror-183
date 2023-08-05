from setuptools import setup
import pip


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='Downloader_plus',
    version='0.0.4',
    packages=['downloader_plus'],
    url='https://github.com/Win11BSOD/downloader_plus',
    author='Guo Minghao',
    author_email='qu11182021@outlook.com',
    long_description=long_description,
    long_description_content_type="text/markdown"
)

if __name__ == '__main__':
    pip.main(['install', 'tqdm'])
    pip.main(['install', 'requests'])