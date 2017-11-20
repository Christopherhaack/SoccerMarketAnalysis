import scrapy
import codecs

class TransferSpider(scrapy.Spider):
    name = 'transferspider'
    start_urls = ['https://www.transfermarkt.com/premier-league/transfers/wettbewerb/GB1/saison_id/2017']
    leagueCodeToName = { 'GB1': 'Premier League', 'FR1': 'Ligue 1', 'L1': 'Bundesliga', 'ES1': 'La Liga', 'IT1': 'Serie A'}

    def start_requests(self):
        urls = []
        leagues = [('premier-league', 'GB1'), ('ligue-1', 'FR1'), ('1-bundesliga', 'L1'), ('laliga', 'ES1'), ('serie-a', 'IT1')]
        for year in range(2010, 2018):
            for league in leagues:
                urls.append('https://www.transfermarkt.com/' + league[0] + '/transfers/wettbewerb/' + league[1] +'/plus/?saison_id=' + str(year) + '&s_w=s&leihe=0&intern=0')
                urls.append('https://www.transfermarkt.com/' + league[0] + '/transfers/wettbewerb/' + league[1] +'/plus/?saison_id=' + str(year) + '&s_w=w&leihe=0&intern=0')
       
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    filename = 'transfers_test_1.csv'
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write('Name, Country 1, Country 2, Age, Position, Previous Club, Next Club, Previous Club League, Next Club League, Season, Year, Transfer Fee\n')
    def parse(self, response):
        #print (response.url)
        if 's_w=w' in response.url:
            season = 'Winter'
        if 's_w=s' in response.url:
            season = 'Summer'
        year = response.url.split('saison_id=')[1][:4]

        leagueCodeToName = { 'GB1': 'Premier League', 'FR1': 'Ligue 1', 'L1': 'Bundesliga', 'ES1': 'La Liga', 'IT1': 'Serie A'}
        leagueCode = response.url.split('/')[6]
        print (leagueCode)
        leagueName = leagueCodeToName[leagueCode]

        with codecs.open(self.filename, 'a', 'utf-8') as f:
            for table in response.css('div.box'):
                for teamName in table.css('div.table-header a::text'):
                    curClub = teamName.extract()
                    print ('CURCLUB: ' + curClub)
                    for section in table.css('table'):
                        typeTrans = section.css('thead tr th.spieler-transfer-cell::text').extract()[0] # Arrivals or Departures
                        #print ('#### ' + typeTrans + ' ####')
                        for row in section.css('tbody tr'):
                            if row.css('td::text').extract()[0] != ' No arrivals' and row.css('td::text').extract()[0] != ' No departures':
                                #print(row.css('td::text').extract())
                                #print('NOT NO ARRIVALS')
                                name = row.css('td div.di.nowrap span.hide-for-small a::text').extract()[0] # Name
                                countries = row.css('td.zentriert.nat-transfer-cell').css('img::attr(title)').extract() # Countr(ies)
                                country1 = countries[0].replace(",", " ") 
                                if len(countries) == 1:
                                    country2 = 'None'
                                else:
                                    country2 = countries[1]
                                #print (row.css('td a.vereinprofil_tooltip::text').extract())
                                difClub = row.css('td a.vereinprofil_tooltip::text').extract() # Previous/Next Club
                                if len(difClub) == 0:
                                    difClub = 'None'
                                else:
                                    difClub = difClub[0]

                                fee = row.css('td.rechts a::text').extract()[0].replace(",", ".") # Transfer Fee
                                age = row.css('td.zentriert.alter-transfer-cell::text').extract()[0] # Age
                                position = row.css('td.kurzpos-transfer-cell.zentriert::text').extract()[0] # Position

                                if typeTrans == 'Arrivals':
                                    f.write(name + ', ' + country1 + ', ' + country2 + ', ' + age + ', ' + position + ', ' + difClub + ', ' + curClub + ', ' 
                                        + '' + ',' + leagueName + ',' + season + ', ' + year + ', ' + fee + '\n')
                                else:
                                    f.write(name + ', ' + country1 + ', ' + country2 + ', ' + age + ', ' + position + ', ' + curClub + ', ' + difClub + ', ' 
                                        + leagueName + ',' + '' + ',' + season + ', ' + year + ', ' + fee + '\n')
