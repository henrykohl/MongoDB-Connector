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
# Lecture 1 Note -- [MLOps Foundations and Fundamentals](https://www.youtube.com/watch?v=jpU8F0M5axo)

* (21:45) The prerequisite: The basics of the machine learning
  > 1. Basics of ML/DL
  > 
  > 2. Basics of the Python

## (29:30) MLOps -- DevOps: SDLC(software development live cycle)

* 5 phases in Software Development live cycle (五階段)
  > 1. Planning & Requirement
  > 
  > 2. Design
  > 
  > 3. Building -- Dev. w.r.t any sort of a language like python, Java, ... 
  > 
  > 4. Testing
  > 
  > 5. Deploy

* Types of software development models
  > 1. Waterfall Model
  > 
  > 2. Agile methodology (state-of-art) – deliver a APP in a shortest time with a minimalistic feature

## (45:20) Corona scenario

* 開發 Aarogya Setu 應用程式 -- (顧客 Government)，(賣方 Organization)有以下兩者：
  > 交給 XYZ 公司 ：需 8~10 months，遵循 SDLC 五階段 \n
  > 交給 abc 公司 ：需 2~3 weeks，每一個iteration 只實現簡單一部份功能！ \n

* launch the APP in iterations. At the first place, create a simple UI. Take the information from the user. Based on that, show the basic guidelines/ only the basic detail. In the next iteration, keep it to the advanced one. Add a few more information(e.g., regarding traveling and all). In the third iteration, again add something over there. So they are working in iteration. The first iteration follows all the step regrading 五階段 in waterfall + production. Deploy and then, the APP is visible to everyone. In the second iteration, again, they came up, again, they have planned with a new feature and they have implemented that and then basically they have tested and then deployed. So, they are working on iteration-wise. They are not going to build up the entire APP in a single shot and then they are going to test it and then they are going to be deployed.

* So the waterfall, it’s having many disadvantages. It's not for the complex project and it's not a Time effective. On the other hand, agile, it is working in iterations. Therefore, nowadays in a market actually we are using agile, not a waterfall because agile is the state-of-art and with that basically we are able to deliver an APP in a shortest time and with a minimalistic feature also.

## (53:00) DevOps

* Dev+Ops
  > * Development
  > |Dev|: Java/Python/PHP, Git/GitHub \n
  > --> |testing| \n
  > --> |QA| Jenkins/Github Action/Circle ci/Travis ci
  >
  > * Operations
  > --> |Delivery|: Docker/Kubernetes \n
  > --> |Deployment| \n
  > --> |maintenance/monitoring|

* Manual (every step in Waterfall) VS. Automated (the entire process)

* two methodologies (whatever application we are building nowadays)
  > Agile
  >
  > DevOps

## (1:06:23) MLOps
* Development:
|Buidling| 
--> |Testing|: manual/automated/UAT(user acceptance testing)/unit/integration 
-----> |QA(quality assurance)|

* Operation:
|Delivery|
-->|Deployment|
---->|monitor/maintenance|

* MLOps: ML + Ops

  > ML: 
  > 1. Data
  > 2. Validation
  > 3. EDA--Exploratory Data Analysis
  > 4. Feature Engineering
  > 5. Model building/ Model Evaluation

## (1:13:44) ML & DL 

* Machine Learning -- Regression, Classification
* Deep Learning -- Vision, NLP => App
  > <pre>採用Agile -- |MLOPS| : building a ML APP & responsible for maintaining the entire pipeline. \
  >                 ^ 
  >                 ^ 
  > 採用Agile -- |DEVOPS| 
  >                 ^ 
  >                 ^ 
  >              |SDLC|</pre>

## (1:21:55) Flow regarding one application (MLOps engineers)
* ML-APP
  > <pre>|Build|: Python, Git..(tools) ~ [local] 
  > -->|test|: unit, integration ~ [central repo/github]
  > -->|Deliver|: Docker image ~ [Docker Hub/Amazon]
  > -->|Deploy|: container ~  [AWS]
  > -->|Monitor/Maintain| </pre>

* (1:30:40) More terms in market
  > <pre>Amazon - DevOps、MLOps
  > GCP - DevOps、MLOps
  > Azure - DevOps、MLOps</pre>

* open source tools (for MLOps engineers):
  > Git、CircleCI、Terraform、Ansible、Docker Hub

## (1:33:55) CI/CD/CD + CT (Continuous Training): Air flow

* CI
  > |Develop| (local) 

  > --> |testing|

  > --> |QA|

* CD
  > --> |Deliver|

* CD
  > --> |Deploy|

  > --> |Monitor/Maintain|

* (1:38:07) MLOPS engineers 的工作
  > CI/CD/CD/CT

* (1:43:30) MLOps Architecture [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)

* (1:52:00) Create a GitHub Repository 

# Lecture 2 Note -- [MLOps End-to-End Project Setup with GitHub](https://www.youtube.com/watch?v=6qnx3okPvkc)
* MLOPS(ML- + [OPS]):
  > <pre>1-. Data Ingestion/collection 
  >     > Data Pipeline: Source to Destination - Data engineering
  > 2-. EDA
  > 3-. FE--feature engineering
  > 4-. Model Creation
  > 5-. Model Evaluation
  > [6]. Deploy
  > [7]. Monitor
  > [8]. Retrain </pre>

* (37:55)Devops VS. MLOps

## (48:00) 建立 `template.py`

```python
import os
from pathlib import Path

package_name = "mongodb_connect"

list_of_files = [
   ".github/workflows/.gitkeep",
   "src/components/__init__.py",
   "src/components/data_ingestion.py",
"src/components/data_transformation.py",
"src/components/data_trainer.py",
"src/components/data_evaluation.py",
"src/pipeline/__init__.py",
"src/pipeline/training_pipeline.py",
"src/pipeline/prediction_pipeline.py",
"src/utils/__init__.py",
"src/utils/utils.py",
"src/logger/logging.py",
"src/exceptions/exception.py",
"tests/utils/__init__.py",
"tests/integration/__init__.py",
"init_setup.sh",
"requirements.txt",
"requirements_dev.txt",
"setup.py",
"setup.cfg",
"pyproject.toml",
"tox.ini",
"experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
```

* 執行 `python template.py`

* 執行 git push
  > ```bash
  > git add .
  > git commit -m "folder structure updated" # 出錯
  > 
  > git config --global user.email "u860218@gmail.com"
  > git config --global user.name "henrykohl"
  > git commit -m "folder structure updated" # 再次執行
  > git push -f origin main
  > ```
