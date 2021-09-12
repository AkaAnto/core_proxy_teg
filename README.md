# core_proxy_teg

## .env file example
export APP_SETTINGS="config.DevelopmentConfig"
export SECRET_KEY="sins88Y7402ksm564aa11"
export USE_DATABASE="oracle"
export SQLALCHEMY_TRACK_MODIFICATIONS=False

## Postgres .env.postgres example
export DATABASE_URL="postgresql:///core_bancario"

## Mysql .env.mysql example
export DATABASE_URL="mysql://root:core_bancario@localhost/core_bancario"

## Oracle .env.oracle example
export DATABASE_URL="postgresql:///core_bancario"


## Mysql Notes
1. Install https://github.com/PyMySQL/mysqlclient
2. yum install python3-devel mysql-devel

## Postgres Notes
1. pip3 install psycopg2-binary

## Oracle Notes
1. https://yum.oracle.com/oracle-instant-client.html
2. https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html)
3. pip3 install cx-Oracle==8.2.1

## Database Management
0. Delete migrations folder
1. python3 manage.py db init
2. python3 manage.py db migrate
3. python3 manage.py db upgrade

### Fix para error psycopg2-binary
1. sudo apt-get install postgresql-server-dev-all
2. sudo apt-get install postgresql-common

### Fix para error de migrate/upgrade de oracle/postgress
1. Oracle remove unique constraint from primary keys
2. Postgress add unique constraint from primary keys