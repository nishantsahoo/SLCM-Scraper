import mechanize
import sys
from bs4 import BeautifulSoup
import string

userId   = sys.argv[1]
password = sys.argv[2]

url           = "http://slcm.manipal.edu/loginForm.aspx"
browserObject = mechanize.Browser()
response      = browserObject.open(url)

browserObject.select_form("form1")
browserObject.form['txtUserid']   = userId
browserObject.form['txtpassword'] = password
browserObject.method              = "POST"

response = browserObject.submit()

def getAcademics(academics):
	sys.stdout = open('InteralMarks.txt', 'w')
	panelGroup = academics.find('div', attrs={'class': 'panel-group internalMarks'})
	panelsList = panelGroup.findAll('div', attrs={'class': 'panel panel-default'})
	for each in panelsList:
		a = each.find('a', attrs={'data-parent': '#accordion'})
		panelData = a.text.strip(string.whitespace)
		data = ' '.join(panelData.split())
		print data
		print '-------------------------------------------'


response   = browserObject.open("http://slcm.manipal.edu/Academics.aspx")
academics  = BeautifulSoup(response.read(), "html5lib")

getAcademics(academics)

response   = browserObject.open("http://slcm.manipal.edu/GradeSheet.aspx")
gradeSheet = BeautifulSoup(response.read(), "html5lib")

# sys.stdout = open('GradeSheet.txt', 'w')
# print 'Grade Sheet: \n', gradeSheet
