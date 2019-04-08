# Django Rest Task List

Simple tasklist with single user authentication.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisites

Have a Docker up and running.
Clone the repository:

```
git clone https://github.com/lfniederauer/django-rest-task-list.git
```

### Installing and Running

With the terminal, access the local folder you cloned into. The root contains the Dockerfile and alike. Then run:

```
docker-compose up -d
```

The flag ```-d``` let you return to the terminal.
Make sure you´re running a tty terminal, could be unix bash or powershell on Windows:

```
docker exec -it django-admin bash
```
Let´s make migrations and create the superuser:

```
$ django-admin makemigrations
$ django-admin migrate
$ django-admin createsuperuser
```

Now access via browser:
```
http://localhost:3000
```

That is it!

## Authors

*  [Luis Filipe Niederauer](https://servicos.pro)

## License

This project is licensed under the MIT License.

## Acknowledgments

“Scientists study the world as it is; engineers create the world that has never been.”

― Theodore von Karman


 “The world would be a better place if more engineers, like me, hated technology. The stuff I design, if I’m successful, nobody will ever notice. Things will just work, and be self-managing.”

― Radia Pearlman
