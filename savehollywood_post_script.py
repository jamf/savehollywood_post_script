#!/usr/bin/env python

import os
from subprocess import Popen, PIPE
from plistlib import readPlistFromString
from SystemConfiguration import SCDynamicStoreCopyConsoleUser

# DO NOT EDIT BELOW THIS LINE #

# Grabs the computer UUID needed to name files in user ByHost preference folder
systemProfiler = Popen(
    ["system_profiler", "SPHardwareDataType", "-xml"],
    stdout=PIPE).communicate()[0]
plist = readPlistFromString(systemProfiler)
uuid = plist[0]["_items"][0]["platform_UUID"]

# Grabs the currently logged in username
lastUser = username = (
    SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]
username = [username, ""][username in [u"loginwindow", None, u""]]

# Drectory for the User Library folder for ByHost folder
userPath = '/Users/'
libraryPath = '/Library/Preferences/ByHost'
fullPath = str(userPath) + str(username) + str(libraryPath)

# Renames package added plist names with current computer hardware UUID
for dpath, dnames, fnames in os.walk(fullPath):
    for f in fnames:
        os.chdir(dpath)
        if f.startswith('fr.white'):
            os.rename(f, f.replace(
                f, 'fr.whitebox.SaveHollywood.' + uuid + '.plist'))
for dpath, dnames, fnames in os.walk(fullPath):
    for f in fnames:
        os.chdir(dpath)
        if f.startswith('com.apple.loginwindow.'):
            os.rename(f, f.replace(
                f, 'com.apple.loginwindow.' + uuid + '.plist'))
for dpath, dnames, fnames in os.walk(fullPath):
    for f in fnames:
        os.chdir(dpath)
        if f.startswith('com.apple.screensaver.'):
            os.rename(f, f.replace(
                f, 'com.apple.screensaver.' + uuid + '.plist'))
for dpath, dnames, fnames in os.walk(fullPath):
    for f in fnames:
        os.chdir(dpath)
        if f.startswith('com.apple.ScreenSaverPhoto'):
            os.rename(f, f.replace(
                f, 'com.apple.ScreenSaverPhotoChooser.' + uuid + '.plist'))

# Copies the User/Library/Preferences/ByHost plists to the New User Template
systemLibraryPath = '/System/Library/User Template/Library/Preferences/ByHost'
for dpath, dnames, fnames in os.walk(systemLibraryPath):
    for f in fnames:
        os.chdir(dpath)
        if f.startswith('fr.white'):
            os.rename(f, f.replace(
                f, 'fr.whitebox.SaveHollywood.' + uuid + '.plist'))
for dpath, dnames, fnames in os.walk(systemLibraryPath):
    for f in fnames:
        os.chdir(dpath)
        if f.startswith('com.apple.loginwindow.'):
            os.rename(f, f.replace(
                f, 'com.apple.loginwindow.' + uuid + '.plist'))
for dpath, dnames, fnames in os.walk(systemLibraryPath):
    for f in fnames:
        os.chdir(dpath)
        if f.startswith('com.apple.screensaver.'):
            os.rename(f, f.replace(
                f, 'com.apple.screensaver.' + uuid + '.plist'))
for dpath, dnames, fnames in os.walk(systemLibraryPath):
    for f in fnames:
        os.chdir(dpath)
        if f.startswith('com.apple.ScreenSaverPhoto'):
            os.rename(f, f.replace(
                f, 'com.apple.ScreenSaverPhotoChooser.' + uuid + '.plist'))
