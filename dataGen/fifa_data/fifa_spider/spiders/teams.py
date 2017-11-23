#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from lxml import etree 
import io
import os
leagues = ['English Premier League (1)', 'French Ligue 1 (1)', 'German Bundesliga (1)', 'Italian Serie A (1)', u'Spanish Primera División (1)', 'French Ligue 2 (2)', 'English Championship (2)', 'German 2. Bundesliga (2)', 'Italian Serie B (2)', 'Spanish Segunda División (2)', 'English League One (3)', 'English League Two (4)']

def asciiMake(s):
    return ''.join([i if ord(i) < 128 else '' for i in s])
def checkNumeric(s):
    try:
        int(s)
        return True
    except:
        return False
parser = etree.XMLParser(recover=True)
def getGameDate(response):
    val = response.xpath('//div[@class="columns"]//div[@class="column col-16"]').extract()[0]
    root = etree.fromstring(val, parser)
    s = ''
    for elem in root.iter():
        if elem.text is not None and 'FIFA' in elem.text:
            s = elem.text
    if s is not None:    
        s = s.split()
        game = s[0] + ' ' + s[1]
        date = s[2] + ' ' + s[3][:len(s[3])-1] + ' ' + s[4]
        return game, date
    else:
        return None
def parseAgeInfo(ageData):    
    i = ageData.index('Age ')
    vals = ageData[i:].split()
    age = vals[1]
    bday = vals[2][1:] + ' ' + vals[3][:len(vals[3])-1] + ' ' + vals[4][:len(vals[4])-1]
    height = vals[5]
    weight = vals[6][:len(vals[6])-7]
    return age, bday, height, weight
def getPlayerInfo(response):
    ageData = response.xpath('//div[@class="player"]//div[@class="info"]//span').extract()[0]
    age, bday, height, weight = parseAgeInfo(ageData)
    gameData = response.xpath('//div[@class="player"]//div[@class="stats"]').extract()[0]
    root = etree.fromstring(gameData, parser)
    vals = []
    val2 = []
    prev = ''
    for elem in root.iter():
        if checkNumeric(elem.text) and (elem.text[0] != '+' and elem.text[0] != '-'):
            vals.append(elem.text)
        prev = elem.text
    potential = vals[1]
    overallRating = vals[0]
    return overallRating, potential, age, bday, height, weight
def getTeam(response):
    vals = response.xpath('//div[@class="player"]//a').extract()
    teams = []
    for s in vals:
        if s[9:15] == '/team/':
            root = etree.fromstring(s, parser)
            teams.append(root.text)
    return teams[0]
def getPlayerPosName(response):
    '''gets player position and name from sofifa'''
    val = response.xpath('//div[@class="player"]//div[@class="info"]//div[@class="meta"]//span').extract()[0]
    root = etree.fromstring(val, parser)
    vals = []
    for elem in root.iter():
        
        vals.append(elem.text)
        prev = elem.text
    return vals[0] , vals[3]
def getPlayerStats(response):
    val = response.xpath('//div[@class="columns"]//div[@class="column col-3 mb-20"]').extract()
    lst = []
    for i, attrib in enumerate(val):
        
        root = etree.fromstring(attrib, parser)
        
        for elem in root.iter():
            if i != 7:
                if checkNumeric(elem.text) and (elem.text[0] != '+' and elem.text[0] != '-'):
                    lst.append(elem.text)
            else:
                if elem.tag != 'h5' and elem.text != '\n':
                    lst.append(elem.text)
    return lst
class PlayerSpider(scrapy.Spider):
    name = "teams"     
    filename = 'playerInfo2011.csv'
    def start_requests(self):
        urls = [#'https://sofifa.com/leagues?v=18&e=158835&set=true'
                #'https://sofifa.com/leagues?v=17&e=158466&set=true'
                #'https://sofifa.com/leagues?v=16&e=158103&set=true'
                #'https://sofifa.com/leagues?v=15&e=157739&set=true'
                #'https://sofifa.com/leagues?v=14&e=157376&set=true'
                #'https://sofifa.com/leagues?v=13&e=157011&set=true'
                'https://sofifa.com/leagues?v=12&e=156644&set=true'
                #'https://sofifa.com/leagues?v=11&e=156279&set=true',
                #'https://sofifa.com/leagues?v=10&e=155914&set=true',
                #'https://sofifa.com/leagues?v=09&e=155549&set=true',
                #'https://sofifa.com/leagues?v=08&e=155183&set=true',
                #'https://sofifa.com/leagues?v=07&e=154818&set=true'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parseLeagues)
    
    with open(filename, 'w') as f:
            f.write(u'Name, P_id, Position, Game, Date, Team, Age, Birthday, Height, Weight, Overall, Potential, Crossing, Finishing, Heading accuracy, Short passing, Volleys, Dribbling, Curve, Free kick accuracy, Long passing, Ball control, Acceleration, Sprint speed, Agility, Reactions, Balance, Shot power, Jumping, Stamina, Strength, Long shots, Aggression, Interceptions, Positioning, Vision, Penalties, Composure, Marking, Standing tackle, Sliding tackle, GK diving, GK handling, GK kicking, GK positioning, GK reflexes, trait 1, trait 2, trait 3, trait4, trait 5\n')    
    
    def parseLeagues(self, response):
        val = response.xpath('//a').extract()
        lToScrape = []
        for i in val:
            if i[9:17] == '/league/':
                root = etree.fromstring(i, parser)
                for elem in root.iter():
                    league = elem.text
                if league in leagues:
                    lToScrape.append(i[9:19])
        for l in lToScrape:
            url = 'https://sofifa.com' + l
            yield scrapy.Request(url=url, callback=self.parseTeams)
    def parseTeams(self, response):
        val = response.xpath('//a').extract()
        teamsToScrape = []
        for s in val:
            if s[9:15] == u'/team/':
                temp = s.split('"')
                teamsToScrape.append(temp[1])
        for t in teamsToScrape:
            url = 'https://sofifa.com' + t
            yield scrapy.Request(url=url, callback=self.parsePlayers)
    def parsePlayers(self, response):
        val = response.xpath('//a').extract()
        playersToScrape = []
        for s in val:
            if s[9:17] == '/player/':
                temp = s.split('"')
                playersToScrape.append(temp[1])
        for p in playersToScrape:
            url = 'https://sofifa.com' + p
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        vals = []
        p_id = response.url.split('/')[-1]
        getPlayerInfo(response)
        name, pos = getPlayerPosName(response)
        game, date = getGameDate(response)
        overall, pot, age, bday, height, weight = getPlayerInfo(response)
        team = getTeam(response).replace(',', '')
        vals.append(name)
        vals.append(p_id)
        vals.append(pos)
        vals.append(game)
        vals.append(date)
        vals.append(team)
        vals.append(age)
        vals.append(bday)
        vals.append(height)
        vals.append(weight)
        vals.append(overall)
        vals.append(pot)
        stats = getPlayerStats(response)
        if game != 'FIFA 18' and game != 'FIFA 17':
            stats =  stats[:25] + ['0'] + stats[25:]
        
        vals += stats        
        for i, val in enumerate(vals):
            # delete trailing and start spaces
            if val[0] == ' ':
                vals[i] = val[1:]
            if val[-1] == ' ':
                vals[i] = val[:len(val) - 1]
        valString = u''
        for val in vals:
            valString += unicode(val) + u','
        valString += u'\n'
        with io.open(self.filename, 'a', encoding = 'utf-8') as f:
            f.write(valString)
        self.log('Saved file %s' % self.filename)    