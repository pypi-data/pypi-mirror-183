# This Library is intended to assist with SPATIAL ANALYSES
  # For purposes of this library, a SPATIAL ANALYSIS is defined as the ANALYSIS of
    # PROPERTIES SURROUNDING a CENTRAL LOCATION via their PROPERTY VALUE and
    # STRAIGHT LINE DISTANCE (SLD) to the CENTRAL LOCATION within a RADIUS OF INTEREST.
# To utilize this library, a CSV FILE is required
  # the file MUST be a database CONTAINING PROPERTY ADDRESSES and PROPERTY VALUES
  # it MUST be organized into TWO COLUMNS with the above data
  # THESE COLUMNS MUST HAVE NAMES CONTAINED IN THE FIRST CELL - THIS IS HOW WE TRAVERSE
# To utilize this library GEOPANDAS, GEOPY, and HAVERSINE MUST be INSTALLED
  # either local installation or Google Colab installation via '!pip install #library name#'
# The comments throughout this file explain the purpose of each function via REQUIRES, 
  # MODIFIES, and EFFECT (RME) clauses and occasional notes
# This LIBRARY is organized via a CLASS called !!SpatialAnalysis!!. This was the best
  # way I would think to organize all the data with abstraction
# READ the COMMENTS above !!def __init__!! to understand how to declare an instance
  # of the class

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from geopy.geocoders import Nominatim
from codecs import register
from io import IncrementalNewlineDecoder
import haversine as hs
from haversine import Unit
from sklearn.linear_model import LinearRegression


