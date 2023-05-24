# Overview

This is my 2nd project for Udacity CloudDevOps Engineer Nanodegree. It is about deploying a Flask Machine Learning Application on Azure App Services. The application predicts house prices in Boston. 

## Project Plan
<TODO: Project Plan

* A link to a [Trello](https://trello.com/invite/b/rdzy0Xtw/ATTIae0e869fbd6efc8db62c1ccb6d80fb22543769CF/project-2-building-a-ci-cd-pipeline) board for the project 
* A link to a spreadsheet that includes the original and final project plan>

## Instructions

* Architectural Diagram 
* <img width="542" alt="image" src="https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/aaa5dc2e-f3d9-4d36-927f-31ef89b317d7">


Instructions for running the Python project:
* Clone this Report to your Azure Cloud shell: git clone git@github.com:BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline.git

* Create a virtual environment
```python
python3 -m venv ~/.myrepo
```
* Activate the virtual environment:
```

source ~/.myrepo/bin/activate
* ```
* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


