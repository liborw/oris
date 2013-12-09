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

        self.parsers = {"json":self._parse_json}

        if self.format in self.parsers:
            self.parse_output = self.parsers[self.format]
        else:
            self.parse_output = lambda x: x

    def getCSOSClubList(self):
        url = self._make_request("getCSOSClubList")
        return self._query(url)

    def getClub(self, id):
        url = self._make_request("getClub", {"id":id})
        return self._query(url)

    def getEventList(self, all=None, name=None, sport=None, rg=None, datefrom=None, dateto=None):
        url = self._make_request("getEventList", {"all":all, "name":name, "sport":sport, "rg":rg, "detafrom":datefrom, "datato":dateto})
        return self._query(url)

    def getEvent(self, id):
        url = self._make_request("getEvent", {"id":id})
        return self._query(url)

    def getEventEntries(self, eventid, classid=None, classname=None, clubid=None, entrystop=None, entrystopout=None):
        url = self._make_request("getEventEntries", {"eventid":eventid, "classid":classid, "classname":classname, "clubid":clubid, "entrystop":entrystop, "entrystopout":entrystopout})
        return self._query(url)

    def getEventResults(self, eventid, classid=None, classname=None, clubid=None):
        url = self._make_request("getEventResults", {"eventid":eventid, "classid":classid, "classname":classname, "clubid":clubid})
        return self._query(url)

    def getUser(self, rgnum):
        url = self._make_request("getUser", {"rgnum":rgnum})
        return self._query(url)

    def _parse_xml(self, res):
        """Parse XML response.

        Arguments:
            res     : {string}
                      ORIS API response in XML format.
        Returns:
            status  : {string}
            content :
        """
        pass

    def _parse_json(self, res):
        """Parse JSON response.

        Arguments:
            res     : {string}
                      ORIS API response in JSON format.

        Returns:
            status  : {string}
            data    : {JSON dict}
        """
        db = json.loads(res)
        return db["Status"], db['Data']

    def _make_request(self, method, params={}):
        args = dict([("format",self.format), ("method",method)] + params.items())
        args = dict((k, v) for k, v in args.iteritems() if v)
        url = urllib.urlencode(args)
        return self.uri + "?" + url

    def _query(self, url):
        res = urllib2.urlopen(url)
        return res.read()
