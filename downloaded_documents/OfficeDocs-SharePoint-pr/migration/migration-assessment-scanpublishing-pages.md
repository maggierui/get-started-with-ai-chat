---
title: "Migration Assessment Scan Publishing Pages"
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
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
ms.assetid: 7f8e8ee7-c400-4530-a550-598c9bf33c44
description: Learn about how the SharePoint assessment tool scans for issues in publishing pages.
---

# Migration Assessment Scan: Publishing Pages

## Overview

Publishing sites are typically customized intranet sites that rely on page layouts to allow end users to quickly create articles published to end users. Due to the high level of customization involved with publishing sites, they may be difficult to migrate to SharePoint in Microsoft 365. Migrating these sites may require an extensive amount of remediation effort.

## Data Migration

The files can migrate, however the pages may not function correctly on the new platform. The common causes are changes to SharePoint provided master pages, JavaScript, and CSS files.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Catalog the pages using page layouts. Perform test migrations and plan for post migration remediation. You may find it's easier to start a new portal in SharePoint in Microsoft 365 and archive your on-premises portal once the Microsoft 365 site is up and running.

## Post Migration

Apply the fixes to your page layouts and publishing pages post migration.

## Scan Result Reports

The following table describes the columns in the **PublishingPages-detail.csv** report. This scan report provides a list of all the add-ins installed in the environment.

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
|PublishingPageURL |Url to the publishing page. |
|PageLayoutName |Name of the page layout associated with the publishing page. |
|PageLayoutURL |Url to the page layout associated with the publishing page. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
