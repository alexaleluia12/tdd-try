#!/usr/bin/env python
#-*- coding:utf-8 -*-


class FileEmpty(Exception):
    def __init__(self, msg):
        self.value = msg
    def __str__(self):
        return repr(self.value)
