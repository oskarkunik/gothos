# gothos

Gothos is an attempt at getting away from [Pocket](https://getpocket.com) and self-hosting a simpler solution that suits my needs. I need a way to get to links that I save every day from my computers and to sync them between my devices.

**Warning! The setup is convoluted and will most likely not work for you out of the box. I'm putting this up here mostly for future me to reference.**

To make it work I decided to start adding links to my [todo.txt](http://todotxt.org/) file that I already keep in sync using [syncthing](https://syncthing.net/), but any file syncing service will do.

The Python script (`todo_parser.py`) then periodically parses the `todo.txt` file and tries to retrieve page titles for newly added links. It then adds a "+parsed" file to the end of lines to know to skip them the next time.

Gothos is meant to be served from an http server. In my case it's Python's built-in server on a local Raspberry Pi Zero W.

## files

| file 						| description 																										|
| ---- 						| -----------																											|
| gothos.service	| systemd service file that should go to /etc/systemd/system			|
| index.html			| website to be served 																						|
| README.md				| this file																												|
| script.js				| js to append href elements to index.html												|
| style.css				| basic stylesheet for index.html																	|
| todo_parser.py	| python script that parses urls in todo.txt and gets page titles	|
| gothos_cron			| script to run as a cron job																			|
| todo.txt				| example, to be replaced by a symlink to actual todo.txt					|

## requirements

- systemd (it comes with ubuntu-based distros that I use),

- python3 (I use its `http.server` module to serve the links site as well as to run the parsing script),

- todo.txt file or another plain text file where links are saved/synced to.

## installation

1. Pull the entire project

2. Modify `gothos.service` to match your system and path to `gothos` directory and place the file in `/etc/systemd/system`

	`sudo cp gothos.service /etc/systemd/system/`

3. Reload service files so that gothos can be started:

	`sudo systemctl daemon-reload`

4. Start the service:

	`sudo systemctl start gothos.service`

4. If the website can be accessed (by default on port 8000), enable the service:

	`sudo systemctl enable gothos.service`

5. Symlink or copy your todo.txt file into gothos directory

6. Modify the `file_path` in `todo_parser.py` to match your absolute path to todo.txt file

7. Automate running `todo_parser.py`. I added `gothos_cron` (with `sudo chmod +x 777`) to `/etc/cron.hourly/` with the following content:

	```
	#!/bin/bash

	python3 /home/pi/gothos/todo_parser.py
	```

## todo

- rewrite youtube links as yewtu.be links
- add separate tags for videos in the website
- display url below/next to the title
