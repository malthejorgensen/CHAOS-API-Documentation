CHAOS.Portal JavaScript Client
==============================

Setting up
----------
Import the Javascript CHAOS.Portal Client into your site.

.. code-block:: html

    <script src="CHAOS.Portal.Client.PortalClient.js" type="text/javascript"></script>

The first thing we need to do is to instantiate the client.

.. code-editor:: javascript
    :linenos:

    // Setup settings
    var ChaosSettings = {
      "servicePath":"http://api.chaos-systems.com/",
      "clientGUID":"9f62060c-64ff-e14f-a8d5-d85a1e2e21b8",
      "accessPointGUID":"C4C2B8DA-A980-11E1-814B-02CEA2621172",
    };
    // Instantiate client
    var client = new PortalClient(
                       ChaosSettings.servicePath,
                       ChaosSettings.clientGUID
                     );

* :code:`servicePath`
  is the URL at which your CHAOS.Portal is set up.
* :code:`clientGUID`
  should be unique for each application, any GUID can be used.
* :code:`accessPointGUID`
  is an ID that authenticates us to use the CHAOS.Portal. This
  should be given to you by your friendly neighbourhood CHAOS.Portal
  administrator.

Instantiating the :code:`PortalClient` this way automatically
sets up a session. When the session has been set up we are ready to use
the CHAOS.Portal.

We can add callbacks to :code:`PortalClient.SessionAcquired()` in
order to do work when the session has been set up:

..  Next we need to set up a session. Session are for logging in with some
    user on the CHAOS.Portal server and thereby authenticating yourself with the
    server. In this case we don't need to login, and a session is automatically
    created for us.

..      <!-- When the session is created, we are ready to grab objects from the CHAOS -->
        <!-- server. We can add event handlers to the SessionAcquired() event &#45; these -->
        <!-- will be called when a session has been set up for us. -->
        </p>

.. code-editor:: javascript
    :eval:

    client.SessionAcquired().Add(function(sender, sessionGUID) {
          alert("Session created: " + sessionGUID);
    });

Now we are ready to get some objects!

Searching
---------
The easiest way to retrieve some objects from a CHAOS database is to
search. You can do this with the function
:code:`PortalClient.Object_GetBySearch()`

.. code-editor:: javascript
    :eval:

    // Add search schemas
    var fields = [
      "5906a41b-feae-48db-bfb7-714b3e105396",
      "00000000-0000-0000-0000-000063c30000",
      "00000000-0000-0000-0000-000065c30000"
    ];
    // Retrieve objects
    client.SessionAcquired().Add(function(sender, sessionGUID) {
      client.Object_GetBySearch(
        showObjects                     // callback
        , "mut"                         // query
        , fields                        // fields
        , "da"                          // langCode
        , null                          // sort
        , ChaosSettings.accessPointGUID // accessPointGuid
        , 0                             // pageIndex
        , 3                             // pageSize
        , true                          // includeMetadata
        , true                          // includeFiles
        , true                          // includeObjectRelations
        , false                         // includeAccessPoints
      );
    });

    function showObjects(serviceResult) {
      var count = serviceResult.MCM().Count();
      var totalcount = serviceResult.MCM().TotalCount();
      alert("Got " + count + "/" + totalcount + " objects");
    }


:code:`fields`
  are search fields to use in the Solr index. The long GUIDs refers to
  metadata schemas. So what we're doing here is searching the object
  metadata for the word 'mut'.  
:code:`pageIndex`
  is the starting page of the search results, where the page size is
  determined by :code:`pageSize`
:code:`pageSize`
  is the number of results you want retrieve  
:code:`includeFiles`
  include files attached to objects in the results.  
:code:`includeMetadata`
  include metadata attached to objects in the results.  
:code:`includeObjectRelations`
  include object relations for an object in the results.  

When the search results has been recieved from the CHAOS.Portal, the
callback is invoked with :code:`serviceResult` as its argument.
The :code:`serviceResult` has a number of fields, of which
:code:`MCM()` is the most important and the one we are going to be
using.

:code:`serviceResult.MCM().Results()`
  The result of the CHAOS query: A list of objects (URL, metadata
  etc.). An explaination of these objects is found in the next section.  
:code:`serviceResult.MCM().Count()`
  The number of objects on this page, i.e. the number of  objects available
  to you in the :code:`serviceResult.MCM().Results()`.<br>
  If you want all the objects from a query at
  once you will have to increase the :code:`pageSize` or go through
  all pages via :code:`pageIndex`.  
:code:`serviceResult.MCM().TotalCount()`
  The number of objects that matched the query  

Now the resulting objects are quite big, so let's only grab one, by
setting pageSize to 1:

