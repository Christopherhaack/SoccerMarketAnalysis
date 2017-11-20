#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from lxml import etree 
import codecs
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
    bday = vals[2][1:] + ' ' + vals[3] + ' ' + vals[4]
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
        if checkNumeric(elem.text):
            vals.append(elem.text)
        prev = elem.text
    potential = vals[1]
    overallRating = vals[0]
    return overallRating, potential
def getPlayerPosName(response):
    '''gets player position and name from sofifa'''
    val = response.xpath('//div[@class="player"]//div[@class="info"]//div[@class="meta"]//span').extract()[0]
    root = etree.fromstring(val, parser)
    vals = []
    for elem in root.iter():
        
        vals.append(elem.text)
        prev = elem.text
    print type(vals[0]), vals[0]
    return vals[0] , vals[3]
def getPlayerStats(response):
    val = response.xpath('//div[@class="columns"]//div[@class="column col-3 mb-20"]').extract()
    lst = []
    for i, attrib in enumerate(val):
        
        root = etree.fromstring(attrib, parser)
        for elem in root.iter():
            if i != 7:
                if checkNumeric(elem.text):
                    lst.append(elem.text)
            else:
                if elem.tag != 'h5' and elem.text != '\n':
                    lst.append(elem.text)
    return lst
def getTeam(response):
    vals = response.xpath('//div[@class="player"]//a').extract()
    teams = []
    for s in vals:
        if s[9:15] == '/team/':
            root = etree.fromstring(s, parser)
            teams.append(root.text)
    return teams[0]
class PlayerSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls = [
            'https://sofifa.com/player/153079'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    filename = 'bs.csv'
    with codecs.open(filename, 'w', 'utf-8') as f:
            f.write('Name, Position, Game, Date, Overall, Potential, Crossing, Finishing, Heading accuracy, Short passing, Volleys, Dribbling, Curve, Free kick accuracy, Long passing, Ball control, Acceleration, Sprint speed, Agility, Reactions, Balance, Shot power, Jumping, Stamina, Strength, Long shots, Aggression, Interceptions, Positioning, Vision, Penalties, Composure, Marking, Standing tackle, Sliding tackle, GK diving, GK handling, GK kicking, GK positioning, GK reflexes, trait 1, trait 2, trait 3, trait4, trait 5\n')    
    
    def parse(self, response):
        vals = []
        getPlayerInfo(response)
        name, pos = getPlayerPosName(response)
        game, date = getGameDate(response)
        overall, pot = getPlayerInfo(response)
        getTeam(response)
        vals.append(name)
        vals.append(pos)
        vals.append(game)
        vals.append(date)
        vals.append(overall)
        vals.append(pot)
        vals += getPlayerStats(response)
        
        valString = ''
        for val in vals:
            valString += val + ', '
        valString += '\n'
        with codecs.open(self.filename, 'a', 'utf-8') as f:
            f.write(valString)

