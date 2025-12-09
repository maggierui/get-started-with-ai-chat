---
title: "Migration Assessment Scan Checked-out files"
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
ms.assetid: 43ca2e32-1ed7-4a4b-a575-7573b435594b
description: "Learn about issues with checked-out files during data migration."
---

# Migration Assessment Scan: Checked-out files

Learn about issues with checked-out files during data migration.

## Overview

Migration reads the source SharePoint farm using an account that has Full Read access to the environment. If a user checks out a file, the migration tooling isn't able to read the checked out file. However, the migration tooling sees the last checked in version of the file instead. To avoid losing data, users should check in their files before their site migration.

## Data Migration

Only checked-in content is migrated. To avoid any potential data loss, encourage users to check in their files before migration. A site administrator can check in a file for a user, however only the content that the user save to SharePoint would be migrated. If a user downloaded the file and was working on it outside of SharePoint, those changes wouldn't appear post check-in.

> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Users should ensure that their content is checked-in before the migration date provided.

## Post Migration

Site owners performing user acceptance testing (UAT) on their content should validate that their sites migrated correctly.

## Scan Result Reports

The following table describes the columns in the **CheckedOutFiles-detail.csv** report.

This scan report provides a view of the files that are checked out and which user has the files checked out at the time the scan was executed.

|**Column** |**Description** |
|:----------|:---------------|
|SiteId |Unique identifier of the impacted site collection. |
|SiteURL |URL to the impacted site collection. |
|SiteOwner |Owner of the site collection. |
|SiteAdmins |List of people listed as site collection administrators. |
|SiteSizeInMB |Size of the size collection MB |
|NumOfWebs |Number of webs that exist in the site collection. |
|ContentDBName |Name of the content database hosting the site collection. |
|ContentDBServerName |SQL Server hosting the content database. |
|ContentDBSizeInMB |Size of the content database hosting the site collection. |
|LastContentModifiedDate |Date/Time the site collection had content modified. |
|TotalItemCount |Total number of items found in the site collection. |
|Hits |Number of requests logged for the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DistinctUsers |Number of distinct users who accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|File |File that is checked out. |
|CheckedOutUser |User that has the file checked out. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
