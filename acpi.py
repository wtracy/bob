import glob, os, sys

class PowerSupply:
	def isOnline(self):
		f = open(self.ac + '/online', 'r')
		online = f.readline()
		f.close()
		return online == '1\n'
	def getStatus(self):
		f = open(self.ac + '/online', 'r')
		online = f.readline()
		f.close()
		if (online == '1\n'):
			return 'on-line'
		elif online == '0\n':
			return 'off-line'
		else:
			return 'read error'
	def __init__(self, path):
		self.ac = path

class Battery:
	def getCharge(self):
		f = open(self.bat + '/charge_full', 'r')
		max = int(f.readline())
		f.close()
		f = open(self.bat + '/charge_now', 'r')
		curr = int(f.readline())
		f.close()
		charge = 100 * curr / max
		return charge
	def getStatus(self):
		f = open(self.bat + '/status', 'r')
		s = f.readline().strip()
		f.close()
		return s
	def __init__(self, path):
		self.bat = path

def onAc():
	for ac in getPowerSupplies():
		if (not ac.isOnline()):
			return False
	return True

def getBatteries():
	return [Battery(p) for p in glob.glob('/sys/class/power_supply/BAT*')]

def getPowerSupplies():
	return [PowerSupply(p) for p in  glob.glob('/sys/class/power_supply/AC*')]