class SpatialAnalysis:
  #private member vars
  __path = None
  __centralAddress = None
  __AddressColumnName = None
  __ValueColumnName = None
  __LatPark = None
  __LongPark = None
  __radSize = None

  # REQUIRES:
    # Inputs: 
    # path_in MUST be a STRING of the path to the FILE LOCATION of the .csv of dataset
    # centralAddress_in MUST be the address of the central location as a STRING
    # AddressColumnName_in MUST be a STRING containing the COLUMN NAME FOR ADDRESSES (for Pandas nav)
    # ValueColumnName_in MUST be a STRING containing the COLUMN NAME FOR PROPERTY VALUES ' ' '
    # radSize_in MUST be a FLOAT/INT containint the length of the radius of intrest
    # SLDneeded MUST be a BOOLEAN, FALSE IF NO INPUT, TRUE IF SLDneeded=True passed in as parameter
    # QuadsNeeded MUST be a BOOLEAN, FALSE IF NO INPUT, TRUE IF QuadsNeeded=True passed in as parameter
      #EXAMPLE INPUT: TraverseCityAnalysis = SpatialAnalysis('/content/drive/MyDrive/BIOPHYS117/Final Project/TestingGR.csv',
      #                                      '/content/drive/MyDrive/BIOPHYS117/Final Project/TestingGR.csv', 'Site Address',
      #                                      'Currently Assessed Value', 1, SLDneeded=True, QuadsNeeded=True)
      # The above input WILL find the SLD for each address in the data base passed in.
  # MODIFIES:
    # .csv file passed in with path, __path, __centralAddress, __AddressColumnName, __ValueColumnName, c, 
      # __LatPark, __LongPark, __centCords, __radSize
  # EFFECT: 
    # Initalizes private vars: __path, __centralAddress, __AddressColumnName, __ValueColumnName, c, 
      # __LatPark, __LongPark, __centCords, __radSize
    # IF SLDneed=True:
      # Utilizes: GeoPy to gather Latitude and Longitude for each address in the database, adds columns to .csv passed in
      # Utilizes: harvesine to find Straight Line Distance using latitude and longitude of each address in data base and 
        # the latitude and longitude of the central address passed in.
    # IF QuadsNeeded=True:
      # Uses the lat and long of addresses in comparison to the central address lat and long to classify each address
        # into directional quadrants in relation to the central address i.e. NW, NE, SW, SE
    # Classifies each address as an Outlier or not by adding a column to the .csv file and flagging True if outlier
      # Note: Outliers are defined by the standard statistical definition (if value is less than 25th Quartile - 1.5*IQR,
        # or value is greater than 75th Quartile - 1.5*IQR
  # IMPORTANT: GeoPy is NOT guaranteed to find all addresses, and MAY PULL THE WRONG ADDRESS in some cases!
    # CORRECT THIS by manually checking the data and correcting errors then reruning the constructor but with the
      # the class decleration NOT CONTAINING SLDneeded=TRUE (bc default is SLDneeded=False), and QuadsNeeded=TRUE
  def __init__(self, path_in: str, centralAddress_in: str, AddressColumnName_in: str, ValueColumnName_in: str,
      radSize_in: float, SLDneeded=False, QuadsNeeded=False):
      self.__path = path_in
      self.__centralAddress = centralAddress_in
      self.__AddressColumnName = AddressColumnName_in
      self.__ValueColumnName = ValueColumnName_in
      self.c = pd.read_csv(self.__path)
      self.__radSize = radSize_in

      locator = Nominatim(user_agent='myGeocoder')
      location = locator.geocode(self.__centralAddress, timeout=10000)
      if location is not None:
          self.__LatPark = location.latitude
          self.__LongPark = location.longitude
      else:
          self.__LatPark = float(input("ERROR, Input Latitude of Central Address: "))
          self.__LongPark = float(input("ERROR, Input Longitude of Central Address: "))

      self.__centCords = (self.__LatPark, self.__LongPark)

      if (SLDneeded): ##Note: Some Cleaning may be needed if GeoPy could not find lat and longitude
          assert(input('Please confirm Straight Line Distance is needed by entering 1: ') == '1')
          #Abv is so the user can cancel out of the SLD computation if it was a mistake
          print('Please be patient, this computation can last a while')
          locator = Nominatim(user_agent='myGeocoder')
          for i in range (0, len(self.c)):
              if (i % 100 == 0):
                print(str(i)+'th', 'Address being searched for now.')
              location = locator.geocode(self.c[self.__AddressColumnName][i], timeout=10000)
              if location is not None:
                  self.c.loc[i, 'Latitude'] = location.latitude
                  self.c.loc[i, 'Longitude'] = location.longitude
                  if self.c['Latitude'][i] is not None:
                      geoAdd = (float(self.c['Latitude'][i]), float(self.c['Longitude'][i]))
                      self.c.loc[i, 'Distance from Stadium (miles)'] = hs.haversine(self.__centCords, geoAdd, unit=Unit.MILES)
          self.c.to_csv(self.__path, index=False)
      else:
          print('NOTE: IF YOUR SYNTAX FOR COLUMN NAMES DIFFERS FROM THE FOLLOWING THE PROGRAM WILL NOT WORK')
          print('"Latitude" for latitude value column')
          print('"Longitude" for longitude value column')
          print('"Distance from Stadium (miles)" for the straight line distance from central point column')
          failCondition = input('Input "1" if you wish to cancel out to modify your database (not necessary if the program made the columns for you): ')
          if failCondition == '1':
              assert(False) #break out of code

      if (QuadsNeeded):
          for i in range(0, len(self.c)):
              if self.c['Latitude'][i] is not None: #avoiding errors where GeoPy could not find address
                  if self.c['Latitude'][i] > self.__LatPark and self.c['Longitude'][i] > self.__LongPark:
                      self.c.at[i, 'Region'] = 'NE'
                  elif self.c['Latitude'][i] > self.__LatPark and self.c['Longitude'][i] < self.__LongPark:
                      self.c.at[i, 'Region'] = 'NW'
                  elif self.c['Latitude'][i] < self.__LatPark and self.c['Longitude'][i] < self.__LongPark:
                      self.c.at[i, 'Region'] = 'SW'
                  elif self.c['Latitude'][i] < self.__LatPark and self.c['Longitude'][i] > self.__LongPark:
                      self.c.at[i, 'Region'] = 'SE'
              else:
                  self.c.at[i, 'Region'] = 'FIX ME'
          self.c.to_csv(self.__path, index=False)
      else:
          print('Column in .csv file containing regions must be titled "Region"')
          failCondition = input('Input "1" if you wish to cancel out to modify your database (not necessary if the program made the columns for you): ')
          if failCondition == '1':
              assert(False) #break out of code
      

      # Removing GeoPy Errors and printing number of failed address fetches
      for i in range(0, len(self.c)):
          if self.c['Distance from Stadium (miles)'][i] > self.__radSize or self.c['Distance from Stadium (miles)'][i] == 0:
              self.c['Distance from Stadium (miles)'][i] = np.nan
              self.c['Region'][i] = np.nan
              self.c['Latitude'][i] = np.nan
              self.c['Longitude'][i] = np.nan
              self.c['Is Outlier'][i] = np.nan
      print('GeoPy failed to find', self.c['Distance from Stadium (miles)'].isna().sum(), 'Values.')
      if (self.c['Distance from Stadium (miles)'].isna().sum() != 0):
          print('For now, they have been set blank, which may have resulted in a statement below from the Pandas Library.')
          print('To complete an accurate analysis, manually gather the Straight Line Distance and Region for each')
      
      values = self.c[self.__ValueColumnName].values.tolist()
      values_float = []
      for i in range(0, len(values)):
          values_float.append(float(values[i]))
      Qrt1 = np.percentile(values_float, 25)
      Qrt3 = np.percentile(values_float, 75)
      self.ValueIQR = Qrt3 - Qrt1
      self.OutCheck = 1.5 * self.ValueIQR
      self.LowCheck = Qrt1 - self.OutCheck
      self.HighCheck = Qrt3 + self.OutCheck

      for i in range(0, len(self.c)):
          if float(self.c[self.__ValueColumnName][i]) > self.HighCheck or float(self.c[self.__ValueColumnName][i]) < self.LowCheck:
              self.c.at[i, 'Is Outlier'] = True
          else:
              self.c.at[i, 'Is Outlier'] = False
      self.c.to_csv(self.__path, index=False)
      
  ####################################################################################################################################
  ####################################################### MISC. FUNCTIONS ############################################################
  ####################################################################################################################################

  # When coming from an excel sheet I ran into an error
  # where some values were '#DIV/O!', this may have been a 
  # one time issue, but I wanted to change these values all to zero
  # Note: this does not neccessarly mean values are 0, but will allow
  # the user to run the code. - Manual entry may be needed to fix

  # REQUIRES: Default constructor has ran
  # MODIFIES: c[self.__ValueColumnName]
  # EFFECT: Sets #DIV/0! errors in database that are sometimes seen when .csv files are
      # converted to and from excel/sheets back to .csv format
  def cleanDIV0(self):
      for i in range(0, len(self.c)):
          if self.c[self.__ValueColumnName][i] == '#DIV/0!':
              self.c.at[i, self.__ValueColumnName] = '0'

  # REQUIRES: self.c[Region] is valid
  # MODIFIES: print()
  # EFFECT: prints number of properties in each quadrant
  def showQuadDist(self):
      NW_count = 0
      NE_count = 0
      SW_count = 0
      SE_count = 0
      for i in range(0, len(self.c)):
          if self.c['Region'][i] == 'NW':
              NW_count += 1
          elif self.c['Region'][i] == 'NE':
              NE_count += 1
          elif self.c['Region'][i] == 'SW':
              SW_count += 1
          elif self.c['Region'][i] == 'SE':
              SE_count += 1

      print('NW: ', NW_count)
      print('NE: ', NE_count)
      print('SW: ', SW_count)
      print('SE: ', SE_count)

  # REQUIRES: No constructor, getRangeAveValue, or getRangeAveValueReg Requires violations,
      # A positive incrementTotal input, default is 20.
  # MODIFIES: print / terminal output
  # EFFECT: finds all regions where PERCENT CHANGE is POSITIVE for full area and quadrants
  # NOTE1: Percent change is defined as follows:
      # [(average property value(0 - x)) - (average property value(x - radSize))]/(average property value(x - radSize))
          # This is because the INNER bound must BEGIN at the CENTRAL ADDRESS (0) and the OUTER bound must
            # end at the RADIUS SIZE. X can be thought of as a slider to include all the data while adjusting
            # the size of each slice of the area being analyzed as we cannot justly just leave out a part of
            # the data set.
  # NOTE2: The purpose of this function is to find which slices of the data set provide the BEST RESULTS
      # so further analysis can be conducted
  def printPositiveChange(self, incrementTotal=20):
      assert(incrementTotal > 0)
      regions = ['NW', 'NE', 'SW', 'SE']
      increment = self.__radSize / incrementTotal
      check = increment
      checks = []
      while check < self.__radSize:
          checks.append(round(check, 2))
          check += increment
      print('///////////////////////')
      print('////FULL AREA CHECK////')
      print('///////////////////////')
      for i in range (0, len(checks)):
          Inner = self.getRangeAveValue(0.0, checks[i])
          Outer = self.getRangeAveValue(checks[i], self.__radSize)
          if (Outer != 0):
              Change = (Inner - Outer) / Outer
              if (Change > 0):
                  Change = ''.join((str(round((Change * 100), 2)),'%'))
                  print('BINGO!:', Change, 'for x value:', checks[i], 'for entire area!')
      print('///////////////////////')
      print('/////REGIONS CHECK/////')
      print('///////////////////////')
      for i in range(0, len(regions)):
          for j in range(0, len(checks)):
              Inner = self.getRangeAveValueReg(0.0, checks[j], regions[i])
              Outer = self.getRangeAveValueReg(checks[j], self.__radSize, regions[i])
              if (Outer != 0):
                  Change = (Inner - Outer) / Outer
                  if (Change > 0):
                      Change = ''.join((str(round((Change * 100), 2)),'%'))
                      print('BINGO!:', Change, 'for x value:', checks[j], 'for region', regions[i])
    
  # REQUIRES: numeric input
  # MODIFIES: print / matplotlib output
  # EFFECT: prints a bar chart of parts of the circle the user wishes to plot
    # can be used for full area of regions (user specifies in input prompts)
  def manualBarChart(self):
      toGetAvgVals = []
      toPrintAvgVals = []
      while(input('Enter 1 to stop inputing, otherwise any other input: ') != '1'):
          Inner = float(input('Inner Constraint: '))
          Outer = float(input('Outer Constraint: '))
          toPrintAvgVals.append(str(Inner)+'-'+str(Outer))
          toGetAvgVals.append([Inner, Outer])
      choice = input('Enter a quadrant (NW, NE, SW, SE) or 1 for whole area analysis chart: ') 
      aveVals = []
      if (choice != '1'):
          for i in range(0, len(toGetAvgVals)):
            aveVals.append(self.getRangeAveValueReg(toGetAvgVals[i][0], toGetAvgVals[i][1], choice))
            #print(i)
          plt.figure(figsize=(10,5))
          plt.bar(toPrintAvgVals, aveVals, color='maroon')
          plt.title('Average Property Value in Key Ranges from Stadium in '+choice)
          plt.xlabel('Range from Stadium in Miles')
          plt.ylabel('Average Value (USD$ may be rounded to 6 decimals)')
      else:
          for i in range(0, len(toGetAvgVals)):
              aveVals.append(self.getRangeAveValue(toGetAvgVals[i][0], toGetAvgVals[i][1]))
          plt.figure(figsize=(10,5))
          plt.bar(toPrintAvgVals, aveVals, color='maroon')
          plt.title('Average Property Value in Key Ranges from Stadium in Full Area')
          plt.xlabel('Range from Stadium in Miles')
          plt.ylabel('Average Value (USD$ may be rounded to 6 decimals)')


        
      


  ####################################################################################################################################
  #################################################### FULL AREA GRAPHING FUNCTIONS ##################################################
  ####################################################################################################################################


  #For Outliers, True = On - Flase = Off
  # If true: include outliers
  # If false: do not include outliers

  # REQUIRES: self.c['Distance from Stadium (miles)] has been defined manually or through
      # marking SLD needed as True in constructor, __ValueColumnName is valid
  # MODIFIES: N/A
  # EFFECT: returns average value in region specified by inner and outer constraints
      # this value includes outliers by default but can excluded them by 'Outliers=False'
  def getRangeAveValue(self, innerConstraint, outerConstraint, Outliers=True):
      totalValue = 0
      numValues = 0
      averageValue = 0
      if (Outliers):
          for i in range(0, len(self.c)):
              if self.c['Distance from Stadium (miles)'][i] > innerConstraint and self.c['Distance from Stadium (miles)'][i] <= outerConstraint:
                  totalValue += self.c[self.__ValueColumnName][i]
                  numValues += 1
      else:
          for i in range(0, len(self.c)):
              if self.c['Distance from Stadium (miles)'][i] > innerConstraint and self.c['Distance from Stadium (miles)'][i] <= outerConstraint:
                if self.c['Is Outlier'][i] != True:
                  #FIXME!
                  totalValue += self.c[self.__ValueColumnName][i]
                  numValues += 1
      if totalValue > 0:
          averageValue = totalValue / numValues
      return round(averageValue, 2)

  #For Outliers, True = On - Flase = Off
  # If true: include outliers
  # If false: do not include outliers

  # REQUIRES: endVal is greater than beginVal, increment is greater than 0,
      # no requires claus from getRangeAveValue is violated
  # MODIFIES: print() / plt from matlibplot library
  # EFFECT: prints a graph of average property value in regions of the data incremented
      # by the increment parameter
  def __makeAllChart(self, beginVal, endVal, increment, Outliers=True):
      assert(endVal > beginVal)
      assert(increment > 0)
      i = beginVal
      average_arr = []
      range_arr = []
      r1 = str(beginVal)
      while i < endVal:
          inConst = i
          r1 = str(inConst)
          i += increment
          i = round(i, 3)
          outConst = i
          r2 = str(outConst)
          range_arr.append((r1+" - "+r2))
          if (Outliers):
              average_arr.append(self.getRangeAveValue(inConst, outConst))
          else:
              average_arr.append(self.getRangeAveValue(inConst, outConst, False))
      plt.figure(figsize=(15,10))
      plt.bar(range_arr, average_arr, color = 'maroon', width = 0.8)
      plt.xlabel("Range of Distance from Stadium in Miles")
      plt.ylabel("Average Property Value(USD$ may be rounded to 6 decimals)")
      plt.title("Average Property Value in Ranges")
      
  # REQUIRES: Numeric Inputs
  # MODIFIES: print / terminal
  # EFFECT: graph is printed. Function meant to make sure inexperienced coders can utilize the library
  def FullAreaSummary(self):
      BeginMiles = 0
      EndMiles = 0
      IncrementalValue = ''

      print("For following inputs, include only numeric values")
      Outliers_input = input("Input 1 to include outliers, 0 to remove them for the analysis: ")
      while (Outliers_input != '1' and Outliers_input != '0'):
          print("ERROR! Enter 1 or 0")
          Outliers_input = input("Input 1 to include outliers, 0 to remove them for the analysis: ")
      BeginMiles = float(input("Input Begining Value in Miles for Region: "))
      EndMiles = float(input("Input End Value in Miles for Region: "))
      IncrementalValue = float(input("Input increment value (ex 0.1): "))
      print("Printing Graph...")

      if (Outliers_input == '1'):
          self.__makeAllChart(BeginMiles, EndMiles, IncrementalValue)
      else:
          self.__makeAllChart(BeginMiles, EndMiles, IncrementalValue, False)


  # REQUIRES: no 'nan' or blank cells in the pandas frame
  # MODIFIES: N/A
  # EFFECT: prints a linear regression chart for full area. Analysts can clearly see if a 
    # true trend exists via this, or if more manipulation is needed
  def linRegressFull(self):
      df = self.c.dropna()
      X = df['Distance from Stadium (miles)'].values[:,np.newaxis]
      # target data is array of shape (n,) 
      y = df[self.__ValueColumnName].values
      model = LinearRegression()
      model.fit(X, y)
      keyTicks = [round(np.percentile(X, 0), 2), round(np.percentile(X, 25), 2), round(np.percentile(X, 50), 2),
                  round(np.percentile(X, 75), 2), round(np.percentile(X, 100), 2)]
      plt.figure(figsize=(15,10))
      plt.scatter(X, y, color='g')
      plt.xticks(keyTicks)
      Y_max_tick = y.max()
      print(Y_max_tick)
      Y_tick_increm = Y_max_tick / 8
      Y_ticks = []
      for i in range(0, 9):
        Y_ticks.append(Y_tick_increm * i)
      plt.yticks(Y_ticks)
      plt.plot(X, model.predict(X),color='k', linewidth=3)
      plt.ylabel('Property Value (USD$ may be rounded to 6 decimals)')
      plt.xlabel('Distance From Central Point (miles)')
      plt.show()
  ####################################################################################################################################
  #################################################### QUADRANT GRAPHING FUNCTIONS ###################################################
  ####################################################################################################################################

  #For Outliers, True = On - Flase = Off
  # If True: include outliers
  # If False: do not include outliers

  # REQUIRES: self.c['Region] is valid via running QuadsNeeded=True in constructor or manual
        # definition of quadrants, RegionIn any of (NW, NE, SE, SW)
      # self.c['Distance from Stadium (miles)] has been defined manually or through
        # marking SLD needed as True in constructor, __ValueColumnName is valid,
  # MODIFIES: N/A
  # EFFECT: returns average value in region specified by inner and outer constraints
      # this value includes outliers by default but can excluded them by 'Outliers=False'
  def getRangeAveValueReg(self, innerConstraint, outerConstraint, RegionIn, Outliers=True): ##default behavior is to include outliers
      assert(RegionIn == 'NW' or RegionIn == 'NE' or RegionIn == 'SW' or RegionIn == 'SE')
      totalValue = 0
      numValues = 0
      averageValue = 0
      if (Outliers == False): ##Remove Outliers
          for i in range(0, len(self.c)):
              if self.c['Distance from Stadium (miles)'][i] > innerConstraint and self.c['Distance from Stadium (miles)'][i] <= outerConstraint and self.c['Region'][i] == RegionIn and self.c['Is Outlier'][i] != True:
                  totalValue += self.c['Currently Assessed Value'][i]
                  numValues += 1
      else: ##Include Outliers
          for i in range(0, len(self.c)):
              if self.c['Distance from Stadium (miles)'][i] > innerConstraint and self.c['Distance from Stadium (miles)'][i] <= outerConstraint and self.c['Region'][i] == RegionIn:
                  totalValue += self.c['Currently Assessed Value'][i]
                  numValues += 1

      if totalValue > 0:
          averageValue = totalValue / numValues
      return round(averageValue, 2)

  # REQUIRES: endVal is greater than beginVal, increment is greater than 0,
      # no requires claus from getRangeAveValueReg is violated
  # MODIFIES: print() / plt from matlibplot library
  # EFFECT: prints a graph of average property value in specified quad of the data incremented
      # by the increment parameter. Data shown is in range (beginVal, endVal)
  def __makeRegionChart(self, beginVal, endVal, increment, reg, Outliers=True):
      assert(endVal > beginVal)
      assert(increment > 0)
      i = beginVal
      average_arr = []
      range_arr = []
      r1 = str(beginVal)
      while i < endVal:
          i += increment
          i = round(i, 3)
          outConst = i
          r2 = str(outConst)
          range_arr.append((r1+"-"+r2))
          if(Outliers):
              average_arr.append(self.getRangeAveValueReg(beginVal, outConst, reg))
          else:
              average_arr.append(self.getRangeAveValueReg(beginVal, outConst, reg, Outliers=False))
      plt.bar(range_arr, average_arr, color = 'maroon', width = 0.4)
      plt.xlabel("Range of Distance from Stadium in Miles")
      plt.ylabel("Average Property Value(USD$ may be rounded to 6 decimals)")
      plt.title("Average Property Value in Ranges for "+reg+" Region")

  # REQUIRES: Numeric Inputs
  # MODIFIES: print / terminal
  # EFFECT: graph is printed for specified quad. Function meant to make sure inexperienced coders can utilize the library
  def RegionalSummary(self):
      regIn = ''
      BeginMiles = 0
      EndMiles = 0
      IncrementalValue = ''

      regIn = str(input("Enter Region of Interest: "))
      regIn.capitalize()
      print("For following inputs, include only numeric values")
      Outliers_input = input("Input 1 to include outliers, 0 to remove them for the analysis: ")
      while (Outliers_input != '1' and Outliers_input != '0'):
          print("ERROR! Enter 1 or 0")
          Outliers_input = float(input("Input 1 to include outliers, 0 to remove them for the analysis: "))
      BeginMiles = float(input("Input Begining Value in Miles for Region: "))

      EndMiles = float(input("Input End Value in Miles for Region: "))

      IncrementalValue = float(input("Input increment value (ex 0.1): "))
      print("Printing Graph...")

      if (Outliers_input == '1'):
          self.__makeRegionChart(BeginMiles, EndMiles, IncrementalValue, regIn)
      else:
          self.__makeRegionChart(BeginMiles, EndMiles, IncrementalValue, regIn, Outliers=False)

  # REQUIRES: no 'nan' or blank cells in the pandas frame, quad is str type
  # MODIFIES: N/A
  # EFFECT: prints a linear regression chart for full area. Analysts can clearly see if a 
    # true trend exists via this, or if more manipulation is needed
  def linRegressRegion(self, quad: str):
      df = self.c.dropna()
      X = df[df['Region']==quad]['Distance from Stadium (miles)'].values[:,np.newaxis]
      # target data is array of shape (n,) 
      y = df[df['Region']==quad][self.__ValueColumnName].values

      model = LinearRegression()
      model.fit(X, y)
      keyTicks = [round(np.percentile(X, 0), 2), round(np.percentile(X, 25), 2), round(np.percentile(X, 50), 2),
                  round(np.percentile(X, 75), 2), round(np.percentile(X, 100), 2)]
      plt.figure(figsize=(15,10))
      plt.figure(figsize=(15,10))
      plt.scatter(X, y, color='g')
      plt.xticks(keyTicks)
      Y_max_tick = y.max()
      Y_tick_increm = Y_max_tick / 8
      Y_ticks = []
      for i in range(0, 9):
        Y_ticks.append(Y_tick_increm * i)
      plt.plot(X, model.predict(X),color='k', linewidth=3)
      plt.ylabel('Property Value (USD$ may be rounded to 6 decimals)')
      plt.xlabel('Distance From Central Point (miles)')
      plt.show()


