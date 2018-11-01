# -*- coding: utf-8 -*-

from datetime import datetime

def strptime(input):
    # format example: Sun Oct 28 09:35:42 +0000 2018
    return datetime.strptime(input, '%a %b %d %H:%M:%S %z %Y')

def strftime(input):
    # format example: 12:57 PM - 7 Mar 2018
    return datetime.strftime(input, '%-I:%M %p - %-d %b %Y')