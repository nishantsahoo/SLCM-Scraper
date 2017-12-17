'''
Author      - Nishant Sahoo
Github id   - nishantsahoo
Description - This code will be used to scrape user data from the SLCM portal developed by Manipal Academy of Higher Education.
'''

import mechanize
import sys
from bs4 import BeautifulSoup
import string

def getAcademics(academics):
	sys.stdout = open('DataSets/InternalMarks.txt', 'w')

	username   = academics.find('span', attrs={'id':'lblUserName'}).text
	print 'Welcome,', username
	print '-------------------------------------------'

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

		print

		internalsData  = each.findAll('table', attrs={'class': 'table table-bordered'})

		sessionalsData = internalsData[0]
		tableRowList   = sessionalsData.findAll('tr')[1:]
		for tr in tableRowList:
			print 'Internal Data:'
			tdList = tr.findAll('td')
			print tdList[0].text + ': ' + tdList[2].text + '/' + tdList[1].text

		print

		if len(internalsData)>1:
			print 'Assignment Data:'
			assignmentData = internalsData[1]
			tableRowList   = assignmentData.findAll('tr')[1:]
			for tr in tableRowList:
				tdList = tr.findAll('td')
				print tdList[0].text + ': ' + tdList[2].text + '/' + tdList[1].text

		print '-------------------------------------------'


	# Left with Assignment, and Sessional Marks
	

	# End of the function getAcademics


def getGradeSheet(gradeSheet):
	sys.stdout = open('DataSets/GradeSheet.txt', 'w')

	semester = gradeSheet.find('option', attrs={'selected': 'selected'}).text
	print 'Semester:', semester
	print '-------------------------------------------'

	GPA  = gradeSheet.find('span', attrs={'id': 'ContentPlaceHolder1_lblGPA'}).text
	CGPA = gradeSheet.find('span', attrs={'id': 'ContentPlaceHolder1_lblCGPA'}).text
	print 'GPA:', GPA
	print 'CGPA:', CGPA
	print '-------------------------------------------'

	gradeTable = gradeSheet.find('table', attrs={'id': 'ContentPlaceHolder1_grvGradeSheet'})
	tableRows  = gradeTable.findAll('tr')[1:]

	for tableRow in tableRows:
		spanList     = tableRow.findAll('span')
		subjectCode  = spanList[0].text
		subjectName  = spanList[1].text
		subjectGrade = spanList[2].text
		print 'Subject Code:', subjectCode
		print 'Subject Name:', subjectName
		print 'Subject Grade:', subjectGrade
		print '-------------------------------------------'

	# End of the function getGradeSheet


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

	getAcademics(academics)  # call of the function getAcademics

	response   = browserObject.open("http://slcm.manipal.edu/GradeSheet.aspx")
	gradeSheet = BeautifulSoup(response.read(), "html5lib")
	
	getGradeSheet(gradeSheet)  # call of the function getGradeSheet

	# End of the main function


main()  # call of the main function
