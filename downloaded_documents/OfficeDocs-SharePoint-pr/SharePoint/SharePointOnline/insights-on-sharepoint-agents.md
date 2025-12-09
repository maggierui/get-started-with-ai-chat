---
ms.date: 11/21/2025
title: "Get SharePoint agent Insights report"
ms.reviewer: pullabhk
ms.author: ruihu
author: maggierui
manager: dansimp
recommendations: true
audience: Admin
customer-intent: As a SharePoint admin, I want to monitor SharePoint agent activity and usage across my organization.
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- Highpri
- Tier2
- M365-sam
- M365-collaboration
- trust-pod
ms.custom:
- admindeeplinkSPO
search.appverid: 
description: "In this article, you learn about how to create and view insights on SharePoint agents in SharePoint and OneDrive sites."
---
# Insights report on SharePoint agents

Insights report on SharePoint agents provides SharePoint Administrators with rich information on the recently created SharePoint agents across all SharePoint sites and OneDrive sites within their organization. This report provides admins with the ability to learn about the sites with the highest number of agents created. Using this report, SharePoint admins can further govern and maintain the integrity of the content used by agents as grounding data.  

The insights report is based on the Microsoft audit data logged for SharePoint agents through the FileCreated and FileRenamed events.

You can generate and manage SharePoint agent Insights report in SharePoint Admin Center or with SharePoint Online Management Shell.  

## What do you need to access SharePoint Agent Insights report

[!INCLUDE[Advanced Management Copilot only ](includes/advanced-management-copilot-only.md)]

> [!IMPORTANT]
> If you don't have a Microsoft SharePoint Advanced Management license, you are asked to enable data collection, so that the product starts to collect the relevant audit data to build this report. Once enabled, the reports can be generated 24 hours later and contain data from the point of collection. Data is stored for 28 days. If no reports are generated at least once in three months, data collection is paused and should be enabled again. To enable data collection for these reports, refer to [the Data collection for Insights report on SharePoint agents section in this article](#data-collection-for-insights-report-on-sharepoint-agents).

## How to access SharePoint Agent Insights report in SharePoint Admin Center

1. Sign in to the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219) with the [SharePoint administrator](sharepoint-admin-role.md) credentials for your organization.
2. In the left pane, expand **Reports** and then select **Agent Insights**.

### How to create reports in SharePoint Admin Center

1. With permissions of a SharePoint Administrator, you can create the report by selecting **Create a report**.  

    ![Screenshot of creating report in SharePoint Agent Insights.](media/agent-insights/create-report.png)

2. Provide the Report name and under Report duration, specify the time frame for the report.  

    ![Screenshot of specifying report time frame in SharePoint Agent Insights.](media/agent-insights/create-report-time-frame.png)

3. Select **Create and run**. 
 
> [!NOTE]
> You can create a report for the past 1, 7, 14, or 28 days. 

### View report status in SharePoint Admin Center

To check if a report is ready or when it was last updated, see the **Status** column.  

![Screenshot of report status.](media/agent-insights/reports-status.png)

### View report in SharePoint Admin Center 

When a report is ready, select it to view the data. You can view the top 100 records hosting the highest number of agents. You can search for sites or filter on the site template, and governance policies.  

![Screenshot of view report.](media/agent-insights/agent-report.png)

### Apply Content governance policies in SharePoint Admin Center

You can apply content governance policies on the sites from the insights report. The policies available are [Restrict site access policy](/SharePoint/restricted-access-control) and [Restrict Content Discovery policy](/sharepoint/restricted-content-discovery).


 ![Screenshot of applying RCD.](media/agent-insights/RCD-lightbox.png)

> [!NOTE]
> After a policy is applied to the site from the insights report, the policy status on the existing report won't be updated. To view the updated status of the policy on the site, select the policy to view the latest status or access the Active site panel and review the site settings.

 
## SharePoint Agent Insights report in SharePoint Online Management Shell 
 
You can generate and manage SharePoint agent Insights report using SharePoint Online Management Shell. 

1. If you haven't, [download](https://www.microsoft.com/download/details.aspx?id=35588) and install the latest version of SharePoint Online Management Shell.
2. Connect to SharePoint Online as at least a [SharePoint administrator](/sharepoint/sharepoint-admin-role) in Microsoft 365. For more information, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
3. To generate and view these reports, ensure the organization has the SharePoint Advanced Management add-on SKU or Microsoft 365 Copilot license.

