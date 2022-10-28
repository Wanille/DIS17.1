# DIS17.1
***
### Installations
* clone this file by using `git clone 
* Open terminal
* use `cd` to navigate into this folder
* Install Elasticsearch with [these instructions](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/targz.html). But skip step *`Enable automatic creation of system indices`* 
* You should now have another folder in this one called elasticsearch-SOME_VERSION_NUMBER

create a virtual environment and activate:  
```
python3 -m venv .venv
source .venv/bin/activate`
```

Install Notebook requirements:
```
pip3 install jupyter-lab elasticsearch pandas
```
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
***

### On every startup
Open 2 terminals.  

On terminal 1 run:
```
source .venv/bin/activate
jupyter lab
``` 
On terminal 2 run:
```
cd elasticsearch-SOME_VERSION_NUMBER
./bin/elasticsearch
```