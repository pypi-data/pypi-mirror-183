from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
README = (this_directory / "README.md").read_text()

setup(name='network_utils',
      version='1.0',
      description='Helpful tools for building socket applications',
      long_description_content_type='text/markdown',
      long_description=README,
      packages=['network_utils'],
      author_email='leroy.ryan09@gmail.com',
      zip_safe=False)
