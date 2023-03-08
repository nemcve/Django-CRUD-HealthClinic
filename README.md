# Django-CRUD-HealthClinic
With this app, you can fully manage a health clinic website. Made with Python in Django Framework, PostgreSQL, HTML, CSS and Bootstrap.
<h2>Key features :</h2>
<ul>
  <li>User registration</li>
  <li>User login</li>
  <li>Admin user authorized pages</li>
  <li>Display all available doctors</li>
  <li>Display all patients</li>
  <li>Display all scheduled appointments</li>
  <li>Appointment search by patient's JMBG</li>
  <li>Appointment deletion</li>
  <li>Appointment editing</li>
  <li>Appointment scheduling</li>
  <li>Appointments printing</li>
  <li>Doctors deletion</li>
  <li>Doctors editing</li>
  <li>Doctors adding</li>
  <li>Doctors printing</li>
  <li>Patients deletion</li>
  <li>Patients editing</li>
  <li>Patients adding</li>
  <li>Patients printing</li>
</ul>
<br>

To get it running on your local machine, run the commands below in your terminal :
<br>

``` 1. $ git clone https://github.com/nemcve/Django-CRUD-HealthClinic.git ``` 
<br> 

``` 2. $ cd Django-CRUD-HealthClinic ```
<br>

``` 3. $ docker build -t djangoapp ```
<br>

``` 4. $ docker run -p 8000:8000 djangoapp ```
<br>

``` 5. Open your browser and navigate to http://127.0.0.1:8000/ ```
<br>

``` Admin login username: admin, password: admin ```
<br>
<br>
If you want to create a new admin user :

```$ cd Django-CRUD-HealthClinic/HealthClinic/
<br>

```$ python manage.py createsuperuser, and follow the prompts```
<br>

To access the Django admin control panel and manage users and user groups, in your browser's url field, add /admin. Like this :

``` https://127.0.0.1:8000/admin ```


