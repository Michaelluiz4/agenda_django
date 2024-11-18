# iniciar projeto DJANGO
python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp contact

# configurar git
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

# Migrando a base de dados do Django
python manage.py makemigrations (esse aqui não é necessário usar porque já é criado por padrão, mas em caso de atualizar é preciso usar)
python manage.py migrate

# Criandoe modificando senha de um super usuário
python manage.py createsuperuser
python manage.py changepassword USERNAME  (alterar senha para caso esqueça a senha)