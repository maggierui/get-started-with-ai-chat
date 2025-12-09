---
title: "Transport Layer Security (TLS) 1.3 Support"
ms.reviewer: 
ms.author: serdars
author: serdars
manager: serdars
ms.date: 08/05/2025
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- IT_Sharepoint16
ms.assetid: 
description: "This article describes the supported and unsupported components on Transport Layer Security (TLS) protocol version 1.3."
---

# Transport Layer Security (TLS) 1.3 Support

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

TLS 1.3 is the latest version of the TLS encryption protocol. SharePoint Server Subscription Edition by default supports TLS 1.3 when deployed with Windows Server 2022 and 2021-06 Cumulative Update for .NET Framework 3.5, and 4.8 for Microsoft server operating system x64 (KB5003529).

> [!NOTE]
> TLS 1.3 doesn't require any additional configuration and might not support all software and systems. Microsoft recommends you to contact your software and hardware administrator to check compatibility of TLS 1.3.
>
> TLS 1.3 isn't available and isn't supported when SharePoint Server Subscription Edition is deployed with earlier versions of Windows Server. Microsoft recommends deploying SharePoint Server Subscription Edition with Windows Server 2022 or higher.

Starting from Version 25H1, SharePoint Server Subscription Edition uses [Microsoft.Data.SqlClient](/sql/connect/ado-net/overview-sqlclient-driver) for its database connectivity layer.<br>
The Microsoft.Data.SqlClient database connectivity layer supports advanced security capabilities like Tabular Data Stream (TDS) Version 8.0 and TLS Version 1.3.

## Support for TDS 8.0
SharePoint Server Subscription Edition supports TDS 8.0 while also remaining backward compatible with previous versions of SQL Server that don't support TDS 8.0. TDS 8.0 is currently supported by SQL Server 2022, Azure SQL Database, and Azure SQL Managed Instance.
 
TDS 8.0 supports newer encryption protocols such as TLS 1.3 that older versions of TDS can't support, while maintaining compatibility with older versions of TLS. 

## Support for TLS 1.3
SharePoint Server Subscription Edition adds support for connecting to SQL databases using TLS 1.3 connection encryption, while also remaining backward compatible with previous versions of SQL Server that don't support TLS 1.3 connection encryption. TLS 1.3 is currently supported by SQL Server 2022. SQL Server 2022 and Windows-based applications connecting to it must be running on Windows 11 or Windows Server 2022 (or higher) to be able to use TLS 1.3. 

## Database settings 

The database connectivity layer has the following properties for each SharePoint database (Microsoft.SharePoint.Administration.SPDatabase). 
1. Encrypt ([Microsoft.Data.SqlClient.SqlConnectionEncryptOption](/dotnet/api/microsoft.data.sqlclient.sqlconnectionencryptoption)) 

    1. Optional: Connection encryption can be used if required by the SQL Server. However, if encryption isn't required by the SQL Server, then no connection encryption is used. The connection is limited to using TDS 7.4. 

    2. Mandatory: Connection encryption must be established with the SQL Server. If connection encryption can't be established, then the connection is blocked. The connection is limited to using TDS 7.4. 

    3. Strict: Connection encryption must be established with the SQL Server and the connection must use TDS 8.0 or higher. If connection encryption using TDS 8.0 or higher can't be established, then the connection is blocked. 

1. HostnameInCert (String): Specifies the hostname in the SSL/TLS server certificate of the SQL Server. SharePoint farm administrators should specify this property if the hostname in the certificate doesn't match the hostname that SharePoint connects to. 

### Behaviors when upgrading a farm with existing databases

Databases that are part of a SharePoint farm will be configured to use **Optional** encryption by default. This is to ensure the SharePoint farm remains compatible with the existing SQL Servers in its farm in case they don't support the newer TDS 8.0 and TLS 1.3 protocols. This means SharePoint will continue to use TDS 7.4 when connecting to those databases. If connection encryption is used to connect to those databases, it will be based on TLS 1.2 or lower. 

### Behaviors when adding/editing a database to a farm 

Previously, the settings for all databases are based on the configuration database's settings. Newly created databases that are added to a farm are configured to use the same encryption settings with farm configuration database.

Since 2025 September PU, users can select different connection encryption settings per database, which can be particularly useful when databases are stored on different SQL servers or serve different purposes. This behavior is applicable to both content database and service application database.

#### Create a new content database (only applicable after 2025 September PU)

- To create a new content database, in PowerShell, add the following optional parameters to the `New-SPContentDatabase` cmdlet:

  ```powershell
  -DatabaseConnectionEncryption {Mandatory | Optional | Strict}
  -DatabaseServerCertificateHostName <String>
  ```

  > [!NOTE]
  > DatabaseConnectionEncryption and/or DatabaseServerCertificateHostName are the same as configuration database by default in case you don't specify it.

