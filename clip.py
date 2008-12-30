#!/usr/bin/env python

# Filename: stdin2clip.py
# Author: Saphalon (aka Chaim)
# Description:
# Command-line tool to copy standard input (stdin) to clipboard

# Required modules:
# pygtk, gtk

import sys
import pygtk
pygtk.require('2.0')
import gtk

try:
    buffer = ''.join(sys.stdin.readlines())
    c = gtk.Clipboard()
    c.set_text(buffer)
    c.store()
    print 'Successfully copied the following to the clipboard:'
    print '---------------------------------------------------'
    print buffer
except:
    sys.stderr.write('\nAn error occurred! Failed to copy to clipboard!\n')
