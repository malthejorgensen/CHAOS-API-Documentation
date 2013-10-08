==============
Error handling
==============

Let's make a call that will return an error:

.. code-editor:: php

    <?php
    $serviceResult = $client->Object()->GetSearchSchemas(
      "*",       // search string
      array("5906a41b-feae-48db-bfb7-714b3e105396"), // fields/schemas to search
      "da",         // language code
      $accessPointGUID,
      0,            // pageIndex
      10,           // pageSize
      true,         // includeMetadata
      true,         // includeFiles
      true          // includeObjectRelations
    );


    if ($serviceResult->WasSuccess() && $serviceResult->MCM()->WasSuccess()) {
      $count = $serviceResult->MCM()->Count();
      $totalcount = $serviceResult->MCM()->TotalCount();
      echo "Got " . $count . "/" . $totalcount . " objects<br>";

      $object = $serviceResult->MCM()->Results()[0];
      echo "Grabbed object (GUID): " . $object->GUID;
    } else {
      if (!$serviceResult->WasSuccess()) {
        echo "Portal error: " . $serviceResult->Error()->Message() . "<br>";
      } else if (!$serviceResult->MCM()->WasSuccess()) {
        echo "MCM error: " . $serviceResult->MCM()->Error()->Message() . "<br>";
      }
    }
    ?>

Running this code you should get:
:code:`MCM error: The remote server returned an error: (400) Bad Request.`
Not much help there.

Let's have a more thorough look, by adding :code:`MCM()->Exception` and
:code:`MCM()->Stacktrace()`


.. code-editor:: php

    <?php
    $serviceResult = $client->Object()->GetSearchSchemas(
      "*",       // search string
      array("5906a41b-feae-48db-bfb7-714b3e105396"), // fields/schemas to search
      "da",         // language code
      $accessPointGUID,
      0,            // pageIndex
      10,           // pageSize
      true,         // includeMetadata
      true,         // includeFiles
      true          // includeObjectRelations
    );

    if ($serviceResult->WasSuccess() && $serviceResult->MCM()->WasSuccess()) {
      $count = $serviceResult->MCM()->Count();
      $totalcount = $serviceResult->MCM()->TotalCount();
      echo "Got " . $count . "/" . $totalcount . " objects<br>";

      $object = $serviceResult->MCM()->Results()[0];
      echo "Grabbed object (GUID): " . $object->GUID;
    } else {
      if (!$serviceResult->WasSuccess()) {
        echo "Portal error: " . $serviceResult->Error()->Message();
      } else if (!$serviceResult->MCM()->WasSuccess()) {
        $error = $serviceResult->MCM()->Error();

        $err_msg = "Exception: " . $error->Name() . "<br>";
        $err_msg .= "Message: " . $error->Message() . "<br>";
        $err_msg .= "Stacktrace: <pre>" . $error->Stacktrace() . "</pre>";
        echo $err_msg;
      }
    }
    ?>

If you run that you should get

.. code::

    Exception: System.Net.WebException
    Message: The remote server returned an error: (400) Bad Request.
    Stacktrace:
       at System.Net.HttpWebRequest.GetResponse()
       at CHAOS.Index.Solr.Solr.SendRequest(SolrCoreConnection core, HttpMethod method, String command, String data)
       at CHAOS.Index.Solr.Solr.Get[TReturnType](IQuery query)
       at CHAOS.MCM.Module.ObjectModule.Get(ICallContext callContext, IQuery query, UUID accessPointGUID, Nullable`1 includeMetadata, Nullable`1 includeFiles, Nullable`1 includeObjectRelations, Nullable`1 includeAccessPoints)

Now that's quite a mouthful! |br|
Let's have a closer look: Neither the message nor the exception type is useful.
But from the stacktrace you should see is that there was an error in the request
to Solr. So there's probably something wrong with our search string.

We are trying to search for :code:`*` – which is everything. This is not allowed on this
particular field in the Solr index (you can assume that this is the case for
most fields).

In general CHAOS.Portal can give quite a large range of errors. Giving an
accessPointGUID that is too short or too long typically results in a
:code:`System.ArgumentOutOfRangeException: Index and length must refer to a location
within the string.`
But if the accessPointGUID contains invalid characters (non-hex: 0-F) it returns:
:code:`System.FormatException: Could not find any recognizable digits.`
In other words, the CHAOS.Portal error handling is not complete yet.

I encourage you to explore and play around with the interface
– Have fun!
