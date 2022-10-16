FROM oraclelinux:7-slim

RUN yum install -y gcc
RUN yum install -y postgresql-devel
# Install python and virtualenv
RUN yum install -y python36-devel
RUN yum install -y python36-setuptools  # install easy_install-3.4
RUN easy_install-3.6 pip
RUN curl https://packages.microsoft.com/config/rhel/8/mssql-server-2019.repo -o /etc/yum.repos.d/mssql-server-2019.repo
RUN curl https://packages.microsoft.com/config/rhel/8/prod.repo -o /etc/yum.repos.d/msprod.repo
RUN yum install -y nano
RUN export CLIENT_HOME=/usr/lib/oracle/21/client64
RUN export LD_LIBRARY_PATH=$CLIENT_HOME/lib
RUN PATH=$PATH:$HOME/bin:$CLIENT_HOME/bin
RUN export PATH

# SqlServer
RUN yum install -y mssql-server
# Mysql
RUN yum install -y mariadb-devel
# Postgres
RUN yum install -y postgresql
# Oracle
RUN yum install -y  oracle-instantclient-release-el7
RUN yum install -y oracle-instantclient-basic
# Set the working directory to /usr/src/app.
WORKDIR /usr/src/app
RUN python3 -m venv venv
RUN . venv/bin/activate

# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . .

RUN python3 manage.py db init
RUN python3 manage.py db migrate
RUN python3 manage.py db upgrade

EXPOSE 5000
CMD ["python3", "main.py"]

