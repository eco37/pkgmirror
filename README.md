# pkgmirror
A FreeBSD pkg repo mirror tool thats scrapes a freebsd repo webpage and stores it localy to easier setup a local repo.

Tested on Ubuntu 18.04

## Dependencies
* Python 2.7
* python-requests

### Ubuntu Install Dependencies
<pre>sudo apt-get install python python-requests</pre>

## Setup
* Install a webserver with the ABI directories in the root, eg. FreeBSD:12:amd64
* DNS needs to be pointed with a wildcard for *.freebsd.org to the local repo web server
* Need to run a pkg update on all FreeBSD hosts that are affected

## FreeBSD Default domains if a waildcard cant be used
* pkg.freebsd.org
* pkgmir.geo.freebsd.org
* pkg0.isc.freebsd.org
* pkg0.nyi.freebsd.org
