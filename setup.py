from distutils.core import setup

VERSION = __import__('narcissus').__version__

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

description = "A blogging app that helps you easily share status updates, "
description += "links, photos, videos, and long-form articles on your personal"
description += " website."


setup(
    name='django-narcissus',
    version=VERSION,
    description=description,
    long_description = long_description,
    author='Lincoln Loop',
    license='License :: OSI Approved :: BSD License',
    url='http://github.com/lincolnloop/django-narcissus',
    packages=['narcissus'],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
    ]
)
