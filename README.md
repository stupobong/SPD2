# SPD2
ACAS Project Files - source code 

#I'm currently running a debian bash machine hosted in the virtualbox from my computer with a given static IP address of 192.168.1.2 on Ports 8000. To work on the project, I run the visual studio code with a connection to host (192.168.1.2) as admin user with the admin password. As for the backend database, I work on MySQL Workbench and django admin panel (192.168.1.2/admin) for the time being. 

#This is how I get it started
With Debian already running, I first 
1. install the package "#apt-get install python3-venv"
2. create directory "#mkdir djangoenv"
3. Activate Virtual Environment "#source djangoenv/bin/activate"
4. Install Django "#pip install django"
5. Create a project "#django-admin startproject acas"
6. Create an app in the project "#python manage.py startapp caisam"
7. Make migrations "#python manage.py makemigrations"
8. Do migrate "#python manage.py migrate"
9. Run the server "python manage.py runserver"
#These are how I get it all started

#Then come the advance part, we need some time to work between the running debian server and my currently Windows 10, so witht the help of Visual Studio Code Host connection i was able to connect using IP address, ports, and user admin/password for this connection to happen.

MORE UPDATES are COMING!
