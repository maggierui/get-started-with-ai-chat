---
ms.date: 04/07/2025
title: Migrating OneNote folders with the SharePoint Migration Tool (SPMT)
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
description: "How to migrate OneNote folder using the SharePoint Migration Tool SPMT."
---

# How the SharePoint Migration Tool (SPMT) migrates OneNote folders

The SharePoint Migration Tool (SPMT) supports migrating your OneNote folders to Microsoft 365.
But before migrating your OneNote folders, it's important to understand a little about their file structure.

On your computer, a OneNote Notebook is presented as a normal folder. For each Notebook, there's a **.onetoc2** file created under the root folder of the Notebook folder. You can have as many Notebooks as you want.

![Screenshot of a OneNote notebook icon of a folder, with a ONETOC file underneath the folder.](media/onenote-file-1.png)

If you create section groups in your Notebook, those groups are also presented as a folder. Under each section group, you can create multiple sections, and each one of those sections is presented as **.one** file in file system.

You can create multiple pages within a section, but the content of those pages is contained in the same **.one** file as the section to which they belong.

![A screenshot of a section in a OneNote.](media/onenote-file-2.png)

When you open the OneNote application, the notebook, section groups, and sections appear to the left side of the application. Individual section pages you can put content into are on the right side of the application:

![A screenshot of the OneNote application showing the notebook name, section groups with sections on the left-hand side of the screen, and an empty section page on the right side of the screen.](media/onenote-file-3.png)

Folders are migrated to SharePoint as **OneNote Notebook** content rather than a normal folder with files. They appear in a SharePoint Document Library with a OneNote link and the name of the folder applied:

![A screenshot of a SharePoint communication site, showing the Documents foler with a OneNote document in the folder.](media/onenote-file-5.png)

For this **OneNote Notebook** to appear in your Notebooks list in OneNote, select the **Show Actions** ellipses next to the notebook name in the Document library, then select **Open > Open in app**. Remember to first close the OneNote application for the already migrated notebooks.
