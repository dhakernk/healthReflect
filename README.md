Welcome to This Simple App.

This app requires Python and Django pip and  Git

For Linux Install git using:
sudo apt-get install git

For other OS download Git From here https://git-scm.com/downloads


First, update your local package index with apt, and then install the python-django package:

sudo apt-get update
sudo apt-get install python-django

#You can test that the installation was successful by

django-admin --version

O/p: 1.8.7

#First, we need to install the pip package manager. Refresh your apt package index:

sudo apt-get update

#Now you can install pip. If you plan on using Python version 2, install using the following commands:
sudo apt-get install python-pip

#Fast Approximate String Matching in a Dictionary, Used in Searching string 
#Install fuzzywazzy
pip install fuzzywuzzy


#You have installed all packages and Dependancies 

#Create a Directory healthReflect using Command:
mkdir healthReflect

#Change to Directory healthReflect
cd healthReflect

#Clone Code from git 
git clone git@github.com:dhakernk/healthReflect.git

#Project is Clone to local disk Apply migration 
python manage.py makemigrations
python manage.py migrate

#Hoooo.... ALL Set Run server Using Command:
python manage.py runserver 
