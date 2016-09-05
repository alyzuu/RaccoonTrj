
def run(**args):
	try:
		import os
	except:
		print "Could not load the module on this host. Skipping."
		return 0, "failed"
	try:
		print "[*] In environment module."
		return str(os.environ), "envr"
	except:
		print "Could not run module, exiting..."
		return 0, "failed"