- To create a new content database, in Central Administration, add two settings on the page.

  :::image type="content" source="media/add-content-db.png" alt-text="Screenshot of add a content database.":::

#### Create a new service application with different encryption database (only applicable after 2025 September PU)

- To create a new service application that has its customized database, in PowerShell, add the following optional parameters to the PowerShell cmdlets:

   ```powershell
  -DatabaseConnectionEncryption {Mandatory | Optional | Strict}
  -DatabaseServerCertificateHostName <String>
  ```
   
  > [!NOTE]
  > DatabaseConnectionEncryption and/or DatabaseServerCertificateHostName are the same as configuration database by default in case you don't specify it.
  
  For example:
  ```powershell
  New-SPMetadataServiceApplication -Name "MetadataServiceApp1" -ApplicationPool "AppPool1" -DatabaseName "MetadataDB1" -DatabaseConnectionEncryption "Mandatory" -DatabaseServerCertificateHostName "SQL-01.internal.contoso.com"
  ```

- To create a new service application that has its customized database, in Central Administration, add the same two settings as content database on the page.

  :::image type="content" source="media/new-svc-app.png" alt-text="Screenshot of create a service application.":::

#### Edit an existing database attached to a service application (only applicable after 2025 September PU)

- To edit a database belongs to a service application, in PowerShell, add the following optional parameters to the PowerShell cmdlets:

  ```powershell
  -DatabaseConnectionEncryption {Mandatory | Optional | Strict}
  -DatabaseServerCertificateHostName <String>
  ```

  For example:
  ```powershell
  $sa = Get-SPMetadataServiceApplication -Identity "Managed Metadata Service Application"
  Set-SPMetadataServiceApplication -Identity $sa -DatabaseName "MetadataDB2" -DatabaseConnectionEncryption "Optional"
  ```

- To edit a database belongs to a service application, in Central Administration, You can change encryption settings by clicking the 'Properties' button.

### Specify encryption settings during PSConfig

#### Creating a new farm

- To create a new farm, in PowerShell, add the following optional parameters to the `New-SPConfigurationDatabase` cmdlet: 
  
  ```powershell
  -DatabaseConnectionEncryption {Mandatory | Optional | Strict} 
  -DatabaseServerCertificateHostName <String>
  ```

  > [!NOTE]
  > DatabaseConnectionEncryption is **Mandatory** by default in case you don't specify it.

  For example: 
  ```powershell 
  New-SPConfigurationDatabase -DatabaseName "SharePointConfigDB1" -DatabaseServer "SQL-01" -DatabaseConnectionEncryption "Mandatory" -DatabaseServerCertificateHostName "SQL-01.internal.contoso.com" -Passphrase (ConvertTo-SecureString "MyPassword" -AsPlainText -force) -FarmCredentials (Get-Credential) -LocalServerRole "Application" 
  ``` 

- In PSConfig.exe, add the following optional parameters to the configdb operation: 

  ```powershell 
  -dbencryption {Mandatory | Optional | Strict} 
  -dbcerthostname <String>
  ```

  > [!NOTE]
  > dbencryption is **Mandatory** by default in case you don't specify it. 

  For example: 
  ```powershell 
  psconfig.exe -cmd configdb -create -database "SharePointConfigDB1" -server "SQL-01" -dbencryption "Mandatory" -dbcerthostname "SQL01.internal.contoso.com" -passphrase "the_passphrase" -user "DOMAIN\username" -password "the_password" -localserverrole "Application" 
  ```

- In the SharePoint Products Configuration Wizard (PSConfigUI.exe), specify the settings in the **Database connection encryption** and **Database server certificate host name** fields in the configuration database form.

  :::image type="content" source="media/config-db-settings.png" alt-text="Screenshot of Configuration Wizard.":::

#### Joining the existing farm
To join the existing farm, you need to specify the encryption settings that the existing farm is using as follows.

1. Select **Database connection encryption** as **Mandatory** if your configuration database is Mandatory encrypt.
1. Enter the **Database server certificate hostname** and click **Retrieve Database Names**.
1. Then you can select the farm that you want the second server to join.

    :::image type="content" source="media/join-farm.png" alt-text="Screenshot of settings for joining existing farm.":::

  Also, run the following PowerShell command to join the farm:
  ```powershell
  Connect-SPConfigurationDatabase -DatabaseServer "SQL-01" -DatabaseName "SharePointConfigDB1" -DatabaseConnectionEncryption Mandatory -DatabaseServerCertificateHostName "SQL-01.internal.contoso.com" -Passphrase (ConvertTo-SecureString "****" -AsPlainText -Force) -LocalServerRole "Application"
  ```