.. code-editor:: javascript
    :eval:

    // Retrieve objects
    client.SessionAcquired().Add(function(sender, sessionGUID) {
      client.Object_GetBySearch(
        showObjects                     // callback
        , "mut"                         // query
        , "5906a41b-feae-48db-bfb7-714b3e105396" // schemas
        , "da"                          // langCode
        , null                          // sort
        , ChaosSettings.accessPointGUID // accessPointGuid
        , 0                             // pageIndex
        , 1                             // pageSize
        , true                          // includeMetadata
        , true                          // includeFiles
        , true                          // includeObjectRelations
        , false                         // includeAccessPoints
      );
    });

    function showObjects(serviceResult) {
      var json_result = serviceResult.MCM().Results();

      // The code below is simply for showing you the JSON results
      var string_result = JSON.stringify(json_result, null, '\t').replace('&lt;', '&amp;lt;').replace('&gt;', '&amp;gt;')
      $('#search-results').data('codeMirror').setValue(string_result);
    }

Results:

..  <aside class="code" id="search-results">
    <pre><code class="language-json">

.. code-editor:: json
    :id: search-results

    // The result should look something like this
    [
      {
        "GUID": "00000000-0000-0000-0000-00004e040016",
        "ObjectTypeID": 36,
        "DateCreated": -2147483648,
        "Metadatas": [
          {
            "GUID": "29d669cf-c3e5-4749-beb9-20bb7ac18b05",
            "EditingUserGUID": "80d15fb4-c1fb-9445-89c6-1a398cbd85e5",
            "LanguageCode": "da",
            "MetadataSchemaGUID": "5906a41b-feae-48db-bfb7-714b3e105396",
            "RevisionID": 1,
            "MetadataXML": "&lt;some&gt;&lt;xml&gt;&lt;data&gt;&lt;/data&gt;&lt;/xml&gt;&lt;/some&gt;",
            "DateCreated": -2147483648,
            "FullName": "CHAOS.MCM.Data.DTO.Metadata"
          }
          //, ... more metadata
        ],
        "Files": [
          {
            "ID": 506457,
            "ParentID": null,
            "Filename": "db_fo_sa_00564.jpg",
            "OriginalFilename": "db_fo_sa_00564.jpg",
            "Token": "HTTP Download",
            "URL": "http://example.org/some/url/to/a/file.jpg",
            "FormatID": 42,
            "Format": "KB Source JPEG ",
            "FormatCategory": "Image Source",
            "FormatType": "Image",
            "FullName": "CHAOS.MCM.Data.DTO.FileInfo"
          }
          //, ... more files
        ],
        "ObjectRelations": [],
        "FullName": "CHAOS.MCM.Data.DTO.Object"
      }
    ]

What you can see here is that we get a list of objects. Each object
has a GUID and an ObjectTypeID. Furthermore we can see that each object
has a list of files and a list of metadata.

Try turning off and on :code:`includeFiles` and
:code:`includeMetadata` and changing :code:`pageSize` and
:code:`pageIndex` in order to
familiarize yourself with the interface.
Unfortunately this object has no relations.

You are now ready to head on to the next section, which will teach you
how to use files and metadata.

Member functions
----------------

.. js:class:: PortalClient(servicePath[, clientGUID, autoCreateSession=true])

   :param string name: URL of the CHAOS Portal service
   :param string clientGUID: A GUID identifying this client service
   :param bool autoCreateSession: Create session automatically

The class of the Javascript client through which all communication with CHAOS
Portal goes.


.. js:function:: PortalClient.Folder_Get(callback, id, folderTypeID, parentID)

   :param function(serviceResult) callback: Function to be called with `serviceResult`.
   :param int id: Folder ID

.. js:function:: PortalClient.Object_Get(callback, query, sort, accessPointGUID, pageIndex, pageSize[, includeMetadata, includeFiles, includeObjectRelations, includeAccessPoints])

   :param function(serviceResult) callback: Function to be called with `serviceResult`.
   :param string query: Solr query to get objects by
   :param bool sort: Can be `null`
   :param string accessPointGUID: GUID identifying the accessPoint and thus authenticating the call
   :param int pageIndex: Which page to get in pagination
   :param int pageSize: Size of each page in pagination

CHAOS paginates all result so you need to specify a page size (`pageSize`) and a
page index (`pageIndex`) that specifies which page of objects should be
returned.

.. js:function:: PortalClient.Object_GetBySearch(callback, searchString, schemas, langCode, sort, accessPointGUID, pageIndex, pageSize[, includeMetadata, includeFiles, includeObjectRelations, includeAccessPoints])

   :param function(serviceResult) callback: Function to be called with `serviceResult`.
   :param string searchString: Solr query to get objects by
   :param string|array schemas: A string or an array of strings of the schemas to be searched
   :param string langCode: The language code that should be used for search, e.g. `da_dk`, `en_us`
   :param bool sort: Can be `null`
   :param string accessPointGUID: GUID identifying the accessPoint thereby authenticating the call
   :param int pageIndex: Which page to get in pagination
   :param int pageSize: Size of each page in pagination



