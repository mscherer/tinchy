tinchy
======

Uh, so... tinchy
----------------

**tin·chy** _adj._ smaller than tiny.

Yep, it's a ridiculously simple and compact personal URL shortener that takes fatty URLS and makes them tinchy.

tinchy urls are in the form of http://my-tinchy-domain/abc

Dependancies
------------

Just [Python 2.5+][py] and [Bottle][bottle]. No database needed, tinchy uses shelve (which is included in Python) to persist URLs.

Give it to me in bullets
------------------------

* Personal URL shortener.
* <50 lines of code.
* [Bottle][bottle] is the only dependancy and it's only one file.
* No database needed.
* Good for storing a few thousand personal URLs, if you expect to be storing tens of thousands then look somewhere else. This is not a bit.ly clone.
* Do whatever you want with it.
* Fully [PEP8][pep8] compliant code (for those who cares :)

  [py]: http://python.org/
  [bottle]: http://bottlepy.org/
  [pep8]: http://www.python.org/dev/peps/pep-0008/
