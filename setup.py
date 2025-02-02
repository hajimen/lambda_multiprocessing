from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()


setup(
 name='lambda_multiprocessing',
 version='0.5.2',
 description='drop-in replacement for multiprocessing.Pool in AWS Lambda functions (without /dev/shm shared memory)',
 long_description=long_description,
 long_description_content_type="text/markdown",
 url='https://github.com/hajimen/lambda_multiprocessing',
 author=['Matthew Davis', 'Hajime Nakazato'],
 author_email='hajime@kaoriha.org',
 classifiers=[
   'Development Status :: 3 - Alpha',
   'Intended Audience :: Developers',
   'Operating System :: OS Independent',
   'License :: OSI Approved :: MIT License',
   'Programming Language :: Python :: 3',
   'Programming Language :: Python :: 3.7',
   'Programming Language :: Python :: 3.8',
   'Programming Language :: Python :: 3.9',
   'Programming Language :: Python :: 3.10',
 ],
 keywords=['python', 'AWS', 'Amazon', 'Lambda', 'multiprocessing', 'pool', 'concurrency'],
 packages=find_packages()
)
