#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import requests

# configuration
file_path = 'todo.txt'
parsed_tag = '+parsed'

# fetches actual website title
def get_page_title(url, title_re=re.compile(r'<titl.+>(.*?)</title>', re.UNICODE )):
    print("Parsing {}:".format(url))
    try:
        r = requests.get(url)
        r.raise_for_status()
        if r.status_code == 200 and r.text:
            match = title_re.search(r.text)
            if match:
                print("found")
                return match.group(1)
            return url
        return url
    except requests.exceptions.ConnectionError:
        print("error")
        return url
    except requests.exceptions.HTTPError:
        print("error")
        return url

# extracts url from line
def get_url(line):

    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.search(regex, line)
    if url:
      return url.group(0)

# checks if line has been already parsed (title added, tag changed)
def is_url_parsed(line):
    regex = r"(\+parsed)"
    parsed = re.search(regex, line)
    if parsed:
        return True
    else:
        return False

# open input file
input_file = open(file_path, 'r')

new_data = []

for line in input_file:
    new_data.append(line)

current_line = 0
# go through entire file, find links, parse unparsed
for line in new_data:
    url = get_url(line)
    if(url and not is_url_parsed(line)):
        title = get_page_title(url)
        line = "{} {} {}\n".format(title.strip(), url.strip(), parsed_tag)
        new_data[current_line] = line
        output_file = open(file_path, 'w')
        output_file.writelines(new_data)
        output_file.close()
    current_line += 1

input_file.close()
