---
ms.date: 04/04/2025
title: "File & folder permission when using SharePoint Migration Tool"
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
ms.localizationpriority: medium
mscollection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150
ms.assetid:
description: "Learn about what happens to the file and folder permissions when using the SharePoint Migration Tool (SPMT)."
---

# File and folder permissions when using the SharePoint Migration Tool

## What happens to the permissions on a migrated file?

The location of your on-premises data, and whether your Active Directory accounts to Microsoft Entra ID are synchronized or not, can affect the permission settings on your files after they're migrated to SharePoint in Microsoft 365.

**Syncing your environment**: In order to maintain existing on-premises file permissions, there must be a corresponding user in SharePoint. The easiest way to accomplish this permission maintenance is to synchronize your Active Directory accounts to Microsoft Entra ID.

|User mapping type |File share details |SharePoint on-premises file |
|------------------|-------------------|----------------------------|
|User mapped between on-premises and SharePoint |There are three types of permissions that are migrated: **Read**, **Write**, and **Full control**. </br>If a file has **Write** permission for user1, then the file is set to **Contribute** for user1 in SharePoint in Microsoft 365. If a file has **Read** permission for user1, then the file is set to **Read** for user1 in SharePoint. For **Full control** permission, the file is migrated as **Full control** in SharePoint in Microsoft 365. </br>**Note:** At this time, the special permissions, such as **Deny**, aren't saved. |All the unique permissions on a file are migrated to SharePoint in Microsoft 365. Inherited permissions aren't migrated. |
|No user mapping (not synced, no user mapping file) |Files are assigned the default permission of the location to which it's migrated in SharePoint in Microsoft 365. |Files are assigned the default permission of the location to which it's migrated in SharePoint in Microsoft 365. |

### Permissions conditions and results

Various conditions affect the SharePoint Migration Tool's permission control. The following table lists all the conditions and the corresponding results.

|Source |Preserve user permissions setting set to On |Migrating to |Target library permission before migration |Target library permission after migration |Note |
|---|---|---|---|---|---|
|File share |No |Root folder |Inherited |Inherited |Role assignments of the target library and existing files aren't changed; migrated files inherit permission (Inherited role assignments from the target library). |
|File share |No |Root folder |Unique |Unique |Role assignments of the target library and existing files aren't changed. Migrated files inherit permission (Inherited role assignments from the target library). |
|File share |No |Sub folder |Inherited |Inherited |Role assignments of the target library and existing files aren't changed. Migrated files inherit permission (Inherited role assignments from the target library). |
|File share |No |Sub folder |Unique |Unique |Role assignments of the target library and existing files aren't changed. Migrated files inherit permission (Inherited role assignments from the target library). |
|File share |Yes |Root folder |Inherited |Unique |The role assignments in the source root folder replace the role assignments of the target library. Existing files with inherited permissions are still inheriting permissions but with a new role assignment from the target library. Existing files with Unique permissions aren't changed. Migrated files without any permission in the source inherit permissions and role assignments from the target library. Migrated files with any permissions in the source carry over these permissions as unique. |
|File share |Yes |Root folder |Unique |Unique |Permissions from the source folder are added as new role assignments to the target library. Existing files with inherited permissions are still inherited permissions but with a new role assignment from the target library. Existing files with unique permissions aren't changed. Migrated files without any permissions in the source inherit permissions and role assignments from the target library. Migrated files with any permissions in the source carry over these permissions as unique. |
|File share |Yes |Sub folder |Inherited |Inherited |Role assignments of the target library and existing files aren't changed. Permissions from the source folder and files are carried over to the target subfolder and corresponding files, which have unique permissions as new role assignments. |
|File share |Yes |Sub folder |Unique |Unique |Role assignments of the target library and existing files aren't changed. Permissions from the source folder and files are carried over to the target subfolder and corresponding files, which have unique permission as new role assignments. |
|List/Document library |No |Root folder |Inherited |Inherited |The same as file share migration with the same condition. |
|List/Document library |No |Root folder |Unique |Unique |The same as file share migration with the same condition. |
|Document library |No |Sub folder |Inherited |Inherited |The same as File share migration with the same condition. |
|Document library |No |Sub folder |Unique |Unique |The same as file share migration with the same condition. |
|List/Document library |Yes |Root folder |Inherited |Unique |The same as file share migration with the same condition. |
|list/Document library |Yes |Root folder |Unique |Unique |The same as file share migration with the same condition. |
|Document library |Yes |Sub folder |Inherited |Inherited |The same as file share migration with the same condition. |
|Document library |Yes |Sub folder |Unique |Unique |The same as file share migration with the same condition. |
|Site/Web |No |Not applicable |Inherited |Inherited |The role assignment of the target site/web is unchanged. |
|Site/Web |No |Not applicable |Unique |Unique |The role assignment of the target site/web is unchanged. |
|Site/Web |Yes |Not applicable |Inherited |Unique |The role assignment in the source site/web **replace** the role assignment in the target site/web. |
|Site/Web A with Subsite B (both migrated with SPMT) |Yes |Not applicable | | |Subsite B or sub web inherited from main Site A Subsite B/web unique from the new SharePoint main site A. Site A is migrated as described for normal site migration. Subsite B becomes unique Subsite B's role assignments are **replaced**. |
|Site/Web |Yes |Not applicable |Unique |Unique |The role assignment of the source site/web is added as new role assignments to the target site/web. |
