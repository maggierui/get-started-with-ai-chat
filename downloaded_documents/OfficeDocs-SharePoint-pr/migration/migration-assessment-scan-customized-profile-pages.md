---
title: "Migration Assessment Scan Customized Profile Pages"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
ms.date: 04/08/2025
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
ms.assetid: b4f41860-3db9-4e30-8b5d-9748aa7d95a8
description: "Learn how to mitigate issues with Customized Profile pages during migration."
---

# Migration Assessment Scan: Customized Profile Pages

Learn how to mitigate issues with Customized Profile pages during migration.
  
## Overview

In the source environment, a page hosted in the My Site Host named Person.aspx manages the viewing of a user's profile. For example, selecting a colleague's name in a document library or from their Microsoft OneDrive takes you to the person.aspx page to view the user's profile.

After migration to the target environment, the Delve serves manages the profile experience. There's currently a limitation in that the Delve profile page can't be modified. This scan report shows you any customizations made to the Person.aspx page in the source environment. This data can be used to understand any impact with the move to the target environment regarding the profile experience.

To learn more, see: [How can I find people and information in Microsoft Delve?](https://support.office.com/article/5b8bffdd-a50a-430a-8570-09b39481887c).

## Preparing for Migration

Understand any customizations made to the Person.aspx page in the source environment, and investigate whether there's any impact with the move to the new Delve profile experience. The new experience solves most of the scenarios that resulted in customization on the previous platform.

## Post Migration

Validate the profile experience on the new platform.

## Scan Result Reports

**CustomizedProfilePages_\<Date\>_\<Time\>.csv** This scan report shows whether the Person.aspx profile page was modified in SharePoint Designer, or if any of the web parts added, deleted, or moved on the page.

|Column |Description |
|:------|:-----------|
|DisplayTitle |Display title of the web part. If the page was modified, there's a row with DisplayTitle of "Profile Page". |
|WebPart |Type of web part. |
|Scope |One of the following options: <br/> Page - The page was modified in SharePoint Designer. <br/> SharedWebPart - A Shared Web Part was added, deleted, or moved. <br/> UserWebPart - A User Web Part was added, deleted, or moved. |
|Difference |The piece of information that was flagged as a change. This flag could be a combination of the following options: <br/> Added Web Part. <br/> Web Part Zone. <br/> Web Part Order. <br/> Web Part Missing. <br/> Page modified in SharePoint Designer. |
