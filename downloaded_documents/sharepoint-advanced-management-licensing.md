---
ms.date: 10/28/2025
ms.update-cycle: 180-days
title: "Licensing for SharePoint Advanced Management"
ms.reviewer: daminasy
ms.author: ruihu
author: maggierui
manager: dansimp
audience: Admin
customer-intent: As an IT admin, I want to understand how licensing works for SharePoint Advanced Management.
f1.keywords:
- NOCSH
ms.topic: concept-article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- Highpri
- Tier2
- M365-sam
- M365-collaboration
search.appverid:
- MET150
recommendations: false
description: "Learn how SharePoint Advanced Management licensing works, including details about Microsoft 365 Copilot licenses that include SharePoint Advanced Management features."
---

# How does licensing work for SharePoint Advanced Management?

SharePoint Advanced Management uses a per-user licensing model. You can purchase a standalone SharePoint Advanced Management license for each user in your organization. External users don't require this license.

If your organization has a Microsoft 365 Copilot license and at least one user is assigned to a Copilot license, SharePoint administrators automatically receive access to the [SharePoint Advanced Management features required for Copilot deployment](/sharepoint/sharepoint-advanced-management-licensing#sharepoint-advanced-management-features-in-microsoft-365-copilot-licenses).

## SharePoint Advanced Management standalone license

To use SharePoint Advanced Management as a standalone license, your organization must have one of the following base licenses:
Users must be licensed for SharePoint K, P1, or P2 via standalone or a Microsoft 365 suite.

You can purchase the *SharePoint Advanced Management Plan 1* add-on in the Microsoft 365 admin center, through a Cloud Solution Provider (CSP), or through volume licensing enrollment. Contact your Microsoft account manager for further information.

SharePoint Advanced Management is available for Commercial, WW Commercial Public Sector, Education, and Charity. Support for US GCC, GCC-High, and DoD customers is coming soon. 

SharePoint Advanced Management is $3 per user per month for commercial customers. For more details on licensing, please contact your account manager.

## SharePoint Advanced Management features in Microsoft 365 Copilot licenses

The following SharePoint Advanced Management features are included in Microsoft 365 Copilot licenses:

- **Advanced tenant rename**
  - Applies to large tenants with up to 100,000 sites
- **[AI-Powered Insights](/sharepoint/ai-insights)**: Find the **Get AI insights** button next to various reports in the SharePoint admin center. Once selected, the AI insights feature extracts patterns from the report and offers a list of potential actions.
- **[App insights for SharePoint](/sharepoint/app-insights)**: Gain insights on the various non-Microsoft applications registered to your Microsoft Entra admin center and how they access your SharePoint content.
- **[Block download policy](/sharepoint/block-download-from-sites)**: Create and manage block download policies to block downloads for:
  - Files in SharePoint and OneDrive sites
  - Teams meeting recording files specifically
- **[Catalog management](/sharepoint/catalog-management)**: Organize and govern SharePoint sites by grouping them into logical categories based on regions, departments, users, information barriers, and custom properties.
- **[Change history](/sharepoint/change-history-report)**: Create change history reports to track changes made to:
  - Individual SharePoint sites
  - Organization settings in the SharePoint admin center
- **[Conditional access policies](/sharepoint/authentication-context-example)**: Use authentication contexts to connect a Microsoft Entra Conditional Access policy to a SharePoint site. 
- **[Content management assessment](/sharepoint/content-management-assessment)**: The hub for a comprehensive set of tools for assessing and improving your organization's content management practices with actionable insights and recommendations.
- **[Compare SharePoint site policies](/sharepoint/site-policy-comparison)**: Easily identify sites with similar content but different security policies. This feature helps you review and adjust site policies and settings, ensuring consistent security across your organization.
- **[Data Access Governance (DAG) reports](/sharepoint/data-access-governance-reports)**: Help you govern access to SharePoint data. The reports let you discover sites that contain potentially overshared or sensitive content by providing insights on:
  - [Content shared with "Everyone Except External Users" (EEEU)](/sharepoint/data-access-governance-reports#what-is-the-everyone-except-external-users-eeeu-report)
  - [Site permissions for the organization](/sharepoint/data-access-governance-site-permissions-report) for Sites, OneDrives, and Files
  - [Site permissions for given users](/sharepoint/data-access-governance-site-permissions-users-report) lists all sites a user can access and allows admins to determine whether they can access the entire site or specific sections
  - [Sharing Links](/sharepoint/data-access-governance-reports#what-is-the-sharing-links-report) and [Sensitivity Labels](/sharepoint/data-access-governance-reports#what-is-the-sensitivity-labels-for-files-report)
- **[Inactive SharePoint sites policy](/sharepoint/site-lifecycle-management)**: Detect inactive sites and notify site owners via email.
- **[Insights on agents accessing content](/sharepoint/insights-on-agent-access)**: Gain insights on how the agents are accessing content across all SharePoint and OneDrive sites in your organization.
- **[Insights on SharePoint agents](/sharepoint/insights-on-sharepoint-agents)**: Gain visibility into recently created SharePoint agents and their activities.
- **[Recent admin actions](/sharepoint/recent-actions-panel)**: Review and monitor the last 30 changes you made to a SharePoint site's properties (such as renaming a site, deleting a site, changing storage quota) within the last 30 days in the SharePoint admin center.
- **[Restrict site creation by apps](/sharepoint/restricted-site-creation-by-apps)**: Control which non-Microsoft applications can create SharePoint sites in your organization.
- **[Restricted Content Discovery (RCD)](/sharepoint/restricted-content-discovery)**: Limit the ability of end users to search for files from specific SharePoint sites and prevent the sites from surfacing in Microsoft 365 Copilot Business Chat, unless a user had a recent interaction.
- **[Restricted Access Control (RAC)](/sharepoint/restricted-access-control)**: Restrict access to:
  - [SharePoint sites by security groups](/sharepoint/restricted-access-control)
  - [OneDrive sites by security groups](/sharepoint/limit-access)
  - [Specific OneDrives](/sharepoint/onedrive-site-access-restriction)
- **[Site Access Review](/sharepoint/site-access-review)**: Delegate the process of reviewing data access governance reports to site owners of overshared sites.
- **[Site Ownership Policy](/sharepoint/create-sharepoint-site-ownership-policy)**: Define who should be responsible for each site, set minimum owner or admin counts, and automate notifications when sites don't meet your criteria.

## Which Microsoft 365 Copilot SKUs include SharePoint Advanced Management?

The following Copilot SKUs include the SharePoint Advanced Management:

- Microsoft 365 Copilot
- Microsoft 365 Copilot GCC
- Microsoft Sales Copilot for Faculty
- Microsoft Sales Copilot for Students
- Microsoft 365 Copilot for Finance
- Microsoft 365 Copilot for Sales
- Microsoft 365 Copilot for Service
- Microsoft 365 Copilot Developer
- Microsoft 365 Copilot (Education Faculty)
- Microsoft 365 Copilot (Education Student 18+)
- Microsoft 365 Copilot for Finance (Education Faculty)
- Microsoft 365 Copilot for Finance (Education Student 18+)
- Microsoft 365 Copilot for Sales (Education Faculty)
- Microsoft 365 Copilot for Sales (Education Student 18+)
- Microsoft 365 Copilot for Service (Education Faculty)
- Microsoft 365 Copilot for Service (Education Student 18+)

> [!NOTE]
> The features listed in this article are essential for enabling Copilot deployment and are included as part of SharePoint Advanced Management (SAM). Future features developed for SAM may not be included in the current Copilot SKUs. Customers with Copilot SKUs have access to the current SAM features necessary for Copilot deployment.