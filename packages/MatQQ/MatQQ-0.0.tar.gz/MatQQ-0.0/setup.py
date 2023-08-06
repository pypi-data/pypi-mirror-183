from setuptools import setup

install_requires = ['dimod>=0.12.3','dwave_neal>=0.5.9','dwave_system>=1.16.0','numpy>=1.23.1','pyqubo>=1.3.1']

setup_requires = []

python_requires = '>=3.6, <3.12'


setup(name='MatQQ',
      version='0.0',
      description='MatQQ',
      packages=['MatQQ'],
      install_requires=install_requires,
      setup_requires=setup_requires,
      python_requires=python_requires,
      author_email='aryatahlil@yahoo.com',
      zip_safe=False)
