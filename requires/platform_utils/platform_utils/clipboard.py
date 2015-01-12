import platform

def Copy(text):
 """Copies text to the clipboard."""

 plat = platform.system()
 if plat == 'Windows':
  import win32clipboard
  import win32con
  win32clipboard.OpenClipboard()
  win32clipboard.EmptyClipboard()
  win32clipboard.SetClipboardText(text, win32con.CF_UNICODETEXT)
  win32clipboard.CloseClipboard()
 elif plat == 'Linux':
  import gtk
  cb = gtk.Clipboard()
  cb.set_text(text)
  cb.store()
 elif plat == 'Darwin':
  import Carbon.Scrap
  Carbon.Scrap.ClearCurrentScrap()
  scrap = Carbon.Scrap.GetCurrentScrap()
  scrap.PutScrapFlavor('TEXT', 0, text)
 return True
