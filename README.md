# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/CodeAkio/eventex.svg?branch=master)](https://travis-ci.org/CodeAkio/eventex)
[![Maintainability](https://api.codeclimate.com/v1/badges/702d683ae2243ffc329a/maintainability)](https://codeclimate.com/github/CodeAkio/eventex/maintainability)

## Como desenvolver?

1. Clone o repositório;
2. Crie um virtualenv com Python 3.5;
3. Ative o seu virtualenv;
4. Instale as dependências;
5. Configure a instância com o .env;
6. Execute os testes.

```console
git clone https://github.com/CodeAkio/eventex.git eventex
cd eventex
python -m venv .eventex
source .eventex/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```


## Como fazer o deploy?

1. Crie uma instância no Heroku;
2. Envie as configurações para o Heroku;
3. Defina uma SECRET_KEY segura para a instância;
4. Defina DEBUG=False;
5. Configure o serviço de e-mail;
6. Envie o código para o Heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# Configura o email
git push heroku master --force
```