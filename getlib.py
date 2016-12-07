import urllib2
import json

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
def check_modul(url=None):
	data = get_url()
	number_git = len(data)
	number_awal = 0
	for number_awal in xrange(number_awal,number_git):
		jumlah = (number_awal+1)-1
		modul = data[jumlah]
		cek_modul = data[jumlah]['name']
		if 'modul' in cek_modul:
			list_name = []
			list_name.append(data[jumlah]['name'])
			print "true"
			return list_name
			url = modul['contents_url']
			url_modul = url.replace("{+path}", "list_modul.json")
			try:
				data2 = get_url(url_modul)
				print data2
			except Exception as error:
				print error
		else:
			print "false"
print check_modul()