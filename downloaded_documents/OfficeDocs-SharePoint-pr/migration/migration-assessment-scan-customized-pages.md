---
title: "Migration Assessment Scan Customized Pages"
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
ms.assetid: 55004bf2-5b96-4272-8f8f-970672fc84d4
description: "Learn how to mitigate issues with Customized Pages during migration."
---

# Migration Assessment Scan: Customized Pages

Learn how to mitigate issues with Customized Pages during migration.

## Overview

Customized files are out of the box SharePoint files not modified by a user. A common example is using a tool like SharePoint Designer to open a site and modify the default.aspx file of a site. During migration, these pages are reverted to their uncustomized state.

Any file modified by the SharePoint System Account is excluded from the scan report.

For more information on customized files and how to reset a file back to the default, read the following article:

- [Customize a SharePoint page by using remote provisioning and CSS](/sharepoint/dev/solution-guidance/customize-a-sharepoint-page-by-using-remote-provisioning-and-css).
 
## Data Migration

Customized files are reverted to their uncustomized state during migration.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Notify the site collection owners of sites that contain customized pages that they need to reapply any customizations made to impacted files post migration. Page owners should look for out of the box behavior to replace customization where possible.

## Post Migration

Site owners need to reapply any customizations post migration.

## Scan Result Reports

The following table describes the columns in the **CustomizedPages-detail.csv** report.

This scan report provides a list of all the customized files and who last modified them.

|**Column** |**Description** |
|:----------|:---------------|
|SiteId |Unique identifier of the impacted site collection. |
|SiteURL |URL to the impacted site collection. |
|SiteOwner |Owner of the site collection. |
|SiteAdmins |List of people listed as site collection administrators. |
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
|ModifiedBy |User that modified the file |
|File |File that was customized. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
