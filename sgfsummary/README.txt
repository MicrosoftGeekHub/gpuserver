========================
Go Tools: SGF Summarizer
========================

Description
===========

Reads multiple SGF (Smart Game Format) files, specifically those recording
Go/WeiQi/Baduk games, and summarizes their game information, suitable for
importing into a spreadsheet or database package for storage and manipulation.

Installation
============

You'll need the Python language itself, freely available from
[[http://www.python.org]].

The sgfsummary.tgz (tarred, gzipped) archive contains the following:

- sgfsummary.py -- The main program. Put this wherever you like. On Unix/Linux,
  you will have to set the mode bits (chmod a+x sgfsummary.py), and if your
  Python interpreter is not at /usr/local/bin/python, you will have to edit the
  first (#!) line.

- sgflib.py -- SGF Parser Library. Put this in a folder on Python's path.

- typelib.py -- Type Class Library. Put this in a folder on Python's path.

- README.txt -- Installation instructions (the file you're reading now).

- gpl.txt -- The GNU General Public License; applies to sgfsummary.py.

- lgpl.txt -- The GNU Lesser General Public License; applies to sgflib.py.

I have only tested this code on my system, MacOS 8.6, running Python 1.5.2. I
did write it to be at least minimally portable (POSIX-style command-line &
stdout interface) to other platforms. If you have any trouble running it, find
(fix?) any bugs, or add any features, please contact me.

MacOS users: please see the Macintosh Python Notes and the Macintosh SGF Notes
at [[http://gotools.sourceforge.net]].

To Do
=====

- Test on Unix, Linux, Windows...

- Add an interactive GUI for other OSes. (Make a Tk GUI for all OSes?)
   
- Make the summary format flexible (columns, order of columns; options file?).
   
- Add byo-yomi information extraction from IGS files (BL/WL property).

Have any other suggestions? Want to help? Let me know!

Contact
=======

Project administrator: David Goodger [[mailto:dgoodger@bigfoot.com]]
Go Tools Project website: [[http://gotools.sourceforge.net]]
