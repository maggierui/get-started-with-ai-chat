---
ms.date: 11/17/2025
title: Monitor agent access to SharePoint and OneDrive
ms.reviewer: nibandyo
ms.author: ruihu
author: maggierui
manager: dansimp
audience: Admin
customer-intent: As a SharePoint admin, I want to monitor all agents' access to SharePoint and OneDrive, including SharePoint agents, Declarative agents, Custom agents, and more, so that I can ensure security and compliance for my organization's content.
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection: 
- M365-collaboration
- M365-sam
- trust-pod
ms.custom:
search.appverid:
ms.assetid: 0ecb2cf5-8882-42b3-a6e9-be6bda30899c
description: Learn how to monitor all agents' access to SharePoint and OneDrive, including SharePoint agents, Declarative agents, Custom agents, and more, using the Agent Access Insights report in SharePoint Admin Center or SharePoint Online Management Shell.
---
# Monitor agent access to SharePoint and OneDrive

The Agent Access Insights report provides SharePoint administrators with rich information on how the agents are accessing content across all SharePoint and OneDrive sites in your organization. The report includes all agents registered and activated agent, such as [SharePoint agents](/sharepoint/get-started-sharepoint-agents), [Declarative agents](/microsoft-365-copilot/extensibility/overview-declarative-agent), [Custom agents](/microsoft-365-copilot/extensibility/overview-custom-engine-agent), and more. With this report, you can see how agents interact with your content, spot access patterns, and view agent distribution across sites. Use these insights to strengthen your security and apply governance controls like [Restricted access control](/sharepoint/restricted-access-control) and [Restricted content discovery](/sharepoint/restricted-content-discovery).

Agent Access Insights use Microsoft 365 unified audit logs to track how agents access your SharePoint sites and OneDrive accounts. These logs capture signals like reading, searching, and interacting with content, giving you a clear view of agent activity.
 
You can generate and manage the Agent Access Insights report in the SharePoint Admin Center or using SharePoint Online Management Shell. 
 
## What do you need to get insights on agent access to SharePoint and OneDrive?

[!INCLUDE[Advanced Management Copilot only ](includes/advanced-management-copilot-only.md)]

> [!IMPORTANT]
> If you don't have a Microsoft SharePoint Advanced Management license, you'll be asked to enable data collection, so that the product starts to collect the relevant audit data to build this report. Once enabled, the reports can be generated 24 hours later and contain data from the point of collection. Data is stored for 28 days. If no reports are generated at least once in three months, data collection is paused and should be enabled again. To enable data collection for these reports, refer to [the Data collection for Agent Access Insights report section in this article](#data-collection-for-agent-access-insights-report).

## How to access the Agent Access Insights report in SharePoint Admin Center?

1. Sign in to the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219) with the [SharePoint administrator](/sharepoint/sharepoint-admin-role) credentials for your organization. 
1. In the left navigation pane, expand Reports, and select **Agent Insights**.
1. Select **Agent Access**.
1. Review the report details, including agent activity, access patterns, and site distribution.

![Screenshot showing Agent Insights in SharePoint Admin Center.](media/sam-insights-agent-access/get-started-agent-access.jpg "Agent Access Insights ")

## How to create agent access reports in SharePoint Admin Center 

1. On the **Agent Insights** page, select **Create a report**.
2. Provide a Report name and specify the report duration (1, 7, 14, or 28 days).
3. Select **Create and run**.
![Screenshot of creating agent access reports under Agent Insights in SharePoint Admin Center.](media/sam-insights-agent-access/create-agent-access-report.jpg "Create Agent Access reports ")

> [!NOTE]
> You can create reports for the past 1, 7, 14, or 28 days. Data older than 28 days is automatically rolled off.

## View the agent access report status in SharePoint Admin Center

To check if a report is ready or when it was last updated, see the **Status** column.

![Screenshot of viewing status of agent access reports under Agent Insights in SharePoint Admin Center.](media/sam-insights-agent-access/view-report-status.png "View status of Agent Access reports ")

## View the agent access report details in SharePoint Admin Center

When a report is ready, select it to view the data. You can view the top 100 sites hosting the highest number of agents. You can search for sites or filter by site template, and governance policies.

![Screenshot of agent access reports under Agent Insights in SharePoint Admin Center.](media/sam-insights-agent-access/agent-access-report.png "View Agent Access reports ")

## View top 20 agents for a specific site

When you select a site, you can view the top 20 agents accessing the content across the selected site. 

![Screenshot of viewing top agents for a specific site under Agent Insights in SharePoint Admin Center.](media/sam-insights-agent-access/top-agents-per-site.png "View top agents for a specific site ")

## View agent distribution across sites

On the Agent Access report page, choose **Unique Agents found in SharePoint Sites** or **Unique Agents in OneDrive Account**. This view displays how agents are distributed across your organization's sites. You can quickly see the number of sites in each site template category and how many unique agents are accessing them.

![Screenshot of viewing agent distribution across sites under Agent Insights in SharePoint Admin Center.](media/sam-insights-agent-access/agent-distribution.png
 "View agent distribution across sites ")

