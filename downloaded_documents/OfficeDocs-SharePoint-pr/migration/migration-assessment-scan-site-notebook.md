---
title: "Migration Assessment Scan Site Notebook"
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
description: "Learn about migration issues with Site Notebook."
---

# Migration Assessment Scan: Site Notebook

## Overview

SharePoint Server 2013 and later support a feature called Site Notebook. This SharePoint feature is activated on the site and generates a OneNote in the Site Assets library of the web. The file is named with the title of the site.

Depending on the migration tools being used, your Site Notebook migrates. However, the name of the Site Notebook in SharePoint in Microsoft 365 is different from the name of the file in the on-premises environment. As a result, links referencing the original file name is broken. This report provides a list of OneNote files that match the following scenario:

- OneNote Notebook files
- Files exist in the Site Assets library
- Files have a name that ends in Notebook
- OneNote isn't empty
- File isn't flagged as deleted

## Data Migration

Depending on the migration tools being used, the Site Notebook migrates but the file has a different name resulting in broken links.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Prepare for questions about missing Site Notebooks and provide guidance to impacted users.

## Post Migration

Educate users on the change related to Site Notebooks.

## Scan Result Reports

The following table describes the columns in the **Apps-detail.csv** report. This scan report provides a list of all the add-ins installed in the environment.

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
|File |Path to the Site Notebook. |
|TimeCreated |Date/Time the file was created. |
|TimeModified |Date/Time the file was last modified. |
|ModifiedBy |Person who last modified the file. |
|ScanId |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
