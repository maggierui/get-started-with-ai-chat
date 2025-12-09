---
title: "Migration Assessment Scan Apps"
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
- SPMigration
- m365initiative-migratetom365
ms.custom: 
ms.assetid: 2e57511d-07f0-4395-a795-11be19417c1a
description: "Learn how to mitigate issues with SharePoint add-ins during migration."
---

# Migration Assessment Scan: Apps

Learn how to mitigate issues with SharePoint add-ins during migration.

## Overview

Migrating SharePoint add-ins (formerly called apps) isn't supported in the target environment. The site content is migrated, but the add-ins aren't. As a result, once the site is migrated, the add-ins need to be reinstalled. If you purchased the add-in, you need to reclaim the license from the Add-in store.

## Data Migration

Site content is migrated, but add-ins need to be installed on the destination environment. If any add-ins stored data in the SharePoint App-web, that data is orphaned and the add-in is reinstalled cleanly.

> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Read through the provided report.

## Post Migration

Site owners need to reinstall the add-in during the user acceptance testing (UAT) process. If there was an add-in that was purchased, the user who purchased the add-in needs to recover the license.

## Scan Result Reports

The following table describes the columns in the **Apps-detail.csv** report.

This scan report provides a list of all the add-ins installed in the environment.

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
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this period is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|OwnerLogin |Owner of the site collection. [duplicate of Site Owner column] |
|OwnerTitle |Display name for the owner. |
|AppTitle |Title of the add-in. |
|AppSource |This information is the location the application was installed from. |
|AppID |ID assigned to the add-in. |
|WebID |ID or the web hosting the add-in. |
|LaunchURL |URL used to launch the add-in. If this URL is ~appWebUrl, then the add-in runs on the SharePoint environment. If the URL isn't associated with the SharePoint environment, then the add-in is a provider-hosted add-in that runs outside of the environment. |
|CreationTime |Time the add-in was installed. |
|RemoteAppURL |If the add-in is a provider-hosted add-in, this row contains the URL for the add-in. |
|SettingsPageURL |URL for the settings page associated with an add-in. |
|WebSiteTitle |Title of the web hosting the add-in. |
|WebURL |URL of the web hosting the add-in. |
|PageURL |If the add-in is an app part that sites on a page, this entry is the URL to the page. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
