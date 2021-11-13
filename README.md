# gothos

Gothos is an attempt at getting away from [Pocket](https://getpocket.com) and self-hosting a simpler solution that suits my needs. I need a way to get to links that I save every day from my computers and to sync them between my devices.

To make it work I decided to start adding links to my [todo.txt](http://todotxt.org/) file that I already keep in sync using [syncthing](https://syncthing.net/), but any file syncing service will do. 

The Python script (`todo_parser.py`) then periodically parses the `todo.txt` file and tries to retrieve page titles for newly added links. It then adds a "+parsed" file to the end of lines to know to skip them the next time.

Gothos is meant to be served from an http server. In my case it's Python's built-in server on a local Raspberry Pi Zero W.

## files

.
├── gothos.service	| systemd service file that should go to /etc/systemd/system
├── index.html		| website to be served
├── README.md		| this file
├── script.js		| js to append href elements to index.html
├── style.css		| basic stylesheet for index.html
├── todo_parser.py	| python script that parses urls in todo.txt and gets page titles
└── todo.txt		| example, to be replaced by a symlink to actual todo.txt
