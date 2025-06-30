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
# Lecture Note -- [How to Create Python Package for MLOps Project](https://www.youtube.com/watch?v=vKi-l__1xg0)

* GitHub Repository Resource -- [MongoDB-Connector-PYPI-Package](https://github.com/sunnysavita10/MongoDB-Connector-PYPI-Package)

* (34:15) 執行 `python template.py`

* (38:50) Problem statement



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


