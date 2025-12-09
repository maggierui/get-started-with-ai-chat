---
ms.date: 01/13/2025
title: Report on file and folder sharing in a SharePoint site
ms.reviewer: srice
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_OD_share
- M365-collaboration
- Tier2
search.appverid:
- SPO160
- MET150
ms.custom:
- seo-marvel-apr2020
description: Learn how to create a report on file and folder sharing on a SharePoint site.
---

# Report on file and folder sharing in a SharePoint site

You can create a CSV file of every unique file, user, permission, and link on a given SharePoint site or OneDrive. This can help you understand how sharing is being used and if any files or folders are being shared with guests. You must be a site admin to run the report. Additional reporting options are available with [Microsoft Graph Data Connect](/graph/data-connect-datasets#onedrive-and-sharepoint-online).

When you run the report, the CSV file is saved to a location of your choosing on the site. If you don't want site members to see the report, consider creating a folder with different permissions where only site owners can access the report.

To run the report (SharePoint):

1. Open the site where you want to run the report
2. On the **Settings** menu, select **Site usage**.
3. In the **Shared with external users** section, select **Run report**.
4. Choose a location to save the report, and then select **Save**.

To run the report (OneDrive):

1. From the Microsoft 365 app launcher, select the OneDrive tile.
2. On the **Settings** menu, select **OneDrive settings**.
3. Select **More settings**, and then select **Run sharing report**.
4. Choose a location to save the report, and then select **Save**.

The report may take some time to run depending on the size of the site.

When the report is finished running, you receive an email with a link to the report.

## CSV format

For items shared with direct access, the report contains one row for each user / item combination. SharePoint groups are shown in the report, but not individual users inside them.

For items shared with a link, the report contains a row for each signed-in user who has used the link or has been sent the link through the sharing dialog. Links emailed directly that haven't been clicked, and *Anyone* links aren't included in the report.

The report contains the following columns:

|Column|Description|
|:---|:---|
|Resource Path|The relative URL of the item|
|Item Type|The type of item (web, folder, file, etc.)|
|Permission|The permission level the user has on this item|
|User Name|Friendly name of the user or group that has access to this item. If this is a sharing link, the user name is *SharingLink*|
|User E-mail|The email address of the user who has access to this item. This is blank for SharePoint groups.|
|User or Group Type|The type of user or group: Member (internal), Guest (external), SharePoint group, Security group or Microsoft 365 group. (*Member* refers to a member in the directory, not a member of the site.)|
|Link ID|The GUID of the sharing link if user name is *Sharing Link*|
|Link Type|The type of link (Anonymous, Organization, Specific People) if user name is *Sharing Link*|
|AccessViaLinkID|The **Link ID** used to access the item if a user's permission to an item is via a link.

## Related articles

[Overview of Microsoft Graph Data Connect](/graph/data-connect-concept-overview)
