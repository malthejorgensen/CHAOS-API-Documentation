==============
Authentication
==============

To access objects through CHAOS.Portal you need authentication. Authentication
can be granted through one of the following methods:

 * :ref:`authentication-accesspointguid`
 * :ref:`authentication-login`

.. _authentication-accesspointguid:

accessPointGUID
---------------
accessPointGUID is the general authentication method for anonymous end-user
access. Because of this it is also more limited than other authentication such
as :ref:`authentication-login`, e.g. accessPointGUID does not give you access to
browse folders or edit objects.

Authentication via accessPointGUID happens on a per-object basis: Each object
has a list of accessPointGUIDs through which it is accessible. If an object is
accessible via an accessPointGUID it is said to "published" on the
accessPointGUID. The object can be published on an accessPointGUID for a certain
time period.

You can authenticate yourself with accessPointGUID by supplying it as an
parameter to the service:

:chaos_api_link_object_get_apg:`pageSize=5&query=*:*`

For testing the API you can use the following accessPointGUID: |chaos_test_accesspointguid|

.. _authentication-login:

Login
-----
Login is a more powerful authentication method typically used for administration
because it allows for editing objects and browsing folders.  Authentication via
login happens on a per-folder basis. That means a user has access to certain
folders and by logging the user will have access to all objects in those folders.

To use login you first need to create a session

:chaos_api_link:`Session/Create?protocolVersion=4`

This call gives you a sessionGUID which you must supply as a parameter to all
following API calls, e.g. :code:`sessionGUID=...`

You can then authenticate the session by logging in:
:func:`EmailPassword.Login`

:chaos_api_link:`EmailPassword/Login?email=test@example.org&password=mysecret&sessionGUID=...`

