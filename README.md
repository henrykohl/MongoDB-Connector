# neurolab-mongo-python

![image](https://user-images.githubusercontent.com/57321948/196933065-4b16c235-f3b9-4391-9cfe-4affcec87c35.png)

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

* Ineuron Lab 所建立的 MongoDB 範本，但無法直接使用 ineuron lab ，此 section 是手動建立的（從sunnysavita10/MongoDB-Connector-PYPI-Package 的初始 commit 內容複製而來）！

* 從 sunnysavita10/MongoDB-Connector-PYPI-Package 所在 github 執行 fork，後用 vscode.dev 開啟自己的 repository，然後將一些檔案刪除到如（23:00）這般，再 push 到自己的 repository，完成類似用 ineuron lab 所建立的 MongoDB 範本，接著用 Gitpod.io 開啟自己的 Github repository，接著就可以按照 Lecture 的步驟進行操作!

---
# Lecture 3 Note -- [How to Create Python Package for MLOps Project](https://www.youtube.com/watch?v=vKi-l__1xg0)

* GitHub Repository Resource 1 -- [MongoDB-Connector-PYPI-Package](https://github.com/sunnysavita10/MongoDB-Connector-PYPI-Package)

* GitHub Repository Resource 2 -- [MongoDB-Connector](https://github.com/sunnysavita10/MongoDB-Connector)

* (34:15) 執行 `python template.py`

## Problem statement (38:50)

* Python Package
       |
       ----> folder
                |
                ----> multiple files (python)

* Problem statement: Release our own package -> Push our entire code to the Github

* In this lecture, we create our own package.

* (46:30) MongoDB --> NoSql => Document{Key: value} (Dict, JSON, ...)
           |
           -----> Local server
           |
           -----> Cloud service (Atlas)  
  > If using Python-Client, we'll have to write down some sort of python scripts

* Unified package -- Unified Python package
  > write down the code (follow the documentation guideline): 1. MongoDB 2. Cassandra 3. My-sql
  >
  > --> single function -- passing different parameters: 1. URL 2. DB name 3. Collection -- (e.g., `insert_data()` to store a single row or multiple rows). So in such a way, we  can customize my code and publish the code in terms of the package. 
  >
  > We are going to create one python package. The python package name is a DB connector or MongoDB connector.  Initially, we will write down the code for MongoDB inside our own customized package. We will customize all the steps whatever step is required for connecting with MongoDB. Customizing in such a way, we don't need to follow all the step again and again. We create our package. Inside the package, it means that inside the folder we will be having a python file. We will write down the MongoDB code in such a way. You can download the package. Then, you can utilize those thing in a unified manner. No need to follow all the step again and again (e.g., database creation, collection creation and all).


## Code (54:50)

* 完成 `requirements.txt`、`requirements_dev.txt`、`setup.py`、`pyproject.toml`、`tox.ini`，執行 `git push`
  > ```bash
  > git init
  > git add .
  > git commit -m "code updated"
  > git config --global user.email "github郵箱地址"
  > git config --global user.name "github帳號名稱"
  > git branch -M main # 此步驟沒執行，git push 會出錯
  > git remote add origin https://github.com/henrykohl
  > git push -u origin main
  > ```

* code explanation
  > (1:10:45) `requirements_dev.txt`: requirement for development environment. dsnpython -- for MongoDB. ensure -- use for ensuring something. pytest -- test for use cases. tox (用在tox.ini) --  using the tox, we can create a testing environment. black and flask8 -- linting tools. \n
  > (1:14:55) `setup.py`: \
  > (1:23:45) `setup.cfg`: 檔案中 每一個 tag/title - 也就是 [] - 後面對應的是 Key & value. It's just an extension of `setup.py`, representing a configuration of `setup.py`. \
  > (1:30:40) `tox.ini` (testing for development environment) are using for testing our code in local environment in a development environment if we want our code in a local environment or while we are going to integrate it. So, while performing this CI, I'm going to perform it by using the GitHub. GitHub is also having one service which provides us a server -- the service name is called GitHub Action. Once it creats the python environment, the first place it will create a python environment. Then, it will install the dependency inside that environment. In [testenv], `deps=...` will install the requirements_dev.txt. Finally, it's going to perform the following particular commands (`commands=...`). `flake8 src ...` means that going into the `src` folder, it is using the `flake8`. `mypy src/` means that checking `src/` we are using `mypy`. `mypy` is a linting tool, which is able to check whether the code is correct. Using `flake8` for all our code is following all the protocol or not. Again, we are going to do testing by using the tox.ini file. `pytest -v ...` will do unit testing and integration testing.
  > Provide you the local environment for testing your application (the number of environments can be more than one). We can create the environments for different versions. PS. `-v` is verbose -- whatever execution is happening in backend, you are going to see all the execution in your screen. PS. `--count` is the command line argument. PS. (E9, F63, ...) **PEP** they define the python protocol. PS. `--select ... --statistics` can be removed. PS. `mypy` 是 linting tool: check the code whether it's correct or not. \
  > (1:42:45)  `pyproject.toml`: the configuration is related to/ visible to our packages. 

* (1:44:35) 完成 `.github/workflows/ci.yaml`

* (1:45:00) 建立 `.github/workflows/python-publish.yaml`
  > 主要來自於 [Publish Python Package](https://github.com/henrykohl/MongoDB-Connector/actions/new)，點選 **Configure**，就可以看到  Github 編寫好的 yaml/yml 檔案。\
  > `flake8 .` 中那一個點是指 current directory. We are checking into the current directory, whatever thing is wrong like we have not written according to the protocol. It will generate a like warning or information of the message regarding to those thing/those issues. `flake8` 後也可以指定一個 specific folder over here.
  It means that you can look into the entire workspace. \
  > `pytest`: we are using for testing like we have test cases for that. \ 
  > (2:03:21) this particular configuration for deploying the code on PYPI.

* (1:50:05) review [PyPI · The Python Package Index](https://pypi.org/)
  > 註冊帳號，登入pypi，在 Account setting 中 API tokens，按下 Add API token，在 Create API token 頁面中，設定 Token name (e.g., deconnection) 與 scope (e.g., entire account)，按下 Create token，獲得 TOKEN
  >
  > 在GitHub 的 setting 中 Secrets and variables，設置 New secret，Name* 為 `PYPI_API_TOKEN`，Secret* 為剛獲取的 TOKEN

* (2:00:15) 解析 `.github/workflows/ci.yaml`
  > This file is not related to PYPI. This is just for the continuous integration. We are going to integrate our code over the GitHub. And GitHub is providing a server. The server name is nothing GitHub Action.GitHub action is a service. Under that we have different servers (e.g., Windows, Linux, ...). In ci.yaml, the particular code/configuration we have written tells us if we are going to integrate our code with GitHub, so immediately we can run all the test cases. We can check our code is fine or not. This ci file is just for testing our code while integrating. This is the work for development.  

* (2:05:20) `src/mongodb_connect/mongo_crud.py`（more details in Lecture 4），`tests/integration/__init__.py`，`tests/__init__.py`  
  > Everything we have unified in a single method

* (2:08:58) 刪除 `main.py`

* (2:09:15) 執行 git push
  > ```bash
  > git add .
  > git commit -m "everything updated"
  > git push -u origin main
  > ```

* (2:11:25) GitHub Release
  > 按下 **Create a new release**: \n
  > * Choose a tag: `v0.0.1` \n
  > * Release a title: `0.0.1` \n
  > * Describe a release: `this is my testing package`
  > * 按下 `Publish release`
  >

  > 在 GitHub Actions 頁面可以看到，The package is going to be deployed in backend

---

# requirements_dev.txt we use for the testing
It makes it easier to install and manage dependencies for development and testing, separate from the dependencies required for production.

# difference between requirements_dev.txt and requirements.txt

requirements.txt is used to specify the dependencies required to run the production code of a Python project, while requirements_dev.txt is used to specify the dependencies required for development and testing purposes.

# tox.ini
We use if for the testing in the python package testing against different version of the python 

## how tox works tox enviornment creation
1. Install depedencies and packages 
2. Run commands
3. Its a combination of the (virtualenvwrapper and makefile)
4. It creates a .tox


# pyproject.toml
it is being used for configuration the python project it is a alternative of the setup.cfg file. its containts configuration related to the build system
such as the build tool used package name version author license and dependencies

# setup.cfg
In summary, setup.cfg is used by setuptools to configure the packaging and installation of a Python projec

# Testing python application
*types of testing*
1. Automated testing 
2. Manual testing

*Mode of testing*
1. Unit testing
2. Integration tests

*Testing frameworks*

1. pytest
2. unittest
3. robotframework
4. selenium
5. behave
6. doctest

# check with the code style formatting and syntax(coding standard)

1. pylint
2. flake8(it is best because it containt 3 library pylint pycodestyle mccabe)
3. pycodestyle


