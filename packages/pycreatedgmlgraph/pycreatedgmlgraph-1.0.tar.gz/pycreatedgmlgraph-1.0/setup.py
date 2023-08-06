import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().split('\n')

setuptools.setup(
	name="pycreatedgmlgraph",
	version="1.0",
	author="Alexey-Chebotarev",
	description="A package for creating graphs from modules dependency",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Chebotarev-Alexey/PyCreateDgmlGraph",
	packages=setuptools.find_packages(),
	install_requires=requirements,
	classifiers=[
        "Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)