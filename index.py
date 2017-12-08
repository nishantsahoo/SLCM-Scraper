'''
Author      - Nishant Sahoo
Github id   - nishantsahoo
Description - This code will be used to scrape user data from the SLCM portal developed by Manipal University.
'''

import mechanize
import sys
from bs4 import BeautifulSoup
import string

def getAcademics(academics):
	sys.stdout = open('DataSets/InternalMarks.txt', 'w')
	panelGroup = academics.find('div', attrs={'class': 'panel-group internalMarks'})
	panelsList = panelGroup.findAll('div', attrs={'class': 'panel panel-default'})
	for each in panelsList:
		dataParent  = each.find('a', attrs={'data-parent': '#accordion'})
		panelData   = dataParent.text.strip(string.whitespace)
		subjectData = panelData.split('\n')
		print 'Subject Code:', subjectData[0].split('  ')[0][14:]
		print 'Subject Name:', subjectData[0].split('  ')[1]
		print 'Marks Obtained:', subjectData[2].strip()[-6:].strip()
		print 'Maximum Marks:', subjectData[3].strip()[-6:].strip()
		print '-------------------------------------------'


def getGradesheet(gradeSheet):
	sys.stdout = open('DataSets/GradeSheet.txt', 'w')
	print 'Grade Sheet: \n', gradeSheet


def main():
	userId   = sys.argv[1]
	password = sys.argv[2]

	url           = "http://slcm.manipal.edu/loginForm.aspx"
	browserObject = mechanize.Browser()
	response      = browserObject.open(url)

	browserObject.select_form("form1")
	browserObject.form['txtUserid']   = userId
	browserObject.form['txtpassword'] = password
	browserObject.method              = "POST"

	response   = browserObject.submit()
	response   = browserObject.open("http://slcm.manipal.edu/Academics.aspx")
	academics  = BeautifulSoup(response.read(), "html5lib")

	sys.stdout = open('DataSets/Academics.txt', 'w')
	print 'Academics: \n', academics

	getAcademics(academics)

	response   = browserObject.open("http://slcm.manipal.edu/GradeSheet.aspx")
	gradeSheet = BeautifulSoup(response.read(), "html5lib")
	
	getGradesheet(gradeSheet)

	# End of the main function


main()
