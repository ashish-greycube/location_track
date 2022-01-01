from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in location_track/__init__.py
from location_track import __version__ as version

setup(
	name="location_track",
	version=version,
	description="Track Location",
	author="GreyCube Technologies",
	author_email="admin@greycube.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