With permissions of at least a SharePoint administrator, you can generate and view the insights report using the following commands:  
 
1. To generate report for a one-day default report duration, run the command:  
 
    ```powershell
    Start-SPOCopilotAgentInsightsReport
    ```  

2. To generate a report for any other duration (7, 14 or 28 days), run the command:  
 
    ```powershell
    Start-SPOCopilotAgentInsightsReport -ReportPeriodInDays
    ```  
 
    For example, to generate report for the past 28 days, run the command:  
 
    ```powershell
    Start-SPOCopilotAgentInsightsReport -ReportPeriodInDays <28>
    ```
 
     ![Screenshot of powershell scripts to genearte report.](media\agent-insights\powershell-spocopilotagent-generate.png)

3. To check the status of all active and available reports, run the command:  
 
    ```powershell
    Get-SPOCopilotAgentInsightsReport
    ``` 
 
     ![Screenshot of powershell script status.](media\agent-insights\powershell-spocopilotagent-status.png)

4. To check the status of a specific report, run the command: 
 
    ```powershell
    Get-SPOCopilotAgentInsightsReport –ReportId
    ``` 

5. To download and view the report, run the command: 
 
    ```powershell
    Get-SPOCopilotAgentInsightsReport –ReportId -Action Download
    ``` 
    > [!NOTE]
    > PowerShell displays up to 100 records, but downloaded reports can contain up to 1 million records.
    
    ```powershell
    Get-SPOCopilotAgentInsightsReport –ReportId -Action View
    ``` 

6. To view further detailed reports, the following options are available: 
 

    a. CopilotAgentsOnSites: Provides the name of all the agents currently available on all sites. This report contains up to 1,000,000 records.  

    > [!NOTE]
    > The default value for the `-Content` parameter is `CopilotAgentsOnSites`. 
     
    ```powershell
    Get-SPOCopilotAgentInsightsReport –ReportId -Content CopilotAgentsOnSites
    ```  

    b. TopSites: Provides a list of 100 sites with the number of agents available on each site.  

    ```powershell
    Get-SPOCopilotAgentInsightsReport –ReportId -Content TopSites
    ```

    c. SiteDistribution: Provides the summarized view of agents across all types of sites like Communication sites, Microsoft 365 group connected sites, OneDrive site, etc.  

    ```powershell
    Get-SPOCopilotAgentInsightsReport –ReportId -Content SiteDistribution
    ```

### Data collection for insights report on SharePoint agents 

If you don't have a Microsoft SharePoint Advanced Management license, you are asked to enable data collection. This section explains how to enable and check status for data collection for the Insights report on SharePoint agents.

#### Enable data collection

This PowerShell command starts collecting audit data for reports on activities from the last 28 days. 

```powershell
Start-SPOAuditDataCollectionForActivityInsights  
```

#### Disabling data collection

This PowerShell command stops collecting audit data for reports on activities from the last 28 days. 

```powershell

Stop-SPOAuditDataCollectionForActivityInsights  
```

#### Checking the data collection status 

Once data collection is enabled, the reports can be generated after 24 hours. To check whether reports can be generated, use the PowerShell command Get-SPOAuditDataCollectionStatusForActivityInsights. The command returns the current data collection status, which can be "NotInitiated,""InProgress," "Paused". Reports can be generated when the status is "InProgress."

```powershell
Get-SPOAuditDataCollectionStatusForActivityInsights 
```

## Known experiences with SharePoint Agent Insights reports

The following are some known experiences with SharePoint Agent Insights reports generated in SharePoint Admin Center or using SharePoint Online Management Shell:

- A report can be rerun only after 24 hours since the last report generated.  

- In large tenants, it might take up to 48 hours for the data to be available.  

- Only one report can exist for each report range value (1, 7, 14, or 28 days). This means you can see a maximum of four reports at a given point.  

- The newly generated report replaces the previously created report with the same date range. To preserve the previously created report, download the report first before creating a new report for the same date range.  

- These reports are generated using Microsoft 365 unified audit data and might not cover all audit events.

## Related articles

- [Restrict SharePoint site access with Microsoft 365 groups and Microsoft Entra security groups](/SharePoint/restricted-access-control)
- [Restrict discovery of SharePoint sites and content](/sharepoint/restricted-content-discovery)
