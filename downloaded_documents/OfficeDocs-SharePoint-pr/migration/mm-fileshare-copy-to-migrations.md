---
ms.date: 03/24/2025
title: "Step 3: Copy to migrations for file share migration"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection:
- m365solution-migratefileshares
- m365solution-migratetom365
- m365solution-scenario 
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
search.appverid: MET150to the migration list in Migration Manager."
description: "Learn how to copy to migrations for file share migration."
---

# Step 3: Copy to migrations for file share migration

After a file share is scanned and determined to be ready, add it to your migration list.

## Add migrations

1. Highlight one or rows from the scanned list. From the menu bar, select **Copy to migrations**.

    :::image type="content" alt-text="File share scan list." source="media/mm-fileshare-scan-list.png" lightbox="media/mm-fileshare-scan-list.png":::

2. Add a destination: OneDrive, SharePoint, or Teams. Select **Next**.

3. Select a SharePoint site destination. Enter the site path and the location within the site from the dropdown list. Select **Next**.

   :::image type="content" alt-text="Select a destination for your file share." source="media/mm-fileshare-copy-migrations-destinations.png":::

4. Depending on the destination you selected:
    - For OneDrive, enter a OneDrive URL or email address and the location/folder name
    - For SharePoint, enter site URL and location
    - For Teams, select the team and the channel

4. Under configure settings, enter a friendly name for your migration.

5. Select an agent group and then review and edit your settings as needed.

6. If you choose **Run later**, select a date and time, and then select **Schedule**.

7. If you choose **Run now**, select **Run**.

   :::image type="content" alt-text="Configure settings for your file share migration." source="media/mm-fileshare-copy-migrations-configure-settings-page.png":::

## Incremental migration

After a migration task is completed, you can rerun it at a later date, allowing you to copy only those new or updated files in the source location. This process is known as incremental migration.

There are two options for incremental migration. You can choose the one that best fits your scenario.

1. **Delta sync** migrates only new or updated items since the last migration, skipping items migrated previously. 

1. **Full incremental** migrates new or updated items by comparing all source items with the destination items.

Delta sync is faster than full incremental, as it processes fewer files. Full incremental is recommended when files are added to the source with a last modified time earlier than the last migration time, which delta sync would miss.

An incremental check of your SharePoint destination environment is performed. Files are evaluated as follows (regardless of an initial or incremental migration):
  
| Status | Result |
|:-----|:-----|
|The modified time of the source file is earlier than the modified time of the target file. |File isn't migrated. |
|A file is removed from the source location. |Already migrated files remain in the target location. |
|Files or lists exist in the SharePoint target location. |Migration skips those existing objects during scan. |
|The time stamp on files or objects in the source location is newer than in the source. |The newer files are migrated. |
|The source is a file share. |Validation for migration is based on the file/folder path. |
|The source is an on-premises SharePoint server. |Validation for migration is based on list item GUID. Use the folder path as a fallback. |
|An already migrated file is renamed or path is changed but still in the same document library. |Incremental migration uses the corresponding source file and overwrites the file. |
|The migrated file is changed in the destination location, but the file name remains the same. |Incremental migration doesn't overwrite the changed file. |

>[!Important]
>We strongly recommend that you don't rename or move migrated files before the final migration is completed. Doing so results in files being overwritten.
