---
title: "Migration Assessment Scan Unsupported Site Templates"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
ms.date: 04/10/2025
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
ms.assetid: 7cd48080-1e02-443b-9e3d-8361b2903959
description: "Learn how to fix issues with Unsupported Site Templates during migration."
---

# Migration Assessment Scan: Unsupported Site Templates

Learn how to fix issues with Unsupported Site Templates during migration.

## Overview

Every SharePoint site is based on a site template. In the SharePoint source environment, it was possible to create site collections using various default templates and templates deployed via Full Trust Code (FTC). However, site collections that are supported for migration are the Team Site and Personal Site templates. The Personal Site Template is used for creating Microsoft OneDrive sites.

Supported Site Templates:

|**Template Friendly Name** |**Template** |**ID** |
|:--------------------------|:------------|:------|
|TeamSite                   |STS          |1      |
|Personal Site              |SPSPERS      |21     |

## Data Migration

Any site that isn't using a Team Site or Personal Site template should be mapped to the Team Site template during migration. The content from the source environment is then copied into the new Team Site on the target.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Use the scan report for Unsupported Site Templates to identify site collections that are impacted. The impacted site's content is copied into a Team Site template during migration, but it's possible the Team Site template doesn't include the features/functionality of the source site.

## Post Migration

Validate that your sites work post migration.

## Scan Result Reports

**UnsupportedWebTemplate-detail.csv** This scan report contains a list of sites that are currently using a site template that isn't supported on the target platform.

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
|LastContentModifiedDate  |Date/Time the site collection had content modified. |
|TotalItemCount |Total number of items found in the site collection. |
|Hits |Number of requests logged for the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DistinctUsers |Number of distinct users that accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|FullURL |URL to the impacted site. |
|WebID |ID for the site linked to the invalid site template. |
|WebTitle |Title for the impacted site. |
|WebTemplateID |ID for the site template that isn't supported in the source environment. |
|WebTemplate |Friendly name for the site template. If this row is empty, it indicates that the site template is no longer registered on the source environment. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
