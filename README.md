# DIS17.1
***
### Installations
* clone this file by using `git clone https://github.com/Wanille/DIS17.1.git`
* Open terminal
* use `cd` to navigate into this folder
* Install Elasticsearch with [these instructions](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/targz.html). But skip step *`Enable automatic creation of system indices`* 
* You should now have another folder in this one called elasticsearch-SOME_VERSION_NUMBER

create a virtual environment and activate:  
```
python3 -m venv .elastic_env
source .elastic_env/bin/activate
```

Install Notebook requirements:
```
pip install jupyter elasticsearch pandas
```

Add environment to jupyter:
```
python -m ipykernel install --user --name=.elastic_env
```
If you want to learn more about virtual environments read [this](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).
***
### On first startup
To stop elastic from displaying warnings follow these steps:
* Create a user and password via [this tutorial](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/security-minimal-setup.html).
* Copy password from tutorial for user *elastic*
* The elasticsearch.yml file should be located under *elasticseach-SOME_VERSION_NUMBER/config/elasticsearch.yml*
* Then create a file called *credentials.py* in base folder *DIS17.1*
* Add this template to the file:

```
username = "elastic"
password = "YOUR_PASSWORD_HERE"
```

* open terminal
* run `jupyter lab`
* Go to Kernel > Change Kernel
* Select .elastic_env
* start elasticsearch by opening another terminal navigating into your elasticsearch-SOME_VERSION_NUMBER folder and run `./bin/elasticsearch`
* Now run the [Test Notebook](./Test.ipynb)
***

### On every startup
Open 2 terminals and navigate into this folder.

On terminal 1 run:
```
jupyter lab
```

On terminal 2 run:
```
cd elasticsearch-SOME_VERSION_NUMBER
./bin/elasticsearch
```
