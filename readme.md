# Profiles REST API

Profiles RESAT API Code

- Setup up Vagrant development server

`` vagrant init ubuntu/bionic64 ``

- above command will initialise our project with the new vigrant file

``vagrant up // to start the vagrant server for our project  ``

``vagrant ssh   // to connect to the vagrant server ``
- By default local system file is not sync on our development virtual server and as we know our code is on local server and vagrant work by creating a synchronised directory on our vagrant server.


`` cd /vagrant   // this command will show you all local file which is on server``  

- Now how we can create a python virtual environment so we can install all the dependencies such as python and the django rest framework
- we will create virtual environment on the vagrant server
`` python -m venv ~/env //this will create new virtual environment for our project `` 
- above is the set of files and this is the dir where it installs all the dependencies when we install them with the Python package manager
- we need to activate and deactivate the virtual environment. So when you activate on virtual environment then all of the dependencies that you run in the Python application will be pulled from the virtual environment instead of the base os

``source ~/env/bin/activate // this will activate the python environment`` 

``deactivate // to deactivate the virtual environment`` 
- In the we are using to packages 
    1. Django
    2. Django Rest Framework

- to manage all the dependencies we will use requirment.txt and we will put all the packages in it and the to install type the command 

``pip install -r requirements.txt // this will install all the packages ``

- Now after setting up our environment we can create the project 

``django-admin.py startproject project_name . ``

- . is specifying the path where we want to create the project dir
> Inside the Django project we can create different applications i.e. one project can consist of one or more sub applications within the in projects.

``python manage.py startapp profiles_api`` 
- TO run and test our application type below command

``python manage.py runserver 0.0.0.0:8000``

``python manage.py makemigrations app_name`` // to create a migration file using Django cli

`` python manage.py migrate`` //this will run all the migrations in our projects 

- to access the admin panel http://127.0.0.1:8000/admin/ type superuser cred 

- We have added serializer to a view which allows us (it is the features from the django rest framework) to easily convert data input into Python objects and vice versa its kind a similar to the django form. 

- Django Rest Framework offers two classes that helps us to write the logic for our API i.Ae 
    1. APIView - [doc link](https://www.django-rest-framework.org/api-guide/views/)
    2. ViewSet - [doc link](https://www.django-rest-framework.org/api-guide/viewsets/)
    
- We can restrict the user to update and delete his own profile and we can do that using Django Permission Class 

``chmod +x deploy/*.sh`` 

``curl -sL https://raw.githubusercontent.com/nishantml/profiles-rest-api/master/deploy/setup.sh | sudo bash -`` // to setup our server on aws

- Now go to setting.py which is in your project and search for ALLOWED_HOSTS this is the setting which enables access via
 specific domain name its security features to make sure that if somebody just finds a random IP address for our server
  they can't access the application unless they use a valid hostname.
