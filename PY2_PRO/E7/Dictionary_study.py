# -*- coding: utf-8 -*-

My_Dict = {'name':'chen','age':18,'high':172}
My_Dict['stat'] = 'married'
My_Dict['name'] = 'Jay'
print My_Dict['name']

#Class study
class song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        print self.lyrics
    def sing_a_song(self):
        for line in self.lyrics:
            print line
happy_bday = song(['Happy birthday to you', "I don't want to get sued", "So I'll stop right there"])
happy_bday.sing_a_song()
happy_bday.__init__("haha")



