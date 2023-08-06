from setuptools import setup, find_namespace_packages


setup(name='PerAssist',
      version='13',
      description='Personal Jesus',
      url='https://github.com/LarryLynne/PersonalAssistant',
      author='Проект_кор_група_2',
      author_email='vovka.drunique@gmail.com',
      #packages=['addressbook', 'address']
      packages=find_namespace_packages(),
      install_requires = ['colorama'],
      entry_points={'console_scripts': ['Assistant = PersonalAssistant.main: main']}
      )