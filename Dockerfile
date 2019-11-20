# Using ubuntu image like a base

FROM ubuntu:16.04

# Installing python and requirements
RUN    apt-get update && apt-get -y install curl python python-pip vim \
python-tk && apt-get clean
RUN    apt-get -y install curl gnupg
RUN    curl -sL https://deb.nodesource.com/setup_11.x  | bash -
RUN    apt-get -y install nodejs
RUN    npm install
RUN    pip install --upgrade pip
RUN    mkdir -p /sma_genesys
RUN    mkdir -p ~/.pip/
COPY . /sma_genesys
RUN    pip install --no-cache-dir -r /sma_genesys/requirements.txt
RUN    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN    pip install requests


# Set the working directory
WORKDIR /sma_genesys
RUN npm install
RUN chmod +x /sma_genesys/run.sh
RUN chmod +x /sma_genesys/app/app.py

ENTRYPOINT ["/bin/bash","/sma_genesys/run.sh"]
