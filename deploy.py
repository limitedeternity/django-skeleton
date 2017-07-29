# -*- coding: utf-8 -*-
import subprocess


def exec_com(command):
    command_list = command.split(" ")
    return subprocess.call(' '.join(command_list), shell=True)

exec_com('git add .')
print("enter your git commit comment: ")
comment = input()
exec_com('git commit -am "%s"' % comment)
exec_com('heroku maintenance:on')
exec_com('git push heroku master')
exec_com('heroku maintenance:off')
