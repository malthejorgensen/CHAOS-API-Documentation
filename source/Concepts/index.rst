==============
CHAOS concepts
==============
In this chapter the general concepts in CHAOS will be explained.

.. .. toctree::
..    :maxdepth: 2
..    :glob:
.. 
..    intro

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

New table

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

Metadata
--------
