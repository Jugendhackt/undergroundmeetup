# Underground Meetup

You want to meet your friends, but can't figure out where?
No problem, Underground Meetup is here to help.

By using the nearest Metro stations, it finds the nearest
location for all your friends to meet up.

## Setup

Install

* git
* Flask
* Numpy
* yarn & node.js

Then run

```shell
git clone https://bitbucket.org/undergroundmeetup/ugm_main.git
cd ugm_main
git submodule update --init
python ugm_generator.py
yarn install
yarn run build:prod
export FLASK_APP=ugm_web.py
flask run
```
