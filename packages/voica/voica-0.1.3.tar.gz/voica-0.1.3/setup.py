import setuptools
with open(r'C:\Users\Kuler\Desktop\README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='voica',
	version='0.1.3',
	author='voica',
	author_email='nmaks6385@gmail.com',
	description='',
	long_description=long_description,
	long_description_content_type='text/markdown',
	packages=['voica'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)