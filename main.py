#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "3.0")
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, Gio, GLib, Gdk, GObject, WebKit2
#import threading
#import time

#GLib.threads_init()

from windows.browser import Browser

win = Browser()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