# A note to members of the Michigan Sports Consulting Group using this file past Winter 2025:
  #   If you have decided to dive into this file, even though the Colab tutorial
  # makes it simple to utilize without doing so, you clearly have an interest in
  # coding . I hope by the time you are reading this I have a job in software dev
  # or data analysis, and assuming you have an interest in such, please reach out with
  # questions, advice, and/or assistance in your job search. I am writting this halfway 
  # through my Sophmore year, but MSCG has already been an integral part of my college
  # experience and I would love to assist future members of the club in their careers!
  # Connect with me on LinkedIn https://www.linkedin.com/in/jacob-brinkmann-567438206
  # and I'll be happy to talk also my email is jbrinkmann10@gmail.com but is often cluttered.
  # Best,
  # Jacob Brinkmann


# Spatial.py was written over the course of the Fall 2022 semester by Jacob Brinkmann
# Jacob is working towards a Bachelor of Science in Computer Science with aspirations
# of a Business Minor as well. Jacob is involved with the Michigan Sports Consulting
# Group (MSCG), for whom he intends this library to be utilized primarly. Outside of 
# MSCG and Courses, Jacob currently works as a Personal Trainer for the Recreational 
# Sports Department at the University of Michigan. Jacob is also involved in the
# Michigan Alpha Chapter of Phi Delta Theta International Fraternity. 