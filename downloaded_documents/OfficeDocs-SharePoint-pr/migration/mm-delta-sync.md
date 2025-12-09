---
ms.date: 04/01/2025
title: Delta Sync
ms.reviewer: heidip
ms.author: kbchen
author: MetMS2023
manager: DAPODEAN
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: medium
ms.collection: 
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
description: "Configure file transfer behaviors for delta sync"
---
# Delta Sync

When a migration task is conducted for the first time, we call it an **initial migration** or new migration. After the initial migration, the destination can't be changed. If the task is migrated again, we call it a **delta sync**. We may also call it an incremental sync, or incremental migration.

Migration Manager supports configuring file transfer behaviors for delta sync. The settings can be found under **Project settings – Advanced**.

## Skip files already migrated and transfer only updated or new ones

This default mode skips migrated files, transferring only updated files or newly created files in the source. A file is skipped in the delta sync only when:
- The destination full path (including the file name) remains the same, and,
- The last modified time in the destination is newer than in the source.

>[!NOTE]
> A file isn't migrated if:
>
> - The file is updated in both the source and destination and,
> - The destination file's last modified time is newer.

## Migrate all files and overwrite any existing ones at the destination

In this mode, all files in the source are migrated to the destination again, overwriting those files from previous migrations. Even if the files in the destination are updated, they're still overwritten.

This process takes longer than the default mode.

>[!NOTE]
> Normally, when the source permissions are inherited, the migrated destination permissions are also inherited. However, in special cases where the destination permission is changed to explicit while the source remains inherited, the destination permissions aren't overwritten in this mode.

## Delta sync and permission update 

Permissions are migrated along with the files and are updated only when the corresponding files are migrated in the delta sync. A file's permissions can be updated but its last modified time remains unchanged. In this case, the permission update isn't migrated in the delta sync because the file itself isn't migrated by default.

You can ensure permission updates are migrated even when file content remains unchanged. Select the option to **Migrate all files and overwrite any existing ones at the destination** as the file transfer setting for the delta sync.
