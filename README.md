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

## (38:50) Problem statement

* Python Package
       |
       ----> folder
                |
                ----> multiple files (python)

* Problem statement: Release our own package -> Push our entire code to the Github

* (46:30) MongoDB --> NoSql => Document{Key: value} (Dict, JSON, ...)
           |
           -----> Local server
           |
           -----> Cloud service (Atlas)  
  > If using Python-Client, we'll have to write down some sort of python scripts

* Unified package -- Python package
  > write down the code (follow the documentation guideline): 1. MongoDB 2. Cassandra 3. My-sql
  >
  > --> single function -- passing: 1. URL 2. DB 3. Collection -- (e.g., `insert.data()`)

## Code

* 完成 `requirements.txt`、`requirements_dev.txt`、`setup.py`、`pyproject.toml`、`tox.ini`
  > 在 cfg 檔案中 每一個 [] 後面對應的是 Key & value
  >
  > tox.ini (testing for development environment) are using for testing our code in local environment in a development environment if we want our code in a local environment or while we are going to integrate it. While performing this CI, I'm going to perform it by using the GitHub. GitHub is also having one service which provides us a server -- the service name is called GitHub Action. Provide you the local environment for testing your application (the number of environments can be more than one). PS. `-v` is verbose -- whatever execution is happening in backend, you are going to see all the execution in your screen. PS. `--count` is the command line argument. PS. (E9, F63, ...) **PEP** they define the python protocol. PS. `--select ... --statistics` can be removed.
  >
  > mypi 是 linting tool: check the code whether it's correct or not.

* (1:44:35) 完成 `.github/workflows/ci.yaml`

* 建立 `.github/workflows/python-publish.yaml`
  > 主要來自於 [Publish Python Package](https://github.com/henrykohl/MongoDB-Connector-PYPI-Package/actions/new)，點選 **Configure**，就可以看到  Github 編寫好的 yaml/yml 檔案。

* (1:50:05) review [PyPI · The Python Package Index](https://pypi.org/)
  > 註冊帳號，獲得 TOKEN
  >
  > 在GitHub 的 setting 中 Secrets and variables，設置 New secret，Name* 為 `PYPI_API_TOKEN`，Secret* 為剛獲取的 TOKEN

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


