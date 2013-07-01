
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

