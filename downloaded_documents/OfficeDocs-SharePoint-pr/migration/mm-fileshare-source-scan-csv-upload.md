---
ms.date: 04/02/2025
title: "Upload file share sources to Migration Manager using a CSV file."
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- CSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
description: "Bulk upload file share sources to scan in Migration Manager."
---

# Upload file share sources using a CSV file

Migration Manager lets you use a comma-separated (CSV) file to bulk upload your file share sources to scan. Create the CSV file using any text editor, or an application like Excel. You can also download the blank CSV template from Migration Manager file share workflow.

:::image type="content" source="media/mm-fileshare-upload-csv.png" alt-text="Fileshare source choice screenshot.":::

- **Column heading**. You can optionally use the column headings in your CSV file to make your file easier to read.
- **UTF-8**. The encoding of the CSV file must be UTF-8.

## Create and format your file

Create a single column CSV file. There's only one column, the source path.

 :::image type="content" source="media/mm-fileshare-addsource-upload.png" alt-text="Upload a file share csv file.":::

The following example creates the CSV file using Excel.
  
1. Start Excel.
2. Enter source paths. Enter one source path per row. *Required.*
3. Close and save as a Comma delimited (\*.csv) file.

  :::image type="content" source="media/mm-fileshare-scan-csv.png" alt-text="A screenshot of a sample csv in Excel.":::
