Wordzilla
=========

Wordzilla is a commandline based dictionary for viewing the meanings
of English words from the commandline. It can be useful for people who spend
a lot of time on the command line. It can also be integrated with your favourite
editor to view meanings of words.

**Installation :**

1. Clone this repo
2. Run ``python setup.py install``

**Usage :**

* Return four meanings for the word set
  ``wordzilla -n 4 set``
* Return the meanings for the word set used as a verb
  ``wordzilla -p verb set``

**Dictionary data :**

The data is taken from Wikitionary and colored output is platform-dependent. Its
a port of the perl script I wrote a while back. An android version of the dictionary
is also available at `Google play store<https://play.google.com/store/apps/details?id=com.Yennaachi.Wordzilla>`
