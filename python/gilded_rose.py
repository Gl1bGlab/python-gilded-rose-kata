# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.ticket = "Backstage passes to a TAFKAL80ETC concert"
        self.brie = "Aged Brie"
        self.legendary = "Sulfuras, Hand of Ragnaros"

        self.special_items = {
            self.ticket,
            self.brie,
        }

    def update_quality(self):
        for item in self.items:
            if item.name == self.legendary:
                continue

            if not item.name in self.special_items:
                item.quality -= 1
            else:
                if item.quality < 50:
                    item.quality += 1

                    if item.name == self.ticket:
                        if item.sell_in < 11 and item.quality < 50:
                                item.quality += 1
                                
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality += 1
            
            if item.name != self.legendary:
                item.sell_in = item.sell_in - 1
                
            if item.sell_in < 0:
                if item.name == self.brie:
                    item.quality += 1

                if item.name != self.brie:
                    if item.name != self.ticket:
                        item.quality -= 1
                    else:
                        item.quality = 0
            
            if item.quality > 50:
                item.quality = 50

            if item.quality < 0:
                item.quality = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
