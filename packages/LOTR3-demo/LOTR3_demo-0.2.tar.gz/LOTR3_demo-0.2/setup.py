from setuptools import setup, find_packages   

setup(
    name='LOTR3_demo', version='0.2', license='MIT',     
    author="Juan Francisco Verhook",     author_email='juanfranciscoverhook@gmail.com',     
    packages=find_packages('src'),     package_dir={'': 'src'},     
    url='https://github.com/Juanvulcano/Juan_Verhook-SDK',     
    keywords='sdk',     
    install_requires=['requests',],  
)