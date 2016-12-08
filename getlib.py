import urllib2
import json
import random
import base64
import pprint
def get_url(url="https://api.github.com/orgs/openedoo/repos"):
	try:
		response = urllib2.Request(url,headers={'User-Agent' : "Magic Browser"})
		read = urllib2.urlopen(response).read()
		data = json.loads(read)
		return data
	except Exception as e:
		raise e

def check_modul_available(url="https://api.github.com/orgs/openedoo/repos"):
	data = get_url(url)
	number_git = len(data)
	number_awal = 0
	list_all = []
	for number_awal in xrange(number_awal,number_git):
		jumlah = (number_awal+1)-1
		modul = data[jumlah]
		cek_modul = data[jumlah]['name']
		if 'modul' in cek_modul:
			modul_url = modul['contents_url']
			modul_url_original = modul_url.replace("{+path}", "")
			modul_url_requirement = modul_url.replace("{+path}", "requirement.json")
			modul_name = modul['name']
			modul_list = {'name':modul_name,'url':modul_url_original,'url_requirement':modul_url_requirement}
			list_all.append(modul_list)
		else:
			pass
	return list_all
def check_modul_requirement(url):
	try:
		response = get_url(url)
		content = response['content']
		data = base64.b64decode(content)
		data = json.loads(data)
		return data
	except Exception as e:
		return e

def download_modul_git(url):
	try:
		response = get_url(url)
		return response
	except Exception as e:
		return e
data = check_modul_available()
download = download_modul_git('https://api.github.com/repos/openedoo/modul_hello/contents/')
pprint.pprint (download)