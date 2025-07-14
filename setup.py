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
   

__version__ = "0.0.3" # 修改過 0.0.3 到 0.0.4 變成 0.0.4.0
REPO_NAME = "MongoDB-Connector" # 修改過
PKG_NAME= "mongodbautoconnect" # only visible on PYPI repository; 修改過
AUTHOR_USER_NAME = "henrykohl" # 修改過; GitHub 使用者名稱
AUTHOR_EMAIL = "u860218@gmail.com" # 修改過

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description='# firstproject', # long_description, # 修改後，就不需要去讀取 README.md
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"}, # 表示 src 是 root 目錄
    packages=find_packages(where="src"),
    install_requires=get_requirement("requirements_dev.txt"),
    
    
)