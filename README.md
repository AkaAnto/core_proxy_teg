# core_proxy_teg
## Create MYSQL Database
0. export PATH=$PATH:/usr/local/mysql/bin, cp -r /usr/local/mysql/lib/* /usr/local/lib/
1. mysql
2. create database core_bancario;
3. use core_bancario;
4. python3 manage.py db init

## Migrate MYSQL Database
1. python3 manage.py db migrate
2. python3 manage.py db upgrade