# Copyright (c) Libor Wagner - All Rights Reserved
#
# Author:      Libor Wagner <wagnelib@cmp.felk.cvut.cz>
# Created on:  Dec 9, 2013


import urllib2
import urllib
import json


class ORIS(object):
    """Implementation of the ORIS API (http://oris.orientacnisporty.cz/API)
    """

    def __init__(self, format="json", uri="http://oris.orientacnisporty.cz/API/"):
       self.format = format
       self.uri = uri

    def getCSOSClubList(self):
        url = self._make_request("getCSOSClubList")
        return req._query(url)

    def getClub(self, id):
        url = self._make_request("getClub", {"id":id})
        return req._query(url)

    def getEventList(self, all=None, name=None, sport=None, rg=None, datefrom=None, dateto=None):
        url = self._make_request("getEventList", {"all":all, "name":name, "sport":sport, "rg":rg, "detafrom":datefrom, "datato":dateto})
        return req._query(url)

    def getEvent(self, id):
        url = self._make_request("getEvent", {"id":id})
        return req._query(url)

    def getEventEntries(self, eventid, classid=None, classname=None, clubid=None, entrystop=None, entrystopout=None):
        url = self._make_request("getEventEntries", {"eventid":eventid, "classid":classid, "calssname":classname, "clubid":clubid, "entrystop":entrystop, "entrystopout":entrystopout})
        return req._query(url)

    def getEventResults(self, eventid, classid=None, classname=None, clubid=None):
        url = self._make_request("getEventResults", {"eventid":eventid, "classid":classid, "classname":classname, "clubid":clubid})
        return req._query(url)

    def getUser(self, rgnum):
        url = self._make_request("getUser", {"rgnum":rgnum})
        return req._query(url)

    def _make_request(self, method, params={}):
        args = dict([("format",self.format), ("method",method)] + params.items())
        args = dict((k, v) for k, v in args.iteritems() if v)
        url = urllib.urlencode(args)
        print self.uri + "?" + url

    def _query(self, url):
        req = usrllib2.urlopen(url)
        return req.read()
