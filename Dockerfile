FROM oraclelinux:7-slim

RUN yum -y update
RUN yum install -y gcc
RUN yum install -y postgresql-devel
RUN yum install -y oracle-softwarecollection-release-el7
RUN yum install -y gzip
RUN yum install -y tar
#RUN yum install -y make
#RUN yum install -y libffi-devel
#RUN yum install -y zlib
#RUN yum install -y bzip2-libs
#RUN yum install -y wget
#RUN yum install -y perl
RUN yum install -y make gcc perl-core pcre-devel wget zlib-devel
RUN yum -y install libffi-devel


## SSL
RUN wget https://ftp.openssl.org/source/openssl-1.1.1k.tar.gz
RUN tar -xzvf openssl-1.1.1k.tar.gz
WORKDIR openssl-1.1.1k
RUN ./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib no-shared zlib-dynamic
RUN make
RUN make install


# Install python and virtualenv
RUN wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz
RUN tar -xvzf Python-3.8.12.tgz
RUN sh Python-3.8.12/configure --enable-optimizations
RUN make altinstall
RUN curl https://packages.microsoft.com/config/rhel/8/mssql-server-2019.repo -o /etc/yum.repos.d/mssql-server-2019.repo
RUN curl https://packages.microsoft.com/config/rhel/8/prod.repo -o /etc/yum.repos.d/msprod.repo
RUN yum install -y nano
RUN export CLIENT_HOME=/usr/lib/oracle/21/client64
RUN export LD_LIBRARY_PATH=$CLIENT_HOME/lib
RUN PATH=$PATH:$HOME/bin:$CLIENT_HOME/bin
RUN export PATH

# SqlServer
#RUN yum install -y mssql-server
# Mysql
RUN yum install -y mariadb-devel
# Postgres
RUN yum install -y postgresql
# Oracle
RUN yum install -y  oracle-instantclient-release-el7
RUN yum install -y oracle-instantclient-basic
# DB2

# Set the working directory to /usr/src/app.
WORKDIR /usr/src/app
RUN python3.8 -m venv venv
RUN . venv/bin/activate

# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./

# Install requirements
RUN pip3.8 install --no-cache-dir -r requirements.txt

# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . .

EXPOSE 5000

