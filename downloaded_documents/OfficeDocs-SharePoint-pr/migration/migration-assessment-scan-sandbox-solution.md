---
title: "Migration Assessment Scan Sandbox Solution"
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
ms.assetid: 411c5512-e99c-4010-8a25-113515851cd7
description: "Learn how to mitigate issues with sandbox solutions during migration."
---

# Migration Assessment Scan: Sandbox Solution

Learn how to mitigate issues with sandbox solutions during migration.

## Overview

> [!IMPORTANT]
> SharePoint in Microsoft 365 doesn't support sandbox solutions.

SharePoint doesn't support sandbox solutions. As a result, any functionality using the sandbox in your current environment needs to be replaced with a supported technology. See the Office Dev Center Patterns and Practices site for information on building customizations:

[https://pnp.github.io/](https://pnp.github.io/)

## Data Migration

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Scan Result Reports

The following table describes the columns in the **SandboxSolution-detail.csv** report.

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
|DaysOfUsageData  <br/> |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|SandboxSolutionName |Sandbox solution name. |
|WebApplicationURL |Web application URL hosting the sandbox solution. |
|SandboxSolutionID |Sandbox solution ID. |
|Signature |Sandbox solution hash value. |
|HasAssembly |True if the solution contains assemblies; otherwise, false. |
|SolutionStatus |Sandbox solution status, which may be activated, deactivated, or disabled. |
|SolutionType |Sandbox solution type, which may be **Custom Code**, **Site Template**, or **Design Package**. |
|CreatedBy |User identity who created the solution. |
|CreatedDate |Date when the solution was created. |
|ModifiedBy |User identity who last modified the solution. |
|ModifiedDate |Date when the solution was last modified. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
