#!/bin/bash


#check and see if sqlite3 is installed
#if not
[ -x /usr/bin/sqlite3 ] && sqlite3 app.sqlite || echo "try installing sqlite3 by doing 'sudo apt-get install sqlite3 libsqlite3-dev'"
