#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Waterpool(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__

    def add_water(self, water_name: str, water_value, replace=True):
        if replace or self.get(water_name, None) is None:
            self[water_name] = water_value
        if not replace and self.get(water_name, None) is not None:
            pass
        return self

    def remove_water(self, water_name: str):
        self.pop(water_name, "no such thing in varpool, don't need remove.")
        return self

    def get_water(self, water_name: str):
        target = self.get(water_name, None)
        if target is not None:
            return target
        else:
            print("water pool does not contain water name: %s \n" % water_name, "Please check your spelling.")
            raise Exception
