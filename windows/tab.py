from gi.repository import Gtk, Gio, GLib, Gdk, GObject, WebKit2

class BrowserTab(Gtk.VBox):
    def __init__(self, tabId, *args, **kwargs):
        super(BrowserTab, self).__init__(tabId, *args, **kwargs)
        self.tabId = tabId
        self.webView = WebKit2.WebView()
        self.add(self.webView)
        #self.webView.connect("load-changed", self.load)
        GLib.idle_add(self.webView.load_uri, 'http://www.google.com')
        print("my id: ", tabId)
