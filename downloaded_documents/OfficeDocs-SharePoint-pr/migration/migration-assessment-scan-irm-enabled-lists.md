---
title: "Migration Assessment Scan IRM Enabled Lists"
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
ms.assetid: fce14caf-dc41-485d-91c6-4d533c8d1097
description: "Learn how to mitigate issues with IRM enabled lists during migration."
---

# Migration Assessment Scan: IRM Enabled Lists

Learn how to mitigate issues with IRM enabled lists during migration.

## Overview

Information Rights Management (IRM) is a feature that lets you encrypt content when a user accesses it to ensure it can't be forwarded or manipulated. The files are stored in an unencrypted format in SharePoint. When a user accesses a file in an IRM protected list, the file is protected before transit. The file can only be opened in an IRM-supported client application such as Microsoft Office.

There are two main components to the IRM migration process:

- Configure the target environment to support Microsoft Entra Rights Management.
- Disable IRM on the source and target SharePoint libraries. This disabling is required as the migration tooling accesses the files in the same manner as a user. If IRM is enabled on the source, the migration tooling receives an encrypted file and upload that encrypted file to the target environment. This circumstance results in a file that can't be opened successfully.

## Data Migration

IRM settings associated with lists and libraries aren't migrated. The following process is required to enable the migration tooling to properly handle IRM protected libraries. This process ensures that the content is transferred and accessible post migration.

1. Disable IRM on the source and target list.
2. Migration tooling copies the files from the source and places them in the target.
3. Enable IRM on the source and target list.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

1. IRM needs to be configured for SharePoint.
2. IRM needs to be disabled on the source list before the migration event for that site collection.

## Post Migration

1. Enable IRM on the migrated content list.
2. Perform the following steps to ensure documents in IRM protected libraries are protected.
  - Download a document from an IRM protected list.
  - Open the document on the client machine.
  - If the document is protected, there's a status displayed beneath the ribbon.

## Scan Result Reports

The following table describes the columns in the **IRMEnabledLibrary-detail.csv** report. This scan report contains lists and libraries that have IRM enabled. If IRM is disabled on the farm, the scan doesn't execute, and the output file indicates as much.

|**Column** |**Description** |
|:----------|:---------------|
|SiteId |Unique identifier of the impacted site collection. |
|SiteURL |URL to the impacted site collection. |
|SiteOwner |Owner of the site collection. |
|SiteAdmins |List of people listed as site admins. |
|SiteSizeInMB |Size of the size collection in megabytes (MB). |
|NumOfWebs |Number of webs that exist in the site collection. |
|ContentDBName |Name of the content database hosting the site collection. |
|ContentDBServerName |SQL Server hosting the content database. |
|ContentDBSizeInMB |Size of the content database hosting the site collection. |
|LastContentModifiedDate |Date/Time the site collection had content modified. |
|TotalItemCount |Total number of items found in the site collection. |
|Hits |Number of requests logged for the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DistinctUsers   |Number of distinct users that accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|ListTitle |Title of the list or library with IRM enabled. |
|URL |URL to the default list view. |
|ItemCount |Number of items in the list. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
