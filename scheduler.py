#!/usr/bin/env python

from crontab import CronTab

cron = CronTab(user='jeff')
job = cron.new(command='python greeter.py')
job.minute.every(1)

cron.write()
