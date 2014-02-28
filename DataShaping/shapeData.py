#
#	Python code for reshaping data from Urban Data Challenge into a more compact form
#	outputs a CSV file, with flat structure for each timestamp
#
# 	by Kristin Henry,  @KristinHenry 
#	Feb 2014
#

import csv


class shapeData() :

	def __init__ (self, infile=None) :

		if infile == None :
			# ToDo: make better handler for lack of indicated input file
			print "No Infile"
			
		else:
			self.src = infile
			self.data = dict()

			self.getRawData()
			self.writeFile(self.data)
			#self.printData()



	def getRawData(self):
		
		src = self.src

		csvfile = open(src, 'rb')
		reader = csv.reader(csvfile, delimiter=',')

		for row in reader:

			if len(row) > 0 and row[0] != 'Timestamp':

				if not self.data.has_key(row[0]):
					self.data[row[0]] = ['n','n','n','n',
									 	 'n','n','n','n',
									 	 'n','n','n','n',
									 	 'n','n','n','n']
				
				col = self.getNewIndex(row[1], row[2])

				self.data[row[0]][col] = row[3]

				# print "-----"
				# print "emb b, emb c, emb t, emb p, mont b, mont c, mont t, mont p, pow b, pow c, pow t, pow p, civ b, civ c, civ t, civ p"
				# self.printData()
				# print "-----"

		csvfile.close()



	def getNewIndex(self, station, mode):
		#print 'station: ', station, '  mode: ', mode
		if station == 'Embarcadero':
			if mode == 'Buses':
				return 0
			elif mode == 'Cars':
				return 1
			elif mode == 'Trucks':
				return 2
			elif mode == 'Pedestrians':
				return 3

		elif station == 'Montgomery':
			if mode == 'Buses':
				return 4
			elif mode == 'Cars':
				return 5
			elif mode == 'Trucks':
				return 6
			elif mode == 'Pedestrians':
				return 7

		elif station == 'Powell':
			if mode == 'Buses':
				return 8
			elif mode == 'Cars':
				return 9
			elif mode == 'Trucks':
				return 10
			elif mode == 'Pedestrians':
				return 11

		elif station == 'Civic Center':
			if mode == 'Buses':
				return 12
			elif mode == 'Cars':
				return 13
			elif mode == 'Trucks':
				return 14
			elif mode == 'Pedestrians':
				return 15


	def writeFile(self, d):

		# first get list of timestamps, and sort them
		keylist = d.keys()
		keylist.sort()
		

		with open('flatData.csv', 'wb') as f:
			f.write("time, st1Bus, st1Car, st1Trk, st1Ped, st2Bus, st2Car, st2Trk, st2Ped, st3Bus, st3Car, st3Trk, st3Ped, st4Bus, st4Car, st4Trk, st4Ped" + "    \n")

			for key in keylist:
				dat = key

				f.write(dat 
				 	+ ',' + str(d[dat][0])
				 	+ ',' + d[dat][1]
					+ ',' + d[dat][2]
				 	+ ',' + d[dat][3]
				 	+ ',' + d[dat][4]
				 	+ ',' + d[dat][5]
					+ ',' + d[dat][6]
				 	+ ',' + d[dat][7]
				 	+ ',' + d[dat][8]
				 	+ ',' + d[dat][9]
				 	+ ',' + d[dat][10]
				 	+ ',' + d[dat][11]
				 	+ ',' + d[dat][12]
				 	+ ',' + d[dat][13]
				 	+ ',' + d[dat][14]
				 	+ ',' + d[dat][15]
					+ '     \n')
			
		f.close()



	def printData(self):
		for dat in self.data:
			print dat, ": " , self.data[dat]



# go
#-------------------------------------
shapeData('urban_data_v2.csv') 

