---
title: "Migration Assessment Scan Alerts"
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
ms.assetid: 11fa99a3-9e65-48f6-b460-31c8cf8d30e5
description: "Learn how to fix issues with alerts during migration."
---

# Migration Assessment Scan: Alerts

Learn how to fix issues with alerts during migration.

## Overview

Most migration tools don't migrate alerts. Alerts are created on items, lists, and libraries to notify a user of when content changed. This report provides visibility into the alerts that are currently configured in the source environment. If users want to be notified of content changes after the migration, they need to configure the alerts on the new environment. As a result of alerts not migrating, we provide ample raw data associated with the alerts if you need to recreate the alerts post-migration.

## Data Migration

Basic migration tools don't migrate alerts.
  
> [!IMPORTANT]
> Any site configured as "No Access" (locked), in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.
  
## Preparing for Migration

Provide communication with users to avoid confusion post migration.
  
## Post Migration

Provide communication with users to avoid confusion post migration.
  
## Scan Result Reports

The following table describes the columns in the **Alerts-detail.csv** report.

This scan report provides a list of all the alerts installed in the environment.

|**Column**|**Description**|
|:-----|:-----|
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
|DistinctUsers |Number of distinct users who accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this period is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|WebURL |Web URL. |
|Title |Title of the alert. |
|AlertTemplateName |Name of the alert. |
|Filter |The Collaborative Application Markup Language (CAML) query filter applied to the alert. |
|ID |ID assigned to the alert. |
|MatchID |Per-filtering ID for an externally matched alert. |
|ItemID |ID of the item an alert is associated with. IF this column is empty, the alert is associated with the list instead. |
|ListURL |Time the add-in was installed. |
|ListID |ID of the list the alert is associated with. |
|List |ID or the web hosting the add-in |
|AlwaysNotify |URL of the web hosting the add-in. |
|DeliveryChannels |Title of the web hosting the add-in. |
|AlertType |The type of object to which the alert applies. It can be a list or document library, a list item or document, or a custom object. |
|EventType |The type of event to which the alert applies. |
|EventTypeBitmask |This column can be ignored. |
|AlertFrequency |Gets or sets the time interval for sending the alert. |
|AlertTime |The date and time for sending the alert. |
|Status |Determines if the alert is enabled or not. |
|User |User the alert is associated with. |
|DynamicRecipient |If the alert is dynamically generated, determines how the recipient is defined. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
