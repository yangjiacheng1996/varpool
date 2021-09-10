#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging


class Letter:
    def __init__(self, queue):
        self.q = queue

    def get_first_message(self):
        if not self.q.empty():
            message = self.q.get()
            return message
        else:
            logging.error("the letter is empty")
            raise EOFError

    def put_message(self,message):
        self.q.put(message)
        return self.q