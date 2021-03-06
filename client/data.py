import subprocess

options = {
"systemDate":"date",
"osVersion":"cat /etc/issue",
"kernelVersion":"uname -a",
"uptime":"w",
"userAccounts":"cat /etc/passwd",
"groups":"cat /etc/group",
"networkConnections":"netstat -anp",
"loadedDrivers":"lsmod",
"networkInterfaces":"ifconfig -a",
"routingTable":"netstat rn",
"browserHistory":"python3 browserHistory.py",
"bashHistory":"python3 bashHistory.py"
}


def getData(command):
	command = command.split()
	data = subprocess.check_output(command)
	return(data)


def getValue(command):
	value = getData(options[command])
	return(value)
