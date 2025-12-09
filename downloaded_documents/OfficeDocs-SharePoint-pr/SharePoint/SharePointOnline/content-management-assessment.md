---
ms.date: 11/26/2025
title: "Assess your organization's content management status"
ms.reviewer: daminasy
ms.author: ruihu
author: maggierui
manager: dansimp
recommendations: true
audience: Admin
customer_intent: As a SharePoint administrator, I want to assess my organization's current content management status.
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
description: "In this article, you learn about how to assess your organization's current content management status and identify areas for improvement."
---

# Assess your organization's content management status

[SharePoint Advanced Management](/sharepoint/advanced-management) (SAM) provides a comprehensive set of tools for assessing and improving your organization's content management practices with actionable insights and recommendations. Content Management Assessment is the hub for these capabilities.

## What is Content Management Assessment?

Content Management Assessment is a built-in, easy-to-use feature of SharePoint Advanced Management. With just one click, you can quickly check and improve how your organization manages content within SharePoint environments. Content Management Assessment provides a simple, guided process for administrators to:

- Identify potentially overshared content
- Find issues or risks (such as inactive or ownerless sites)
- Define Copilot readiness for the organization
- Ensure compliance and maintain data integrity
- Receive actionable recommendations for remediation
- Track progress over time with recurring assessments

:::image type="content" source="media/sam-content-management-assessment/sam-content-management-assessment.png" alt-text="Screenshot of the SharePoint Advanced Management Content Management Assessment dashboard showing the assessment results with impacted sites on the left and report findings panel on the right.":::

The assessment uses the SharePoint Advanced Management (SAM) toolkit, running a suite of essential reports to surface key findings and categorize sites that might require attention. It's intended to make content governance accessible and actionable, even for admins who might not have deep technical expertise.

## Included reports

Currently, the Content Management Assessment includes the following reports:

- **[Inactive sites](/sharepoint/site-lifecycle-management)** - Identifies sites with no activity in the past 180 days
- **[Site ownership](/sharepoint/create-sharepoint-site-ownership-policy)** - Detects sites without owners or with only one owner
- **[Broken inheritance](/sharepoint/what-is-permissions-inheritance)** - Finds sites where permission inheritance has been broken
- **[Unrestricted internal sharing via EEEU (Everyone Except External Users)](/sharepoint/data-access-governance-reports#what-is-the-everyone-except-external-users-eeeu-report)** - Locates content shared with all internal users
- **[Unrestricted sharing via sharing links](/sharepoint/data-access-governance-reports#what-is-the-sharing-links-report)** - Discovers content shared through overly permissive sharing links

> [!NOTE]
>
> - Reports may take between 2 hour – 72 hours to run, depending on the size of the tenant.
> - Reports run on all sites across the organization, and don't take any action without the admin's consent.

## Why Use Content Management Assessment?

Organizations face increasing complexity in managing content across large Microsoft 365 tenants. Common challenges include:

- Uncertainty about where to start with governance.
- Difficulty identifying whether there are actual problems or risks.
- Lack of clarity on whether existing governance measures are sufficient.
- The need for ongoing monitoring and improvement.

Content Management Assessment addresses these challenges by:

- **Automating discovery**: Automatically discover and categorize potentially impacted sites without manual intervention
- **Clear, actionable findings**: Provide a clear list of issues with specific recommended next steps for each finding
- **Eliminating manual work**: Reduce the need for custom scripts or manual audits, which can be time-consuming and error-prone
- **On-demand reassessment**: Allow administrators to rerun the assessment monthly to ensure continuous improvement and compliance

## What do you need to access Content Management Assessment?

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

## Where to Find Content Management Assessment

You can access Content Management Assessment in the SharePoint Admin Center:

1. Sign in to the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219) with the [SharePoint administrator](sharepoint-admin-role.md) credentials for your organization.
2. In the left navigation pane, select **Advanced Management**.
3. Look for the new assessment starting screen (the previous menu-based view is still available under “All Features”).
:::image type="content" source="media/sam-content-management-assessment/start-content-management-assessment.png" alt-text="Screenshot of the SharePoint Advanced Management Content Management Assessment dashboard showing the start assessment button.":::
4. Select **Start assessment**.

The assessment automatically runs the relevant SAM reports, analyze the results, and present findings in a user-friendly dashboard.

- Left side: Visual summary of impacted sites
- Right hand side: The Report Findings Panel lists each impacted site, the specific findings, and recommended actions for remediation. Select each of the findings, you see more details and related Microsoft Learn documentations to address the issue.
- Below the results: You see the latest guidelines and documentations related to these policies.



## Next Steps After Running the Assessment

1. Review Findings: Examine the list of sites flagged as potentially impacted. The dashboard shows both the number and details of these sites.
2. Take Action: For each finding, follow the recommended steps provided. These steps might include:
   - Creating or adjusting site policies (for example, for potential oversharing, inactivity or ownership).
   - Using built-in tools to remediate issues.
   - Consulting linked documentation for further guidance.
3. Monitor Progress: Rerun the assessment every 30 days to track improvements and catch new issues.

## Summary

Content Management Assessment is a powerful, evolving toolset for Microsoft 365 admins, designed to simplify and automate the process of content governance. By providing clear assessments, actionable recommendations, and ongoing monitoring, it empowers organizations to maintain a secure and compliant environment.
