---
title: "Migration Assessment Scan File Versions"
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
ms.assetid: e847ee5e-342b-45a1-94c1-89244f81bef4
description: "Learn how to fix issues with file versions during migration."
---

# Migration Assessment Scan: File Versions

Learn how to fix issues with file versions during migration.

## Overview

Versions historically impact the length of a migration for a given site in a linear fashion. The more versions you have, the longer it takes to migrate a given site.

## Data Migration

By default, versioning is enabled for all lists and libraries on the target platform. In the destination SharePoint site, there's no limit when versioning is enabled.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Examine the report and determine if preserving versions is needed or not for your business.

## Post Migration

Site owners should validate their version information was migrated as expected.

## Scan Result Reports

The following table describes the columns in the **FileVersions-detail.csv** report.

This scan report provides a list of all the files in the environment that have versions.

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
|DistinctUsers |Number of distinct users that accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|SiteURL |URL to the site collection. |
|SiteOwner |Site collection owner. |
|VersionCount |Number of versions the items have. |
|File |File that the versions are associated with. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
