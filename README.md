## Run local server


```bash
./manage.py runserver --settings=plasticjam_backend.settings._local
```
 or change wsgi.py and manage.py

I know that it's a bad practice to make local settings is public but it's a demo project.

First, run `migrate`

To add users and statistics from json files need to run `management` commands `addusers` and `addstatistics`


## Other

Overriden `CorsMiddleware`

Customized `Pagination`

Used [`generator`](https://github.com/m0nte-cr1st0/plasticjam_back/blob/master/apps/users/serializers.py#L81)

Wrote documentation using [`drf-yasg`](https://github.com/m0nte-cr1st0/plasticjam_back/blob/master/apps/users/views.py#L12)

## Heroku

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

Users list: [/api/v1/users/](https://plastickjambackend.herokuapp.com/api/v1/users/)

Detail statistic: [/api/v1/users/id/](https://plastickjambackend.herokuapp.com/api/v1/users/1/)
