==========
The Basics
==========

Setting up
----------
The first thing to do is to load the PHP Portal Client into your webpage:

.. code-editor:: php

    <?php
    set_include_path(get_include_path() . PATH_SEPARATOR . __DIR__ .
                     "/../src"); // <-- Relative path to Portal Client

    require_once("CaseSensitiveAutoload.php");

    spl_autoload_extensions(".php");
    spl_autoload_register("CaseSensitiveAutoload");

    use CHAOS\Portal\Client\PortalClient;
    ?>

This is just some code for setting up PHP's include path and loading the needed
files.  All you need to worry about is the `"/../src"` which should be the path
from your current PHP file to the PHP Portal Client src directory.

Having loaded the client, we can now instantiate it:

.. code-editor:: php
    :id: setup-code

    <?php
    $servicePath = "http://api.chaos-systems.com/";
    $clientGUID = "B9CBFFDD-3F73-48FC-9D5D-3802FBAD4CBD";
    $accessPointGUID = "C4C2B8DA-A980-11E1-814B-02CEA2621172";

    $client = new PortalClient($servicePath, $clientGUID);

    echo "SessionGUID: " . $client->SessionGUID() . "<br>";
    ?>

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


..  Next we need to set up a session. Session are for logging in with some
    user on the CHAOS.Portal server and thereby authenticating yourself with the
    server. In this case we don't need to login, and a session is automatically
    created for us.

..      <!-- When the session is created, we are ready to grab objects from the CHAOS -->
        <!-- server. We can add event handlers to the SessionAcquired() event &#45; these -->
        <!-- will be called when a session has been set up for us. -->
        </p>

Searching
---------
The easiest way to retrieve some objects from a CHAOS database is to search.
This is done with the method `PortalClient::Object()::GetBySearch()`

.. code-editor:: php

   <?php
   $fields = [
     "5906a41b-feae-48db-bfb7-714b3e105396",
     "00000000-0000-0000-0000-000063c30000",
     "00000000-0000-0000-0000-000065c30000"
   ];

   $serviceResult = $client->Object()->GetSearchSchemas(
     "test",       // search string
     $fields,      // fields to search
     "da",         // language code
     $accessPointGUID,
     0,            // pageIndex
     10,           // pageSize
     true,         // includeMetadata
     true,         // includeFiles
     true          // includeObjectRelations
   );
   $objects = $serviceResult->MCM()->Results();

   echo "Got " . $serviceResult->MCM()->Count() . "/" . $serviceResult->MCM()->TotalCount() . " objects";
   ?>


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

`PortalClient::Object()::GetBySearch()` returns a serviceResult. The serviceResult
has a number of fields, of which `MCM()` is the most important and the one we are
going to be using.

:code:`serviceResult->MCM()->Results()`
The result of the CHAOS query: A list of objects (URL, metadata etc.). An
explaination of these objects is found in the next section.
:code:`serviceResult->MCM()->Count()`
The number of objects on this page, i.e. the number of objects available to you
in the `serviceResult->MCM()->Results()`.  If you want all the objects from a
query at once you will have to increase the pageSize or go through all pages via
pageIndex.
:code:`serviceResult->MCM()->TotalCount()`
The number of objects that matched the query


Now the resulting objects are quite big, so let's only grab one, by
setting pageSize to 1:

.. code-editor:: php

    <?php
    // Retrieve objects
    $serviceResult = $client->Object()->GetSearchSchemas(
      "test",       // search string
      ["5906a41b-feae-48db-bfb7-714b3e105396"],      // fields to search
      "da",         // language code
      $accessPointGUID,
      0,            // pageIndex
      1,           // pageSize
      true,         // includeMetadata
      true,         // includeFiles
      true          // includeObjectRelations
    );
    $objects = $serviceResult->MCM()->Results();

    var_dump($objects[0]);
    ?>

The results you get should look something like this:
(I have Xdebug installed so it might look a little different on your setup)