## Machine Learning:

* Supervised VS. Unsupervised

* Two stages
  > 1. (tp): training -- pipeline
  > 
  > 2. (vp): validation/testing/inferencing -- pipeline

* (tp):
  > |Data| -> |Data Validation| -> |FE| -> |Model training| -> |Model evaluation|

* (vp):
  > <pre>|Data| -> |Data Validation| -> |FE| -> |Model evaluation|
  > Two types of testing
  > Single value prediction
  > Bulkd prediciton<pre>

* 執行 git push
  > ```bash
  > git add .
  > git commit -m "structure_updated"
  > git push -f origin main
  > ```

## (1:48:00) Discuss something before the main project
<pre>(1) Introduciton
(2) Structure
(3) Python Package -> PyPi</pre>

* CI
  > github action
  >
  > github page

* MongoDB -- Database

* `setup.py`、`setup.cgf`、`pyproject.toml`、`tox.ini` are required

* (1:55:15) Demo GitHub Template repositories 

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
  > (1:14:55) `setup.py`: 在 Lecture 3 中加入 `install_requires=get_requirement("requirements_dev.txt")`，自行實現時，在 GitHub Action 中執行 Test with tox 時，找不到 `"requirements_dev.txt"`，不知道為何！後來才google到解決方式~建立 `MANIFEST.in` 加入 `include requirements_dev.txt`
  > (1:23:45) `setup.cfg`: 檔案中 每一個 tag/title - 也就是 [] - 後面是 information ，有對應的 Key & value. It's just an extension of `setup.py`, representing a configuration of `setup.py`.  \
  > (1:30:40) `tox.ini` (testing for development environment) are using for testing our code in local environment in a development environment if we want our code in a local environment or while we are going to integrate it. So, while performing this CI, I'm going to perform it by using the GitHub. GitHub is also having one service which provides us a server -- the service name is called GitHub Action. Once it creats the python environment, the first place it will create a python environment. Then, it will install the dependency inside that environment. In [testenv], `deps=...` will install the requirements_dev.txt. Finally, it's going to perform the following particular commands (`commands=...`). `flake8 src ...` means that going into the `src` folder, it is using the `flake8`. `mypy src/` means that checking `src/` we are using `mypy`. `mypy` is a linting tool, which is able to check whether the code is correct. Using `flake8` for all our code is following all the protocol or not. Again, we are going to do testing by using the tox.ini file. `pytest -v ...` will do unit testing and integration testing.
  > Provide you the local environment for testing your application (the number of environments can be more than one). We can create the environments for different versions. PS. `-v` is verbose -- whatever execution is happening in backend, you are going to see all the execution in your screen. PS. `--count` is the command line argument. PS. E9, F63, ..., **PEP**, they define the python protocol. PS. `--select ... --statistics` can be removed. PS. `mypy` 是 linting tool: check the code whether it's correct or not. \
  > (1:42:45)  `pyproject.toml`: the configuration is related to/ visible to our packages. [] 也就是 tag. Inside the tage, you will find out the information. Either you can write it down inside the `setup.cfg` or in the `pyproject.toml`; these two files.

* (1:44:35) 完成 `.github/workflows/ci.yaml` (檔案裡可以有中文註釋)

