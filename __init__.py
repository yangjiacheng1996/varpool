#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import queue


class _Varpool(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


messager = queue.Queue(maxsize=1)
pool = _Varpool()



