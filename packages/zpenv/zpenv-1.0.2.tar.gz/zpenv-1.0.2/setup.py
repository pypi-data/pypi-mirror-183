from setuptools import setup
import os
import zpenv


setup(name="zpenv",
      version=zpenv.__version__,
      author="ZephyrOff",
      author_email="contact@apajak.fr",
      keywords = "venv virtualenv terminal zephyroff",
      classifiers = ["Development Status :: 5 - Production/Stable", "Environment :: Console", "License :: OSI Approved :: MIT License", "Programming Language :: Python :: 3"],
      packages=["zpenv"],
      entry_points = {
        'console_scripts': ['zpenv = zpenv.__main__:main'],
      },
      install_requires=['psutil','zpp_args','zpp_config'],
      description=zpenv.__descriptor__,
      long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
      long_description_content_type='text/markdown',
      url = "https://github.com/ZephyrOff/py-zpenv",
      platforms = "ALL",
      license="MIT")