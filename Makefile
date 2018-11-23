#######################################################################
#
# SAFI MAKEFILE
#
#	This Makefile exposes various targets related to the compiling
#	and building of the `safi` application.
#
#######################################################################


clean:
	rm -rf var
	rm -rf .coverage.*
	rm -rf .coverage

env:
	virtualenv env
