---
title: "Migration Assessment Scan Workflow Running Solutions 2010"
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
ms.assetid: 479f89dc-f6ba-4252-a72e-5cf1d02946ac
description: "Learn about issues migrating workflows that are in progress."
---

# Migration Assessment Scan: Workflow Running Solutions 2010

## Overview

The migration is unable to migrate workflows that are in progress. If a workflow on a site or item is In Progress, it appears as if the workflow was never started on the item before migration. If you have business critical workflows that are in progress before migration, we recommend you finish the workflow before migration.

## Data Migration

Workflow definitions migrate, however in progress workflow information isn't migrated.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Communicate with end users that in progress workflows need to be restarted after migration.

## Post Migration

Communicate with end users that in progress workflows need to be restarted after migration.

## Scan Result Reports

The following table describes the columns in the **WorkflowRunning2010-detail.csv** report.

|Column |Description |
|-------|------------|
|SiteID |Unique identifier of the impacted site collection. |
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
|DistinctUsers |Number of distinct users who accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|WorkflowName |Name of the workflow |
|ItemURL |URL to the item the workflow was started against. <br/>If this item is a **site workflow**, the URL points to the site. <br/>If this item is a **list item workflow**, the URL points to the list item. |
|Scope |Either Site or List. |
|WorkflowInitiator |User that started the workflow. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
