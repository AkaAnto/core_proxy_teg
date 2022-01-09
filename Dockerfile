FROM oraclelinux:7-slim

RUN yum install -y gcc
RUN yum install -y postgresql-devel
RUN yum install -y unixODBC
RUN yum install -y unixODBC-devel
RUN yum install -y gcc-c++
# Install python and virtualenv
RUN yum install -y python36-devel
RUN yum install -y python36-setuptools
RUN easy_install-3.6 pip
RUN yum install -y nano

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

EXPOSE 5000

