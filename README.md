* Project decription 'My Price Check'

My Price check is web application that allows the client to get the best price of what he looks for
the application will give differents prices from the most famous websites like Amazon, ebay, Alibaba, ...
and will compare prices, display all prices and allows him to visit each link of product he want to choose.
- User enters the site and types the name of product he want
- After clicking search button, products from internationals websites with their prices
- In the front the client will also see the best price (lowest one)
- The client can choose the link that was given by the system and he even can choose the others links.

* [Technical section]

* How to start

- pip intall pipenv
- pipenv shell

- install django-static-sites in your python path or in your virtualenv path (pip install https://github.com/ciotto/django-static-sites/archive/master.zip)
- create an empty optimized project by django-static-admin startproject PROJECT_NAME command
- move to the PROJECT_NAME folder and create site by python manage.py startsite SITE_NAME command
- migrate python manage.py migrate
- deploy python manage.py deploy
- start server python manage.py runserver
enjoy it at http://127.0.0.1:8000

* Hosting
pip install gunicorn
pip install django-heroku
pip freeze > requirements.txt
# login to your heroku
heroku login
# create new app if one doesn't yet exist
heroku create
# create a new postgres database for your app 
heroku addons:create heroku-postgresql:hobby-dev
# heroku master
git push heroku master
# migrate your database to the heroku app
heroku run python manage.py migrate
# before you do this, make sure to add your SECRET_KEY to your env variables in your heroku app settings
git add.
git commit -m "Ready to heroku this sucker in the face."
git push heroku master
