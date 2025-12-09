---
ms.date: 11/21/2025
title: "Generate Enterprise App Insights reports"
ms.reviewer: goagarwal
ms.author: ruihu
author: maggierui
manager: dansimp
audience: Admin
customer-intent: As a SharePoint admin, I want to generate App insights reports to monitor non-Microsoft applications accessing SharePoint content.
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- Highpri
- Tier2
- M365-sam
- M365-collaboration
- SAM-FY25

search.appverid:
recommendations: false
description: "Learn how to generate App insights reports to view how non-Microsoft applications registered on your Microsoft Entra admin center access your SharePoint content."
---

# Generate App insights reports to monitor non-Microsoft applications

App insights is a [SharePoint Advanced Management](advanced-management.md) feature that lets [IT administrators](/microsoft-365/admin/add-users/about-admin-roles) gain insights on the various non-Microsoft applications registered to your Microsoft Entra admin center and how they access your SharePoint content. This report can help you maintain and protect the integrity of your content.

The report is based on the Microsoft audit data logged when a non-Microsoft application accesses content through the following set of events:

- FileAccessed
- FileDownloaded
- FileModified
- FileUploaded  

## What do you need to generate App insights reports?

[!INCLUDE[Advanced Management Copilot only](includes/advanced-management-copilot-only.md)]

## App insights reports in SharePoint admin center

### Data collection for Enterprise App Insight report

> [!IMPORTANT]
> As a one time activity you will see a pop up on the UI to enable data collection for 'Enterprise App Insight' reports, so that the product starts to collect the relevant audit data to build this report. Once enabled, the reports can be generated 24 hours later and contains data from the time of data collection. Data is stored for 28 days. If no reports are generated even once in three months, data collection is paused and should be enabled again.

### Create report

1. Sign in to SharePoint admin center with your SharePoint admin credentials.
2. In the left pane, expand **Reports** and then select **App insights**.
3. Once on the **App insights** landing page, select **Add a report** to generate a new report.

    :::image type="content" alt-text="Screenshot of the create reports page for app insights dashboard in SharePoint admin center." source="media/app-insights/1-enterprise-app-insights-landing-page.png" lightbox="media/app-insights/1-enterprise-app-insights-landing-page.png":::

4. Under **Report range**, you can specify and filter data from a respective time frame for your report.
     :::image type="content" alt-text="Screenshot of the report range for app insights in SharePoint admin center." source="media/app-insights/2-enterprise-app-insights-create-new-report.png" lightbox="media/app-insights/2-enterprise-app-insights-create-new-report.png":::

5. Select **Add and run**.
  
> [!NOTE]
>
> - It can take up to several hours for generated reports to be available.
> - Only one report is allowed per report range.
> - Reports can be rerun after 24 hours.

### Manage reports in SharePoint admin center

#### View report status

To check if a report is ready or when it was last updated, see the **Status** column. When a report is ready, select it to view the data.

:::image type="content" alt-text="Screenshot of created app insight report in SharePoint admin center." source="media/app-insights/3-enterprise-app-insights-view-report.png" lightbox="media/app-insights/3-enterprise-app-insights-view-report.png":::

You're able to see the top 100 (by request volume) results on the screen.

You can also filter by App name, App permissions, and Site sensitivity to view relevant results from the top 100 rows.

:::image type="content" alt-text="Screenshot of list of insight reports in SharePoint admin center." source="media/app-insights/4-enterprise-app-insights-manage-reports.png" lightbox="media/app-insights/4-enterprise-app-insights-manage-reports.png":::

> [!IMPORTANT]
> To view up to 1 million results, you must select **Download detailed report**.

#### Delete report

To delete a report, select the existing report you want to delete and select **Delete report**.

#### Rerun a report

To get updated data for a given report range, select an existing report and select **Run**.

> [!TIP]
> A rerun prompt also appears if you select **Add a report** and select a report range for which there already exists a report.  

## App insights reports in SharePoint PowerShell Module

You can generate and manage App insights reports using SharePoint Online Management Shell.

1. [Download](https://go.microsoft.com/fwlink/p/?LinkId=255251) and install the latest version of SharePoint Online Management Shell.
2. Connect to SharePoint Online as a [SharePoint Administrator](sharepoint-admin-role.md) in Microsoft 365. For more information about SharePoint Online Management Shell, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
3. Ensure you have the SharePoint Advanced Management license.

### PowerShell commands for App insights reports

To perform the necessary operations, use the following commands:

#### Create a one-day default duration report

To generate report for the default duration of one day, run the following command:

```powershell
Start-SPOEnterpriseAppInsightsReport
```

#### Create report for any other duration

To generate report for any other duration, run the following command:

```powershell
Start-SPOEnterpriseAppInsightsReport -ReportPeriodInDays $ReportPeriodInDays (possible values = 1, 7, 14, 28) 
```

#### Check status of all active and available reports

To check status of all active and available reports, run the following command:

```powershell
Get-SPOEnterpriseAppInsightsReport
```

#### Check status of a specific report

To check status of a specific report, run the following command:

```powershell
Get-SPOEnterpriseAppInsightsReport -reportID $reportID (for the given report ID)
```

#### View a specific report

To view a specific report, run the following command:

```powershell
Get-SPOEnterpriseAppInsightsReport -reportID $reportID
```

#### Download a report

To download the report, run the following command:

```powershell
Get-SPOEnterpriseAppInsightsReport -reportID $reportID -action download
```

> [!IMPORTANT]
> Rerun and delete report capabilities are unavailable for PowerShell. The [Create report cmdlets](#create-a-one-day-default-duration-report) can be used with relevant report duration.

## Known experiences

- In new tenants, it can take a few days for data to be available and for these reports to be generated successfully. In large tenants, the data can be delayed by up to 48 hours (about two days).  
- A report can be rerun only after 24 hours since the last report generation.
- There can only be one report for each value of **Report range**. This means that you can see a maximum of four reports in the **Enterprise Application Insights** homepage.
- These reports are powered by Audit data and don't include all audit events.  
- You might see App ID of a non-Microsoft app, but App name of a middle-tier app in some cases.
