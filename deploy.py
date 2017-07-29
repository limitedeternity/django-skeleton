from subprocess import call

call('git add .')
print("enter your git commit comment: ")
comment = input()
call('git commit -am "%s"' % comment)
call('heroku maintenance:on')
call('git push heroku master')
call('heroku maintenance:off')
