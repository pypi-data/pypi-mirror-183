import setuptools
import gqylpy

with open(gqylpy.__file__, encoding='utf8') as f:
    for line in f:
        if line.startswith('@version: ', 2):
            version = line.split()[-1]
            break
    author, email = f.readline().split(': ')[-1].rstrip().split()
    source = f.readline().split()[-1]

setuptools.setup(
    name=gqylpy.__name__,
    version=version,
    author=author,
    author_email=email,
    license='Apache 2.0',
    url='http://gqylpy.com',
    project_urls={'Source': source},
    description='The GQYLPY.',
    long_description=open('README.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    py_modules=['gqylpy'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License'
    ]
)
