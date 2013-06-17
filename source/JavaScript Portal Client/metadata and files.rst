========================
Using metadata and files
========================

Grabbing a single object
------------------------
In many cases it will makes sense to only request a single known object. Objects
are identified by their GUID, and can be retrieved with
:code:`PortalClient.Object_GetByObjectGUID()`

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
attribute of the objects in :code:`serviceResult.MCM().Results()`: 

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
          tr += '<td><img src="' + obj.Files[i].URL + '"></td>';
        } else {
          tr += "<td>No representation</td>";
        }
        tr += "</tr>";
        $('#file-table tbody').append(tr);
      }
    }

.. raw:: html

   <table id="file-table">
     <thead>
       <tr>
         <th>FormatType</th>
         <th>Filename</th>
         <th>URL</th>
         <th>Representation</th>
       </tr>
     </thead>
     <tbody>
       <tr>
         <td>Some file format</td>
         <td>example.tiff</td>
         <td>http://example.org/patd/example.tiff</td>
         <td>Try to show the file</td>
       </tr>
     </tbody>
   </table>
   </section>

Metadata
--------
Now, we have an object and possibly some files related to it. But we might still
have some questions: What's the name of the object? What color does it have?
What length? Texture?  Taste? |br|
-- and what noise does it make when it's out of paper? |br|
These are questions for the metadata.

The CHAOS database can be filled with all kinds of objects. What kind of objects
you can expect to get from your specific database  should be known to you
already. Or at the latest when you start working with your CHAOS database.

*The metadata of an object is a list of XML documents with related XML schemas*.
Again, the structure of these XML document is specific to your specific
database, and I recommend that you familiarize yourself the structure of these
documents before you begin doing serious work with CHAOS. In this case we're
just experimenting and getting to know the interface - so let's have a look. The
metadata can be found in the Metadatas attribute of the objects in
serviceResult.MCM().Results():

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
     var metadata = obj.Metadatas;

     var string_result = JSON.stringify(metadata, null, '\t').replace('<', '&lt;').replace('>', '&gt;')
     $('#metadata-results').data('codeMirror').setValue(string_result);
   }

Our object's metadata:

..  <aside class="code" id="search-results">
    <pre><code class="language-json">

.. code-editor:: json
    :id: metadata-results

    // The result should look something like this
    [
      {
        "GUID": "29d669cf-c3e5-4749-beb9-20bb7ac18b05",
        "EditingUserGUID": "80d15fb4-c1fb-9445-89c6-1a398cbd85e5",
        "LanguageCode": "da",
        "MetadataSchemaGUID": "5906a41b-feae-48db-bfb7-714b3e105396",
        "RevisionID": 1,
        "MetadataXML": "<DKA xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"http://www.danskkulturarv.dk/DKA2.xsd\" xmlns:oa=\"http://www.openarchives.org/OAI/2.0/\" xmlns:ese=\"http://www.europeana.eu/schemas/ese/\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:dcterms=\"http://purl.org/dc/terms/\" xsi:schemaLocation=\"http://www.danskkulturarv.dk/DKA2.xsd ../../Base/schemas/DKA2.xsd\"><Title>Uden titel</Title><Abstract /><Description><div xmlns=\"http://www.w3.org/1999/xhtml\"><p>En mand i profil med sideskilning og et mut ansigtsudtryk</p><p>Tusch</p><p><strong><a target=\"_blank\" href=\"http://www.kb.dk/images/billed/2010/okt/billeder/da/\">\r\n\t\t\tMere fra samme udgivelse</a></strong></p></div></Description><Organization>The Royal Library: The National Library of Denmark and Copenhagen University Library</Organization><ExternalURL>http://www.kb.dk/images/billed/2010/okt/billeder/object108593/en/</ExternalURL><ExternalIdentifier>oai:kb.dk:oai:kb.dk:images:billed:2010:okt:billeder:object108593</ExternalIdentifier><Type>IMAGE</Type><Contributors /><Creators><Creator Role=\"creator\" Name=\"ukendt\" /></Creators><TechnicalComment /><Location /><RightsDescription>Copyright © The Royal Library: The National Library of Denmark and Copenhagen University Library</RightsDescription><Categories /><Tags /></DKA>",
        "DateCreated": -2147483648,
        "FullName": "CHAOS.MCM.Data.DTO.Metadata"
      },
      {
        "GUID": "cde9176a-d4c9-ad4f-b8f0-aaede63764d0",
        "EditingUserGUID": "80d15fb4-c1fb-9445-89c6-1a398cbd85e5",
        "LanguageCode": "da",
        "MetadataSchemaGUID": "00000000-0000-0000-0000-000063c30000",
        "RevisionID": 1,
        "MetadataXML": "<DKA><Title>Uden titel</Title><Abstract>En mand i profil med sideskilning og et mut ansigtsudtryk</Abstract><Description /><Organization>Det Kongelige Bibliotek</Organization><Type /><CreatedDate>2010-10-06T00:00:00</CreatedDate><FirstPublishedDate>2010-10-06T00:00:00</FirstPublishedDate><Identifier>108593</Identifier><Contributor /><Creator><Person Name=\"ukendt\" Role=\"Creator\" /></Creator><TechnicalComment /><Location /><RightsDescription>Billedet er beskyttet af loven om ophavsret</RightsDescription><Categories /></DKA>",
        "DateCreated": -2147483648,
        "FullName": "CHAOS.MCM.Data.DTO.Metadata"
      }
    ]

Parsing XML with Javascript can be `tricky business`_. I recommend using a library
such as jQuery. In the following example we are using jQuery_ 1.9.1 to parse and
retrieve data from the XML.

.. _`tricky business`: http://stackoverflow.com/a/8412989/118608
.. _jQuery: http://jquery.com/

.. code-editor:: javascript
   :eval:

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
      var metadata = obj.Metadatas;
      var xml = metadata[1].MetadataXML;

      var xmlDoc = $.parseXML( xml ); // XML document
      var $xmlDoc = $( xmlDoc ); // jQuery XML document


      var obj_title = $xmlDoc.find("Title").text();
      var obj_desc = $xmlDoc.find("Abstract").text();

      alert(obj_title + "\n" + obj_desc);
    }

The next section will teach you about handling errors when dealing with
CHAOS.Portal.
