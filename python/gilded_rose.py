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

    def quality_regulator(self):
        for item in self.items:
            if item.name == self.legendary:
                continue

            if item.quality > 50:
                item.quality = 50

            if item.quality < 0:
                item.quality = 0

    def sell_by_logic(self, item):
            item.sell_in -= 1
            if item.sell_in < 0:
                if item.name == self.brie:
                    item.quality += 1
                elif item.name == self.ticket:
                    item.quality = 0
                else:
                    item.quality -= 1
            return item
    
    def basic_quality_logic(self, item):
        if not item.name in self.special_items:
            item.quality -= 1
        else:
            item.quality += 1

            if item.name == self.ticket and item.sell_in < 11:
                item.quality += 1
                
                if item.sell_in < 6:
                    item.quality += 1
        return item

    def update_quality(self):
        for item in self.items:
            if item.name == self.legendary:
                continue

            item = self.basic_quality_logic(item)
            item = self.sell_by_logic(item)
        self.quality_regulator()
            



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
