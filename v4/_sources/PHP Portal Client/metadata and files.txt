========================
Using metadata and files
========================

Grabbing a single object
------------------------
In many cases it will makes sense to only request a single known object. Objects
are identified by their GUID.
We can grab a single object by its GUID with `PortalClient::Object()::GetByObjectGUID()`:

.. code-editor:: php

    <?php
    $serviceResult = $client->Object()->GetByObjectGUID(
      "00000000-0000-0000-0000-00004e040016" // objectGUID
      , $accessPointGUID // accessPointGuid
      , true                          // includeMetadata
      , true                          // includeFiles
      , true                          // includeObjectRelations
      , false                         // includeAccessPoints
    );
    $object = $serviceResult->MCM()->Results()[0];
    echo "Grabbed object (GUID): " . $object->GUID;
    ?>

Files
-----
Files belonging to an object can be of different types -- video, audio, images
and basically any other kind of file. The files can be found in the `Files`
attribute of the objects in :code:`serviceResult->MCM()->Results()`: 

.. code-editor:: php

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
    <?php
    $serviceResult = $client->Object()->GetByObjectGUID(
      "00000000-0000-0000-0000-00004e040016" // objectGUID
      , $accessPointGUID // accessPointGuid
      , true                          // includeMetadata
      , true                          // includeFiles
      , true                          // includeObjectRelations
      , false                         // includeAccessPoints
    );
    $object = $serviceResult->MCM()->Results()[0];

    for ($i = 0; $i < count($object->Files); $i++) {
      $tr = "";
      $tr .= "<tr>";
      $tr .= "<td>" . $object->Files[$i]->FormatType . "</td>";
      $tr .= "<td>" . $object->Files[$i]->Filename . "</td>";
      $tr .= "<td>" . $object->Files[$i]->URL . "</td>";
      if ($object->Files[$i]->FormatType == "Image") {
        $tr .= "<td><img src=\"" . $object->Files[$i]->URL . "\"></td>";
      } else {
        $tr .= "<td>No representation</td>";
      }
      $tr .= "</tr>";
      echo $tr;
    }
    ?>
      </tbody>
    </table>

Running the code you should get the output:

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
          <td>Image</td>
          <td>db_fo_sa_00564.jpg</td>
          <td> http://www.kb.dk/imageService//online_master_arkiv_9/non-archival/Images/BLADTE_VANDMAERKER//db_fo_sa_00564.jpg</td>
          <td><img src="http://www.kb.dk/imageService//online_master_arkiv_9/non-archival/Images/BLADTE_VANDMAERKER//db_fo_sa_00564.jpg"> </td>
        </tr>
        <tr>
          <td>Image</td>
          <td>db_fo_sa_00564.jpg</td>
          <td>http://www.kb.dk/imageService/w150/online_master_arkiv_9/non-archival/Images/BLADTE_VANDMAERKER/db_fo_sa_00564.jpg</td>
          <td><img src="http://www.kb.dk/imageService/w150/online_master_arkiv_9/non-archival/Images/BLADTE_VANDMAERKER/db_fo_sa_00564.jpg"></td>
        </tr>
      </tbody>
    </table>

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
Again, the structure of these XML document is specific to your
database, and I recommend that you familiarize yourself the structure of these
documents before you begin doing serious work with CHAOS. In this case we're
just experimenting and getting to know the interface - so let's have a look. The
metadata can be found in the `Metadatas` attribute of the objects in
`serviceResult->MCM()->Results()`:

`Metadatas` is an array of strings containing XML documents. Let's have a look:

.. code-editor:: php

    <?php
    $serviceResult = $client->Object()->GetByObjectGUID(
      "00000000-0000-0000-0000-00004e040016" // objectGUID
      , $accessPointGUID // accessPointGuid
      , true                          // includeMetadata
      , true                          // includeFiles
      , true                          // includeObjectRelations
      , false                         // includeAccessPoints
    );
    $object = $serviceResult->MCM()->Results()[0];

    echo "<pre>" . $object->Metadatas[1]->MetadataXML . "</pre>";
    ?>

Our object's metadata:

..  <aside class="code" id="search-results">
    <pre><code class="language-json">

.. code-editor:: xml

   <DKA>
     <Title>Uden titel</Title>
     <Abstract>En mand i profil med sideskilning og et mut ansigtsudtryk</Abstract>
     <Description />
     <Organization>Det Kongelige Bibliotek</Organization>
     <Type />
     <CreatedDate>2010-10-06T00:00:00</CreatedDate>
     <FirstPublishedDate>2010-10-06T00:00:00</FirstPublishedDate>
     <Identifier>108593</Identifier>
     <Contributor />
     <Creator>
       <Person Name="ukendt" Role="Creator" />
     </Creator>
     <TechnicalComment />
     <Location />
     <RightsDescription>Billedet er beskyttet af loven om ophavsret</RightsDescription>
     <Categories />
   </DKA>

Parsing XML with PHP can be done in a `number of ways`.
In the following example I will use SimpleXML to parse and access the XML.

.. _`number of ways`: http://www.php.net/manual/en/refs.xml.php

.. code-editor:: php

    <?php
    $serviceResult = $client->Object()->GetByObjectGUID(
      "00000000-0000-0000-0000-00004e040016" // objectGUID
      , $accessPointGUID // accessPointGuid
      , true                          // includeMetadata
      , true                          // includeFiles
      , true                          // includeObjectRelations
      , false                         // includeAccessPoints
    );
    $object = $serviceResult->MCM()->Results()[0];

    $xmlstr = $object->Metadatas[1]->MetadataXML;

    $xmlDoc = new SimpleXMLElement($xmlstr);

    $obj_title = $xmlDoc->Title;
    $obj_desc = $xmlDoc->Abstract;

    echo "Title: " . $obj_title . "<br>";
    echo "Abstract: " . $obj_desc;
    ?>

The result should be:

.. code::

    Title: Uden titel
    Abstract: En mand i profil med sideskilning og et mut ansigtsudtryk

The next section will teach you about handling errors when dealing with CHAOS.Portal.
