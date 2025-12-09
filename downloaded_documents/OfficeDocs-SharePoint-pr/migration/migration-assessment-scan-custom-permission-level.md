---
title: "Migration Assessment Scan Custom Permission Level"
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
ms.localizationpriority: medium
ms.assetid: 617ba8f7-eff1-4fcb-b9b8-ee5ef459a18c
ms.collection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
description: "Learn about issues with custom permission level during data migration."
---

# Migration Assessment Scan: Custom Permission Level

## Overview

In SharePoint, it's possible to create a custom permission level and then assign that permission level to users and groups. Some migration tools have problems moving this information to SharePoint. As a result, permissions aren't the same for impacted users and groups post migration.
  
For more information on permission levels, see [Understanding permission levels in SharePoint](/sharepoint/understanding-permission-levels).
  
## Data Migration

With some tooling, this data isn't migrated. We recommend you use the permission levels provided by SharePoint. However, if custom permission levels are required, the permission levels would need to be manually recreated on the SharePoint sites.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Determine the plan to move forward by understanding the custom permission levels in use in your source environment. Either move users and groups to the default SharePoint permission levels, or build out a plan for creating the custom permission levels and fixing permissions post migration.
  
## Post Migration

Validate the users and groups have the correct permission levels. If you needed to create custom permission levels, ensure those custom levels are functioning as expected.
  
## Scan Result Reports

The following table describes the columns in the **CustomPermissionLevel-detail.cs** v report. This scan report provides a list of all the custom permission levels in the environment. 
  
|**Column** |**Description** |
|:----------|:---------------|
|SiteId |Unique identifier of the impacted site collection. |
|SiteURL |URL to the impacted site collection. |
|WebApplicationURL |URL of the Web Application hosting the site collection. |
|SiteOwner |Owner of the site collection. |
|SiteAdmins |List of people listed as site collection administrators |
|SiteSizeInMB |Size of the size collection in megabytes (MB) |
|NumOfWebs |Number of webs that exist in the site collection. |
|ContentDBName |Name of the content database hosting the site collection. |
|ContentDBServerName |SQL Server hosting the content database. |
|ContentDBSizeInMB |Size of the content database hosting the site collection. |
|LastContentModifiedDate |Date/Time the site collection had content modified. |
|TotalItemCount |Total number of items found in the site collection. |
|Hits |Number of requests logged for the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DistinctUsers |Number of distinct users who accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|WebURL |Url to the site that has publishing features enabled. |
|PermissionLevelName |Name of the custom permission level. |
|PermissionLevelDescription |Description of the custom permission level. |
|Permission LevelURL |Url to the custom permission level. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
