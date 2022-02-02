FROM ubuntu:18.04

#MAINTAINER Unoparty Developers <dev@.io>

# Install common dependencies
RUN apt-get update && apt-get install -y apt-utils ca-certificates wget curl git mercurial \
    python3 python3-dev python3-pip python3-setuptools python3-appdirs \
    build-essential vim unzip software-properties-common sudo gettext-base \
    net-tools iputils-ping telnet lynx locales

# Upgrade pip3 to newest
RUN pip3 install --upgrade pip

# Set locale
RUN dpkg-reconfigure -f noninteractive locales && \
    locale-gen en_US.UTF-8 && \
    /usr/sbin/update-locale LANG=en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Set home dir env variable
ENV HOME /root

# Install python-bitcoinlib
ARG BITLIB_BRANCH=master
ENV BITLIB_BRANCH ${BITLIB_BRANCH}
RUN git clone -b ${BITLIB_BRANCH} https://github.com/terhnt/python-bitcoinlib.git /python-bitcoinlib
WORKDIR /python-bitcoinlib
RUN python3 setup.py install

# Install python-altcoinlib
ARG ALTLIB_BRANCH=main
ENV ALTLIB_BRANCH ${ALTLIB_BRANCH}
RUN git clone -b ${ALTLIB_BRANCH} https://github.com/terhnt/python-altcoinlib.git /python-altcoinlib
WORKDIR /python-altcoinlib
RUN python3 setup.py install

# Install unoparty-lib
COPY . /unoparty-lib
WORKDIR /unoparty-lib
RUN pip3 install -r requirements.txt
RUN python3 setup.py develop
RUN python3 setup.py install_apsw

# Install unoparty-cli
# NOTE: By default, check out the unoparty-cli master branch. You can override the BRANCH build arg for a different
# branch (as you should check out the same branch as what you have with unoparty-lib, or a compatible one)
# NOTE2: In the future, unoparty-lib and unoparty-cli will go back to being one repo...
ARG CLI_BRANCH=master
ENV CLI_BRANCH ${CLI_BRANCH}
RUN git clone -b ${CLI_BRANCH} https://github.com/terhnt/unoparty-cli.git /unoparty-cli
WORKDIR /unoparty-cli
RUN pip3 install -r requirements.txt
RUN python3 setup.py develop

# Additional setup
COPY docker/server.conf /root/.config/server.conf
COPY docker/start.sh /usr/local/bin/start.sh
RUN chmod a+x /usr/local/bin/start.sh
WORKDIR /

EXPOSE 4000 14000

# NOTE: Defaults to running on mainnet, specify -e TESTNET=1 to start up on testnet
ENTRYPOINT ["start.sh"]
