---
ms.date: 09/10/2025
ms.update-cycle: 180-days
title: Get started with SharePoint agents
ms.reviewer:
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ROBOTS: NOINDEX, NOFOLLOW
ms.topic: how-to
ms.service: sharepoint-online
ms.collection: 
- M365-collaboration
- m365copilot
- magic-ai-copilot
- Tier2

ms.localizationpriority: medium
search.appverid:
- MET150
description: "Learn how admins can get started with SharePoint agents, including setting up pay-as-you-go billing and managing Azure resources for agents. "
---

# Get started with SharePoint agents

[SharePoint agents](https://support.microsoft.com/office/get-started-with-agents-in-sharepoint-69e2faf9-2c1e-4baa-8305-23e625021bcf), powered by AI, help users quickly find information and insights on SharePoint sites, pages, and document libraries. These agents access your organization's data the same way [Copilot in other Microsoft 365 apps](/sharepoint/sharepoint-copilot-best-practices#copilot-and-sharepoint) does, responding to users based on their access permissions to the data. This article discusses how admins can get started with SharePoint agents, including setting up pay-as-you-go billing and managing Azure resources for agents.

## Understand who can set up and use agents

SharePoint agents don't require activation. Once a user is assigned a Copilot license, or if your organization has the pay-as-you-go billing set up, SharePoint agents automatically become available to the user on eligible sites where they have permissions.

| **Action**          | **Requirements for the user**                                                                                       |
|---------------------|--------------------------------------------------------------------------------------------------------|
| **Create and configure an agent** | - Assigned with a Copilot license or your organization has the pay-as-you-go billing set up for you<br>- Ability to add new files to a SharePoint site    |
| **Interact with an agent**    | - Assigned with a Copilot license or your organization has the pay-as-you-go billing set up for you                                                       |

> [!IMPORTANT]
> If your organization hasn't adopted Microsoft 365 Copilot, it's recommended to review the requirements and learn how to adopt it for your organization. [Learn more](/copilot/microsoft-365/microsoft-365-copilot-overview).  

## Use agents with Copilot licenses

Users can use SharePoint agents after being [assigned a Copilot license](/copilot/microsoft-365/microsoft-365-copilot-enable-users#assign-licenses). You can use the [Microsoft 365 Copilot setup guide](https://admin.microsoft.com/Adminportal/Home?Q=learndocs#/modernonboarding/microsoft365copilotsetupguide) in the Microsoft 365 admin center to assign the required licenses to users. For more information, see [Assign licenses to users in the Microsoft 365 admin center](/microsoft-365/admin/manage/assign-licenses-to-users) and [Microsoft 365 Copilot requirements](/copilot/microsoft-365/microsoft-365-copilot-requirements). See more about [controlling user access through licensing](/sharepoint/manage-access-agents-in-sharepoint#control-user-access-through-licensing).

## Use agents with pay-as-you-go billing

To use agents with pay-as-you-go billing, you need to first set up SharePoint agents as a resource in Azure. That resource is used whenever a user without a Microsoft 365 Copilot license uses a SharePoint agent. For more information, see [Use agents with pay-as-you-go billing](/sharepoint/sharepoint-agents-azure-billing).

## Comparison of Copilot licenses, pay-as-you-go billing, and the trial promotion

What does the user get with pay-as-you-go billing, a Copilot license and the trial promotion? Here is a comparison:

| [Licensed for Microsoft 365 Copilot](/copilot/microsoft-365/microsoft-365-copilot-licensing) | [Pay-as-you-go](/sharepoint/sharepoint-agents-azure-billing) Enabled | What does the user get? |
|-----------------------------------------|-----------------------|-----------------------------|-------------------------|
| No                                      | No                    | Cannot create or use agents |
| No                                      | Yes                   | All unlicensed users get to create and use agents and are billed per pay-as-you-go billing. |
| No                                      | Yes                   | All unlicensed users can create and use agents up to 10,000 queries per month and then pay-as-you-go kicks in once the user exceeds the 10,000 queries limit for the month; or once the six-month promotion is over. |
| Yes                                     | Yes                   | - Licensed users can create and use agents without using the trial promotion or pay-as-you-go billing. <br>- Unlicensed users can create and use agents up to 10,000 queries per month and then pay-as-you-go kicks in once the user exceeds the 10,000 queries limit for the month; or once the six-month promotion is over. |
| Yes                                     | No                    | - Licensed users can create and use agents. <br>- Unlicensed users can't create or use agents. |

## Monitor agent usage

Users with at least site visitor's permissions can check the agent's file statistics, use search to find all agents for bulk actions, and see site usage. SharePoint admins can use the SharePoint Online Management Shell, Microsoft Purview audit log, Microsoft Cost Management, and SharePoint Advanced Management to monitor agent usage at the organization level. For more information, see [Monitor SharePoint agent usage](/sharepoint/monitor-agent-usage).