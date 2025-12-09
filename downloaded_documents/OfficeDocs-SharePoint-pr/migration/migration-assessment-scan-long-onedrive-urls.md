---
title: "Migration Assessment Scan Long OneDrive URLs"
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
ms.assetid: a2828065-b060-4784-9a7d-4c214b4054b1
description: "Learn how to fix issues with long OneDrive URLs during migration, when a Universal Principal Names (UPN) is added to the URL."
---

# Migration Assessment Scan: Long OneDrive URLs

Learn how to fix issues with long OneDrive URLs during migration.

## Overview

When you're moving a OneDrive site from your source to the target environment, the OneDrive URL changes formats. On the source platform, the OneDrive sites are in the format of https://onedrive.contoso.com/personal/domain_user. On the target platform, the Domain_User portion of the URL changes to use the UPN for the user. This URL looks similar to https://onedrive.contoso.com/personal/user_contoso_com.

**Example:**

If you used this file:

`https://OneDrive.contoto.com/personal/contoso_bobsmith/Documents/Folder1/Folder2/ProjectA.docx`

The directory name of the file is:

`Personal/contoso_bobsmith/Documents/Folder1/Folder2`

> [!NOTE]
> There's a 400-character limit on the directory path to a file in SharePoint.

After the migration, the file path looks like the following example:

`Personal/bobsmith_contoso_com/Documents/Folder1/Folder2`

Notice the URL is now four characters longer than it was before. Depending on how the UPNs are formed at your company, the change in length may be larger.

If the previous file in the source environment was 255 characters, the length after migration is 259 characters.

We identified four different locations in which failures are likely to occur due to long URLs. As a result, there are four different reports concerning long URLs. The Scan Result Reports section covers each report along with the remediation that needs to occur.

## Data Migration

The migration of the source content resulting in the long URLs fail. This situation causes migration jobs to fail, which prolongs the migration project unnecessarily.

> [!IMPORTANT]
> Any site configured as "No Access" (locked), in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Review the reports and follow the remediation recommended for each report. In general, the remediation involves moving the content closer to the root of the site collection.

## Post Migration

Validate that your content is migrated.

## Scan Result Reports

This scan results in four output files. Each file is for a specific long URL issue that results in migration failures. **LongODBUrl-AllDocs-detail.csv** There are two limitations related to the length of the path to a given file:

- The server relative path to the folder containing the file has a maximum of 400 characters. Using the following example file:

    `https://OneDrive.contoto.com/Personal/contoso_bobsmith/Documents/Folder1/Folder2/ProjectA.docx`

    The directory name is: `Personal/contoso_bobsmith/Documents/Folder1/Folder2`.

    After the migration, the file path looks like the following example. Notice the URL is now longer than it was before: `Personal/bobsmith_contoso_com/Documents/Folder1/Folder2`.

- The server relative path to a file or folder has a total maximum of 400 characters. Using the following example file:

    `https://OneDrive.contoto.com/Personal/contoso_bobsmith/Documents/Folder1/Folder2/ProjectA.docx`

    The server relative path to the file looks similar to: Personal/contoso_bobsmith/Documents/Folder1/Folder2/ProjectA.docx

If there are files listed in this report, the owners need to move the files to shorter paths or delete the files. For example, they could move ProjectA.docx up to a folder directly under Documents, or they could delete the file if it's no longer needed.

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
|UPN |UPN used to determine the difference in the URL length. The UPN displaying as "\*\*\*\*" indicates the owner didn't have a UserPrincipalName set in their SharePoint profile. As a result, the average length of the UserPrincipalName values in the SharePoint profile store was used. |
|URLLengthDifference |Amount the URL grows when the site is renamed. |
|File |File that needs to be remediated. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |

 **LongODBUrl-NavNodes-detail.csv** Navigation nodes have a URL length limitation of 260 characters. This situation can lead to the URL field exceeding the maximum length.

For example, you have a OneDrive site at `https://OneDrive.contoso.com/personal/contoso_bobsmith`. That site has a link in the Quick launch named Reports and the URL of the link points to `https://onedrive.contoso.com/personal/contoso_bobsmith/documents/folder1/...folderN/Reports`. During the migration, SharePoint updates the URL to point to `/bobsmith_contoso_com/`. The extra length added to the URL may result in the length being over 260 characters, which causes the migration to fail.

To remediate this issue, you can move the reports folder close to the root of the /documents/ library and then update the quick launch link. Another option is to remove the quick launch link.

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
|UPN |UPN that was used to determine the difference in the URL length. The UPN displaying as "\*\*\*\*" indicates the owner didn't have a UserPrincipalName set in their SharePoint profile. As a result, the average length of the UserPrincipalName in the SharePoint profile store was used. |
|URLLengthDifference |URLLengthDifference Amount the URL grows when the site is renamed. |
|WebURL |URL to the web that has the navigation node. |
|NavigationNodeLocation |Navigation Node titles showing where the navigation node lives. You can have multiple levels of navigation nodes, and this information helps locate the offending node. |
|NavigationNodeTitle |Title of the impacted navigation node. |
|NavigationNodeURL |URL that's too long after the site rename. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |

 **LongODBUrl-Perms-detail.csv** Permissions set on an object in SharePoint are tracked by the URL of that object. If you set permissions on a folder, SharePoint stores the relative path to the folder. If you set permissions on an item, SharePoint stores the server relative path to the item.

As a result, during a site migration, the URLs associated with permissions are updated. This situation may lead to failures if the new URL is too long.

The remediation for this failure is to move the affected object closer to the root of the site collection. Another option is to remove the distinct permissions from the items in the report.

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
|UPN |UPN UserPrincipalName used to determine the difference in the URL length. If the UPN is "\*\*\*\*" that indicates the owner didn't have a UserPrincipalName set in their SharePoint profile. As a result, the average length of the UserPrincipalName in the SharePoint profile store was used. |
|URLLengthDifference |Amount the URL grows when the site is renamed. |
|WebURL |URL to the web hosting the secured object. |
|SecuredObject |The URL to the secured object that's too long after the site rename. If you add permissions to a file, it's the server relative path to the file. If you set permissions on a folder, it's the server relative path to the folder. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |

**LongODBUrl-Deps-detail.csv** Certain files can have other dependencies. The URL is used to track those dependencies. During the migration, if the dependency information is too long, the migration fails.

There are two limitations in this report to be aware of:

- FullURL has a limit of 260 characters. This entry in the file has the dependencies. To remediate if the FullURL is too long, either remove the file or move the file to a location closer to the root of the site collection.
- DependencyDescription has a limit of 270 characters. This entry is the dependency associated with the FullURL. To remediate the DependencyDescription, either remove the dependency or move the dependency closer to the root of the site collection.

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
|UPN|UPN used to determine the difference in the URL length. If the UPN is "\*\*\*\*", that entry indicates the owner didn't have a UserPrincipalName set in their SharePoint profile. As a result, the average length of the UserPrincipalName in the SharePoint profile store was used. |
|URLLengthDifference |Amount the URL grows when the site is renamed. |
|FullURL |URL to the file that has the dependencies. |
|DependencyDescription |DependencyDescription Description associated with the dependency. This entry may be a URL that's getting renamed. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
