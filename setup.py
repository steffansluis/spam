from setuptools import setup

setup(
	name="spam",
	version="0.1",
	author="Steffan Sluis",
    url='http://github.com/steffansluis/spam',
	author_email="steffansluis@gmail.com",
	license="MIT",
	packages=["spam"],
	data_files=[('/usr/bin/', [
		'bin/spam',
	])],
	install_requires=[
		'simpleCLI',
		#'GitPython>=0.3',
	],
)
