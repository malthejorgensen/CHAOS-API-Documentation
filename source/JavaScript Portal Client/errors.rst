==============
Error handling
==============

Let's make a call that will return an error:

.. code-editor:: javascript
   :eval:

   client.SessionAcquired().Add(function(sender, sessionGUID) {
     client.Object_GetBySearch(showObjects, // callback
       {
         query: "*"
       , schemas: "5906a41b-feae-48db-bfb7-714b3e105396"
       , langCode: "da"
       , sort: null
       , accessPointGUID: ChaosSettings.accessPointGUID
       , pageIndex: 0
       , pageSize: 3
       }
     );
   });

   function showObjects(serviceResult) {
     if (serviceResult.WasSuccess() && serviceResult.MCM().WasSuccess()) {
       var count = serviceResult.MCM().Count();
       var totalcount = serviceResult.MCM().TotalCount();
       alert("Got " + count + "/" + totalcount + " objects");
       console.log(serviceResult.MCM().Results());
     } else {
       if (!serviceResult.WasSuccess()) {
         alert("Portal error: " + serviceResult.Error());
         console.log(serviceResult.Error());
       } else if (!serviceResult.MCM().WasSuccess()) {
         alert("MCM error: " + serviceResult.MCM().Error());
         console.log(serviceResult.MCM().Error());
       }
     }
   }

Running this code you should get:
:code:`MCM error: The remote server returned an error: (400) Bad Request.`
Not much help there.

Let's have a more thorough look, by adding :code:`MCM().Exception` and
:code:`MCM().Stacktrace()`


.. code-editor:: javascript
   :eval:

   client.SessionAcquired().Add(function(sender, sessionGUID) {
     client.Object_GetBySearch(showObjects, // callback
       {
         query: "*"
       , schemas: "5906a41b-feae-48db-bfb7-714b3e105396"
       , langCode: "da"
       , sort: null
       , accessPointGUID: ChaosSettings.accessPointGUID
       , pageIndex: 0
       , pageSize: 3
       }
     );
   });

   function showObjects(serviceResult) {
     if (serviceResult.WasSuccess() && serviceResult.MCM().WasSuccess()) {
       var count = serviceResult.MCM().Count();
       var totalcount = serviceResult.MCM().TotalCount();
       alert("Got " + count + "/" + totalcount + " objects");
       console.log(serviceResult.MCM().Results());
     } else {
       if (!serviceResult.WasSuccess()) {
         alert("Portal error: " + serviceResult.Error());
         console.log(serviceResult.Error());
       } else if (!serviceResult.MCM().WasSuccess()) {
         var err_msg = [
           "Exception: " + serviceResult.MCM().Exception() + "\n\n",
           "Message: " + serviceResult.MCM().Error() + "\n\n",
           "Stacktrace: " + serviceResult.MCM().Stacktrace() + "\n"
         ].join('');
         alert(err_msg);
       }
     }
   }

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

.. note::

   A basic rule of thumb is to check whether :code:`TotalCount()` is :code:`null`.
   This is usually indicates an error and in a production environment you should
   display something along the lines of "An error occurred when using CHAOS".

I encourage you to explore and play around with the interface
– Have fun!
