from setuptools import setup, find_packages

with open("README.md", "r") as rd:
    long_description = rd.read()
	
setup(
 name='fmanova',
 version='1.0.0',
 description='This moldule provides functions for calculation of one-way and two-way analysis of variance',
 long_description=long_description,
 long_description_content_type="text/markdown",
 url='https://github.com/fmkundi/kundidocs', 
 author='Fazal Masud Kundi',
 author_email='fmkundi@gmail.com',
 classifiers=[
   'Intended Audience :: Education',
   'Operating System :: OS Independent',
   'License :: OSI Approved :: MIT License',
   'Programming Language :: Python :: 3.9',
 ],
 keywords=['python', 'numpy', 'pandas','statistics','anova','analysis of variance'],
 packages=find_packages()
)