---
title: "Migration Assessment Scan Master Pages"
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
ms.assetid: 487c6ff4-d087-4743-a786-e6b86c2a1223
description: "Learn how to mitigate issues with Master pages during migration."
---

# Migration Assessment Scan: Master Pages

Learn how to mitigate issues with Master pages during migration.
  
## Overview

During migration, the default master page should be set on all migrated sites. This setting ensures the site renders once the migration is complete, as the content migration doesn't have a dependency on any custom master pages. If you have custom master pages assigned to sites, you need to set the Master Page property on the new site after the migration completes.

## Data Migration

> [!IMPORTANT]
> Custom master page files (\*.master) shouldn't be migrated to the new platform. The setting on the destination site is set to the default master page. This process ensures the site renders after the migration.

## Preparing for Migration

Review the report and determine where you can move away from custom master pages before you migrate. Plan and understand what post migration work is necessary to use the customized file moving forward.

## Post Migration

If you decide to continue using the customized master page on the new platform, you need to apply the master page setting and validate your customizations work on the new platform.

## Scan Result Reports

**NonDefaultMasterPages-detail.csv** This scan report contains all the sites with a custom master page applied.

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
|Hits  <br/> |Number of requests logged for the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DistinctUsers  <br/> |Number of distinct users who accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|WebUrl |Url to the subsite with the master page setting configured. |
|WebTitle |Title of the impacted subsite. |
|MasterPageUrl|Server relative path to the master page referenced by the MasterPageUrl property. |
|CustomMasterPageUrl |Server relative path to the master page referenced by the CustomMasterPageUrl property. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
