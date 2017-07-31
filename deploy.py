from subprocess import call

call('git add .', shell=True)
print("enter your git commit comment: ")
comment = input()
call('git commit -am "%s"' % comment, shell=True)
call('heroku maintenance:on', shell=True)
call('git push heroku master', shell=True)
call('heroku maintenance:off', shell=True)
