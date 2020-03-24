import pandas as pd
import csv
years = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
teams = ['crd', 'atl', 'rav', 'buf', 'car', 'chi', 'cin', 'cle', 'dal', 'den', 'det', 'gnb', 'htx', 'clt', 'jax', 'kan', 'sdg',
         'ram', 'mia', 'min', 'nwe', 'nor', 'nyg', 'nyj', 'rai', 'phi', 'pit', 'sfo', 'sea', 'tam', 'oti', 'was']
labels = ['Team']
results = []
count = 0
for team in teams:
    count +=1
    TeamResults = [team]
    numTeamWins = 0
    for year in years:
        url = 'https://www.pro-football-reference.com/teams/' + team + '/' + year + '.htm'
        try:
            df = pd.read_html(url)[1]
            for week, result in enumerate(df.iloc[:,5]):
                theWeek  = int(week)+1
                if theWeek>17:
                    break
                if count == 1:
                    labels.append(year + '--Week ' + str(theWeek))
                if result == 'W':
                    TeamResults.append(numTeamWins + 1)
                    numTeamWins+=1
                elif result == 'L':
                    TeamResults.append(numTeamWins -1)
                    numTeamWins-=1
                else:
                    TeamResults.append(numTeamWins)
        except:
            print(url)
            print(pd.read_html(url))
    results.append(TeamResults)

with open('NFLWeekResultsRunning1.csv', mode='w', newline='') as nfl_export:
    data_writer = csv.writer(nfl_export, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(labels)
    for row in results:
        data_writer.writerow(row)