## Apply content governance policies from the access report 

You can apply content governance policies on the sites from the access insights report. The policies available are [**Restrict site access policy**](/SharePoint/restricted-access-control) and [**Restrict Content Discovery policy**](/SharePoint/restricted-content-discovery).
 
> [!IMPORTANT]
> After a policy is applied to the site from the insights report, the policy status on the existing report won't be updated. To view the updated status of the policy on the site, select the policy to view the latest status or access the **Active site** panel and review the site settings.

## How to access the Agent Access Insights report using SharePoint Online Management Shell?

You can generate, check, and manage Agent Access Insights reports using SharePoint Online Management Shell. 

### Prerequisites

1. If you haven't, [download](https://www.microsoft.com/en-us/download/details.aspx?id=35588) and install the latest version of SharePoint Online Management Shell. 

1. Connect to SharePoint Online as at least a [SharePoint administrator](/sharepoint/sharepoint-admin-role) in Microsoft 365. For more information, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

1. To generate and view these reports, ensure the organization has the SharePoint Advanced Management add-on license or Microsoft 365 Copilot license.

### Create and view an Agent Access Insights report with SharePoint Online Management Shell

With permissions of at least a SharePoint administrator, you can generate and view the insights report using the following commands: 

1. To generate report for a one-day default report duration, run the command: 

```powershell
Start-SPOM365AgentAccessInsightsReport
```
![Screenshot of running Start-SPOM365AgentAccessInsightsReport command in SharePoint Online Management Shell.](media/sam-insights-agent-access/start-agent-report-powershell.jpg "Start Agent Access report ")

This command generates an Agent Access Insights report for the past one day by default.   

2. You can specify a different duration (7, 14, or 28 days) using the `-ReportPeriodInDays` parameter. For example, to create a report for the past 28 days, run:

```powershell
Start-SPOM365AgentAccessInsightsReport -ReportPeriodInDays <28>
```
3. To check the status of all active and available reports, run the command: 

```powershell
Get-SPOM365AgentAccessInsightsReport
```

4. To view the details of a specific report, run the command: 

```powershell
Get-SPOM365AgentAccessInsightsReport -ReportId <ReportId>
```
![Screenshot of running Get-SPOM365AgentAccessInsightsReport command in SharePoint Online Management Shell.](media/sam-insights-agent-access/check-specific-report-powershell.jpg "Get Agent Access report ")
Replace `<ReportId>` with the actual Report ID obtained from the previous command.

5. To download and view the report, run the command: 

```powershell
Export-SPOM365AgentAccessInsightsReport -ReportId <ReportId> -Action Download
```
> [!NOTE]
> PowerShell displays up to 100 sites but downloaded reports can contain up to 1 million sites. 

```powershell
Export-SPOM365AgentAccessInsightsReport -ReportId <ReportId> -View Download
```
Replace `<ReportId>` with the actual Report ID.

6. You can also view summarized insights of agents across all site types by running the command:

```powershell
Get-SPOM365AgentAccessInsightsReport –ReportId -Content SiteDistribution
``` 

**SiteDistribution**: Provides the summarized view of agents across all types of sites like Communication sites, Microsoft 365 group connected sites, OneDrive accounts, and more. 

## Data collection for Agent Access Insights report

 If you don't have a Microsoft SharePoint Advanced Management license, you'll be asked to enable data collection. This section explains how to enable and check status for data collection for the Agent Access Insights report.

### Enable data collection

This PowerShell command starts collecting audit data for reports on activities from the previous day:

```PowerShell
Start-SPOAuditDataCollectionForActivityInsights –ReportEntity M365AgentInsights
```

### Check data collection status

Once data collection is enabled, the reports can be generated after 24 hours. To check whether reports can be generated, use the PowerShell command:

```PowerShell
Get-SPOAuditDataCollectionStatusForActivityInsights -ReportEntity M365AgentInsights
```

The command returns the current data collection status, which can be "NotInitiated,"InProgress," or "Paused." Reports can be generated when the status is "InProgress."

## Known experiences with Microsoft 365 Agent Access Insights

Here are some important known experiences to keep in mind when working with Agent Access Insights reports in SharePoint Admin Center or SharePoint Online Management Shell:

- You can rerun a report only after 24 hours have passed since the last report was generated.

- For large tenants, data may take up to 48 hours to become available.

- Only one report can exist for each report range value (1, 7, 14, or 28 days). This means you can see a maximum of four reports at any given point. 

- When you generate a new report for the same date range, it replaces the previous report. To keep the old report, download it before creating a new one. 

- Reports use Microsoft 365 unified audit data, which may not include every audit event.

## Related articles

- [Manage access to SharePoint agents](/sharepoint/manage-access-agents-in-sharepoint)
- [Insights on SharePoint agents](/sharepoint/insights-on-sharepoint-agents)
- [Restrict SharePoint site access with Microsoft 365 groups and Microsoft Entra security groups](/SharePoint/restricted-access-control)
- [Restrict discovery of SharePoint sites and content](/sharepoint/restricted-content-discovery)
