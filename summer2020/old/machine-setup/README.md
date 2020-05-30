# Machine Setup sp20-516-233 Holly Zhang

## Ubuntu 20.04



### Broker Setup
**Note**: The current setups are still being worked on. Currently the broker setup 
uses the Mosquitto broker, but this may be changed if websockets is not working 
correctly.

To setup the broker, first run `broker-setup-1.sh`.

After the shell script has run, go inside the config.mk file. Search for the 
line `WITH_WEBSOCKETS:=no`. Change the line so that it now displays 
`WITH_WEBSOCKETS:=yes`. Save the changes.

Then run `broker-setup-2.sh`.

### Client Setup

To setup the clients, run `client-setup.sh`.

