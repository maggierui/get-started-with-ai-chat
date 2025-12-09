---
title: "Migration Assessment Scan Managed Metadata Columns"
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
ms.assetid: 787812c2-8742-40c3-bd74-c7df9846c0b0
description: "Learn about scanning managed metadata columns for SharePoint migration."
---

# Migration Assessment Scan: Managed Metadata Columns

## Overview

In SharePoint, it's possible to add a Managed Metadata column to a list and populate the list field with values from the Managed Metadata Service Application. Migration of these columns requires coordination with migration of the Managed Metadata Service Application data.

## Data Migration

Managed metadata columns are typically migrated, but support depends on the migration tooling you select.
  
> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Before you start a migration project, you want to understand how many lists use Managed Metadata. You also want to try to migrate these lists close to the time you migrate your Managed Metadata Service Application data to the cloud.

## Post Migration

If migrating managed metadata columns is supported in the migration tooling you chose, make sure the lists using the columns are migrated and properly configured to create and edit list items.

## Scan Result Reports

The following table describes the columns in the **ManagedMetadataLists-detail.csv** report. This scan report includes all lists that contain Managed Metadata columns.

|**Column** |**Description** |
|:----------|:---------------|
|SiteId |Unique identifier of the impacted site collection. |
|SiteURL |Impacted site collection URL. |
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
|DaysOfUsageData  <br/> |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|ManagedMetadataColumns |Semicolon-delimited list of Managed Metadata columns associated with the list. |
|WebURL |Url to the web hosting the list. |
|ListTitle |Title of the list that contains managed metadata columns. |
|ListURL |URL to the list that contains managed metadata columns. |
|ListItemCount |Number of items in the impacted list. |
|ListTemplate |List template associated with the impacted list. |
|ListType |List type of the impacted list. |
|ListCreator |Account that created the list. |
|ItemLastModifiedDate |Date/Time the list had an item modified. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