.. raw:: html

    <pre class='xdebug-var-dump' dir='ltr'>
    <b>object</b>(<i>stdClass</i>)[<i>47</i>]
      <i>public</i> 'GUID' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'00000000-0000-0000-0000-000064faff15'</font> <i>(length=36)</i>
      <i>public</i> 'ObjectTypeID' <font color='#888a85'>=&gt;</font> <small>int</small> <font color='#4e9a06'>36</font>
      <i>public</i> 'DateCreated' <font color='#888a85'>=&gt;</font> <small>int</small> <font color='#4e9a06'>-2147483648</font>
      <i>public</i> 'Metadatas' <font color='#888a85'>=&gt;</font>
        <b>array</b> <i>(size=2)</i>
          0 <font color='#888a85'>=&gt;</font>
            <b>object</b>(<i>stdClass</i>)[<i>48</i>]
              <i>public</i> 'GUID' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'72164e6d-c9ec-f145-8907-b187ec108fe0'</font> <i>(length=36)</i>
              <i>public</i> 'EditingUserGUID' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'80d15fb4-c1fb-9445-89c6-1a398cbd85e5'</font> <i>(length=36)</i>
              <i>public</i> 'LanguageCode' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'da'</font> <i>(length=2)</i>
              <i>public</i> 'MetadataSchemaGUID' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'5906a41b-feae-48db-bfb7-714b3e105396'</font> <i>(length=36)</i>
              <i>public</i> 'RevisionID' <font color='#888a85'>=&gt;</font> <small>int</small> <font color='#4e9a06'>1</font>
              <i>public</i> 'MetadataXML' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'&lt;DKA xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot; xmlns=&quot;http://www.danskkulturarv.dk/DKA2.xsd&quot; xmlns:oa=&quot;http://www.openarchives.org/OAI/2.0/&quot; xmlns:ese=&quot;http://www.europeana.eu/schemas/ese/&quot; xmlns:dc=&quot;http://purl.org/dc/elements/1.1/&quot; xmlns:dcterms=&quot;http://purl.org/dc/terms/&quot; xsi:schemaLocation=&quot;http://www.danskkulturarv.dk/DKA2.xsd ../../Base/schemas/DKA2.xsd&quot;&gt;&lt;Title&gt;Livets gang i Lidenlund&lt;/Title&gt;&lt;Abstract /&gt;&lt;Description&gt;&lt;div xmlns=&quot;http://www.w3.org/1999/xhtml&quot;&gt;&lt;p&gt;Politibetjent StrÃ¸hmer pÃ¥ p'...</font> <i>(length=1592)</i>
              <i>public</i> 'DateCreated' <font color='#888a85'>=&gt;</font> <small>int</small> <font color='#4e9a06'>-2147483648</font>
              <i>public</i> 'FullName' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'CHAOS.MCM.Data.DTO.Metadata'</font> <i>(length=27)</i>
          1 <font color='#888a85'>=&gt;</font>
            <b>object</b>(<i>stdClass</i>)[<i>49</i>]
              <i>public</i> 'GUID' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'c7d38f18-39cb-9a49-b3be-46c1be735f1c'</font> <i>(length=36)</i>
              <i>public</i> 'EditingUserGUID' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'80d15fb4-c1fb-9445-89c6-1a398cbd85e5'</font> <i>(length=36)</i>
              <i>public</i> 'LanguageCode' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'da'</font> <i>(length=2)</i>
              <i>public</i> 'MetadataSchemaGUID' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'00000000-0000-0000-0000-000063c30000'</font> <i>(length=36)</i>
              <i>public</i> 'RevisionID' <font color='#888a85'>=&gt;</font> <small>int</small> <font color='#4e9a06'>1</font>
              <i>public</i> 'MetadataXML' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'&lt;DKA&gt;&lt;Title&gt;Livets gang i Lidenlund&lt;/Title&gt;&lt;Abstract&gt;Politibetjent StrÃ¸hmer pÃ¥ politigÃ¥rden.&lt;/Abstract&gt;&lt;Description /&gt;&lt;Organization&gt;Det Kongelige Bibliotek&lt;/Organization&gt;&lt;Type /&gt;&lt;CreatedDate&gt;2009-12-17T00:00:00&lt;/CreatedDate&gt;&lt;FirstPublishedDate&gt;2009-12-17T00:00:00&lt;/FirstPublishedDate&gt;&lt;Identifier&gt;102188&lt;/Identifier&gt;&lt;Contributor /&gt;&lt;Creator&gt;&lt;Person Name=&quot;Gantriis, Henning (1918-1989) bladtegner&quot; Role=&quot;Creator&quot; /&gt;&lt;/Creator&gt;&lt;TechnicalComment /&gt;&lt;Location /&gt;&lt;RightsDescription&gt;Billedet er beskyttet af loven om op'...</font> <i>(length=559)</i>
              <i>public</i> 'DateCreated' <font color='#888a85'>=&gt;</font> <small>int</small> <font color='#4e9a06'>-2147483648</font>
              <i>public</i> 'FullName' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'CHAOS.MCM.Data.DTO.Metadata'</font> <i>(length=27)</i>
      <i>public</i> 'Files' <font color='#888a85'>=&gt;</font>
        <b>array</b> <i>(size=2)</i>
          0 <font color='#888a85'>=&gt;</font>
            <b>object</b>(<i>stdClass</i>)[<i>50</i>]
              <i>public</i> 'ID' <font color='#888a85'>=&gt;</font> <small>int</small> <font color='#4e9a06'>501377</font>
              <i>public</i> 'ParentID' <font color='#888a85'>=&gt;</font> <font color='#3465a4'>null</font>
              <i>public</i> 'Filename' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'db_henning_gantriis_01384.jpg'</font> <i>(length=29)</i>
              <i>public</i> 'OriginalFilename' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'db_henning_gantriis_01384.jpg'</font> <i>(length=29)</i>
              <i>public</i> 'Token' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'HTTP Download'</font> <i>(length=13)</i>
              <i>public</i> 'URL' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'http://www.kb.dk/imageService//online_master_arkiv_2/non-archival/Images/BLADTE_VANDMAERKER//db_henning_gantriis_01384.jpg'</font> <i>(length=122)</i>
              <i>public</i> 'FormatID' <font color='#888a85'>=&gt;</font> <small>int</small> <font color='#4e9a06'>42</font>
              <i>public</i> 'Format' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'KB Source JPEG '</font> <i>(length=15)</i>
              <i>public</i> 'FormatCategory' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'Image Source'</font> <i>(length=12)</i>
              <i>public</i> 'FormatType' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'Image'</font> <i>(length=5)</i>
              <i>public</i> 'FullName' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'CHAOS.MCM.Data.DTO.FileInfo'</font> <i>(length=27)</i>
          1 <font color='#888a85'>=&gt;</font>
            <b>object</b>(<i>stdClass</i>)[<i>51</i>]
              <i>public</i> 'ID' <font color='#888a85'>=&gt;</font> <small>int</small> <font color='#4e9a06'>3550788</font>
              <i>public</i> 'ParentID' <font color='#888a85'>=&gt;</font> <font color='#3465a4'>null</font>
              <i>public</i> 'Filename' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'db_henning_gantriis_01384.jpg'</font> <i>(length=29)</i>
              <i>public</i> 'OriginalFilename' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'db_henning_gantriis_01384.jpg'</font> <i>(length=29)</i>
              <i>public</i> 'Token' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'HTTP Download'</font> <i>(length=13)</i>
              <i>public</i> 'URL' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'http://www.kb.dk/imageService/w150/online_master_arkiv_2/non-archival/Images/BLADTE_VANDMAERKER/db_henning_gantriis_01384.jpg'</font> <i>(length=125)</i>
              <i>public</i> 'FormatID' <font color='#888a85'>=&gt;</font> <small>int</small> <font color='#4e9a06'>10</font>
              <i>public</i> 'Format' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'SMK asset thumbnail'</font> <i>(length=19)</i>
              <i>public</i> 'FormatCategory' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'SMK asset thumbnail'</font> <i>(length=19)</i>
              <i>public</i> 'FormatType' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'Image'</font> <i>(length=5)</i>
              <i>public</i> 'FullName' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'CHAOS.MCM.Data.DTO.FileInfo'</font> <i>(length=27)</i>
      <i>public</i> 'ObjectRelations' <font color='#888a85'>=&gt;</font>
        <b>array</b> <i>(size=0)</i>
          <i><font color='#888a85'>empty</font></i>
      <i>public</i> 'FullName' <font color='#888a85'>=&gt;</font> <small>string</small> <font color='#cc0000'>'CHAOS.MCM.Data.DTO.Object'</font> <i>(length=25)</i>
    </pre>

What you get from a CHAOS query is an array of objects like the one above. Each
object has a GUID and an ObjectTypeID. Furthermore we can see that each object
has a list of files and a list of metadata.

Try turning off and on :code:`includeFiles` and :code:`includeMetadata` and
changing :code:`pageSize` and :code:`pageIndex` in order to familiarize yourself
with the interface.  Unfortunately this object has no relations.

You are now ready to head on to the next section, which will teach you
how to use files and metadata.

