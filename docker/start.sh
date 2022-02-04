#!/bin/bash

# Run "setup.py develop" if we need to (can be the case if the .egg-info paths get removed, or mounted over, e.g. fednode)
if [ ! -d /unoparty-lib/unoparty_lib.egg-info ]; then
    cd /unoparty-lib; python3 setup.py develop; cd /
fi
if [ ! -d /unoparty-cli/unoparty_cli.egg-info ]; then
    cd /unoparty-cli; python3 setup.py develop; cd /
fi

# Bootstrap if the database does not exist (do this here to handle cases
# where a volume is mounted over the share dir, like the fednode docker compose config does...)
# !!!!Will add this later once boostrap is uploaded to a server!!!!
# if [ ! -f /root/.local/share/unoparty/unoparty.db ]; then
#     echo "Downloading mainnet bootstrap DB..."
#     unoparty-server bootstrap --quiet
# fi
# if [ ! -f /root/.local/share/unoparty/unoparty.testnet.db ]; then
#     echo "Downloading testnet bootstrap DB..."
#     unoparty-server --testnet bootstrap --quiet
# fi

# Kick off the server, defaulting to the "start" subcommand
# Launch utilizing the SIGTERM/SIGINT propagation pattern from
# http://veithen.github.io/2014/11/16/sigterm-propagation.html
: ${PARAMS:=""}
: ${COMMAND:="start"}

trap 'kill -TERM $PID' TERM INT
/usr/local/bin/unoparty-server ${PARAMS} ${COMMAND} &
PID=$!
wait $PID
trap - TERM INT
wait $PID
EXIT_STATUS=$?
