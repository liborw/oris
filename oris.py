# Copyright (c) Libor Wagner - All Rights Reserved
#
# Author:      Libor Wagner <wagnelib@cmp.felk.cvut.cz>
# Created on:  Dec 9, 2013


import urllib2
import urllib
import json


OB = 1
LOB = 2
MTBO = 3

class ORIS(object):
    """Implementation of the ORIS API (http://oris.orientacnisporty.cz/API)"""

    def __init__(self, format="json", uri="http://oris.orientacnisporty.cz/API/"):
        """Initialize ORIS API

        Arguments:
            format      : {string}, optional, default: json
            uri         : {string}, optional, default: http://oris.orientacnisporty.cz/API/
        """
        self.format = format
        self.uri = uri

        self.parsers = {"json":self._parse_json}

        if self.format in self.parsers:
            self.parse_output = self.parsers[self.format]
        else:
            self.parse_output = lambda x: x

    def getCSOSClubList(self):
        """Get list of all CSOS clubs."""
        url = self._make_request("getCSOSClubList")
        return self._query(url)

    def getClub(self, id):
        """Get single club.

        Arguments:
            id      : {int}
                      Club id or shortcut.
        """
        url = self._make_request("getClub", {"id":id})
        return self._query(url)

    def getEventList(self, all=None, name=None, sport=None, rg=None, datefrom=None, dateto=None):
        """Get list of events.

        Arguments:
            all         : {}, optional
            name        : {string}, optional
            sport       : {int}, optional
            rg          : {string}
            datefrom    : {}
            dateto      : {}
        """
        url = self._make_request("getEventList", {"all":all, "name":name, "sport":sport, "rg":rg, "detafrom":datefrom, "datato":dateto})
        return self._query(url)

    def getEvent(self, id):
        """Get single event.

        Arguments:
            id          : {int}
        """
        url = self._make_request("getEvent", {"id":id})
        return self._query(url)

    def getEventEntries(self, eventid, classid=None, classname=None, clubid=None, entrystop=None, entrystopout=None):
        """List of entries for particular event.

        Arguments:
            eventid         : {int}
            classid         : {int}
            classname       : {string}
            entrustop       : {int}
            entrystopout    : {int}
        """
        url = self._make_request("getEventEntries", {"eventid":eventid, "classid":classid, "classname":classname, "clubid":clubid, "entrystop":entrystop, "entrystopout":entrystopout})
        return self._query(url)

    def getEventResults(self, eventid, classid=None, classname=None, clubid=None):
        """Results for particular event.

        Arguments:
            eventid         : {int}
            classid         : {int}
            classname       : {string}
            clubid          : {int}
        """
        url = self._make_request("getEventResults", {"eventid":eventid, "classid":classid, "classname":classname, "clubid":clubid})
        return self._query(url)

    def getUser(self, rgnum):
        """Get registered user.

        Arguments:
            rgnum           : {int}
                              Registration number CCXXXX.
        """
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
