---
ms.date: 10/30/2025
title: "Data access governance reports - get the 'Everyone except external users' (EEEU) activity report for SharePoint sites"
ms.reviewer: pullabhk
ms.author: ruihu
author: maggierui
manager: dansimp
recommendations: true
audience: Admin
customer_intent: As a SharePoint administrator, I want to get the 'Everyone except external users' (EEEU) activity report so that I can monitor ongoing sharing activities and identify potential oversharing risks in my organization.
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
- trust-pod
ms.custom:
- admindeeplinkSPO
search.appverid: 
description: "In this article, you learn how to get the 'Everyone except external users' (EEEU) activity report to monitor sharing activities for SharePoint sites in your organization."
---
# Monitor 'Everyone except external users' (EEEU) sharing with the EEEU activity report

'Everyone except external users' (EEEU) is a built-in SharePoint group that automatically includes all internal users but excludes any external guests. The 'Everyone except external users' (EEEU) report is one of the two types of Data access governance activity reports available with [SharePoint Advanced Management](advanced-management.md). The EEEU activity reports help you identify sites where content is shared with your entire organization in the past 28 days. We recommend running the  [site permissions report](data-access-governance-site-permissions-report.md) first to understand your organization's current EEEU sharing baseline, then use the EEEU activity report to monitor ongoing EEEU sharing activities.

## When does EEEU sharing occur?

Content can be shared with EEEU in two ways:

1. **Public sites**: When a site is configured as public, the EEEU group becomes part of the site's membership (owners, members, or visitors). Setting a site as public makes all site content visible to everyone in your organization.

2. **Public items**: Individual files or folders can be shared directly with EEEU using the people picker. Setting a file or folder as public makes it accessible to your entire organization while keeping the rest of the site private.

## Why monitor EEEU sharing?

Sharing with EEEU can lead to unintended data exposure since it grants access to all current and future employees. You can combine the EEEU activity reports with the [site permissions report](data-access-governance-site-permissions-report.md) to help you:

- Discover sites with the most EEEU sharing activity in the last 28 days
- Identify potential oversharing risks before they impact your organization
- Take appropriate actions to limit access when necessary

## What do EEEU activity reports show me?

Each EEEU activity report shows:

- **Top 100 sites**: Sites with the highest number of items or groups shared with EEEU in the last 28 days
- **Security policies**: Current policies applied to each site:
    - [Site sensitivity labels](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites)
    - Site privacy settings
    - [Site external sharing settings](external-sharing-overview.md)
- **Primary administrator**: The designated admin responsible for each site

## When to use EEEU activity reports?

We recommend running the EEEU activity reports in combination with other Data access governance reports, especially the site permissions report, to get a complete and ongoing picture of your organization's data access landscape. Here's how:

1. **Start with snapshot reports**: Run site permissions reports first to understand your baseline permission structure, specifically, to get the current state of EEEU sharing.
2. **Follow up with activity reports**: Run the EEEU activity reports to monitor recent EEEU sharing activities and catch emerging risks. We recommend running these monthly to stay on top of ongoing sharing activities.

## How to create an Everyone except external users report?

> [!IMPORTANT]
> Review these important details before creating your first report:
>
> - Reports cover SharePoint sites only (OneDrive support is [available via PowerShell](powershell-for-data-access-governance.md))
> - Maximum of 10 reports allowed
> - Reports may take up to 24 hours to complete
> - Data captured is from up to 24 hours before generation
> - Reports can be run again every 24 hours

When creating an EEEU report, you can configure various options to focus your analysis:

:::image type="content" source="media/data-access-governance/eeeu-addreport.png" alt-text="Screenshot that shows create an everyone except external users report.":::

Here's how:
**Report configure options:**

- **Report name**: Enter a unique name to identify this report
- **Template**: Select which SharePoint site templates to include (you can select multiple template types or choose "All sites"):
    - Classic sites
    - Communication sites
    - Team sites
    - Others
    - All sites (to include everything)
- **Privacy**: For Team sites, filter by privacy setting:
    - Private
    - Public
    - All (both private and public)
- **Site sensitivity**: Choose specific sensitivity labels to focus on sites with particular security classifications. For example, you can identify files shared with EEEU within sites labeled as "Confidential" in the last 28 days
- **Report type**: Select which EEEU scenario to analyze:
    - **Public sites**: Sites where EEEU is part of the site membership
    - **Public items**: Individual files or folders shared with EEEU

## Run the Everyone except external users report

To get the latest data, you need to manually run each report. You can run all reports at once or select individual reports. Check the **Status** column to see if a report is ready or when it was last updated.

## View Everyone except external users reports

After your report completes, it displays key insights about EEEU sharing activity:

:::image type="content" source="media/data-access-governance/dag-eeeu-report.png" alt-text="Screenshot that shows eeeu report details." lightbox="media/data-access-governance/dag-eeeu-report.png":::

## Download Everyone except external users reports

You can download the full report data as a CSV file for detailed analysis:

**Downloaded report contents:**

- Up to 1 million sites sorted by EEEU sharing activity (highest first)
- Complete site information including:
  - Primary administrator name and email
  - Site template type
  - Privacy settings
  - Sensitivity labels
  - Additional site metadata

## Take action based on EEEU report findings

After discovering potential oversharing through EEEU reports, you can take action to remediate risks and improve your organization's data access governance. Learn more [here](data-access-governance-reports.md#remedial-actions-from-data-access-governance-reports).