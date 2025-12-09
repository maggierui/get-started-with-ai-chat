---
ms.date: 03/26/2025
title: "Review the destination paths for your Dropbox migration with Migration Manager"
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
- m365solutions-migratefileshares
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
search.appverid: MET150
description: Review your destination paths for your Dropbox migration while using Migration Manager.
---
# Step 4: Review destination paths in Migration Manager Dropbox

In the **Folder migrations** tab, review the destination paths of the tasks (Dropbox folders) you moved to the migrations list, making sure they're correct. An account can't be migrated without a destination indicated. Once you start migrating content to a destination, the destination can't be modified.

## Edit a destination

If a destination is missing on a single task (Dropbox folder), highlight the row and update the value.

1. Highlight the row. A panel displays. Under **Destination**, select **Edit**.
2. You have the choice of selecting a OneDrive, SharePoint, or Teams path as a destination. Depending on your selection:

    - For OneDrive, enter the OneDrive URL or email address and the location/folder name
    - For SharePoint, enter site URL and location
    - For Teams, select the team and the channel

3. Select **Save path**.

>[!Note]
> Destinations might not be visible on the UI due to admin access limitations, multi-geo tenant issues, recent site creation delays, or special characters in the destination path.  If you cannot locate a destination in the "Edit destination" panel, please upload the data using a CSV file as described in the next section.

## Upload destinations using a CSV file

If there are many destinations to edit, you can choose to upload a bulk destinations CSV file. 

![upload destinations for Google accounts bulk.](media/mm-google-bulk-upload-destination-panel.png)

1. Select **Upload destinations** from the menu bar to activate the upload destinations panel.
2. Download the CSV template to your computer. The template lists all never-run migration tasks.
3. Input your destinations in the correct [destination path format](#destination-path-format) by adding to or modifying the "Destination path (to be added/modified)" column in the downloaded CSV template. Save your file as a .csv file with any name you wish.
4. Select the **Browse** button to upload the file you saved. The destinations are validated upon uploading. The validation process may take a while and a validation report is generated if issues are found. We strongly recommend you complete the validation.
5. Ensure all destinations pass the validation, then select **Save**.

>[!Note]
>Rows with vacant destination paths are skipped in the validation process.

### Destination path format

|Type|Format|Example|
|:-----|:-----|:-----|
|SharePoint URL |https://<*tenant*>.sharepoint.com/sites/<*site name*>/<*library name*>/<*optional folder name*> |https://contoso.sharepoint.com/sites/sitecollection/Shared Documents </br>https://contoso.sharepoint.com/sites/sitecollection/Shared Documents/SubFolder |
|OneDrive UPN |name@example.com |user@contoso.onmicrosoft.com |
|OneDrive URL |https://<*tenant name*>-my.sharepoint.com/personal/<*user principal name*>/Documents/<*optional folder name*> |https://contoso-my.sharepoint.com/personal/user_contoso_onmicrosoft_com/Documents </br>https://contoso-my.sharepoint.com/personal/user_contoso_onmicrosoft_com/Documents/SubFolder |

## Pre-provision OneDrive

If you choose OneDrive as the destination, [pre-provision OneDrive for users in your organization](/SharePoint/pre-provision-accounts) before migration. Otherwise, the OneDrive destinations aren't going to pass validation, causing migrations to fail.

## Go to [**Step 5: Map identities**](mm-google-step5-map-identities.md)
