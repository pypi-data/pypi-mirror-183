import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()
setuptools.setup(
	name="Keyimstr",
	version="0.0.1",
	author="Keywind",
	author_email="watersprayer127@gmail.com",
	description="Numpy <-> Bytes <-> String",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/keywind127/image-string-converter",
	project_urls={
		"Bug Tracker": "https://github.com/keywind127/image-string-converter/issues",
	},
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	package_dir={"": "src"},
	packages=setuptools.find_packages(where="src"),
	python_requires=">=3.6",
	
	install_requires=[
		'markdown',
		'numpy',
		'opencv-python'
	]
	
)