from setuptools import setup

setup(name="led_checker",
      version="0.1",
      description="Check LED board",
      url="",
      author="Conor Wyse",
      author_email="conor.wyse@ucdconnect.ie",
      licence="GPL3",
      packages=['Conor'],
      entry_points={
          'console_scripts':['led_checker=Conor.main:main']
          }
    )