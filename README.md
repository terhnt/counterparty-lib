[![Build Status Travis](https://travis-ci.org/terhnt/unoparty-lib.svg?branch=develop)](https://travis-ci.org/terhnt/unoparty-lib)
[![Build Status Circle](https://circleci.com/gh/terhnt/unoparty-lib.svg?&style=shield)](https://circleci.com/gh/terhnt/unoparty-lib)
[![Coverage Status](https://coveralls.io/repos/terhnt/unoparty-lib/badge.png?branch=develop)](https://coveralls.io/r/terhnt/unoparty-lib?branch=develop)
[![Latest Version](https://pypip.in/version/unoparty-lib/badge.svg)](https://pypi.python.org/pypi/unoparty-lib/)
[![License](https://pypip.in/license/unoparty-lib/badge.svg)](https://pypi.python.org/pypi/unoparty-lib/)
[![Slack Status](http://slack.unoparty.io/badge.svg)](http://slack.unoparty.io)
[![Docker Pulls](https://img.shields.io/docker/pulls/unoparty/unoparty-server.svg?maxAge=2592000)](https://hub.docker.com/r/unoparty/unoparty-server/)


# Description
`unoparty-lib` is the reference implementation of the [Unoparty Protocol](https://unoparty.io).

**Note:** for the command-line interface to `unoparty-lib`, see [`unoparty-cli`](https://github.com/terhnt/unoparty-cli).


# Installation

For a simple Docker-based install of the Unoparty software stack, see [this guide](http://unoparty.io/docs/federated_node/).


# Manual installation

Download the newest [patched Unobtanium Core](https://github.com/unobtanium-official/unobtanium/releases) and create
a `unobtanium.conf` file with the following options:

```
rpcuser=unobtaniumrpc
rpcpassword=rpc
server=1
txindex=1
addrindex=1
rpcthreads=100
rpctimeout=300
```

Then, download and install `unoparty-lib`:

```
$ git clone https://github.com/terhnt/unoparty-lib.git
$ cd unoparty-lib
$ sudo pip3 install --upgrade -r requirements.txt
$ sudo python3 setup.py install
```

Followed by `unoparty-cli`:

```
$ git clone https://github.com/terhnt/unoparty-cli.git
$ cd unoparty-cli
$ sudo pip3 install --upgrade -r requirements.txt
$ sudo python3 setup.py install
```

Then, launch the daemon via:

```
$ unoparty-server bootstrap
$ unoparty-server --backend-password=rpc start
```

# Basic Usage

## Via command-line

(Requires `unoparty-cli` to be installed.)

* The first time you run the server, you may bootstrap the local database with:
	`$ unoparty-server bootstrap`

* Start the server with:
	`$ unoparty-server start`

* Check the status of the server with:
	`$ unoparty-client getinfo`

* For additional command-line arguments and options:
	`$ unoparty-server --help`
	`$ unoparty-client --help`

## Via Python

Bare usage from Python is also possible, without installing `unoparty-cli`:

```
$ python3
>>> from unopartylib import server
>>> db = server.initialise(<options>)
>>> server.start_all(db)
```

# Configuration and Operation

The paths to the **configuration** files, **log** files and **database** files are printed to the screen when starting the server in ‘verbose’ mode:
	`$ unoparty-server --verbose start`

By default, the **configuration files** are named `server.conf` and `client.conf` and located in the following directories:

* Linux: `~/.config/unoparty/`
* Windows: `%APPDATA%\Unoparty\`

Client and Server log files are named `unoparty.client.[testnet.]log` and `unoparty.server.[testnet.]log`, and located in the following directories:

* Linux: `~/.cache/unoparty/log/`
* Windows: `%APPDATA%\Local\Unoparty\unoparty\Logs`

Unoparty API activity is logged in `server.[testnet.]api.log` and `client.[testnet.]api.log`.

Unoparty database files are by default named `unoparty.[testnet.]db` and located in the following directories:

* Linux: `~/.local/share/unoparty`
* Windows: `%APPDATA%\Roaming\Unoparty\unoparty`

## Configuration File Format

Manual configuration is not necessary for most use cases.

A `unoparty-server` configuration file looks like this:

	[Default]
	backend-name = addrindex
	backend-user = <user>
	backend-password = <password>
	rpc-host = 0.0.0.0
	rpc-user = <rpcuser>
	rpc-password = <rpcpassword>

A `unoparty-client` configuration file looks like this:

	[Default]
	wallet-name = unobtaniumcore
	wallet-connect = localhost
	wallet-user = <user>
	wallet-password = <password>
	unoparty-rpc-connect = localhost
	unoparty-rpc-user = <rpcuser>
	unoparty-rpc-password = <password>


# Developer notes

## Versioning

* Major version changes require a full (automatic) rebuild of the database.
* Minor version changes require a(n automatic) database reparse.
* All protocol changes are retroactive on testnet.

## Continuous integration
 - TravisCI is setup to run all tests with 1 command and generate a coverage report and let `python-coveralls` parse and upload it.
   It does runs with `--skiptestbook=all` so it will not do the reparsing of the bootstrap files.
 - CircleCI is setup to split the tests as much as possible to make it easier to read the error reports.
   It also runs the `integration_test.test_book` tests, which reparse the bootstrap files.


# Further Reading

* [Official Project Documentation](http://unoparty.io/docs/)
