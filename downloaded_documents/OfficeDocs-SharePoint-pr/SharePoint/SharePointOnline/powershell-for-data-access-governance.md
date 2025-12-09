---
ms.date: 10/30/2025
title: "Manage Data access governance reports using SharePoint Online PowerShell"
ms.reviewer: pullabhk
ms.author: ruihu
author: maggierui
manager: dansimp
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: how-to
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- Highpri
- Tier2
- M365-sam
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid: MET150
description: "Learn about how to use SharePoint Online PowerShell module to manage Data access governance reports"
---

# Manage Data access governance reports using SharePoint Online PowerShell

While [Data access governance](data-access-governance-reports.md) is available in SharePoint admin center portal, large organizations usually look for PowerShell support in order to manage scale via scripting and automation. This document discusses all appropriate PowerShell commands available via SharePoint Online PowerShell module to manage reports from Data access governance.

> [!IMPORTANT]
> - PowerShell support for Data access governance is available from module "Microsoft.Online.SharePoint.PowerShell" and version "16.0.25409" onwards.
> - Run the **Connect-SPOService** command _without_ the **Credential** parameter. We don't_ support sign-in using the **Credential** parameter inline with the latest security practices.

## What you need to create a data access governance report

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

## Before you start

You must be a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) or have equivalent permissions in Microsoft 365 to run the PowerShell admin scripts.

Before you use the PowerShell scripts in this article, you need to do the following steps:

1. If you haven't, [download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

   > [!NOTE]
   > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

1. Connect to SharePoint as a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) or with equivalent permissions in Microsoft 365 in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

## Creating reports using PowerShell

