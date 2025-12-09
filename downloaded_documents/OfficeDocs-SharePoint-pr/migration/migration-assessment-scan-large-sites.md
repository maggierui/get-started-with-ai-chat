---
title: "Migration Assessment Scan Large Sites"
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
ms.assetid: ee79a293-16a1-4483-8687-6e23d7d3e481
description: "Learn how to mitigate issues with Large sites during migration."
---

# Migration Assessment Scan: Large Sites

Learn how to mitigate issues with Large sites during migration.

## Overview

This assessment lets site owners validate site size and makes them aware of larger sites that might take a longer period of time to migrate.

## Data Migration

It's more difficult to predict a migration schedule and delivery of the migration for sites over 500 GB.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Not applicable.

## Post Migration

Not applicable.

## Scan Result Reports

**LargeSites-detail.csv** This scan report provides a list of all the site collections over 500 GB in size.

|**Column**|**Description**|
|:-----|:-----|
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
|DistinctUsers |Number of distinct users that accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|SizeInGB |Size of the impacted site collection. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
