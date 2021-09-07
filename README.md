A script to check for [Enchantments permits](https://www.recreation.gov/permits/233273). 

To build and run locally, run `make build-local && make run-local`.

To build and run the Docker image, use the `*-image` make commands. The docker image can be used for a lambda to run this in AWS.

The twitter notification functionality is iffy and not currently used in the main script, but the code to either create a tweet or send a DM is in [src/notify.py](./src/notify.py). I was using it to send a DM, which probably triggered some sort of spam detection since it was messaging every 5 minutes and got my app banned. Perhaps using the tweet functionality rather than DM would be more successful.
