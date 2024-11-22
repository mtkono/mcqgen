from setuptools import find_packages, setup

setup(
    name= 'mcqgenerator', 
    version='0.0.1', 
    author='mtkono',
    author_email='mtkonopka@gmail.com',
    install_requires=["openai", "langchain","langchain_community","langchain-openai", "streamlit", "python-dotenv", "PyPDF2"], 
    packages=find_packages()
)
