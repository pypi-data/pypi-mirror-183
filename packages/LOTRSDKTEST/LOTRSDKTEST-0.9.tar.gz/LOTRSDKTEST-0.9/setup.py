from setuptools import setup, find_packages   

setup(
    name='LOTRSDKTEST', version='0.9', license='MIT',     
    author="Juan Francisco Verhook",     author_email='juanfranciscoverhook@gmail.com',     
    packages=find_packages('src'),     package_dir={'': 'src'},     
    url='https://github.com/Juanvulcano/Juan_Verhook-SDK',     
    keywords='sdk',     
    install_requires=['requests',],  
)