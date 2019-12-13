PIP := pip install -r

PROJECT_NAME := viralize-app_new
PYTHON_VERSION := 3.6.7
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)


.pip:
	pip install pip --upgrade

setup-dev: .pip
	$(PIP) requirements.txt

db-up:
	DJANGO_READ_DOT_ENV_FILE=True python manage.py makemigrations
	DJANGO_READ_DOT_ENV_FILE=True python manage.py migrate

run:
	DJANGO_READ_DOT_ENV_FILE=True python manage.py runserver

delay:
	DJANGO_READ_DOT_ENV_FILE=True celery -A viralize worker -l info

celery:
	DJANGO_READ_DOT_ENV_FILE=True celery -A viralize beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

shell:
	DJANGO_READ_DOT_ENV_FILE=True python manage.py shell

createsuperuser:
	DJANGO_READ_DOT_ENV_FILE=True python manage.py createsuperuser

dump-prod:
	ENV=prod \
	ADMIN_ENABLED=active \
	CLOUDINARY_API_SECRET=fuIaeHoHDQ3Ji39ClzLoLtH8fjU \
	CLOUDINARY_KEY=516699214463717 \
	CLOUDINARY_NAME=doisgoldoclayson \
	DATABASE_URL=postgres://lqcyrgtszitjux:bbef650a4df93fdaab663db5d66eeae1e73df669d6d14f98a43ae3683ffbeeab@ec2-54-225-121-235.compute-1.amazonaws.com:5432/da7fvljmsvj7f9 \
	SENDGRID_PASSWORD=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 \
	SENDGRID_USERNAME=apikey \
	BUCKET_NAME='viralize-images' \
	AWS_ACCESS_KEY='AKIAXFEZ45QRXSC5CTGQ' \
	AWS_SECRET_KEY_ID='uOt3Q8StN3l9UtzWSwGQ8iDVxsUZaorNvjZKgeQA' \
	REGION='sa-east-1' \
	python manage.py dumpdata > db.json

load-local:
	DJANGO_READ_DOT_ENV_FILE=True python manage.py loaddata db.json

git-up:
	git pull
	git fetch -p --all

.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv

all: create-venv setup-dev #git-up

front:
	yarn build