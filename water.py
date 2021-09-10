#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging


class Water:
    def __init__(self, pool):
        self.pool = pool
        if not isinstance(pool, dict):
            print("pool is not a dict type")
            raise TypeError

    def add_water(self, water_name: str, water_value, replace=True):
        if replace or self.pool.get(water_name, None) is None:
            self.pool[water_name]: water_value
        if not replace and self.pool.get(water_name, None) is not None:
            pass
        return self.pool

    def remove_water(self, water_name: str):
        self.pool.pop(water_name, "no such thing in pool, don't need remove.")
        return self.pool
