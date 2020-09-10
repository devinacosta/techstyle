#!/bin/bash
LOG=/var/log/sysload.log
LOADAVG=$(cat /proc/loadavg |tr -s ' '|cut -d ' ' -f1,2)
echo "$(date) LA1: $(echo $LOADAVG|cut -d ' ' -f1) LA5: $(echo $LOADAVG|cut -d ' ' -f2)  " >> $LOG
