---
ms.date: 03/27/2025
title: "Step 2: Scan and assess Egnyte folders using Migration Manager"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: microsoft-365-migration
ms.localizationpriority: medium
ms.collection:
- m365solution-migratefileshares
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
search.appverid: MET150
ROBOTS: NOINDEX
description: "Step 2:  Scan and assess Egnyte folders using Migration Manager."
---

# Step 2: Scan and assess Egnyte folders

After you connect to Egnyte, add the tasks (source paths) to scan and assess your Egnyte accounts.

1. Select **Add folders** from the menu bar to choose how to add folders:</br> - **All new folders** to autodiscover all new folders in Egnyte</br>- **Single folder** for only one source path,  or </br>- **Multiple specific folders** to bulk upload source paths by entering them into a CSV file to upload.
2. Choose to **Automatically start scanning now** or choose to scan later.
3. Select **Add**.
4. Highlight any or all of the tasks (Egnyte folders) and then select **Scan** from the menu bar if you chose not to auto scan earlier.
5. Once the scan is complete, a table summary displays to give you an at-a-glance overview of source content, scan status, etc.
6. Review the scanned list. Search for specific text, or select a filter to review the list more easily.

>[!Important]
> The total number of rows (tasks) in the scan list cannot exceed 50,000.

## Download reports
**Scan summary report** and **Scan detailed reports** are available to assist you in troubleshooting. [Download the generated reports](/sharepointmigration/mm-cloud-reports#download-scan-reports) to investigate any possible issues that might block your migration. 

Check the [status code](/sharepointmigration/mm-cloud-reports#status-codes) in **Scan summary report** to address task-level errors. For file-level errors, refer to the [failure code (*ResultCode*)](/sharepointmigration/mm-cloud-reports#failure-codes) in the **Scan detailed report**.


## [**Step 3: Copy to migrations**](mm-egnyte-step3-copy-to-migrations.md)
