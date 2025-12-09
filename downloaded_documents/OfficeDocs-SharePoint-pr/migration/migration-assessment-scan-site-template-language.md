---
title: "Migration Assessment Scan Site Template Language"
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
description: "Learn about SharePoint migration issues with site language packs."
---

# Migration Assessment Scan: Site Template Language

## Overview

In SharePoint, it's possible to install language packs and create sites using multiple languages. During a migration, other planning is required to validate sites that aren't using a language familiar to the migration team.

## Data Migration

Site content migrates, but validation of the content requires someone that speaks the language the content is in to confirm everything migrated correctly.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output. 

## Preparing for Migration

Plan to have appropriate resources available to perform user acceptance testing on the migrated content.

## Post Migration

Content experts need to validate the migrated content.

## Scan Result Reports

The following table describes the columns in the SiteTemplateLanguage-detail.csv report. This scan report provides a list of all the add-ins installed in the environment.

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
|WebURL |Url to the site. |
|Template |Name of the template. This shows a number if SharePoint isn't able to determine name of the site template. |
|TemplateID |ID associated with the site template. For example, 1 is associated with STS (SharePoint Team Site). |
|Locale |Language associated with the site template. If you installed English SharePoint and created a Team Site, the Locale would show 1033. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
