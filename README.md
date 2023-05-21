# Udacity-Project2-Building-a-CI-CD-Pipeline
Building a CI/CD Pipeline to perform continuous delivery for a Python-based machine learning application using the Flask web framework

## Overview
The project is to perform continuous delivery for a python-based machine learning application using the Flask web framework which performs predictions of house prices. It shows the use of CI/CD capablilities to automated deployments of applications in serverles environments by use of the follwoing technologies:
- GitHUB
- GitHUB Actions (CI)
- Agile Boards (Trello)
- Azure Cloud Shell
- Azure DevOps
- Pipelines (CD)
- Flask Web Framework

## Steps to do:
1. Set up of GitHub Repo
2. Launch an Azure Cloud Shell, creation of ssh keys (ssh-keygen -t rsa) and upload of keys to this Repo.
3. Creation of a Makefile. With the Makefile shortcuts to build, test, and deploy a project are created.
4. Creation of a requirements.txt. This file includes the required packages for automated installation.
5. Creation of virtual environment: 
A Python virtual environment gives the ability to isolate the Python development projects from the system installed Python and other Python environments. This gives full control of the project and makes it easily reproducible
          python3 -m venv ~/.myrepo
          source ~/.myrepo/bin/activate
6. Script and Test file for Continous Integration:
          hello.py
          test_hello.py
7. Clone GitHub Repo to Azure Cloud Shell
8. Run make all to install, lint and test code 
9. Configure GitHub Actions. Git Hub Actions will test project upon change events in GitHub. This is necessary to perform Continuous Integration remotely. The push change to GitHuB triggers the GitHub Actions Container, which in turns runs a service of commands.
          Creation of pythonapp.yml and check first successful run
11. Continuous Delivery
          Set up Azure Pipeline and deploy the Flask starter code (provided from Udacity: C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn)
          Fork the repository C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn and clone it to your machine and copy the starter files to the new repository
          
13. Set up Azure Pipelines:
If not already done, ensure to enable Azure Pipelines in GitHub.
15. Making Predictions:

15. xxx

