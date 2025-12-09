---
title: "Migration Assessment Scan Large List Views"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
ms.date: 9/13/2017
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
ms.assetid: e94a941a-b171-41fc-8685-f2fd74bf8487
description: "Learn how to mitigate issues with Large List Views during migration."
---

# Migration Assessment Scan: Large List Views

Learn how to mitigate issues with Large List Views during migration.

## Overview

It's possible to configure list view throttling on the source environment. There are a set number of hours per day where the throttle on views is lifted. The stated product list limits are in place continuously (24x7) on the target platform. These limits can result in some of your list views being throttled.

## Data Migration

The lists and their data are migrated. List views called out in the scan report aren't viewable post-migration without performing the remediation documented in the following section, **Preparing for Migration**. Any list views containing over 12 lookup columns can also be throttled and require remediation. To learn more, see [Designing large lists and maximizing list performance.](/previous-versions/office/sharepoint-server-2010/cc262813(v=office.14)).

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Review the provided report and remediate the large list views before migration. For information on how to optimize list views, see [Manage large lists and libraries in Microsoft 365](https://support.office.com/article/365-b4038448-ec0e-49b7-b853-679d3d8fb784).

## Post Migration

Ensure the lists that you remediated are rendering correctly.
  
## Scan Result Reports

**FileName: LargeListViews-detail.csv** This scan report contains list views that were either throttled, or can be throttled once you migrate to the new platform. The report contains list views that meet one of the following criteria:

- Returned greater than 3,000 items.
- Actively throttled on the scanned environment.
- Contained greater than 12 lookup columns.
- Configured as an aggregate view.
    
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
|Hits |Number of requests logged for the site collection. Relies on data from the usage logging service. This row shows N/A if usage logging service is disabled. |
|DistinctUsers  <br/> |Number of distinct users that accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|LookupColumnCount | |
|ListViewTitle |The title of the impacted list view. |
|DefaultView |True/False. Determines if the view is the default view for the list. |
|AggregateView |True/False. Determines if the view is an aggregate view. For example, the view is configured to display a Total. |
|ListViewThrottled |True/False. Specifies whether the list view was actively throttled on the scanned environment. |
|ViewItemCount |Number of items returned when the list view was executed. This field is empty if ListViewThrottled is True. |
|Hidden |True/False. Indicates the list view is hidden from end users. |
|ReadOnlyView  |True/False. Specifies if the list view is Read Only. |
|WebURL |Url to the subsite that contains the list view. |
|ListTitle |Title of the list view is associated with |
|ListURL |Url to the root folder of the list. |
|ListItemCount |Number of items in the list. |
|ListTemplate |Template used when creating the list. |
|ListType |The type of list is configured. |
|ListCreator |User that created the list. |
|ItemLastModifiedDate |Date/Time an item was last modified on the list. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
