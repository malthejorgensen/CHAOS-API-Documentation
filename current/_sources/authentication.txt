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
accessPointGUID is the general authentication method for anonymous access, and
in general does not allow editing of the objects in the CHAOS database.


Each objects has a list of accessPointGUID through which it is accessible.

You use accessPointGUID by supplying it as an parameter to the service:
:chaos_api_link_object_get_apg:`pageSize=5&query=*:*`

For testing the API you can use the following accessPointGUID: |chaos_test_accesspointguid|

.. _authentication-login:

Login
-----
Login is a more powerful authentication method which typically grants more
permissions and allows for editing objects.

To use login you first need to create a session

:chaos_api_link:`Session/Create?protocolVersion=4`

This call gives you a sessionGUID which you must supply as a parameter to all
following API calls, e.g. :code:`sessionGUID=...`

You can then authenticate the session by logging in:

:chaos_api_link:`EmailPassword/Login?email=test@example.org&password=mysecret&sessionGUID=...`

