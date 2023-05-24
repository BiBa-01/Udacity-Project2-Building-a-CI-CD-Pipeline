# Overview

This is my 2nd project for Udacity CloudDevOps Engineer Nanodegree. It is about deploying a Flask Machine Learning Application on Azure App Services. The application predicts house prices in Boston. 

## Project Plan


* A link to a [Trello](https://trello.com/invite/b/rdzy0Xtw/ATTIae0e869fbd6efc8db62c1ccb6d80fb22543769CF/project-2-building-a-ci-cd-pipeline) board for the project 


## Instructions

* Architectural Diagram 
* <img width="542" alt="image" src="https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/aaa5dc2e-f3d9-4d36-927f-31ef89b317d7">


Instructions for running the Python project:
* Clone this Report to your Azure Cloud shell: git clone git@github.com:BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline.git
<img width="761" alt="image" src="https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/c7a0e3d3-dee9-4f13-ab47-d263c33b922c">

* Create a virtual environment and source
```python
python3 -m venv ~/.flask-ml-azure

source ~/.flask-ml-azure/bin/activate
```
* Run
```
make install
```
<img width="612" alt="image" src="https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/45c58e45-1652-49aa-bbd5-0377e5f9773d">

* Passing test after running the 'make all' command from the 'Makefile'
<img width="548" alt="image" src="https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/636ae775-5d67-4cba-99b3-7d6db05b40ad">

* Successful build in GitHub

<img width="537" alt="image" src="https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/41087b24-c652-4bf0-8f9d-b3884a1d4e7a">


* Project running on Azure App Service
* Create App Service in Azure:
```
az webapp up -n <name>
```
<img width="480" alt="image" src="https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/c9843f8b-20ab-4113-9ce1-09245c4d8be6">

<img width="828" alt="image" src="https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/582c61af-29fe-4182-8e16-28506e347b31">



* Open Azure DevOps Organization
* Open a new project
* Create a service connections (settings)

<img width="501" alt="image" src="https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/71d80796-853e-4013-8f93-4a6c0d399def">

* Set up a pipeline linked to your GitHub Repo (Pipeline with using existing YAML File: azure-pipelines-for-self-hosted-agent.yml )


* Running Azure App Service from Azure Pipelines automatic deployment:
<img width="516" alt="image" src="https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/65467fc2-f4cc-406a-ab8b-94cd6221ce4f">



* Prediction from deployed flask app in Azure Cloud Shell:
For running the app script please change at the end of the make_predict_azure_app.sh file the "-X POST https://mywebappbb2.azurewebsites.net:$PORT/predict" to your own web app name.
Then run the script:
```
./make_predict_azure_app.sh
```

If it runs successfully it should show the following result:

![image](https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/3fb2c2be-0c58-4ba2-b429-4a9f987243f6)

By opening the folloing web address https://mywebappbb1.azurewebsites.net/ you should see the following:

![image](https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/863e0485-20b9-41b8-b6c6-4122ee7a7f29)

* Output of streamed log files from deployed application:
https://<app-name>.scm.azurewebsites.net/api/logs/docker

![image](https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/212ed9a5-6241-430a-bf82-9e0be7c575c4)

* Performing a loadtest with Locust:
 ```
  locust -f locustfile.py --headless -u 10 -r 5 -t 5s --web-port 8079
  ```
  ![image](https://github.com/BiBa-01/Udacity-Project2-Building-a-CI-CD-Pipeline/assets/78079178/600ee3a7-e483-46da-902b-4abea164778a)

 
> 

## Enhancements

For future enhancements it could be considered to use different GitHub branches for staging and production and to look for further automation possibilities.

## Demo 

[Link to Video<link Screencast on YouTube>](https://youtu.be/ZIe0ztoLUPk)


