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
