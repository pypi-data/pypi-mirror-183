from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='CodeExecutor',
      version='1.1',
      description='Running code in a sandbox environment',
      packages=['CodeExecutor'],
      author_email='neuralteam@mail.ru',
      zip_safe=False,
      long_description=long_description,
      long_description_content_type='text/markdown'
      )
