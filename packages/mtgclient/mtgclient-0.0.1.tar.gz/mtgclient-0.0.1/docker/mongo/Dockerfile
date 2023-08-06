FROM debian:11.5

RUN apt-get update &&  \
    apt-get install nano -y && \
    yes | apt-get install gnupg && \
    apt-get install -y curl && \
    echo 'deb http://repo.mongodb.org/apt/debian bullseye/mongodb-org/5.0 main' >>  \
    /etc/apt/sources.list.d/mongodb-org-5.0.list && \
    curl -sSL https://www.mongodb.org/static/pgp/server-5.0.asc  -o mongoserver.asc && \
    gpg --no-default-keyring --keyring ./mongo_key_temp.gpg --import ./mongoserver.asc && \
    gpg --no-default-keyring --keyring ./mongo_key_temp.gpg --export > ./mongoserver_key.gpg && \
    mv mongoserver_key.gpg /etc/apt/trusted.gpg.d/
RUN apt-get update && \
    apt-get install -y mongodb-org

# brew installing
RUN apt update && \
    apt install build-essential procps curl file git -y && \
    yes | /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && \
    eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

# Create core sertificate for setting TLS for MongoDB \

# Server sertificate

# Run MongoDb
CMD ['systemctl', 'start', 'mongod.service']
