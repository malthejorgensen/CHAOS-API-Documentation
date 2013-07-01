==============
CHAOS overview
==============

What is CHAOS?
--------------
CHAOS is a database for media content. |br|
CHAOS does not store the media itself but rather references (URLs) to the media
and metadata (XML) about it.

CHAOS is usually accessed through its webinterface CHAOS.Portal. There exists
PHP and Javascript libraries that wrap the CHAOS.Portal API into simple function
calls on Javascript or PHP objects. 

.. image:: /static/chaos_org_chart.png
   :height: 300
   :alt: Overview of the structure of CHAOS

API versioning
--------------
The current version of CHAOS (as of March 2013) is v5.
Tutorials (including this introduction) can be assumed to be written for v5
unless otherwise noted.
CHAOS v5 was released in November 2012. The primary change from v4 to v5 is that
output is now guaranteed to be UTF-8.
v6 is currently in development.

.. note::

   For v1-v5 there is no built-in way in CHAOS to obtain version
   information, and you have to know which version you are dealing with beforehand.
   In v6 the API will expose which versions are available.

