---
title: "Migration Assessment Scan Large Lists"
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
ms.assetid: a10f6067-5cbe-4eb4-82f8-d57be628a3f6
description: "Learn how to mitigate issues with Large Lists during migration."
---

# Migration Assessment Scan: Large Lists

Learn how to mitigate issues with Large Lists during migration.

## Overview

Lists over 20,000 items historically caused issues with the migration tooling, making the ability to predict the time it takes to migrate sites that contain a larger list to be problematic.

## Data Migration

List data is migrated. However, the larger the list the more unpredictable the migration process. Extremely large lists can result in an extended migration.

> [!NOTE]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output. 

## Preparing for Migration

Investigate the large lists and determine the need for this content to be migrated to the target environment.

## Post Migration

The migration tooling has built-in validation to ensure all list items are migrated. You want to validate large lists migrated as expected.

## Scan Result Reports

**LargeLists-detail.csv** This scan report provides all lists that have over 20,000 items.

|**Column** |**Description** |
|:----------|:---------------|
|SiteId |Unique identifier of the impacted site collection. |
|SiteURL |URL to the impacted site collection. |
|SiteOwner |Owner of the site collection. |
|SiteAdmins |List of people listed as site collection administrators. |
|SiteSizeInMB |Size of the size collection in megabytes (MB). |
|NumOfWebs |Number of webs that exist in the site collection. |
|ContentDBName |Name of the content database hosting the site collection. |
|ContentDBServerName |SQL Server hosting the content database. |
|ContentDBSizeInMB |Size of the content database hosting the site collection. |
|LastContentModifiedDate |Date/Time the site collection had content modified. |
|TotalItemCount |Total number of items found in the site collection. |
|Hits |Number of requests logged for the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DistinctUsers |Number of distinct users who accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|WebURL |Url to the subsite that contains the list. |
|ListTitle |Title of the list. |
|ListURL |Url to the root folder of the list. |
|ListItemCount |Number of items in the list. |
|ListTemplate |Template used when creating the list. |
|ListType |The type of configured list. |
|ListCreator |User who created the list. |
|ItemLastModifiedDate |Date/Time an item was last modified on the list. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
