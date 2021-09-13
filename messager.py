#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import queue


class Messager:
    def __init__(self):
        self.messager = queue.Queue(maxsize=1)

    def get_message(self):
        if not self.messager.empty():
            message = self.messager.get()
            return message
        else:
            print("no message is found , the queue is empty!")
            raise EOFError

    def post_message(self, message,clear=True):
        if not self.messager.full():
            self.messager.put(message)
            return self.messager
        elif clear:
            self.messager.get()
            self.messager.put(message)
        else:
            print("queue is full while you don't want to clear queue,now putting message is blocked.")
            raise BlockingIOError


