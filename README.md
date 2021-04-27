# Zuri Django Blog

Zuri Django Blog is a blog application written using django on the backend. It is a blog that allows users to post articles, read and comment on articles. Users can signup, login, logout, reset password etc.

## Installation

Clone the django directory to your local folder


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the requirements using the command below:

```bash
pip install requirements.txt
```

## Usage

After installing all requirements, make migrations and then migrate all files with the commands below
```bash
python manage.py makemigrations
python manage.py migrate
```
You can then create superuser using the command and enter the details as prompted:
```bash
python manage.py createsuperuser
```
Make sure to update ```DEBUG=True``` in the settings.py file IF you need to see the errors you get when running the application on your local server.

To run the application on your local server, use the command: ```python manage.py runserver```

Voila! You're ready to use the application. Enjoy!


Don't forget to thank [TheZuriTeam](https://twitter.com/theZuriTeam) by following them on Twitter!
You can follow [me](https://twitter.com/oluwa_teeblaq) too. T for Thanks!

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
