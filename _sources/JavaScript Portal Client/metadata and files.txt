Grabbing a single object
------------------------
In many cases it will makes sense to only request a single known object. Objects
are identified by their GUID, and can be retrieved with
`PortalClient.Object_GetByObjectGUID()`

.. code-editor:: javascript
    :eval:

    // Retrieve object
    client.SessionAcquired().Add(function(sender, sessionGUID) {
      client.Object_GetByObjectGUID(
        showObject                      // callback
        , "00000000-0000-0000-0000-00004e040016" // objectGUID
        , ChaosSettings.accessPointGUID // accessPointGuid
        , true                          // includeMetadata
        , true                          // includeFiles
        , true                          // includeObjectRelations
        , false                         // includeAccessPoints
      );
    });

    function showObject(serviceResult) {
      var obj = serviceResult.MCM().Results()[0];
      alert("Grabbed object (GUID): " + obj.GUID);
    }

Files
-----
Files belonging to an object can be of different types -- video, audio, images
and basically any other kind of file. The files can be found in the Files
attribute of the objects in `serviceResult.MCM().Results()`: 

.. code-editor:: javascript
    :eval:

    // Retrieve object
    client.SessionAcquired().Add(function(sender, sessionGUID) {
      client.Object_GetByObjectGUID(
        showObject                      // callback
        , "00000000-0000-0000-0000-00004e040016" // objectGUID
        , ChaosSettings.accessPointGUID // accessPointGuid
        , true                          // includeMetadata
        , true                          // includeFiles
        , true                          // includeObjectRelations
        , false                         // includeAccessPoints
      );
    });

    function showObject(serviceResult) {
      var obj = serviceResult.MCM().Results()[0];

      // Clear results table
      $('#file-table tbody').html('');

      for (var i = 0; i < obj.Files.length; i++) {
        var tr = "";
        tr += "<tr>";
        tr += "<td>" + obj.Files[i].FormatType + "</td>";
        tr += "<td>" + obj.Files[i].Filename + "</td>";
        tr += "<td>" + obj.Files[i].URL + "</td>";
        if (obj.Files[i].FormatType == "Image") {
          tr += "<td><img src=\"" + obj.Files[i].URL + "\"></td>";
        } else {
          tr += "<td>No representation</td>";
        }
        tr += "</tr>";
        $('#file-table tbody').append(tr);
      }
    }
