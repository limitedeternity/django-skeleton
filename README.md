
Django skeleton, that I use in my projects. Ready for deployment to Heroku.

-----------

How to:
====================

*Login to Heroku:*

- "heroku login"

*Initialize git repo:*

- "git init"

*Bind git repo to your Heroku application:*

- "heroku git:remote -a <your_app>"

*Configure application's parameters:*

- "python configure_env.py"

*Set your herokuapp url in settings/base/env.py*

*Now do your stuff. When completed, deploy:*

- "python deploy.py"
