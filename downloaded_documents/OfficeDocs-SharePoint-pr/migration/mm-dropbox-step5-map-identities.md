---
ms.date: 03/26/2025
title: "Step 5: Map Dropbox identities with Migration Manager"
ms.reviewer: jhendr
author: MicrosoftHeidi
ms.author: heidip
manager: jtremper
audience: ITPro
f1.keywords:
- CSH
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
search.appverid: MET150
description: "Step 5:  Map Dropbox identities with Migration Manager." 
---

# Step 5: Map identities of Dropbox Drive to Microsoft 365 accounts

Identity Mapping is the process of matching the domain, user, and group identities in the source to those identities in Microsoft 365. This process is important to migration. If identities aren't properly set up before migration, it can result in users losing access to content. It can also result in file metadata being incorrect at the destination.

To map your identities, select **Map identities** from the menu bar on the **Folder migrations** tab.

> [!Important]
> - Before mapping the identities, ensure you have created all the necessary identities (domains, users and groups) in Microsoft 365.
> - Ensure all the required identity entries (domains, users and groups) in the source are fully mapped before migration.

## Automap
By default, Migration Manager automaps the identities for you based on the exact match of identity names between the source and the destination. 

In most cases, automapping is unlikely to map all the identities. You can manually edit individual identities or import identities.

## Edit individual identities

To edit a single mapping discovered in the automapping process:
1. Highlight the row to activate the mapping panel.
2. Input the equivalent Microsoft 365 domain, user, or group.
3. Select **Save**.

## Import identities

If you want to add one single user mapping or group mapping:
1. Select the **Import users and groups** button from the menu bar to activate the importing panel.
2. Choose **Sing user mapping** or **Sing group mapping**.
3. Input the user or group in both the source and the destination textboxes.
4. Select **Save**.

If you have many mappings to edit:
1. Select the **Import users and groups** button from the menu bar to activate the importing panel.
2. Choose **Batch upload**.
3. Download the CSV template to your computer, adding to or modifying the "Microsoft 365 identity" column in the downloaded CSV template. Save your file as a .csv file with any name you wish.
4. Choose **Select file** to upload the file you saved.
5. Select **Save**.

> [!Important]
> Make sure to verify your mappings before uploading the file. The file isn't validated.

## [**Step 6: Migrate and monitor**](mm-Dropbox-step6-migrate-monitor.md)
