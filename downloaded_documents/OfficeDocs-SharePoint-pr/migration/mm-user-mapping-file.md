---
title: "Create a user-mapping file for Migration Manager"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
ms.date: 04/02/2025
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- m365initiative-migratetom365
ms.custom: admindeeplinkSPO
search.appverid: MET150
description: "Create a user-mapping file for data content migration when using Migration Manager"
---

# Create a user-mapping file for data content migration in Migration Manager

This article shows how to create a user-mapping file to use with Migration Manager. Use Migration Manager to migrate your files shares to Microsoft 365.
  
## Create a user-mapping file for data content migration

Migration Manager uses a default user-mapping file when migrating your file shares, however, you can choose to create your own using the following guidelines. Create the CSV file using any text editor, or an application like Excel.

### CSV file format

> [!IMPORTANT]
> Don't include a header row in your CSV file.

The following example uses Excel to create the CSV file.

1. Start Excel.
2. Enter the values for your user-mapping.
  - **Column A:** From the source location, enter the **log in name of the user**. *Required.*
  - **Column B:** On the destination site, enter the **principal username**. *Required.*
  - **Column C:** If the principal username on the destination site is an Active Directory (AD) group, enter **TRUE**. If it's not an AD group, enter **FALSE**. *Required.*
3. Close and save as a comma-delimited (\*.csv) file.

### Upload your user-mapping file to Migration Manager

After you create your own user-mapping file, upload it to Migration Manager in the SharePoint Admin Center.
  
1. Go to the [Migration center](https://go.microsoft.com/fwlink/?linkid=2185075) in the SharePoint admin center, and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.
2. Select **Global settings**.
3. Select **All settings**.
4. Select **User mapping file**, and then select **Choose file** to browse to the file to use.
5. Select **Save**.

>[!Note]
> It's not possible to map an AD group to a SharePoint group in the destination site.
