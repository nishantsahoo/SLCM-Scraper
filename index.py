import mechanize
import sys
from bs4 import BeautifulSoup

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

response   = browserObject.open("http://slcm.manipal.edu/GradeSheet.aspx")
gradeSheet = BeautifulSoup(response.read(), "html5lib")

sys.stdout = open('GradeSheet.txt', 'w')
print 'Grade Sheet: \n', gradeSheet

response   = browserObject.open("http://slcm.manipal.edu/Academics.aspx")
academics  = BeautifulSoup(response.read(), "html5lib")

sys.stdout = open('Academics.txt', 'w')
print 'Academics: \n', academics