Use the **Start-SPODataAccessGovernanceInsight** command to generate [all reports](/sharepoint/data-access-governance-reports#how-to-access-the-data-access-governance-reports-in-the-sharepoint-admin-center) with appropriate filters and parameters

### Site permissions across your organization report

It's vital for SharePoint admins to understand the permissions setup in their organization, particularly in the wake of Copilot adoption, as it respects user and content permissions. Copilot's data exposure risk increases with the number of users having permissions/access. This report provides deep insights into the 'exposure' that is, unique number of users having permissions, of every SharePoint and OneDrive site in your organization.

It's recommended to run this report first to get a quick overview of permissions in your organization.

This report is considered a 'snapshot' report,  i.e., this report provides the latest snapshot/status of the entire organization as of the report generation date.

To generate a report for all your SharePoint sites, run the following command:

```powershell
Start-SPODataAccessGovernanceInsight -ReportEntity PermissionedUsers -ReportType Snapshot -Workload SharePoint -CountOfUsersMoreThan 0  -Name "OrgWidePermissionedUsersReportSharePoint"
```

To generate a report for all your OneDrive for business accounts, run the following command:

```powershell
Start-SPODataAccessGovernanceInsight -ReportEntity PermissionedUsers -ReportType Snapshot -Workload OneDriveForBusiness -CountOfUsersMoreThan 0  -Name "OrgWidePermissionedUsersReportODB"
```

Review the following important information about the report runs.

- Since these reports are comprehensive and are likely to cover all data in your tenant, the maximum number of reports that are allowed are 2; one per workload.
- The first report always takes upto five days to complete, irrespective of the size of the organization. Subsequent reports complete within 24 hours.
- These reports capture data upto *48 hours before* the report generation.
- Once generated, they can be run again once every 30 days.

These commands generate a list of all sites where at least one user can access any content within the site. More information about the list of sites and how to interpret the results is provided [here](data-access-governance-site-permissions-report.md#how-to-view-the-site-permissions-for-your-organization-report).

Once you understand the extent of oversharing in your tenant, you can track further deviations specifically from active sites in last 28 days. You can generate reports on sites that are active in key factors of potential oversharing such as 'Sharing links' or content shared with 'Everyone except external users', in the last 28 days.

### Sharing link reports

These reports are useful in identifying sites that are active in collaboration and hence needs quicker intervention to mitigate any potential oversharing risk. These 'RecentActivity' based reports identify sites that are generating the most number of sharing links in the last 28 days.

> [!IMPORTANT]
> If you don't have a Microsoft SharePoint Advanced Management license, you are asked to enable data collection for 'RecentActivity' based reports, so that the product starts to collect the relevant audit data to build this report. Once enabled, the data is collected and stored for 28 days. The reports can be generated 24 hours later and contains data from the point of collection. If no reports are generated even once in three months, data collection is paused and should be enabled again. To enable data collection for these reports, refer to [this section of the documentation](#data-collection-for-recent-activity-based-reports).

#### Anyone sharing links created in last 28 days

```powershell
Start-SPODataAccessGovernanceInsight -ReportEntity SharingLinks_Anyone -Workload SharePoint -ReportType RecentActivity
```

Provide the workload value as 'OneDriveForBusiness' to get all OneDrive accounts with the same criteria.

#### PeopleInYourOrg sharing links created in last 28 days

```powershell
Start-SPODataAccessGovernanceInsight -ReportEntity SharingLinks_PeopleInYourOrg -Workload SharePoint -ReportType RecentActivity
```

Provide the workload value as 'OneDriveForBusiness' to get all OneDrive accounts with the same criteria.

#### Specific people (guests) sharing links created in last 28 days

```powershell
Start-SPODataAccessGovernanceInsight -ReportEntity SharingLinks_Guests -Workload SharePoint -ReportType RecentActivity
```

Provide the workload value as 'OneDriveForBusiness' to get all OneDrive accounts with the same criteria.

### Content shared with Everyone except external users in last 28 days

While Sharing links are one possible contributor for potential oversharing, another key contributor is 'Everyone except external users' (EEEU) which makes content 'public' that is, visible to entire organization and makes it easy for others to discover content and get access. These reports identify sites that actively used EEEU at various scopes in last 28 days.

> [!IMPORTANT]
> If you don't have a Microsoft SharePoint Advanced Management license, you are asked to enable data collection for 'RecentActivity' based reports, so that the product starts to collect the relevant audit data to build this report. Once enabled, the data is collected and stored for 28 days. The reports can be generated 24 hours later and contains data from the point of collection. If no reports are generated even once in three months, data collection is paused and should be enabled again. To enable data collection for these reports, refer to the [documentation in the section below](#data-collection-for-recent-activity-based-reports).

#### Sites shared with Everyone except external users in last 28 days

When EEEU is added to a site membership (owners, members, or visitors), the entire content of the site becomes public and more prone to oversharing. The following PowerShell command triggers the report to capture such sites in the last 28 days:

```powershell
Start-SPODataAccessGovernanceInsight -ReportEntity EveryoneExceptExternalUsersAtSite -Workload SharePoint -ReportType RecentActivity -Name "PublicSiteViaEEEU"
```

> [!NOTE]
> Currently report for OneDriveForBusiness with EEEU at the site level isn't supported.

#### Items shared with Everyone except external users in last 28 days

The following PowerShell command triggers the report to capture sites where specific items (files/folders/lists) were shared with EEEU in the last 28 days:

```powershell
Start-SPODataAccessGovernanceInsight -ReportEntity EveryoneExceptExternalUsersAtSite -Workload SharePoint -ReportType RecentActivity -Name "PublicSiteViaEEEU"
```

Provide the workload value as 'OneDriveForBusiness' to get all OneDrive accounts with the same criteria.

### Sensitivity label in files report

This PowerShell command triggers the report to list sites where specific items were labeled with a given 'label', as of report generation date.

First, retrieve the label name or label GUID using "Security and compliance" PowerShell module.

```powershell
Get-Label | Format-Table -Property DisplayName, Name, GUID, ContentType
```

Then, use the Name AND GUID to retrieve sites with files labeled with the given label name or GUID.

```powershell
Start-SPODataAccessGovernanceInsight -ReportEntity SensitivityLabelForFiles -Workload SharePoint -ReportType Snapshot -FileSensitivityLabelGUID "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1" -FileSensitivityLabelName Secret
```

> [!NOTE]
> Currently, the report for 'OneDriveForBusiness' accounts with labeled files isn't supported.

## Data collection for recent activity based reports

> [!IMPORTANT]
> If you don't have a Microsoft SharePoint Advanced Management license, you are asked to enable data collection for 'RecentActivity' based reports, so that the product starts to collect the relevant audit data to build this report. Once enabled, the reports can be generated 24 hours later and contains data from the point of collection. Data is stored for 28 days. If no reports are generated even once in three months, data collection is paused and should be enabled again.

### Enabling data collection

This PowerShell command starts collecting audit data for reports on activities from the last 28 days.

```powershell
Start-SPOAuditDataCollectionForActivityInsights -ReportEntity SharingLinks_Anyone
```

The applicable values for the ReportEntity parameter are SharingLinksAnyone, SharingLinksPeopleInYourOrg, SharingLinksGuests, EveryoneExceptExternalUsersAtSite, EveryoneExceptExternalUsersForItems, CopilotAppInsights

### Disabling data collection

This PowerShell command stops collecting audit data for reports on activities from the last 28 days.

```powershell
Stop-SPOAuditDataCollectionForActivityInsights -ReportEntity SharingLinks_Anyone
```

### Checking the data collection status

Once data collection is enabled, the reports can be generated after 24 hours. To check whether reports can be generated, use the PowerShell command **Get-SPOAuditDataCollectionStatusForActivityInsights**. The command returns the current data collection status, which can be _NotInitiated_, _InProgress_, or _Paused_. Reports can be generated when the status is _InProgress_.

```powershell
Get-SPOAuditDataCollectionStatusForActivityInsights -ReportEntity SharingLinks_Anyone
```

## Tracking reports using PowerShell

> [!IMPORTANT]
> All report creations result in a GUID as output that could be used to track the report status.

```powershell
Start-SPODataAccessGovernanceInsight -ReportEntity SensitivityLabelForFiles -Workload SharePoint -ReportType Snapshot -FileSensitivityLabelGUID "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1" -FileSensitivityLabelName Secret
```

```console
ReportId                             Status
--------                             ------
a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1 NotStarted
```

Use the **Get-SPODataAccessGovernanceInsight** command to retrieve the current status of a specific Data access governance report using the report ID.

```powershell
Get-SPODataAccessGovernanceInsight -ReportID a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
```

```console
ReportId          : a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
ReportEntity      : SharingLinks_Anyone
Status            : InQueue
Workload          : SharePoint
TriggeredDateTime : 11/13/2024 19:32:34
CreatedDateTime   : 11/13/2024 20:09:23
ReportStartTime   : 10/17/2024 19:32:33
ReportEndTime     : 11/13/2024 19:32:33
ReportType        : RecentActivity
SitesFound        : 120
```

The ReportStartTime and ReportEndTime indicate the period of data to generate the report. The status is marked as 'Completed' when the report generation is complete.

You can also view the current status of DAG reports by using the filter **ReportEntity** instead of ID. The reportID is listed in the output and is required later to download a specific report.

```powershell
Get-SPODataAccessGovernanceInsight -ReportEntity PermissionedUsers
```

```console
ReportId             : a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
ReportName           : PermissionReportFor1AsOfSept
ReportEntity         : PermissionedUsers
Status               : Completed
Workload             : SharePoint
TriggeredDateTime    : 09/18/2024 11:06:16
CreatedDateTime      : 09/22/2024 12:12:48
ReportType           : Snapshot
CountOfUsersMoreThan : 1
CountOfSitesInReport : 7
CountOfSitesInTenant : 22
Privacy              : All
Sensitivity          : {All}
Templates            : {All}

ReportId             : b1b1b1b1-cccc-dddd-eeee-f2f2f2f2f2f2
ReportName           : PermissionReportFor1AsOfOct
ReportEntity         : PermissionedUsers
Status               : Completed
Workload             : SharePoint
TriggeredDateTime    : 10/09/2024 14:15:40
CreatedDateTime      : 10/09/2024 15:18:23
ReportType           : Snapshot
CountOfUsersMoreThan : 100
CountOfSitesInReport : 0
CountOfSitesInTenant : 26
Privacy              : All
Sensitivity          : {All}
Templates            : {All}
```

## View and download reports using PowerShell

To download a specific report, you need the reportID. Retrieve the reportID using the **Get-SPODataAccessGovernanceInsight** command and use the **Export-SPODataAccessGovernanceInsight** command to download the report to a specified path.

```powershell
Export-SPODataAccessGovernanceInsight -ReportID a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1 -DownloadPath "C:\Users\TestUser\Documents\DAGReports"
```

This downloads a CSV file to the specified path. Details of the CSV/view for each report are discussed [here](/sharepoint/data-access-governance-reports#how-to-access-the-data-access-governance-reports-in-the-sharepoint-admin-center).

> [!NOTE]
> The default download path is the 'Downloads' folder.

## Remedial actions using PowerShell

Once Data access governance reports are generated, SharePoint admins can perform remedial actions as described [here](data-access-governance-reports.md#remedial-actions-from-data-access-governance-reports). The following section describes PowerShell commands to trigger and track 'site access review' as a remedial action.

### Initiate Site access review using PowerShell

Use **Start-SPOSiteReview** command to initiate a site access review for a specific site, listed under a Data access governance report. The Data access governance report provides the context under which the review should be initiated. Retrieve the reportID, site ID from the CSV file and provide comments to give clarity to the site owner regarding the purpose of the review.

```powershell
Start-SPOSiteReview -ReportID a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1 -SiteID c2c2c2c2-dddd-eeee-ffff-a3a3a3a3a3a3 -Comment "Check for org wide access"
```

```console
ReviewId                : a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
SiteId                  : c2c2c2c2-dddd-eeee-ffff-a3a3a3a3a3a3
ReviewInitiatedDateTime : 13-11-2024 20:55:41
ReportEntity            : PermissionedUsers
Status                  : Pending
AdminComment            : Check for org wide access
SiteName                : All Company
```

This triggers emails to site owner as described [here](site-access-review.md#how-to-initiate-a-site-access-review).

### Track Site access reviews using PowerShell

Use **Start-SPOSiteReview** command to track the status of site access reviews. For specific reviews, you can use the `ReviewID` value as shown in the output. To retrieve all review related to a reporting module, use the `ReportEntity` parameter.

```powershell
Get-SPOSiteReview -ReportEntity PermissionedUsers
```

```console
ReviewId                : a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
SiteId                  : c2c2c2c2-dddd-eeee-ffff-a3a3a3a3a3a3
ReviewInitiatedDateTime : 13-11-2024 20:55:41
ReviewCompletedDateTime :
ReportCreatedDateTime   : 13-11-2024 23:25:41
ReportEndDateTime       : 13-11-2024 23:25:41
ReportEntity            : PermissionedUsers
Status                  : Pending
AdminComment            : Check for org wide access
SiteName                : All Company
ReviewerEmail           :
ReviewerComment         :

ReviewId                : a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
SiteId                  : c2c2c2c2-dddd-eeee-ffff-a3a3a3a3a3a3
ReviewInitiatedDateTime : 24-10-2024 11:07:39
ReviewCompletedDateTime : 15-11-2024 11:07:39
ReportCreatedDateTime   : 15-10-2024 09:24:47
ReportEndDateTime       : 15-10-2024 11:39:52
ReportEntity            : PermissionedUsers
Status                  : Completed
AdminComment            : Check for org wide access
SiteName                : All Company
ReviewerEmail           : Jon@contosofinance.com
ReviewerComment         : Removed EEEU for sensitive documents
```
