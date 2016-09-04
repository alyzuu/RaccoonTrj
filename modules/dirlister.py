def run(**args):
	try:
		import os
	except:
		print "Could not load the module on this host. Skipping."
		return 0, "failed"
	try:
		print "[*] In dirlister module."
		files = os.listdir(".")
		return str(files), "dirl"
	except:
		print "Could not run module, exiting..."
		return 0, "failed"

