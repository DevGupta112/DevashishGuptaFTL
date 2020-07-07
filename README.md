# DevashishGupta_FTL_Assignment
### Description- Using Django Rest framework to create an API in order to display dummy data added using Management commands in the form of Json.

#### Output:
![2020-07-07 (15)](https://user-images.githubusercontent.com/54732775/86751919-9f475d80-c05c-11ea-8947-df8268c2255c.png)

![2020-07-07 (16)](https://user-images.githubusercontent.com/54732775/86751993-ad957980-c05c-11ea-8a93-825c69576856.png)

### Technologies and Packages Used:
    Language- Python
    Framework- Django Rest Framework
    IDE- Intellij IDEA
    Packages- Django, djangorestframework
    Database- Sqlite3
    Server- WSGI
    
### Installation:
    Django: pip install django
    To create a django project: "django-admin startproject Json ."
    To create an app: "python manage.py startapp JsonAssignment"
    
### Insights of the Process:
    Django REST framework is a powerful and flexible toolkit for building Web APIs. Therefore it was wise to use the underscored 
    framework.
#### Step 1: Creating Data Models in Models.py and registering the models in admin.py
    To demonstrate the API, we used 2 data models named User(uid, real_name, tz(location)) and Activity Period(start_time, end_time). 
    We initialized both models with Primary Keys and Foreign key to improve connectivity and reduce redundancy.
    
![2020-07-06 (2)](https://user-images.githubusercontent.com/54732775/86591019-5b961a80-bfae-11ea-83d4-b3d2769ec5b1.png)

![2020-07-07 (2)](https://user-images.githubusercontent.com/54732775/86731746-72d81500-c04d-11ea-9378-eb1bd562ae29.png)

#### Step 2: Using Management commands to add dummy data for use.

![2020-07-07 (1)](https://user-images.githubusercontent.com/54732775/86715227-a317b780-c03d-11ea-9fb0-22fc2a9229b2.png)

    In order to register command into manage.py, we first need to add "management" directory in our app, and also create a subdirectory
    named "commands". Inside that subdirectory we add "createactivity.py". Following the django documentation for management commands,
    we define a method called "handle" that actually executes the command. Inside the method we create instances of both user and 
    ActivityPeriod models and save them to the database.
    
    In order to save the data from the commands, we need to use "manage.py".
##### Command: python manage.py createactivity

![2020-07-07](https://user-images.githubusercontent.com/54732775/86730449-2b04be00-c04c-11ea-9268-6901ea511fff.png)


#### Step 3: Updating settings.py file.
    We need to install rest_framework in order to create API. 
    Command: pip install djangorestframework

![2020-07-07 (3)](https://user-images.githubusercontent.com/54732775/86734864-f561d400-c04f-11ea-9233-1852d2af0a1d.png)

#### Step 4: Creating serializers.py
     To set up a DJA web service, first we need to create “serializers”, which translate models to their end-user-facing format. 
     So we create JsonAssignment/serializers.py file. The fields values we provided mean that those fields will be exposed to the end user.
     Passing __all__ in the fields will include all the attributes of the models.

![2020-07-07 (4)](https://user-images.githubusercontent.com/54732775/86738660-e2043800-c052-11ea-927f-3cac198e1405.png)

     In order to connect those two models, we create activity instance in user as well with argument "MANY= TRUE".
 
#### Step 5: Defining views for each model in views.py
      Using rest_framework's viewsets, we define respective classes for both models.
      
![2020-07-07 (6)](https://user-images.githubusercontent.com/54732775/86744750-740e3f80-c057-11ea-8948-19beb97b6951.png)

#### Step 6: Defining urls for navigation
      Using rest_framework we use "DefaultRouter" to create and register the urls for the project.
![2020-07-07 (7)](https://user-images.githubusercontent.com/54732775/86745479-0282c100-c058-11ea-8a77-fb7d7252aa82.png)




