.. role:: gbg
.. role:: rbg
===
API
===

Session/Create
--------------
Creates a session, which can be authenticated via the :ref:`api-emailpassword-login`
method.

**Parameters**

 * None

.. note::
   As of 3rd October 2013 :code:`Session/Create` still needs the
   :code:`protocolVersion` and the value must be :code:`4`.
   `Reference <https://github.com/CHAOS-Community/Portal/commit/e8e080dd4c75e43b93cc4d2edbf62249f1241e8a#diff-96760c83be16cde55832ddd77975b1b0L65>`_

**Returns**

A :code:`ModuleResult` with a single :code:`Result` with a :code:`SessionGUID`

.. code-editor:: xml

   <PortalResult Duration="12">
     <ModuleResults>
       <ModuleResult Fullname="Portal" Duration="0" Count="1">
         <Results>
           <Result FullName="CHAOS.Portal.DTO.Standard.Session">
             <SessionGUID>47c72c3c-9126-9549-8517-340c4275e22b</SessionGUID>
             <UserGUID>c0b231e9-7d98-4f52-885e-af4837faa352</UserGUID>
             <DateCreated>03-10-2013 14:00:20</DateCreated>
             <DateModified>03-10-2013 14:00:20</DateModified>
           </Result>
         </Results>
       </ModuleResult>
     </ModuleResults>
   </PortalResult>

**See also**

* :ref:`Authentication -> Login <authentication-login>`
* :ref:`api-emailpassword-login`

.. _api-emailpassword-login:

EmailPassword/Login
-------------------

**Parameters**

 * *email* the user's email
 * *password* the user's password
 * *sessionGUID* the GUID of a recently created session

**Returns**

:code:`CHAOS.Portal.Authentication.Exception.LoginException` on error
and 
:code:`CHAOS.Portal.DTO.Standard.UserInfo` on success

http://api.danskkulturarv.dk/EmailPassword/Login?email=test@example.org&password=mysecret

.. code-editor:: xml

   <PortalResult Duration="23">
     <ModuleResults>
       <ModuleResult Fullname="EmailPassword" Duration="0" Count="1">
         <Results>
           <Result FullName="CHAOS.Portal.DTO.Standard.UserInfo">
             <GUID>80d15fb4-c1fb-9445-89c6-1a398cbd85e5</GUID>
             <SystemPermissions>2</SystemPermissions>
             <Email>admin@danskkulturarv.dk</Email>
             <SessionDateCreated>03-10-2013 14:25:42</SessionDateCreated>
             <SessionDateModified>03-10-2013 14:26:14</SessionDateModified>
           </Result>
         </Results>
       </ModuleResult>
     </ModuleResults>
   </PortalResult>

.. _api-object-setpublishsettings:

Object/SetPublishSettings
-------------------------
Publishes/unpublishes an object on an :code:`accessPointGUID` in a given time
period (or indefinitely). 

You need to be logged in to use this feature.

The :code:`accessPointGUID` must exists in the database in order to publish on
it. As of 7th October 2013 you cannot create an :code:`accessPointGUID` in the
database via the API.

**Parameters**

 * *objectGUID* the GUID of the object for which you want to set :code:`accessPointGUID`
 * *accessPointGUID* the :code:`accessPointGUID` you want to publish on
 * *startDate* (optional) the start of publishing period
 * *endDate* (optional) the end of the publishing period

*startDate* and *endDate* should be in the format 
:code:`DD-MM-YYYY HH:MM:SS` where the first :code:`MM` is month and the seconds
is minutes.
e.g. :code:`03-10-2013 14:25:42` is the 3rd of October 2013, twenty-five minutes
and fourty-two seconds past 2 PM.

If no *startDate* is given the object will is unpublished, i.e. it will not be
accessible from the given accessPoint. That is the following situations will
unpublish the object:



================  ================  ================================
      Publishing
--------------------------------------------------------------------
startDate         endDate           What happens
================  ================  ================================
:rbg:`not given`  :rbg:`not given`  Object is unpublished
:rbg:`not given`  :gbg:`given`      Object is unpublished
:gbg:`given`      :rbg:`not given`  Object is published indefinitely
:gbg:`given`      :gbg:`given`      Object is published in given
                                    time period
================  ================  ================================

.. raw:: html

   <script>
     // depends on jQuery and Bootstrap
     $(document).ready(function() {
       $('.gbg').parent().css('background-color', '#dff0d8');
       $('.rbg').parent().css('background-color', '#f2dede');
     });
   </script>

If *startDate* is given but no *endDate* is given the object will be published
until you change the publish period or remove the accessPoint.


**Returns**

* On success: :code:`CHAOS.Portal.DTO.Standard.ScalarResult` with value :code:`1`
* On error: a number of different errors can be given on erroneous dates,
  accessPointsGUID or objectsGUIDs. If the accessPoint does not exists you will
  get :code:`CHAOS.Portal.Exception.InsufficientPermissionsException`

:chaos_api_link_object_setpublishsettings_apg:`objectGUID=00000000-0000-0000-0000-000000820016&sessionGUID=9755b31c-c0d4-2a47-9605-487b1401d1fa&startDate=01-10-2013+06:00:00`

.. code-editor:: xml

   <PortalResult Duration="104">
    <ModuleResults>
      <ModuleResult Fullname="MCM" Duration="0" Count="1">
        <Results>
          <Result FullName="CHAOS.Portal.DTO.Standard.ScalarResult">
            <Value>1</Value>
          </Result>
        </Results>
      </ModuleResult>
    </ModuleResults>
   </PortalResult>

**See also**

* :ref:`Authentication -> accessPointGUID <authentication-accesspointguid>`
