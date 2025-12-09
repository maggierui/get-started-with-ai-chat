---
title: "Migration Assessment Scan Email Enabled Lists"
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
ms.assetid: a15bae85-86b3-4098-9bbd-631638d377b2
description: "Learn how to mitigate issues with Email Enabled Lists during migration."
---

# Migration Assessment Scan: Email Enabled Lists

Learn how to mitigate issues with Email Enabled Lists during migration.

## Overview

It's possible to configure lists that can accept incoming email in the source environment. This feature isn't available on the target environment.

## Data Migration

The contents in the libraries listed in the report migrate, but new emails sent to the library no longer automatically show up as the library no longer accepts incoming emails.

> [!IMPORTANT]
> Any site that is configured as "No Access" (locked) in SharePoint are skipped. To see a list of locked site collections, see the Locked Sites scan output.

## Preparing for Migration

Communicate with end users that email no longer shows up in the target environment.

## Post Migration

Communicate with end users that email no longer shows up in the target environment.

## Scan Result Reports

The following table describes the columns in the **EmailEnabledLists-detail.csv** report.

|Column |Description |
|-------|------------|
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
|WebURL |Url to the web hosting the email enabled list. |
|ListTitle |Title of the email enabled lists. |
|ListURL |URL to the root of the email enabled list. |
|ListItemCount |Number of items in the list. |
|ListTemplate |Template used when creating the list. |
|ListType |Type associated with the list. |
|ListCreator |User that created the list. |
|ItemLastModifiedDate |Date that an item in the list was modified. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
