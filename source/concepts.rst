==============
CHAOS concepts
==============

Objects
-------
Each media reference in CHAOS is called an ``Object``. Objects have a number of
fields (also called properties). The two most important properties are :code:`Files` and
:code:`Metadatas`.

 *  :code:`Files` is a list of files (media URLs) associated with the object
 *  :code:`Metadatas` is a list of metadata (XML strings) associated with the object

An overview can be seen in the figure below. 

.. image:: /static/chaos_objects.png
   :height: 300
   :alt: Diagram of CHAOS objects

===============  ========================================
          ``Object`` properties
---------------------------------------------------------
Property name    Description
===============  ========================================
GUID             Unique ID of the object (a GUID)
ObjectTypeID     The type of the object
Metadatas        A list of metadata objects (Metadata)
Files            A list of file objects (FileInfo)
ObjectRelations  A list of objects related to this object
===============  ========================================


Also check out:
:doc:`/Portal/Object`


Files
-----
A file consists of a filename, a URL and some type specifications. The URL can
be used as-is, meaning that you don't have to concatenate the URL and the
filename.

A file has several different format specifiers. In order of most general to most
specific they are: 


1. **FormatType** is the type of the media: an image, a video, sound etc.
2. **FormatCategory** specifies in what context the media should be used. For
   example it could specify ``Image Thumbnail`` or ``Image Original`` so that a page
   showing many images should use the thumbnail (``Image Thumbnail``) whereas a page
   dedicated to that specific image should use the original (``Image Original``).
3. **Format** and **FormatID** are very specific: for example ``Image JPEG 200x200``.

.. note::

   This hierarchy is still under discussion and is subject to change. Furthermore
   no current CHAOS database lives up to this standard and thus you should ask or
   check your data to find how these format specifications have been used in your
   particular database. 

===============  ========================================
          ``File`` properties
---------------------------------------------------------
Property name    Description
===============  ========================================
URL              Location of the file
Filename         The filename of the particular file
FormatType       Image, Video, Sound, Document
FormatCategory   Image Thumbnail, Image Original, Movie Clip, Movie Original etc.
Format           Image JPEG 320x480, Movie AVI 378x210 etc.
===============  ========================================

Metadata
--------
The metadata is typically some form of description of the object, but could also
be data related to the object such as tags or geodata. Every metadata
XML-document conforms to a specific XML-schema called the :code:`MetadataSchema`
identified by its GUID. The MetadataSchema can be looked up in the CHAOS database
and read out similar to getting an object from the database.

Things such the title and description of an object is typically stored in the
metadata.

An object can have multiple :code:`Metadata` conforming to the same
:code:`MetadataSchema`. Let's say for example that the schema dictates that the
:code:`Metadata` is a description and title of the object. What you would
typically have is then the title and description in multiple languages. The
:code:`LanguageCode` of the :code:`Metadata` tells you the language of the
specific entry such that you can grab the appropriate :code:`Metadata` for your users.
Another case of multiple :code:`Metadata` with the same :code:`MetadataSchemaGUID`
could be tag metadata where each metadata xml-string is a tag.

==================  =====================================
          ``Metadata`` properties
---------------------------------------------------------
Property name       Description
==================  =====================================
GUID                GUID of the Metadata
MetadataSchemaGUID  The GUID of the XML schema describing
                    the MetadataXML XML document.
MetadataXML         The metadata as an XML document
LanguageCode        Language code indicating the language
                    of the metadata.
==================  =====================================

:code:`LanguageCode` should generally be two-letter `IETF language tags`_
(the *primary language subtag*).

.. _IETF language tags: http://en.wikipedia.org/wiki/IETF_language_tag

Related objects
---------------
An object can have relations to other objects. These related objects can be
found in the ``ObjectRelations`` property of the ``Object``.  The related
objects are regular ``Object``\s and should be treated as such, although you
probably want to display them differently to the user (in comparison to the
primary object).

Object retrieval and search
---------------------------
The CHAOS database is indexed in a Apache Solr index, and searching but also
retrieving objects in general is done through this index.

To search the index you specify some query string and send it to CHAOS which
sends it on to Solr. The Solr query syntax is based on the `Lucene query syntax`_.
It is in general not necessarry to know the query syntax – there are built-in
utility functions in the Portal.Client libraries and in CHAOS to handle most
common use cases.

Retrieving a single object can be done by "searching" on the GUID field:
GUID:object_guid and multiple objects can be retrieved by combining guid
searches: GUID:object1_guid OR GUID:object2_guid.


Here we search for

.. code-block:: none

   GUID:00000000-0000-0000-0000-00004e040016

which becomes

.. code-block:: none

   GUID%3A00000000-0000-0000-0000-00004e040016

inside the URL.

So the full CHAOS request URL becomes:

.. code-block:: none

      http://api.chaos-systems.com/v5/Object/Get?
        query=(GUID%3A00000000-0000-0000-0000-00004e040016)&
        accessPointGUID=7A06C4FF-D15A-48D9-A908-088F9796AF28&
        pageIndex=0&
        pageSize=1&
        includeFiles=true

*With added linebreaks for readability.* (You can't copy this directly into the
address bar because of the linebreaks, but here's a link__)

__ http://api.chaos-systems.com/v5/Object/Get?query=(GUID%3A00000000-0000-0000-0000-00004e040016)&accessPointGUID=7A06C4FF-D15A-48D9-A908-088F9796AF28&pageIndex=0&pageSize=1&includeFiles=true
.. _Lucene query syntax: http://lucene.apache.org/core/3_6_0/queryparsersyntax.html
