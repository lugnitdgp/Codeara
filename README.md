# Codeara
An Online Code Execution Platform using API



[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
<br>



[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-js.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com)


> This app is used to compile and execute the program with login feature. It also has sample problems and 
user's progress record.

##  Starting the Project 

* `mkdir CodeCompiler`

* `cd CodeCompiler`

* Creating a virtualenv with python and activate it
```
sudo apt install python3-venv

python3 -m venv <environment name>

source <environment name>/bin/activate
```

* `git clone https://github.com/lugnitdgp/Codeara.git`

* `cd Codeara`

* `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`

* `pip3 install -r requirements.txt`

* `cp .env.example .env`

* Run the Migrations
```
python3 manage.py makemigrations

python3 manage.py migrate

``` 
* Run the development server 
```
python3 manage.py runserver

```
* Head to server http://localhost:8000

* Add Few Questions in Question model to display random questions

## For Contribution

Read the <a href="CONTRIBUTING.md">CONTRIBUTING.md</a> to know how to contribute
1. Find an issue to resolve.
2. Comment on the issue.
3. Fork the repository
4. Make changes and push.
5. Make a pull request and wait for merging.



