# Django + Vue = CRUD

![Vue Logo](/src/assets/logo-vue.png "Vue Logo")
![Django Logo](/src/assets/logo-django.png "Django Logo")

## Setup

```
$ git clone https://github.com/ggarber42/trabalho-vvs.git
$ cd django-vue-template
```

Setup
```
$ yarn install
$ pipenv install --dev && pipenv shell
$ python manage.py migrate
```

## Rodando o servidores de desenvolvimento

```
$ python manage.py runserver
```

Em outro terminal, mas no mesmo diretório

```
$ yarn serve
```

Vue: [`localhost:8080`](http://localhost:8080/)
Django: [`localhost:8000`](http://localhost:8000/).

## Fazendo o build da SPA

```
$ yarn build
```

## Executando Django + SPA

### Via Django

```
$ python manage.py runserver
```

### Via Docker

```
$ docker-compose up -d
```

## Rodando Testes

```
$ pipenv run python manage.py test
```