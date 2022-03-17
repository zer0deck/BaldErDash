from setuptools import setup, find_packages

setup(name='BaldErDash',
      version='0.1.7',
      description="Greatest python platformer ever.",
      long_description="No Hair. Dashes. I'sorry if you didn't take a joke...",
      classifiers=[
        'Development Status :: 0.0.0.0.1 - Alpha',
        'License :: OSI Approved :: Lesser General Public License, Creative Commons',
        'Programming Language :: Python :: 3.9',
        'Topic :: Game developement :: Pygame',
      ],
      keywords='funniest joke comedy flying circus',
      url='http://github.com/zer0deck/BaldErDash',
      author='@zer0deck/Aleksey Grandilevskii',
      author_email='zer0deck@icloud.com',
      license='LGPL, CC',
      packages=find_packages(),
      install_requires=[
          'pygame'
      ],
      include_package_data=True,
      zip_safe=False)