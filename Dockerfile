FROM unoparty/unoparty-server-ethbase

MAINTAINER Counterparty Developers / Unoparty Developers <dev@unoparty.io>

## NOTE: Ethereum dependencies, serpent and solidity are already installed via the base image


# Install unoparty-lib
COPY . /unoparty-lib
WORKDIR /unoparty-lib
RUN pip3 install -r requirements.txt
RUN python3 setup.py develop
RUN python3 setup.py install_apsw
RUN python3 setup.py install_serpent

# Checkout test fixtures
RUN git submodule update --init

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
COPY docker/server.conf /root/.config/unoparty/server.conf
COPY docker/start.sh /usr/local/bin/start.sh
RUN chmod a+x /usr/local/bin/start.sh
WORKDIR /

# Pull the mainnet and testnet DB boostraps
RUN unoparty-server bootstrap --quiet
RUN unoparty-server --testnet bootstrap --quiet

EXPOSE 4000 14000

# NOTE: Defaults to running on mainnet, specify -e TESTNET=1 to start up on testnet
ENTRYPOINT ["start.sh"]