* (1:45:00) 建立 `.github/workflows/python-publish.yaml`
  > 主要來自於 [Publish Python Package](https://github.com/henrykohl/MongoDB-Connector/actions/new)，點選 **Configure**，就可以看到  Github 編寫好的 yaml/yml 檔案。\
  > `flake8 .` 中那一個點是指 current directory. We are checking into the current directory, whatever thing is wrong like we have not written according to the protocol. It will generate a like warning or information of the message regarding to those thing/those issues. `flake8` 後也可以指定一個 specific folder over here. It means that you can look into the entire workspace. \
  > `pytest`: we are using for testing like we have test cases for that. \ 
  > (2:03:21) this particular configuration for deploying the code on PYPI.

* (1:50:05) review [PyPI · The Python Package Index](https://pypi.org/)
  > 註冊帳號，登入pypi，在 Account setting 中 API tokens，按下 Add API token，在 Create API token 頁面中，設定 Token name (e.g., deconnection) 與 scope (e.g., entire account)，按下 Create token，獲得 TOKEN \
  > 在GitHub 的 setting 中 Secrets and variables，設置 New secret，Name* 為 `PYPI_API_TOKEN`，Secret* 為剛獲取的 TOKEN

* (2:00:15) 解析 `.github/workflows/ci.yaml`
  > This file is not related to PYPI. This is just for the continuous integration. We are going to integrate our code over the GitHub. And GitHub is providing a server. The server name is nothing GitHub Action.GitHub action is a service. Under that we have different servers (e.g., Windows, Linux, ...). In ci.yaml, the particular code/configuration we have written tells us if we are going to integrate our code with GitHub, so immediately we can run all the test cases. We can check our code is fine or not. This ci file is just for testing our code while integrating. This is the work for development.  

* (2:05:20) `src/mongodb_connect/mongo_crud.py`（more details in Lecture 4），`tests/integration/__init__.py`，`tests/__init__.py`，Lecture 3 示範的內容，實際測試時，會發生來自 decorator 的錯誤，但 Lecture 4 示範的內容又不同，卻是可以正確運行的！需要注意。  
  > Everything we have unified in a single method

* (2:08:58) 刪除 `main.py`

* (2:09:15) 執行 git push
  > ```bash
  > git add .
  > git commit -m "everything updated"
  > git push -u origin main
  > ```

* Github Actions 出現錯誤 `from tox.config.cli.parser not found` (Lecture 3 未解決)  

* (2:11:25) GitHub Release
  > 按下 **Create a new release**: \n
  > * Choose a tag: `v0.0.1` \n
  > * Release a title: `0.0.1` \n
  > * Describe a release: `this is my testing package`
  > * 按下 `Publish release`
  >

  > 在 GitHub Actions 頁面可以看到，The package is going to be deployed in backend

* (2:14:14) Github Actions 中 deploy 時，Test with pytest 也出現錯誤 (Lecture 3 未解決) 

* (2:16:00-end) No more significant point.

## Trouble issue 自行補充

* `setup.py` 中如果使用 
  > ```python
  > install_requires=get_requirement("requirements_dev.txt"),
  > ``` 
  需要建立 `MANIFEST.in`，其內容加入 `include requirements_dev.txt`，否則在 GitHub Actions 中執行 Test with tox 時，會出現 FileNotFoundError: [Errno 2] No such file or directory: 'requirements_dev.txt' 的錯誤。 

* `setup.py` 中，自行加入  `long_description_content_type='text/markdown',`，否則在 publish 階段，Github Actions 進行 deploy 時（Publish package），會出現 WARNING 'long_description_content_type' missing. defaulting to text/x-rst 的警告

* 每次要 Publish release 時，`setup.py` 中的 version 是需要唯一的，PYPI 不接受相同的 version。此外，在 Publish release 時，Tag (可以與 version是不同的)，如果使用用過的，似乎 Actions 所使用的 code ，就會是之前的 Tag 所 commit 的內容 -- 還不知道為什麼，所以要 Publish release 時，要謹慎一點，因為使用過的 Tag ，等於無法再給更新過的 code 使用。


* `setup.cfg`註釋最好不要用中文，否則（用Windows 系統時）在 Actions 的 install dependencies 之中，會出現 `WARNING: Ignore distutils configs in setup.cfg due to encoding errors.` 警告

* `requirements_dev.txt`中可以有註釋（使用 #），但不能用中文，否則（用Windows 系統時）在 Actions 中 install dependencies(或 Test wit tox)時，會出現 `UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 84: character maps to <undefined>` 的錯誤



---

# Lecture 4 Note -- [GIT & DOCKER For MLOps Projec](https://www.youtube.com/watch?v=KWoyJwqt22I)

## Code Recap (27:00)

* `init_setup.sh`: If you are going to create an environment for that some like repeated command is required like `conda create`、`conda activate`, all which you are running on your bash terminal (on your windows terminal). You can write down each and every command inside your shell script (.sh). And, you can run it in a single shot by using the bash commands.

* (30:13) `/src`: having our main package. It is representing the source code.

* `/experiments`: just for the experiment purpose. Whatever experiment I was doing. Here each and every file I was creating here itself.

so inside this experiment folder, I had created the ipynb file.

* (30:45) `/.github/workflows`: inside the workflows folder, you can find out the complete configuration. The configuration is related to the Continuous Integration and The configuration is related to the PYPI deployment. When we are going to deploy our code on a PYPI repository, for that we have written a configuratin inside this particular yaml file (`python-publish.yaml`). For the continuous integration, if I want to test our code on GitHub Action server, so for that we have written `ci.yaml` file as soon as we want to integrate our code or as soon as we are going to push our code to the GitHub. So the Github Action server will up and then like each and every script is going to be run.

* (32:51) `experiments/experiments.ipynb` 
  > (44:10) MongoDB --> client --> Database --> Collection <--> Document:{key, value}. Inside the collection my data will be available in the form of document. document is nothing key and value pair.

* (37:00) MongoDB

* (42:10-1:35:25) 完成 `experiments/experiments.ipynb` 

* (1:35:25) Review `src/mongodb_connect/mongo_crud.py`
  > 注意，`mongo_crud.py` 要使用 [MongoDB-Connector/src/mongodb_connect
/mongo_crud.py](https://github.com/sunnysavita10/MongoDB-Connector/blob/main/src/mongodb_connect/mongo_crud.py)，而不是使用[MongoDB-Connector-PYPI-Package/src/database_automation
/mongo_crud.py](https://github.com/sunnysavita10/MongoDB-Connector-PYPI-Package/blob/main/src/database_automation/mongo_crud.py)

* (1:36:20) 將 `setup.py` 的 PKG_NAME 改為 "databaseautomation"， 將 `/src` 下的資料夾 改名為 *database_automation*. PS. __version__ = 0.0.2 改成 0.0.3 ??
  > ```bash
  > git add .
  > git commit -m "code and version updated"
  > git push -u origin main
  > ```

* In Github Action webpage，the code is running on top of github action. 

* 在 Github repository 的 release 頁面，可以看到 v0.0.3 的版本

* (1:44:14) 將 `setup.py` 的 __version__ = 0.0.4
  > ``` bash
  > git add .
  > git commit -m "version updated"
  > git push origin main
  > ```

* 在 [github releases 頁面](https://github.com/henrykohl/MongoDB-Connector/releases) ，點選 **Draft a new release**，在 **Choose a Tag** 中選取 v0.0.4，在 release title 輸入 v0.0.4，在 Describe release 中輸入 this is my mongo automation package. 最後按下 **Publish release**.

* (1:48:00) Google Colab，自行將 Lecture 的演示，記錄到 `mongodemo.ipynb`

* (2:10:54) Explanation of YAML file

---

# Lecture 5 Note -- [GIT & DOCKER Part 2 - MLOps Foundatio](https://www.youtube.com/watch?v=VIAcD6P_Etc)

## The basic concept og GIT (18:00)

* Create a new repository in GitHub (名稱：practice)，開啟 VS Code ，在 terminal 中執行
  > ```bash
  > ls -la
  > rm -rf .git # 如果有 .git 存在
  > ```

* (23:45) GIT -- 
  > source code management system (SCMS) \
  > version control \
  > it's much required for DEVOPS or MLOPS. \
  > it's free to install git. \
  > git is an open source, a version control system.
  > to manage different versions of code

  > <pre>git local system:
  > ___________________
  > |       |         |       (1): local folder -- using `git init` to convert it to the repository
  > |       |   (2)   |
  > |       |         |
  > |  (1)  |_________|       (2): staging area -- `git add <>`, <> can be `.`, which means `all`.
  > |       |         |
  > |       |   (3)   |       (3): commit area -- `git commit <'SNAPSHOT'>`
  > |       |         |
  > |_______|_________|
  > </pre>

* After initializing the git so once we got a git as soon as we will run this particular command(`git init`), you will get one folder actually. This is a hidden folder. The name is going to start with DOT -- `.git`. so inside the local workspace yo u will find out the `.git` folder.

  > <pre>one more example:
  > abc.txt(v1):
  > my name is sunny
  > 
  > ____________________
  > | abc.txt |         |    (1): local workspace -- run `git init` -- get `.git` folder
  > |         |   (2)   |
  > |         |         |
  > |  (1)    |_________|    (1)->(2): staging  -- run `git add abc.txt`
  > |         |         |
  > |         |   (3)   |    (2)->(3): run `git commit <'SNAPSHOT'>` -- get hash key id (alpha numeric value)
  > |         |         |
  > |_________|_________|
  > 
  > abc.txt(v2):
  > my name is sunny
  > savita
  > 
  > do (1)->(2)->(3): get another different hash key id
  > </pre>

* (46:04) CVCS -- Centralized Version Control System

  > <pre>
  >  __________________________________________________
  > |                  Central Repo.                   |
  > |__________________________________________________|
  >      |             |             |             |
  >      |             |             |             |
  >      |             |             |             |
  >      |             |             |             |
  >     |A|           |B|           |C|           |D|  
  >     (developer with LSM: local system management)  no git
  > </pre>

* (53:56) DVCS -- Distributed Version Control System
  > i.e., GitHub: Hub for git, Gitlab, bitbucket \
  > After committing inside the local repository right from the stagin area. Then basically they need to push it somewhere inside the centrol repo. \
  > committing means you are just going to save it, you will get one ID
  > <pre>
  > They are working on the same branch on the same code on the same project.
  > They are managing this thing by using the git inside their local folder itself.
  > Finally they are pushing it over the cloud repo--the centralized system repo.
  > Git is managing the entire code.
  > 
  >  __________________________________________________
  > |                  Central Repo.                   |
  > |__________________________________________________|
  >      |             |             |             |
  >      |             |             |             |
  >      |             |             |             |
  >      |             |             |             |
  >     |A|           |B|           |C|           |D|  
  >     git           git           git           git
  > </pre>

  > <pre>
  > Developer A ~ git <-- System Control Management (SCM)
  >  _____________________                                            GITHUB (centralized repo)
  > | login.py  |         |                                        _____________________________
  > |           |   (2)   |                                       |                             |
  > |           |         |                                       |                             |
  > |   (1)     |_________|    -------push----------------------->|          login.py           |
  > |           |         |                                       |                             |
  > |           |   (3)   |                                       |                             |  
  > | course.py |         |    <-------pull-----------------------|                             |
  > |___________|_________|                                       |                             |
  > (1) local folder[local repo]: git init                        |                             |
  > (1)->(2): `git add < >`                                       |                             |
  > (2) staging area                                              |                             |
  > (2)->(3):  `git commit <'snapshot'>` <= hash key              |                             |
  > (3): main branch                                              |                             |
  >                                                               |                             |
  > Developer B ~ git <-- System Control Management (SCM)         |                             |
  >  _____________________                                        |                             |
  > | course.py |         |                                       |                             |    
  > |           |   (2)   |                                       |                             |
  > |           |         |                                       |                             |
  > |   (1)     |_________|    -------push----------------------->|          course.py          |    
  > |           |         |                                       |                             |
  > | login.py  |   (3)   |    <-------pull-----------------------|                             |   
  > |           |         |                                       |_____________________________| 
  > |___________|_________|
  > (1) local folder[local repo]: git init 
  > (1)->(2): `git add < >`
  > (2) staging area
  > (2)->(3):  `git commit <'snapshot'>` <= hash key
  > (3): main branch 
  > </pre>

* Logical representation of the GIT
  > We have main branch and we can create as many as branch over here itself inside our local repository
  > <pre>project xyz 
  > Actually we cannot give the access of the main branch to any new developer.
  > 
  > [main branch]_____________x_______________x__________..
  >                           |               ^
  >                           |               |
  > [test branch]             V_______________|
  >                                                
  >                     branch fork      branch merging 
  > - test branch is for developer-2.    
  > - 'x' is a commit point                
  > </pre>

## (1:18:50) Perform the practical

* In VS Code, create a file -- 'abc.txt'
  > ```bash
  > git init # the local folder will be converted into a local repository
  > git status # checking
  > git add . # promote pending changes in the workspace, to the git staging area. (google來的)
  > 
  > git status # checking again.
  > 
  > git config --global user.email "你的email"
  > git config --global user.name "你的帳戶名"
  > 
  > git commit -m "first commit"
  > 
  > git --version # the version of git
  > which git # the location where the git is available
  > 
  > git config --list # find out the usename, email, ...
  > 
  > git log # find out the particular commit ID
  > ```

* 將 abc.txt 的內容編輯成 `Hey!! my name is sunny savita`
 
  > ```bash
  > git status # 可見到 `modified: abc.txt` 的資訊(紅字) 
  > git add abc.txt
  > git status # 可見到 `modified: abc.txt` 的資訊(綠字) 
  > 
  > git commit -m "second commit"
  > git log # there are two IDs~ And copy the latest commit ID only with a few initial chars
  > git show ... # `...` is copied chars.
  > ```


* 將 abc.txt 的內容新增 `i am working as a data scientist`

  > ```bash
  > git status # checking
  > git add abc.txt && git commit -m "third commit"
  > git log # there are three commit IDs~ copy a particular commit ID only with a few initial chars
  > git show # ... # `...` is copied chars.
  > ```

* 執行 `conda create -p env python=3.8 -y` 建立 env 環境
  > ```bash
  > git add . # staging env
  > git status # a lot of files are shown
  > # git rm --cache # useless??
  > git reset . # unstaging env (don't use `restore`)
  > git status
  > ```

* (1:48:40) 建立 .gitignore  ，編輯內容加入 env

* Branch
  > ```bash
  > git branch # get the branch name
  > git branch testfirstbranch # create a branch, whose name is testfirstbranch. 
  > git branch # get all the branch names
  > git checkout testfirstbranch # swith branch
  > git log # show all commits in testfirstbranch, should be the same as commits in MASTER
  > ```

* 建立 xyz.txt, 編輯內容為 `hey i hope you are enjoying this section`

  > ```bash
  > git status # checking( should show untracked files -- '.gitignore' and xyz.txt) 
  > git add .
  > git commit -m "fourth commit"
  > git log # there are four commits
  > 
  > git branch # two branches
  > git checkout master # switch to master branch
  > git branch # master branch has a '*'
  > 
  > git merge testfirstbranch # branches merge 
  > git status # there are still two branches. We are working in two branches separately
  > ```


# Lecture 6 Note -- [GIT & DOCKER Part 3 - MLOps Foundation](https://www.youtube.com/watch?v=uq-78kXJY4E) 

* Agenda
  > 1. Git branch
  > 2. Merging
  > 3. Conflict
  > 4. stashing
  > 5. reset
  > 6. revert
  > 7. tagging
  >
  > - open source contribution 
  > - fork 
  > - changes 
  > - push 
  > - pull requests 

* Review the logical architecture of the GIT (the same as that in Lecture 5)

* (28:10) Particular Concepts
  > <pre>git local system:
  > ______________________
  > |         |          |    
  > |         |          |
  > |         |          |
  > |         |__________|    
  > |         |   main   |
  > |         |//////////|    
  > |         | branch_1 |
  > |         |//////////|
  > |         | branch_2 |
  > |_________|__________|

  > Project: Facebook
  > - using the git for the version control(source code management & code versioning)
  > - Default branch: 'main' (包含功能 -- 'login', 'logout', 'UI', ...)
  > - Developer A (working in 'main'): functionality -- image uploading, post
  > - Developer B (working in 'branch_1'): functionality -- comment, emojs, like, video uploading
  >
  >
  > [ branch_2 ]                      x_______________x
  >                                   ^               |
  >                                   |               v
  > [main branch]_____________x_______x_______x_______x____________..
  >                           |               ^
  >                           |               |
  > [ branch_1 ]              V_______________|

  > </pre>
Developer A is using the GIT and creating a facebook application.
He has created some sort of functionality (e.g., logging functionality)

* (38:00) Practical concepts
  > 由 Lecture 5 結束地方開始，開啟 VS Code，此時應該包括: env 資料夾，.gitignore，abc.txt，xyz.txt。將abc.txt與xyz.txt刪除。
  > ```bash
  > ls -al # . .. .git .gitignore
  > cd .git 
  > ls # list all the directory
  > cd ..
  > 
  > git status # deleted: abx.txt and xyz.txt (紅色)
  > git add .
  > git status # deleted: abx.txt and xyz.txt (綠色)
  > git commit -m "file deleted" # 未能成功
  > git config --global user.email "email帳號"
  > git config --global user.name "username"
  > git commit -m "file deleted" 
  > git status # checking
  > git branch # 'master' and 'testfirstbranch'
  > git branch -d testfirstbranch 
  > git branch # 'master'
  > 
  > ```

* (49:30) Creating a file -- `testing.py`. Then, run `python testing.py`
  > ```python
  > # version1
  > a, b=10, 20
  >
  > print(a+b)
  > ```
  ```bash
  git add testing.py
  git status # checking
  git commit -m "addition done"

  git log # show all the commits

  git branch branch1 
  git branch # show all the branches
  git checkout branch1 # switch to 'branch1'
  git branch
  ```

* (55:35) Modifying `testing.py`
  > ```python
  > # version2
  > a, b=10, 20
  >
  > print(a+b)
  > 
  > c, d=20, 50
  >
  > print(c*d)
  > ```
  ```bash
  git status
  git checkout master
  git status

  git checkout branch1
  git add .
  git commit -m "multiplication added"
  git branch 

  git checkout branch1
  git status

  git branch
  git checkout master # `testing.py` 內容變回 version1
  ```

* (1:03:00) Creating a file -- `testing2.py`.
  > ```python
  > print("hello how are you?")
  > ```
  ```bash
  git branch # master
  git status

  git add .
  git commit -m "create a new file"

  git branch # master
  git checkout branch1
  ```

* Creating a file -- `testing1.py
  > ```python
  > print("what you are doing?")
  > ```
  ```bash
  git branch # branch1
  git add .
  git commit -m "file added"

  git checkout master
  git branch

  git merge branch1 # have to write a simple message

  git branch # master

  git checkout branch1 # have 'testing.py','testing1.py'

  git branch # branch1
  git checkout master
  ```

* (1:15:00) Creating a file in 'master' -- `demo.txt`
  > ```txt
  > hi there my name is sunny.
  > ```
   ```bash
   git add .
   git commit -m "demo file added"
   git checkout branch1
   ```
* (1:16:32) Creating a file in 'branch1' -- `demo.txt`
  > ```txt
  > i am working as a data scientist and AI developer
  > ```
  ```bash
  git add .
  git commit -m "demo created and file added"

  git checkout master # look into demo.txt
  git checkout branch1 # look into demo.txt (different)
  
  git checkout master
  git merge branch1 # CONFLICT
  ```
* (1:20:40) Tackle content CONFLICT



* (1:27:00) manually edit demo.txt
  > ```bash
  > git add .
  > git commit -m "successfully merged"
  > ```

## (1:30:00) Git stashing

>  > keep something on hold: you cannot 'add', you cannot commit. \
>  > you can keep it inside your temp repository. 


* (1:37:19) practical demo

  > ```bash
  > touch stashingdemo.txt
  > git add .
  > git commit -m "stashed file updated"
  > git status # nothing to commit, working tree clean
  > git branch # master
  > ```
  > - edit 'stashingdemo.txt'
  > > ```txt
  > > hi guys welcome to this community session of mlops.
  > > ```
  > ```bash
  > git stash # 'stashingdemo.txt' becomes empty. It's gone inside the temporary repo.
  > git stash list # stash@{0}...
  > ```
  > - edit 'stashingdemo.txt' again
  > > ```txt
  > > i am sunny savita and i working as a data scientist ml engineer and mentor
  > > ```
  > ``` bash
  > git stash # 'stashingdemo.txt' becomes empty again.
  > git stash list # stash@{0}... stash@{1}...
  > ```
  > - edit 'stashingdemo.txt' once more again!
  > > ```txt
  > > so we are learning git
  > > ```
  > ``` bash
  > git stash # 'stashingdemo.txt' becomes empty once more again.
  > git stash list # stash@{0}... stash@{1}... stash@{2}
  > 
  > git stash apply stash@{0} # show the latest one (so we are learning git).
  > # git stash@{2} # 不可以在未 commit 情況下 繼續呼叫 stash memory 中的其他記錄
  > 
  > git add .
  > git commit -m "text is updated"
  > git stash@{2}  # need to manually check
  > git add .
  > git commit -m "file updated"
  > git stash list # there are still three messages/records
  >
  > git stash clear
  > git stash list # no more message
  > ```

## (1:53:30) Revert and Reset

  > <pre>git local system:
  > ___________________
  > |       |         |       (1): local workspace 
  > |       |   (2)   |       (2): staging area
  > |       |         |       (3): commit area
  > |  (1)  |_________|  
  > |       |         |       (1)->(2): add
  > |       |   (3)   |       (2)->(3): commit
  > |       |         |       (2)->(1): reset
  > |_______|_________|       (3)->(1): revert
  > </pre>

* (1:56:00) Practical demo
  > ```bash
  > touch reseting.txt
  > touch reverting.txt
  > git add reseting.txt
  > git status
  > 
  > git reset reseting.txt
  > git status # become untracked
  > 
  > git add reseting.txt
  > git status # changes to be committed
  >
  > git commit -m "reseting file added"
  > git log --oneline # show all commit ids
  >
  > git revert <指定的commit id> # required to provide your reason (i.e., "this was not good")
  >                              # reseting.txt and reverting.txt are removed
  > ```

# Lecture 7 Note -- [DOCKER - MLOps Foundation](https://www.youtube.com/watch?v=6CgKNVne2lM)

* (15:00) theorectical concept behind the docker -- DOCKER
  > 1. What is a docker?
  > 2. How does it work?
  > 3. Docker engine
  > 4. Docker container and VM
  > 5. Docker file - commands for docker file
  > 6. Docker image
  > 7. Docker commands
  > 8. Port mapping
  > 9. Docker networking
  > 10. Docker volume
  > 11. Docker compose

* Docker (first released as an open-source project in March 2013)
  > - docker engine <-- Linux
  > > the actual virtualization we are going to do by using this Docker engine, which has been written inside this Linux itself. \
  > > the actual docker enigine is responsible for creating a container and for virtualization like natively it has been written in Linux itself. 
  > - GO 
  > > "GO" is a language. it has been developed by the Google itself. this entire Docker has been written inside this GO language. 
  > > 
  > - There are three types of services (1)Iaas (2)**Paas**--Docker (3)Saas
  > - We are going to use it for running the application and for deploying the application. We can build the application and run it basically and deploy it.
  > - The main software Docker is the name of the company. the main software which is responsible for the virtualizaiton that is called Docker engine and it has been written  in Linux OS. It has been developed in a GO language. The main uses of the Docker is to **build-run-deploy** the application.

## (30:30) DevOps

* DevOps: Dev + testing + Ops
  > - Dev: the core development -- build an application, build a project
  > - Ops: deliverying the project, deploying the project, doing a maintenance monitoring

* MLOPS: ML-Dev + testing + Ops
  <pre>
  ML-Dev   -- (build)  --  (different python versions, different servers) one development environment is required                
    |
  testing
    |
  Ops (fails in different servers)
  </pre>

  - some dependencies will also be required for building this particular application. And the dependencies basically which you are going to use. So it will be having a specific version.

  - One example (problem):
  PUBG -> Mobile -> playstore ~> 2GB ~> 90% ~> Error(related to Hardware)



* Basic example"
  <pre>
  ML (created one application in ml) -> AWS (deployed)
        |
        v
  App：scrapping of the data (this code basically you have written inside the python)
  </pre>
  - Regrading the mongodb there also, we faced that particular issue (this internal server error )
  - It means that it was working fine in my local system. Whenever we are going to perform the CI, we are using a GITHUB Action server. But, our testing was going to be failed (because of the compatibility, regarding the different libraries)

* Problem statement: 
  > we are having the issue - miscommunication between the different teams(development team, testing team, ...) \
  > - Solution:
  > 1. Virtualization
  > 2. Containerization (better)

  <pre>
  the high level of overview of the system
  _____________________
  |                   |
  |  APP       APP    |
  |       APP         |
  |___________________|
  |                   | (WIN, LINUX, MAC)
  |        OS         |
  |___________________|
  |     Hardware      | (CPU, RAM, Memory)
  |___________________|
  </pre>

* Virtualization
  > 1. Oracle virtual Box
  > 2. VMware station
  > - hypervisor: 1. & 2.
  <pre>single host system
  _____________________________________
  |                                   |
  |     VM         VM         VM      | VM: VMware station
  |  _________  _________  _________  |
  |  |  APP  |  |  APP  |  |  APP  |  |                   |
  |  |_______|  |_______|  |_______|  |
  |  |  OS'  |  |  OS'  |  |  OS'  |  | guest OS
  |  |_______|  |_______|  |_______|  |
  |  | C,R,M |  | C,R,M |  | C,R,M |  |
  |__|_______|__|_______|__|_______|__|
  |            hypervisor             | 
  |___________________________________|
  |             OS/kernel             | host OS (WIN, LINUX, MAC) 
  |___________________________________| 1. Processing 2. Memmory management 3. Security 4. Access management
  |             Hardware              | (CPU, RAM, Memory: 8 core+i7, 16GB, 1TB)
  |___________________________________|

  It is not possible to share the entire APP + OS with testing team or OPS team.
  
  template VM: APP + OS' + C,R,M.
  It is possible to share template VM with testing team and deployment also.

  Summary: 
             Virtualization -> 遇到 Problem -> 解決方式 Containerization <-  docker engine <- Docker
                   |                                       |
                   |______________   V/S   ________________|
  </pre>

* (1:05:30) The problem which we are having with the Virtualization
  > 1. static, not dynamic
  > 2. Configuration is fixed.  

  <pre>
  Whenever we are going to allot the memory, the configuration, to my VM, it's going to be fixed.

  What we are going to do is to share the Hardware with this VM. But we are installing a separate OS over here. If I want to run this VM so I will have to install the separate OS.
  So let's say here I'm running Mac in VM1, Linux in VM2, Win in VM3. Separately I have to install it and it required more memory.                                   
   ___________________________________
  |                                   |
  |     VM1        VM2        VM3     | 
  |  _________  _________  _________  |
  |  |  APP  |  |  APP  |  |  APP  |  |
  |  |_______|  |_______|  |_______|  |
  |  |  Mac  |  | Linux |  |  Win  |  | 
  |  |_______|  |_______|  |_______|  |
  |  |2,2,100|  |2,4,200|  |2,2,   |  | When APP requires 4GB in VM3, we just have 2GB of RAM. 
  |__|_______|__|_______|__|_______|__| We cannot do that. We cannot allot it.
  |            hypervisor             | 
  |___________________________________|
  |             OS/kernel             | 
  |___________________________________| 
  |             Hardware              | (CPU, RAM, Memory:6 core, 8GB, 500GB)
  |___________________________________|

  whatever configuration we have alloted to this particular machine, so it's going to be fixed. And we cannot take it back. And we cannot use it for the host OS 

  It required much of configuration. If I'm not using it, so in that case, it's not going to be free. It will be fixed.
  </pre>

* (1:12:00) Docker -- providing the containers
  <pre>
  Docker -- container -- Advanced VM, Isolated Process
                             
              [single host]
   ___________________________________
  |                                   |
  |  container      "          "      | container -- lightweight -- portable
  |  _________  _________  _________  |
  |  |       |  |       |  |       |  |                   |
  |  |       |  |       |  |       |  |
  |  |  APP  |  |  APP  |  |  APP  |  | 
  |  |       |  |       |  |       |  |
  |  |_______|  |_______|  |_______|  |  
  |___________________________________| 
  |           docker engine           | 
  |___________________________________|
  |             OS/kernel             | 
  |___________________________________| 
  |             Hardware              | (CPU, RAM, Memory)
  |___________________________________|

  containers are not directly interacting with the hardware and they are not having their own OS. Directly they are connecting with the OS/kernel. they are taking every sort of configuration. This is dynamic also.

  We can launch as many as containers over here. 

  whatever they required for running inside like a container, so directly they are fetching from the Hub. "they are running it over here" means that they are fetching in the form of images. IMAGE is nothing a kind of package where there is some sort of instructions. they are directly running it inside the container. And once the process will be finished the container is going to be stopped. And the memory and all whatever configuration they are going to be used, they are going to be released from the particular HARDWARE.
  </pre>
  > lightweight: containers don't have their own OS. they are taking everything from the OS kernel.

* (1:20:27) Port mapping

  <pre>
  we cannot directly access this flask in our chrome -- directly in our host OS.
  Actually this chrome is running our host OS if we are going to access it, it won't be working. So over here what we have to do , we have to do the port mapping

  whenever we are running the container at that particular time only, we have to perform the port mapping means that whatever service you are running inside the container so this port of the container and the left hand side there will be a port of the host OS. this is the container and inside the container we are running the flask. the container is isolated process. So we cannot directly access this thing inside our host OS. 
  </pre>


## (1:28:40) Docker 

* installation [Install Docker Desktop on Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

* In Windows system, open a terminal: 
  > - run 
  ```bash
  docker
  docker ps
  docker images ## (for testing) 
  ```
  > - run 
  ```bash
  mkdir dockertest
  cd dockertest
  code . ## (open VSCode)
  ```
  <pre>
  執行 `docker images` 遇到 error during connect: This error may indicate that the docker daemon is...
  (1:35:35) 解決方式：開啟 Docker Desktop，用 docker/getting-started 啟動~
  </pre>

* In VS Code, open a terminal and select *Command Prompt*:
  > Lecture Demo 時，用了 Anaconda3 的 activate.bat 進入 '(base)' 模式

* 建立/完成 `app.py`，執行 `python app.py`，開啟 browser，輸入  localhost:5000。完成後，中斷 `app.py` 程序
  ```python
  from flask import Flask
  import numpy as np
  import pandas as pd

  app = Flask(__name__)

  @app.route("/",methods=["GET", "POST"])
  def home():
      return "Hello world"

  if __name__=="__main__":
      app.run(host="0.0.0.0",port=5000)
  ```

* (1:49:45) flow
  <pre>
  APP -> Docker file -> Docker image -> container
   |                                        ^
   |________________________________________| (flask--5000)
   |
   V
  5000
   |
  host os
               
            port mapping
       host port : container port
          5000           5000
  </pre>

* (1:53:20) Create a Docker file -- `Dockerfile`
  ```
  FROM python:3.8 # fetch the python from the Docker Hub

  COPY . /app # '.' means the local space, which means the entire code. # we'll be having one folder -- '/app'

  WORKDIR /app # setting this /app folder as our working directory

  RUN pip install -r requirements.txt

  CMD ["python","app.py"] # "python" is the interpreter. CMD means we're running this particular file -- app.py
  ```
  > "FROM" means that we are going to fetch that particular tool or that particular service from the Docker Hub.

* (1:58:20) 建立 `requirements.txt`
  ```
  flask
  pandas
  numpy
  ```
  

* (2:00:00) 方法一： Create Docker image: 執行  `docker build -t myhelloapp .` ('.' represents the local workspace)
  
* (2:02:45) 執行 `docker images` (檢視) -- we're going to run it inside the container.

* (2:04:00) 方法二：執行 `docker run -d -p 5000:5000 myhelloapp`, `docker ps` (檢視)
  <pre>
  The 2nd way where we can create an image from the container itself.

  The entire container we can convert into an image and then we can pass it to our next team. we can pass the image to the next team. we can also pass the container image to the next team.
  </pre>

* 開啟 browser，輸入  localhost:5000。注意，the localhost server is stopped. We are just running it through the container.

* `docker stop 影像編號` (根據 `docker ps`)。開啟 browser，輸入  localhost:5000，結果就是 nothing is coming.

* 執行 `docker run -d -p 8000:5000 myhelloapp`。開啟 browser，輸入  localhost:8000。


# Lecture 8 Note -- [DOCKER - Part 2 | MLOps Foundation](https://www.youtube.com/watch?v=wQdOTdM0eRo)

* In Windows system, open a terminal: 
  > ```bash
  > docker 
  > where docker
  > docker info
  > docker -v
  >
  > docker images
  > docker ps
  > docker ps -a
  > ```

* Agenda
  > 1. Docker image
  > 2. Image -> container (run image inside the container) -> detached mode
  > 3. Push -> Docker Hub
  > 4. Pull <- Docker Hub
  > 5. Container in interactive
  > 6. Image from the container
  > - compose
  > - network
  > - volume
  
* In VS Code, open a terminal: 執行 `python app.py`後，開啟 browser，輸入  localhost:5000。

* Lecture 用 `docker images` 查看已經有哪些image 在repository 中。已經有 *myhelloapp*，
  執行 `docker run -d -p 8000:5000 myhelloapp`後，開啟 browser，輸入  localhost:8000。

* (46:09) Docker image push
  > ```bash
  > docker build -t <imagename> .
  > docker login # 首次登入，需輸入 username 與 password
  > docker tag myhelloapp <docker帳號>/<repository名> or <image_name>
  > docker push <docker帳號>/<repository名> or <image_name> # push image 
  > ```

* (51:00) Checking in Docker Hub/Repository

* (57:51) Flow
  <pre>
  Dockerfile -> Docker image -> container
                    |
                    v
                  (push)
                    |
                    v
                Docker Hub -(pull)-> container    
  </pre>

* (1:00:07) Three ways for creating images
  <pre>
  1. Docker file -> image -> container
  2. Docker Hub -> image -> container (option -d or -i)
  3. image -> docker container (create image from the docker container itself)
  -d (detach mode) : In backend process basically your container is running. there's meaning of the detach mode.
  -i (interactive mode): so there you will find out a terminal you can directly interact with your container.
  </pre>

* (1:04:55) 執行 `docker pull redis` (pulling redis image from Docker Hub)
  <pre>
              (1) Docker engine   /_________________
                              ^   \                 |
  _first_                     |  ~first time~       | ~second time~  
                              |                     |
  Docker Hub  ____________\  container______________|
  (image)                 /  
  
  Inside the docker you'll find out one component that is called "Docker engine".

  If you are running this particular image first time (let's say) over the Docker Hub basically you have multiple images. (And let's say) you have an image of MySql. -- just taking an example -- you have an image of MySql over here, where, over Docker Hub. (Let's say) you want to run this particular image inside the container, which is in your local system (your local server). 

  Now see if you are running it first time (you're running this particular image first time) inside the container, so first it will find out inside the system [docker engine] itself. So first it will go to the docker engine it will check the image is available or not. If the image is not available then only in that case only it will fetch from the Docker Hub.

  if you want to run any sort of an image inside the container (let's say first time you are running it; you are running MySql image) see it is not having MySql image. First it will check [docker engine]  . If it is avilable then directly it will take it over here from here itself from the docker engine. But if it is not available then it will go to the Docker Hub and will try to pull from here.

  (let's say) it I'm running second time, then again, it will to to the Docker engine. this time the image is already available over here. The image is already available in my local server. so in that case it won't go to the Docker Hub directly. It will take an image from here [docker engine] itself.
  </pre>

* `docker images` (*redis* 已列在其中)

* `docker run -i -t redis /bin/sh` (-i -t: interactive mode for the terminal; /bin/sh: command)
  > 在 # 之後輸入 `ls` 或 `ls -a` 都沒有東西

* `docker run -it ubuntu /bin/sh`
  > 在 > 之後輸入 `ls` 可見到許多資料夾

* `docker run -it ubuntu /bin/bash`
  > 輸入  `ls`

* (1:15:15) 
  <pre>
  Inside the container actually,... Inside the Dockerfile you will find out that as a base image (we were using the python). Whatever we're writting with this "FROM", this is called the base image.The rest of resources basically is what it was taking from our host OS. The Docker engine was responsible for that.

  What I can do as a base image  (let's say) this is our system. As a base image from the Docker Hub,this is what is the Docker Hub. From the Docker Hub, we can keep or we can take the base OS image also. Let's say we're going to take a UBUNTU from the Hub itself. But we won't be having any OS inside the container. This is still true. It's not going to install the entire OS insdie the container. It's just going to take some utility file from the Hub itself.The rest of thing is going to be managed from here the host OS by using the Docker engine.
  </pre>

* (1:20:45) Take some another image from the Docker Hub
  <pre>
  this image is not available in our system. First it will go to the docker engine and it will search that this image is available or not into our local system. Now if it is not able to find it our then directly it will pull it from the Docker Hub itself. The 'container' is nothing our machine only.
  </pre>
  > 執行 `docker run -it kalilinux/kali-rolling /bin/sh`
  <pre>
  一開始會出現 Unable to find image 'kalilinux/kali-rolling:latest' locally
  然後顯示 latest: Pulling from kalilinux/kali-rolling
  最後出現 # 後就可以輸入 'ls', 'cd etc', 'ls', 'touch myfile.txt', 'exit'
  </pre>

* (1:27:54) interactive self with detach mode
  > there is two ways where we can execute our container so the first way is called 'detach mode' and the second way is called 'interactive mode'. \
  > 執行 `docker rmi -f jenkins/jenkins:lts` (移除 image，'lts' 是 TAG) \
  > 執行 `docker run -p 8080:8080 jenkins/jenkins:lts`
  <pre>
  顯示 Unable to find image 'jenkins/kenins:lts' locally
  然後顯示 lts: Pulling from jenkins/jenkins
  ...

  成功後，開啟 browser，輸入 localhost:8080，可以看到 jenkins 畫面 
  CTRL + C 停止服務
  </pre>

* (1:46:00) 
  > Inside our container we made some changes -- we've created "myfile.txt" \
  > `docker run --name sunnycontainer -it ubuntu /bin/bash` \
  > `ls`, `cd tmp`, `ls`, `touch myfile.txt`, `ls`, `exit` \
  > we can get a difference that what all thing we've changes over here inside the container. \
  > `docker diff sunnycontainer`
  <pre>顯示
  C /tmp
  A /tmp/myfile.txt
  C /root
  A /root/.bash_history
  
  說明
  'C' means where you went inside this TMP
  'A' means you appended this particular file
  </pre>
  > `docker commit synnycontainer updatedimage` (container名 與 image名) \
  > `docker images` (檢查 updatedimage 是否成功建立) 
  
* (1:57:40) Push IMAGE to Docker Hub & Pull it from there
  > We can use it and execute inside the container

* (1:58:33) In VSCode, only keep `Dockerfile`, renew the content (removing `app.py` & commands.txt). 建立檔案 `testfile` 
  <pre>
  FROM ubuntu
  WORKDIR /tmp
  RUN echo "Subscribe the ineuron intelligence"
  ENV myname sunny
  COPY testfile /tmp
  ADD test.tar.gz /tmp
  </pre>
  > 'ADD' : unzip the file from the local workspace from Internet or anywhere
  ```bash
  touch test # 建立 test 檔案
  tar -cvf test.tar test # 建立 test 的 tar 檔
  gzip test.tar # 建立 test.tar.gz 檔
  ```
  > 移除 test (不需要了)
  ```bash
  docker build -t newimage . # t: TAG, newimage: IMAGE NAME, '.': local workspace
  ```

* (2:10:10) In Windows CMD terminal, run `docker images` -- 顯示 newimage
  > 執行 `docker run -i -t --name newcontainer newimage /bin/bash` (顯示 'root@.../tmp#') \ 
  > 執行 `ls` (顯示 'test' 與 'testfile')

  * ENV 功能 -- In Windows CMD terminal, run `echo $myname` -- 顯示 sunny

# Lecture 9 Note -- [MLOps End to End Project](https://www.youtube.com/watch?v=G6frVmkVMr4)

* Github Resource：[Gemstone-Price-Prediction-End-to-End-Pipeline](https://github.com/sunnysavita10/Gemstone-Price-Prediction-End-to-End-Pipelin) 

* More details: [My Gemstone Github](https://github.com/henrykohl/Gemstone-Price-Prediction-End-to-End-Pipeline)

# 參考

* 參1: [MongoDB Basics | Tutorial 4: Create Atlas Cluster](https://www.youtube.com/watch?v=esKNjzDZItQ)

* 參2: [Simple documentation for setup.cfg](https://discuss.python.org/t/simple-documentation-for-setup-cfg/11465)
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


