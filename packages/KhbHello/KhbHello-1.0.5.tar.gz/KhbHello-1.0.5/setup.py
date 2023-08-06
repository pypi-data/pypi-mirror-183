from setuptools import setup, find_packages

long_description = "My Hello Test Pack"

setup(
	name="KhbHello",
	version="1.0.5",
	description="A sample pkg",
	long_description= long_description,
	long_description_content_type="text/markdown",
	author="Khobeib Developer",
	author_email="khobeib.moahmmed@gmail.com",
    packages=['KhbHello'],
	classifiers=[
		"Development Status :: 1 - Planning",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Build Tools",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Operating System :: Microsoft :: Windows",
		],
)