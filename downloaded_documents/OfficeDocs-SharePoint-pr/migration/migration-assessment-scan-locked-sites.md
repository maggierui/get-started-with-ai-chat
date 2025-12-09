---
title: "Migration Assessment Scan Locked Sites"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
ms.date: 04/09/2025
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
ms.assetid: 57e13cc6-cec7-4b81-8fe9-7b2646fd5532
description: "Learn how to mitigate issues with locked sites during migration."
---

# Migration Assessment Scan: Locked Sites

Learn how to mitigate issues with locked sites during migration.

## Overview

When a site is configured as **No Access** in SharePoint, the site is inaccessible for users and the system. As a result, the various premigration scans are configured to ignore any site configured as **No Access**. It's **locked**.

## Data Migration

Locked sites can't be migrated to the target environment, as the migration tooling is unable to read the site contents.

> [!IMPORTANT]
> Any site configured as **No Access** (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Ensure the list of locked sites is correct. If you have sites that are incorrectly marked as **No Access**, update their lock status to **Not Locked**.

## Post Migration

To manage the lock status on sites on the target environment, use the SharePoint Online Management Shell.

**How to unlock a site collection on vNext**
  
1. To unlock sites, use the Set-SPSite cmdlet from the PowerShell cmdlets.
2. Download the cmdlets from the [SharePoint Online Management Shell download.](https://www.microsoft.com/download/details.aspx?id=35588) https://www.microsoft.com/download/details.aspx?id=35588.
3. Launch the SharePoint Online Management Shell.
4. Run:  `Set-SPSite -LockStatus Unlock`.

**How to set a site to "No Access"**

1. Use Set-SPSite from the PowerShell cmdlets to lock sites. This action is similar to **No Access** in that users can't get to the site.
2. Download the cmdlets from the [SharePoint Online Management Shell download.](https://www.microsoft.com/download/details.aspx?id=35588) https://www.microsoft.com/download/details.aspx?id=35588.
3. Launch the SharePoint Online Management Shell.
4. Run:  `Set-SPSite -LockStatus NoAccess`.

**How to set a site to "Read only"**

1. Set-SPSite doesn't support setting a site to **Read Only**. An alternative method is to use Site Collection Policies on a site collection.
2. Browse the site you want to be **Read Only**.
3. In the top right, select the gear icon, and then select **Site Settings**.
4. Select **Site Policies**.
5. Select **Create**.
  - Enter a **Name** and **Description**.
  - Select **Do not close or delete site automatically**.
  - Check **The site collection will be read only when it is closed**.
  - Select **OK**.
6. On **Site Settings**, select **Site Closure and Deletion**.
7. For **Site Policy**, select the "Read Only" policy from Step 4.
8. Select **OK**.
9. Go back to **Site Closure and Deletion**, and select **Close this site now**. The site is now **Read Only**.
10. Only a site collection admin can access and select **Open this site**.

## Scan Result Reports

**LockedSites-detail.csv** This scan report contains a list of URLs that are configured as **No Access** in SharePoint.

|**Column** |**Description**                                                                                 |
|:----------|:-----------------------------------------------------------------------------------------------|
|URL        |URL of the site collection configured as **No Access**.                                         |
|ScanID     |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
