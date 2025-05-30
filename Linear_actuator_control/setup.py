from setuptools import setup, find_packages

setup(
       name="linear_actuator_control",
       version="0.1.0",
       description="Simple control of an Actuonix linear actuator ",
       author="Michael Ringleb",
       packages=find_packages(),
       install_requires=[
           "pyserial",
       ],
       python_requires=">=3.7",
   )