#!/bin/bash

process=application.py
if ps ax | grep -v grep | grep $process > /dev/null
then
    exit
else
	sudo python application.py > /dev/null 2>&1 &
fi