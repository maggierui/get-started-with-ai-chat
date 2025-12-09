---
title: "Migration Assessment Scan Large Excel Files"
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
ms.assetid: 359d684a-65bf-4345-8b98-b169a2474ed2
description: "Learn how to mitigate issues with large Excel files during migration."
---

# Migration Assessment Scan: Large Excel Files

Learn how to mitigate issues with large Excel files during migration.
  
## Overview

The maximum limit for opening XLSX files in the browser is 10 MB in the target environment. This setting is configurable in the source environment that may result in a change in behavior for your users. If you attempt to open a file larger than 10 MB from a SharePoint site, it prompts you to open the file in the Excel client application.

## Data Migration

XLSX files are migrated.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Notify users of the expected behavior.

## Post Migration

Attempting to open an XLSX file larger than 10 MB prompts you to open the file in the Excel client. You're prompted with a dialog.

## Scan Result Reports

**LargeExcelFiles-detail.csv** This scan report contains all XLSX files over 10 MB in size.

|**Column** |**Description** |
|:----------|:---------------|
|SiteId |Unique identifier of the impacted site collection. |
|SiteURL |URL to the impacted site collection. |
|SiteOwner |Owner of the site collection. |
|SiteAdmins |List of people listed as site collection administrators. |
|SiteSizeInMB |Size of the size collection in megabytes (MB) |
|NumOfWebs |Number of webs that exist in the site collection. |
|ContentDBName |Name of the content database hosting the site collection. |
|ContentDBServerName |SQL Server hosting the content database. |
|ContentDBSizeInMB |Size of the content database hosting the site collection. |
|LastContentModifiedDate |Date/Time the site collection had content modified. |
|TotalItemCount |Total number of items found in the site collection. |
|Hits |Number of requests logged for the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DistinctUsers |Number of distinct users that accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|File |URL to the XLSX file. |
|FileSizeinMB |Size of the XLSX file in MB. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
