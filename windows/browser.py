from traceback import print_tb
from typing_extensions import Self
from gi.repository import Gtk, Gio, GLib, Gdk, GObject, WebKit2
from windows import tab
from windows.tab import BrowserTab

class Browser(Gtk.Window):
    def __init__(self):
        super().__init__(title="Saffari for Decstopp")
        self.set_border_width(10)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        self.set_titlebar(hb)

        self.set_size_request(1200, 900)

        topbar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        backbtnbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(backbtnbox.get_style_context(), "linked")

        backbtn = Gtk.Button()
        backbtn.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.LEFT, shadow_type=Gtk.ShadowType.NONE)
        )
        backbtn.connect("clicked", self.goBack)
        backbtnbox.add(backbtn)
        self.backbtn = backbtn

        forwardbtn = Gtk.Button()
        forwardbtn.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.RIGHT, shadow_type=Gtk.ShadowType.NONE)
        )
        forwardbtn.connect("clicked", self.goForward)
        backbtnbox.add(forwardbtn)
        self.forwardbtn = forwardbtn

        newtabbtn = Gtk.Button()
        newtabbtn.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.RIGHT, shadow_type=Gtk.ShadowType.NONE)
        )
        newtabbtn.connect("clicked", self._new_tab)
        backbtnbox.add(newtabbtn)
        self.newtabbtn = newtabbtn

        topbar.pack_start(backbtnbox, True, True, 0)

        urlbar = Gtk.Entry()
        urlbar.set_text("Hello World")
        topbar.pack_start(urlbar, True, True, 0)

        hb.pack_start(topbar)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
        self.notebook.connect("switch-page", self._tab_changed)

        self.tabs = []

        self._new_tab("a")

        self.activeTab = self.tabs[0]
        self.notebook.set_tab_reorderable(self.tabs[0], True)

    def _new_tab(self, _):
        tabID = len(self.tabs)
        tab = BrowserTab(tabID)
        self.tabs.append(tab)
        print(str(self.tabs))
        self.notebook.append_page(self.tabs[tabID], Gtk.Label(label="New Tab " + str(tabID)))
        self.notebook.show_all()
        self.notebook.set_tab_reorderable(tab, True)
        print(tabID)

    def _tab_changed(self, notebook, current_page, index):
        #if not index:
        #    return
        #title = self.tabs[index].webview.get_title()
        #if title:
        #    self.set_title(title)
        self.activeTab = current_page
    
        print(current_page.tabId)

    def goBack(self, button):
        self.activeTab.webView.go_back()
    
    def goForward(self, button):
        self.activeTab.webView.go_forward()

    def load(self, _, __):
        if self.webView.can_go_back():
            self.backbtn.set_sensitive(True)
        else:
            self.backbtn.set_sensitive(False)
        
        if self.webView.can_go_forward():
            self.forwardbtn.set_sensitive(True)
        else:
            self.forwardbtn.set_sensitive(False)

