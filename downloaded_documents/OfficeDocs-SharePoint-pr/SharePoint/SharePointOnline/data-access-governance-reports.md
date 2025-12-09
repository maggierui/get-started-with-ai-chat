---
ms.date: 11/11/2025
title: "Data access governance reports for SharePoint sites"
ms.reviewer: pullabhk
ms.author: ruihu
author: maggierui
manager: dansimp
recommendations: true
audience: Admin
customer_intent: As a SharePoint administrator, I want to access data access governance reports to discover sites that contain potentially overshared or sensitive content.
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
description: "In this article, you learn about reports that can help you govern access to data in SharePoint."
---

# Data access governance reports for SharePoint and OneDrive sites

As sprawl and oversharing of SharePoint sites increase with exponential data growth, organizations need help with governing their data. Data access governance reports can help you govern access to SharePoint data. The reports let you discover sites that contain potentially overshared or sensitive content. You can use these reports to assess and apply the appropriate security and compliance policies.

## What you need to create a data access governance report

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

Data governance access reports are available in nongovernment cloud environments, as well as GCC-Moderate, GCC-High, and DoD government cloud environments. The reports are currently unavailable for Gallatin, even if you have the required licenses.

## How to access the Data access governance reports in the SharePoint admin center

1. Sign in to the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219) with the [SharePoint administrator](sharepoint-admin-role.md) credentials for your organization.
2. In the left pane, expand **Reports** and then select **Data access governance**.

    The following reports are currently available from the Data access governance landing page:

   - **[Snapshot reports](/sharepoint/data-access-governance-reports#what-are-snapshot-reports)**
       - [Site permissions across your organization](/sharepoint/data-access-governance-reports#what-is-the-site-permissions-report) (Recommended)
       - [Sensitivity label applied to files](/sharepoint/data-access-governance-reports#sensitivity-labels-for-files-reports)
   - **[Activity reports](/sharepoint/data-access-governance-reports#what-are-activity-reports)**
       - [Sharing links](/sharepoint/data-access-governance-reports#what-is-the-sharing-links-report)
       - [Shared with 'Everyone except external users'](/sharepoint/data-access-governance-reports#what-is-the-everyone-except-external-users-eeeu-report)

    :::image type="content" source="media/data-access-governance/data-access-governance-home-page.png" alt-text="Screenshot of the Data access governance landing page.":::

> [!NOTE]
> IT administrators with Microsoft 365 E5 licensing can access Data access governance reporting, but are unable to view or utilize the other [SharePoint Advanced Management features](advanced-management.md). No snapshot reports are provided. No remedial actions are provided. Activity reports are available but can return only up to 10,000 sites.

## What are snapshot reports?

Snapshot reports give you a snapshot of your organization's current status based on specific reporting criteria. These reports show data as of the date they were generated.

Currently, three types of snapshot reports are available:

- **[Site permissions report](#what-is-the-site-permissions-for-your-organization-report)**: Provides a comprehensive snapshot of permission structure across all SharePoint and OneDrive sites, helping you identify sites with the broadest user access (for example, sites with thousands of users, external guests, or "Everyone except external users" permissions).
- **[Site permissions for users report](#what-is-the-site-permissions-for-users-report)**: Lists all sites a specified user can access, allowing admins to determine whether they can access the entire site or specific sections, granted directly to the user or indirectly through groups.
- **[Sensitivity label for files report](#what-is-the-sensitivity-labels-for-files-report)**: Identifies SharePoint sites containing files with specific sensitivity labels applied, allowing you to verify that appropriate security policies are in place for your most sensitive content.

## What are activity reports?

Activity reports help you track potential oversharing activities that occurred in the last 28 days. These reports focus on "recently active" sites where users created sharing links or shared content with large groups. For all activities tracked in activity reports, you can find corresponding "baseline" data in the [snapshot reports](#what-are-snapshot-reports).

Currently, two types of activity reports are available to help you identify potential oversharing:

- **[Sharing links reports](#what-is-the-sharing-links-report)**: Identifies sites where users recently created the most sharing links (including "Anyone," "People in the organization," and "Specific people" links) to help you catch potential oversharing as it happens.
- **[Shared with 'Everyone except external users' reports](#what-is-the-everyone-except-external-users-eeeu-report)**: Tracks sites where content is shared with all internal users in your organization, helping you identify broad internal exposure that could lead to unintended data access.

> [!IMPORTANT]
> **For organizations without SharePoint Advanced Management:**
> You must enable data collection before you can generate activity reports. Here's what you need to know:
>
> - After enabling data collection, the system starts collecting audit data
> - Data is stored for 28 days
> - Reports become available 24 hours after enabling collection
> - Reports only contain data from when collection was enabled
> - If no reports are generated for 3 months, data collection pauses and must be re-enabled

:::image type="content" source="media/data-access-governance/enable-data-collection-SharingLinks.png" alt-text="Screenshot showing how to enable data collection for sharing link activity reports.":::

## How to use snapshot and activity reports?

As part of your governance strategy, we recommend combining both snapshot and activity reports to get a complete picture of your organization's data access landscape. Here's how to use them together effectively:

1. **Start with snapshot reports**: Run site permissions reports first to understand your baseline permission structure and identify sites with the broadest exposure. We recommend running these quarterly to maintain a comprehensive view of your organization's data access.
2. **Follow up with activity reports**: Use sharing links and EEEU activity reports to monitor recent oversharing activities and catch emerging risks. We recommend running these monthly to stay on top of ongoing sharing activities.

This combination ensures you have both a complete picture of your current state and visibility into ongoing sharing activities that could create new exposure risks.

## What is the site permissions for your organization report?

The site permissions report for your organization report is the first snapshot report that provides a comprehensive view of your organization's current permission structure across all SharePoint and OneDrive sites. This report analyzes every site to help you understand how broadly your data is exposed and identify potential oversharing risks. This snapshot approach helps you quickly assess your overall security posture and identify sites that need immediate attention.

Learn more about the [site permissions for your organization report here](data-access-governance-site-permissions-report.md).

## What is the site permissions for users report?

The site permissions report for users report is the next snapshot report that provides a comprehensive view into permissions of the specified users across all SharePoint and OneDrive sites. This report lists all sites a user can access and allows admins to determine whether they can access the entire site or specific sections, granted directly to the user or indirectly through groups. This approach helps you quickly assess your overall security posture and identify sites that need immediate attention.

Learn more about the [site permissions for users report here](data-access-governance-site-permissions-users-report.md).

## What is the sensitivity labels for files report?

The sensitivity labels for files report is the other snapshot report that helps you control access to sensitive content across your organization. This report identifies sites containing [files with sensitivity labels applied](/microsoft-365/compliance/sensitivity-labels-sharepoint-onedrive-files), allowing you to verify that appropriate security policies are applied. 

Learn more about the [sensitivity labels for files report here](data-access-governance-sensitivity-label-report.md).

## What is the sharing links report?

The sharing links report is one of the two activity reports that helps you identify sites where users created the most new sharing links in the last 28 days. 

Learn more about the [sharing links report here](data-access-governance-sharing-links-report.md).

## What is the 'Everyone except external users' (EEEU) report?

EEEU is a built-in SharePoint group that automatically includes all internal users but excludes any external guests. The 'Everyone except external users' (EEEU) report is one of the two activity reports that helps you identify sites where content has been shared with your entire organization in the past 28 days. You can run the  [site permissions for your organization report](#what-is-the-site-permissions-for-your-organization-report) first to understand your organization's current EEEU sharing baseline, then use this activity report to monitor ongoing EEEU sharing activities.

## Limitations or known issues

- Reports may not work if you have nonpseudonymized report data selected for your organization. To change this setting, you must be a Global Administrator. Go to the [Reports setting in the Microsoft 365 admin center](https://admin.microsoft.com/#/Settings/Services/:/Settings/L1/Reports) and clear **Display concealed user, group, and site names in all reports**.

## Remedial actions from Data access governance reports

After discovering potential oversharing through Data access governance reports, you can take several actions to address these risks. When deciding which actions to take, consider:

- The sensitivity of the exposed content
- The amount of content at risk
- The potential disruption to users and workflows

### Available remediation options

**For immediate action:**

- Use [Restricted access control (RAC)](./restricted-access-control.md) to limit access to a specific group
- Review the ['Change history' report](./change-history-report.md) to identify recent permission changes that may have led to oversharing

**For collaborative remediation:**

- Use the [Site access review feature](site-access-review.md) to request that site owners review and update permissions themselves

This approach ensures you can balance security needs with minimal disruption to your organization's productivity.
