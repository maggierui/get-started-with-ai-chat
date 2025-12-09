---
title: "Migration Assessment Scan External List"
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
ms.assetid: de809b30-8e4d-4223-b47e-81912d617dd1
ms.collection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
description: "Learn how to scan external lists during migration."
---

# Migration Assessment Scan: External List

## Overview

External lists are lists created from a Business Catalogs Services (BCS) application. These lists appear to be SharePoint lists, but are actually backed by an external datasource. For example, you could have a list showing data from an external SQL Server or Web Service.

## Data Migration

BCS applications aren't migrated to the target environment. As a result, external lists aren't migrated.

See [Migration Assessment Scan: BCS](migration-assessment-scan-bcs.md) for more information about BCS.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Build out a plan for the external lists. It's possible to configure Hybrid BCS to access on-premises data from SharePoint in Microsoft 365, but this configuration requires some planning.

See [Migration Assessment Scan: BCS](migration-assessment-scan-bcs.md) for more information about BCS.

## Post Migration

Make sure your solutions, which rely on BCS applications, function with the newly deployed BCS applications.

## Scan Result Reports

The following table describes the columns in the **ExternalLists-detail.csv** report. This scan report provides a list of all the external lists in the environment.

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
|DistinctUsers |Number of distinct users that accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|WebURL |Url to the site with publishing features enabled. |
|ListTitle |Title of the list. |
|ListURL |Url to the root folder of the list. |
|ListItemCount |Number of items in the list. |
|ListTemplate |Template used when creating the list. |
|ListType |The type of list is configured. |
|ListCreator |User that created the list. |
|ItemLastModifiedDate |Date/Time an item was last modified on the list. |
|ScanID | Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
