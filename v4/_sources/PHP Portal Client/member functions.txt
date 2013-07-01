Member functions
==============================

.. php:namespace:: CHAOS\Portal\Client

.. php:class:: PortalClient

   .. php:const:: PortalClient:: CLIENT_VERSION = "1.1.1";

   .. php:const:: PortalClient:: PROTOCOL_VERSION = 4;

   .. php:const:: PortalClient:: FORMAT = "json";

   .. php:const:: PortalClient:: USE_HTTP_STATUS_CODES = false;

   .. php:method:: PortalClient::ClientVersion()

      Returns the version of the client.

      :returns: string

   .. php:method:: PortalClient::ProtocolVersion()

      Returns the protocol version used by the client.

      :returns: int

   .. php:method:: PortalClient::SetSessionGUID()

      Sets a session GUID to use.

      :param string $guid: The GUID to use.
      :param bool $isAuthenticated: True if the GUID is authenticated.

   .. php:method:: PortalClient::SessionGUID()

      Returns the currently used session GUID.

      :returns: string

   .. php:method:: PortalClient::HasSession()

      Returns true if the PortalClient instance has a session.

      :returns: bool

   .. php:method:: PortalClient::ClientGUID()

      Returns the client GUID.

      :returns: string

   .. php:method:: PortalClient::__construct()

      :param String $servicePath: The URL of the Portal service.
      :param String $clientGUID: The GUID by which the client is identified.
      :param Bool $autoCreateSession: If true a session will be created in the constructor call.

   .. php:method:: PortalClient::__destruct()

   .. php:method:: PortalClient::CallService()

   .. php:method:: PortalClient::Session()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\ISessionExtension

   .. php:method:: PortalClient::ClientSettings()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IClientSettingsExtension

   .. php:method:: PortalClient::UserSettings()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IUserSEttingsExtension

   .. php:method:: PortalClient::EmailPassword()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IEmailPasswordExtension

   .. php:method:: PortalClient::SecureCooke()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\ISecureCookieExtension

   .. php:method:: PortalClient::Object()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IObjectExtension

   .. php:method:: PortalClient::ObjectRelation()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IObjectRelationExtension

   .. php:method:: PortalClient::ObjectType()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IObjectTypeExtension

   .. php:method:: PortalClient::File()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IFileExtension

   .. php:method:: PortalClient::Folder()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IFolderExtension

   .. php:method:: PortalClient::FolderType()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IFolderTypeExtension

   .. php:method:: PortalClient::Format()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IFormatExtension

   .. php:method:: PortalClient::Language()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\ILanguageExtension

   .. php:method:: PortalClient::Link()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\ILinkExtension

   .. php:method:: PortalClient::Metadata()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IMetadataExtension

   .. php:method:: PortalClient::MetadataSchema()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IMetadataSchemaExtension

   .. php:method:: PortalClient::ObjectRelationType()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IObjectRelationTypeExtension

   .. php:method:: PortalClient::StatsObject()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IStatsObjectExtension

   .. php:method:: PortalClient::Upload()

      :returns: \\CHAOS\\Portal\\Client\\Extensions\\IUploadExtension
