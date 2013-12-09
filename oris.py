# Copyright (c) Libor Wagner - All Rights Reserved
#
# Author:      Libor Wagner <wagnelib@cmp.felk.cvut.cz>
# Created on:  Dec 9, 2013

class ORIS(object):
    """Implementation of the ORIS API (http://oris.orientacnisporty.cz/API)
    """

    def __init__(self, format="json", uri="http://oris.orientacnisporty.cz/API/"):
       self.format = format
       self.uri = uri

    def getCSOSClubList(self):
        pass

    def getClub(self, id):
        pass

    def getEventList(self, all=None, name=None, sport=None, rg=None, datefrom=None, dateto=None):
        pass

    def getEvent(self, id):
        pass

    def getEventEntries(self, eventid, classid=None, classname=None, clubid=None, entrystop=None, entrystopout=None):
        pass

    def getEventResults(self, eventid, classid=None, classname=None, clubid=None):
        pass

    def getUser(self, rgnum):
        pass

