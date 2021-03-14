import requests
import time
import os


# Some Variable
checked_url = 0
error = 0
success = 0
startMessage = "\033[42mCreated by: Edimar Mosquida"
# the domain  variables
domain = input('\033[32mDomain name/address: ')
type = int(input('\033[32m[1]http or [2]https: '))
if type == 0:
	typeText = "http"
else:
	typeText = "https"
os.system('clear')
# Loading Domain Wordlist File (10k)
file = open('Domains.txt','r')
content = file.read()
subdomains = content.splitlines()

# Loading the logo
logoFile = open('logo.txt','r')
logo = logoFile.read()
print('\33[95m',logo)
print('\033[30m')
# Loadig File for logging
logFileName = domain+str(time.asctime()).replace(' ','-')
logFile = open(logFileName,'w')

# START MESSAGE
print(startMessage)
print('\033[40m')
# Here we start finding subdomains using Brueforce
discovered_subdomains = []
# Iterate through all subdomains list
print('\033[33m')
print("[+] SEARCHING [+]")
print("Searching subdomains for ",typeText+"://"+domain)				
print("Log File: ",logFileName,'\n')

print('''\033[31m
	==================
	   [+] STAT [+]
	==================
''')


for subdomain in subdomains:
	checked_url += 1
	# Construct the url
	url  = typeText+"://"+subdomain+"."+domain
	try:
		requests.get(url)
	except requests.ConnectionError:
		logFile.write('Error: '+url+'\n')
		error += 1
		pass
	else:
		print("\033[32m[-] Discovered subdomain: ",url)
		discovered_subdomains.append(url)
		logFile.write('Success: '+url+'\n')
		success += 1
	# Print the stat
	print('\033[36mChecked url: '+str(checked_url),end="\r")

print('\033[30m')
