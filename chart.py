import numpy as np
import pandas as pd
from datetime import date, timedelta

# IMPORT CSV
csv = pd.read_csv('https://raw.githubusercontent.com/yellowslides/charts/main/2022charts.csv')

# GLOBAL VARIABLES
chartNumbers = csv.chart.unique()
startDate = date(2022, 1, 6)

# CREATE DICTIONARY OF 2022 ALBUMS
twentyTwoChartsDict = {elem : pd.DataFrame() for elem in chartNumbers}
for key in twentyTwoChartsDict.keys():
    twentyTwoChartsDict[key] = csv[:][csv.chart == key]

# RETURN CHART BY CHART CODE  
def chartByChartCode(chartCode):
  return twentyTwoChartsDict[chartCode]

# RETURN DATE OF CHART BY CHART CODE AS STRING
def dateByChartCode(chartCode):
  return (startDate + timedelta(weeks=(int((chartCode)-1)%100))).strftime('%m/%d/%Y') 

#for i in range(2201,2253):
#  print(dateByChartNumber(i))

# RETURN LIST OF DATES OF CHARTS BY CHART CODES
def datesByChartNumbers(listOfCodes):
  listOfDates = []
  for i in listOfCodes:
    listOfDates.append(dateByChartCode(i))
  return listOfDates

#datesByChartNumbers(chartNumbers)

# INSERT LIST OF DATES TO A DATAFRAME BY CHART CODES
def insertDateList(df, listOfCodes):
  return df.insert(0, 'date', datesByChartNumbers(listOfCodes))

# RESET INDEX ON A DATAFRAME
def resetIndex(df):
  df.insert(0, '#', np.arange(1, len(df)+1)) 
  df.set_index('#', inplace=True)
  return df

import numpy as np
import pandas as pd
from datetime import date, timedelta

# IMPORT CSV
csv = pd.read_csv('https://raw.githubusercontent.com/yellowslides/charts/main/2022charts.csv')

# GLOBAL VARIABLES
chartNumbers = csv.chart.unique()
startDate = date(2022, 1, 6)

# CREATE DICTIONARY OF 2022 ALBUMS
twentyTwoChartsDict = {elem : pd.DataFrame() for elem in chartNumbers}
for key in twentyTwoChartsDict.keys():
    twentyTwoChartsDict[key] = csv[:][csv.chart == key]

# RETURN CHART BY CHART CODE  
def chartByChartCode(chartCode):
  return twentyTwoChartsDict[chartCode]

# RETURN DATE OF CHART BY CHART CODE AS STRING
def dateByChartCode(chartCode):
  return (startDate + timedelta(weeks=(int((chartCode)-1)%100))).strftime('%m/%d/%Y') 

#for i in range(2201,2253):
#  print(dateByChartNumber(i))

# RETURN LIST OF DATES OF CHARTS BY CHART CODES
def datesByChartNumbers(listOfCodes):
  listOfDates = []
  for i in listOfCodes:
    listOfDates.append(dateByChartCode(i))
  return listOfDates

#datesByChartNumbers(chartNumbers)

# INSERT LIST OF DATES TO A DATAFRAME BY CHART CODES
def insertDateList(df, listOfCodes):
  return df.insert(0, 'date', datesByChartNumbers(listOfCodes))

# RESET INDEX ON A DATAFRAME
def resetIndex(df):
  df.insert(0, '#', np.arange(1, len(df)+1)) 
  df.set_index('#', inplace=True)
  return df

# RETURN DATAFRAME OF TOP *NUM* SONGS ON CHART IN WEEKS
def mostWeeks(num):
  df = csv[['song','artist']].value_counts()[:num].reset_index()
  df.columns = ['song', 'artist', 'weeks']
  return resetIndex(df)

# RETURN LENGTH OF LONGEST SEQUENCE OF ASCENDING NUMBERS IN A LIST
def longestAscendingSequence(list):
  currentSequence = 1
  maxSequence = 1
  currentNumber = 0
  maxNumber = 0
  for i in range(1, len(list)):
    if (list[i-1] == list[i]-1):
      currentSequence += 1
      currentNumber = list[i]      
    else:
      currentSequence = 1
    if (currentSequence > maxSequence):
      maxSequence = currentSequence
      maxNumber = currentNumber
  return (maxSequence, maxNumber)

#print(longestAscendingSequence([1,2,3,4,5,6]))   # return 6
#print(longestAscendingSequence([1,2,3,4,6]))     # return 4
#print(longestAscendingSequence([1,3,4,5,6]))     # return 4
#print(longestAscendingSequence([1,3,5]))         # return 1

# RETURN DATAFRAME OF TOP *NUM* SONGS WITH MOST CONSECUTIVE WEEKS ON CHART
def mostConWeeks(num):
  df = mostWeeks(num*2)
  listOfWeeks = []
  for index, row in df.iterrows():
    conWeeks, lastDate = longestAscendingSequence((csv.loc[(csv['song'] == row['song']) 
        & (csv['artist'] == row['artist'])])['chart'].tolist())
    df.iloc[index - 1, 2] = conWeeks
    listOfWeeks.append(dateByChartCode(lastDate-(conWeeks-1)) + " - " + dateByChartCode(lastDate))
  df['dates of run'] = listOfWeeks
  return resetIndex(df.nlargest(num, 'weeks'))

mostConWeeks(10)

# RETURN DATAFRAME OF TOP *NUM* SONGS WITH MOST WEEKS IN TOP TEN
def mostTopTenWeeks(num):
  df = csv[csv.position <= 10].filter(['song', 'artist']).value_counts()[:num].reset_index()
  df.columns = ['song', 'artist', 'weeks']
  return resetIndex(df)

mostTopTenWeeks(10)

# RETURN DATAFRAME OF TOP *NUM* SONGS WITH MOST WEEKS AT NUMBER ONE
#def mostWeeksAtNumberOne(num):
#  df = numberOnes()[['title','artist']].value_counts()[:num].reset_index()
#  df.columns = ['song', 'artist', 'weeks']
#  return resetIndex(df)

#mostWeeksAtNumberOne(10)

#topTen(gasolineRun)

# RETURN DATAFRAME OF TOP *NUM* SONGS WITH MOST WEEKS ON CHART WITHOUT PEAKING TOP TEN
#def mostWeeksWithoutTopTenPeak(num):
#  songsWithTopTenPeaks = mostTopTenWeeks(100)
#  for index, row in songsWithTopTenPeaks:
#    #df = csv[csv.song != row['song']]
#  return df

#mostWeeksWithoutTopTenPeak(100)
