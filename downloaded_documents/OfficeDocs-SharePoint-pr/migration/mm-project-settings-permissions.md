---
title: "Permission settings in Migration Manager"
ms.date: 03/11/2025
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
- m365initiative-migratetom365
search.appverid: MET150
description: Learn about configuring project permissions in Migration Manager.
---
# Permission settings in Migration Manager

Review your settings to ensure that the same users with access to files, folders, and metadata will continue to have access after migration.

## Migrate permissions
Permissions are migrated along with the files. During the initial migration, all permissions are migrated. In the delta sync (incremental migration), permissions are only migrated when the corresponding files are transferred. Learn more about [delta sync and permission update](mm-delta-sync.md).

To correctly migrate permissions, please ensure:
- [Identity mapping](#map-identities) is completed before any migration.
- Permission settings are configured as needed:
  + Folder permissions: By default, Migration Manager migrates folders permissions. File permissions aren't migrated, and destination files inherit parent folder permissions.
  + File permissions: File permissions migration can be enabled in the Project settings. Once enabled, the destination file permissions will be the same as they are in the source. This ensures that migrated files are shared with the same users as before migration.

After migration, the permission roles in Microsoft 365:

|**Cloud source**|**Permission role in the source**|**Permission role in OneDrive/SharePoint**|
|:-----|:-----|:-----|
|Google Personal Drive	|Owner	|Owner|
|Google Personal Drive	|Editor	|Can edit|
|Google Personal Drive	|Commenter/Viewer	|Can view|
|Google Shared Drive	|Manager/Content Manager/Contributor	|Can edit|
|Google Shared Drive	|Commenter/Viewer	|Can view|
|Box	|Owner	|Owner|
|Box	|Co-owner/Viewer Uploader/Previewer Uploader/Uploader/Editor	|Can edit|
|Box	|Previewer/Viewer	|Can view|
|Dropbox	|Owner	|Owner|
|Dropbox	|Editor	|Can edit|
|Dropbox	|Viewer	|Can view|
|Egnyte	|Owner	|Owner|
|Egnyte	|Full/Editor	|Can edit|
|Egnyte	|Viewer	|Can view|

> [!Note]
> - Migrating file permissions may slow down your migration process.
> - When migrating to the document library in a SharePoint site, if you choose the library as the destination, the root folder permissions in the source will not be migrated. To avoid this, please create a folder in the library and assign it as the destination.
> - Currently, group mapping of Egnyte is not supported, so group permissions in Egnyte are not migrated.

## Map identities

Identity Mapping is when you match the user and group identities that have access to your source environment and map those identities to Microsoft 365 user and group identities. This process is important to migration. If identities aren't properly set up prior to migration, it can result in users losing access to content. It can also result in information being incorrect at the destination.

Learn more about identity mapping for different cloud scenarios:

- [Google Drive](mm-google-step5-map-identities.md)

- [Dropbox](mm-dropbox-step5-map-identities.md)

- [Box](mm-box-step5-map-identities.md)

- [Egnyte](mm-egnyte-step5-map-identities.md)

> [!Note]
> When migrating Google shared drive permissions, we recommend you do the following:
> - Recreate a Microsoft 365 group that has the same memberships as the Google Drive group. You can either create a new group, or edit the group linked to the Team site which you designate as the migration destination of the Google shared drive.
> - In the "Map identites" setting, map the original Google Drive group of the shared Drive to the Microsoft 365 group recreated above.
