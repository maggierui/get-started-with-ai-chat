---
title: "Migration Assessment Scan Publishing Sites"
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
ms.assetid: 33af6b99-4b90-4edd-8ff7-e8fe2f288d3d
description: Learn about how the SharePoint assessment tool scans for issues in publishing sites.
---

# Migration Assessment Scan: Publishing Sites

## Overview

Publishing sites are typically customized intranet sites that rely on page layouts to allow end users to create articles published to end users. Due to the high level of customizations involved with publishing sites, they may be difficult to migrate to SharePoint in Microsoft 365 without many remediations.

## Data Migration

The content in the publishing site may migrate, but any customization typically requires an extensive amount of remediation effort.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Test migration of the sites with the publishing features enabled. Understand what needs to be corrected after migration.

## Post Migration

Apply the fixes to your customized content after migration.

## Scan Result Reports

The following table describes the columns in the **P-detail.csv** report. This scan report provides a list of all the add-ins installed in the environment.

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
|WebURL |Url to the site that has publishing features enabled. |
|PublishingInfrastructureEnabled |True if the site collection level Publishing Infrastructure feature is enabled. It's only True if the site is the root site in the site collection. |
|PublishingEnabled |True if the site level Publishing Feature is enabled. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
