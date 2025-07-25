from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requirement(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

   
# with open('README.md', 'r', encoding='utf-8') as f:
#     long_description = f.read()     
   

__version__ = "0.0.4" # 每在Github Actions 要執行 publish 時，需修改 version 為唯一(不能重複)
REPO_NAME = "MongoDB-Connector" # 修改過
PKG_NAME= "mongodbconnectpkgauto" # only visible on PYPI repository; 修改過
AUTHOR_USER_NAME = "henrykohl" # 修改過; GitHub 使用者名稱
AUTHOR_EMAIL = "u860218@gmail.com" # 修改過

setup(
    name=PKG_NAME, # the name of the package; the name which we are seeing over the PYPI repository
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description='# firstproject', # long_description, # 修改後，就不需要去讀取 README.md
    long_description_content="text/markdown",
    long_description_content_type='text/markdown', # Lecture 沒有，則出現 warning ... missing 警告
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"}, # 表示 src 是 root 目錄
    packages=find_packages(where="src"), # the package actually it it avaiable inside the SRC folder.
    install_requires=get_requirement("requirements_dev.txt"), 
    # install_requires=["pymongo","ensure","pytest"]
    
    
)