import urllib2
import json
import random
def get_url(url="https://api.github.com/orgs/openedoo/repos"):
	response = urllib2.urlopen(url)
	data = json.load(response)
	return data
'''
url = "https://api.github.com/orgs/openedoo/repos"
data = get_url(url)

number_akhir = len(data)
number_awal = 0
print number_akhir
for number_awal in xrange(number_awal,number_akhir):
	jumlah = (number_awal+1)-1
	modul = data[jumlah]
	cek_modul = data[jumlah]['name']
	if 'modul' in cek_modul:
		print "true"
		url = modul['contents_url']
		url_modul = url.replace("{+path}", "list_modul.json")
		try:
			data2 = get_url(url_modul)
			print data2
		except Exception as error:
			print error
	else:
		print "false"
'''
def check_modul_avaible(url=None):
	data = get_url()
	number_git = len(data)
	number_awal = 0
	list_all = []
	for number_awal in xrange(number_awal,number_git):
		jumlah = (number_awal+1)-1
		modul = data[jumlah]
		cek_modul = data[jumlah]['name']
		if 'modul' in cek_modul:
			modul_url = modul['contents_url']
			modul_url = modul_url.replace("{+path}", "requirement.json")
			modul_name = modul['name']
			modul_list = {'name':modul_name,'url':modul_url}
			list_all.append(modul_list)
		else:
			pass
	return list_all
def autoSolve():
	y = []
	for i in range(5):
		z = random.randrange(1, 10)
		y.append(z)
	print(y)
#autoSolve()
print check_modul_avaible()