---
ms.date: 09/10/2025
ms.update-cycle: 180-days
title: Manage access to SharePoint agents
ms.reviewer:
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
customer-intent: As a SharePoint administrator, I want to manage access to SharePoint agents with built-in SharePoint permission models, SharePoint Advanced Management features such as restricted access control, restricted content discovery, and Microsoft Purview Data Loss Prevention (DLP).
f1.keywords:
- NOCSH
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
description: "Learn how to manage access to SharePoint agents with built-in SharePoint permission models, SharePoint Advanced Management features such as restricted access control, restricted content discovery, and Microsoft Purview Data Loss Prevention (DLP)."
---
# Manage access to SharePoint agents

SharePoint agents, powered by AI, help users quickly find information and insights on SharePoint sites, pages, and document libraries. SharePoint agents access your organization's data the same way [Copilot in other Microsoft 365 apps](/sharepoint/sharepoint-copilot-best-practices#copilot-and-sharepoint) does, responding to users based on their access permissions to the data. As a SharePoint admin, you can manage users' access to an agent in multiple ways by managing:

- Who can access the agents
- What information the user can access through the agent
- Where agents are available

## Manage who can access the agents

SharePoint agents don't require activation. You can manage who can access SharePoint agents through Copilot license assignment. Or, if your organization has the pay-as-you-go billing set up, you can control who can access SharePoint agents through the security groups assigned to the billing policy. Learn more about [setting up pay-as-you-go billing for SharePoint agents](/sharepoint/sharepoint-agents-azure-billing). 

### Control user access through licensing

Currently, users with a [Microsoft 365 Copilot license](/copilot/microsoft-365/microsoft-365-copilot-licensing) can use the agents. You can use the [Microsoft 365 Copilot setup guide](https://admin.microsoft.com/Adminportal/Home?Q=learndocs#/modernonboarding/microsoft365copilotsetupguide) in the Microsoft 365 admin center to assign the required licenses to users. For more information, see [Assign licenses to users in the Microsoft 365 admin center](/microsoft-365/admin/manage/assign-licenses-to-users) and [Microsoft 365 Copilot requirements](/copilot/microsoft-365/microsoft-365-copilot-requirements).

Admins can choose to edit the service plans under the Copilot license to specifically allow or block users from using Copilot experiences on SharePoint. Under the [license details page for Microsoft 365 Copilot](https://admin.microsoft.com/Adminportal/Home?#/licensedetailpage/639dec6b-bb19-468b-871c-c5c441c4b0cb) on the Microsoft 365 admin center, admins can turn *'Microsoft 365 Copilot for SharePoint'* on or off on a per-user basis. For example, a user could be allowed to use Microsoft 365 Copilot on Teams but not use any agents on SharePoint alone. However, this change will also disable Copilots on OneDrive and the SharePoint page authoring Copilot for that user.

### Control user access through pay-as-you-go billing

For users who aren't assigned with a Microsoft 365 Copilot license, you can control user access to agents through pay-as-you-go billing. To do so, you need to first set up SharePoint agents as a resource in Azure. You'll then set up a pay-as-you-go policy that is assigned to a security group. You'll then link that policy to the SharePoint agent resource. Only users in the security group assigned to the billing policy have access to SharePoint agents. For more information, see [Use agents with pay-as-you-go billing](/sharepoint/sharepoint-agents-azure-billing).

### Use file permissions on a specific agent file

As SharePoint agents are represented as [.agent files](https://support.microsoft.com/office/create-and-edit-an-agent-d16c6ca1-a8e3-4096-af49-67e1cfdddd42#where-agent-file), permissions on the *.agent* file governs who can access or edit the agent. Only users who are able to create or access files on a SharePoint site can create or access agents.

>[!NOTE]
> For users who can access and use a SharePoint agent, the agent's responses depend on permissions for each user to the agent's data sources. For instance, if a user has access to the agent but not to the site or document library it references, the agent's responses for this user won't include content from those restricted sources.



<!-- commenting this note as we are archiving the trail access to sharepoint agents - Task 10219406
> [!NOTE]
> From January 6, 2025, to June 30, 2025, enterprise tenants with 50 or more Microsoft 365 Copilot licenses will receive 10,000 free SharePoint agents queries for unlicensed users every month as a trial. Users with a role of SharePoint administrator or higher can [check the trial promotion status](/powershell/module/sharepoint-online/get-spocopilotpromooptinstatus) and [set trial promotion](/powershell/module/sharepoint-online/set-spocopilotpromooptinstatus) using PowerShell cmdlets. See the terms of trial usage [here](/legal/microsoft-365/in-app-trials-terms-of-service). -->

## Manage what information a user can access through the agents

### With built-in SharePoint features

SharePoint agents use SharePoint sites, pages, and document libraries as knowledge sources to respond to the user. You can control a user’s access to the information when they use an agent by controlling their access to the site. SharePoint provides many tools to control access to a site:

- Control access to a site that is associated with a [Microsoft 365 group](/microsoft-365/solutions/collaboration-governance-overview) by [setting the site as private](https://support.microsoft.com/office/change-a-site-s-title-description-logo-and-site-information-settings-8376034d-d0c7-446e-9178-6ab51c58df42) (team sites only) and controlling group membership.
- Control access to a site that isn't associated with a group using [site permissions](/sharepoint/site-permissions).
- Control access with access governance policies available in the SharePoint admin center and PowerShell.

Learn more about using SharePoint's built-in features to control access [here](/sharepoint/sharepoint-copilot-best-practices#step-2---prevent-oversharing-and-control-access-with-sharepoint-and-onedrive).

### With SharePoint Advanced Management

Currently, to restrict access to a site by Microsoft 365 Copilot, the SharePoint Admin can set up a [restricted access control policy](/sharepoint/restricted-access-control). As a result, all access to the site is restricted to only the group of users specified in the policy. Accordingly, the content from the site is visible in Microsoft 365 Copilot only for this restricted group of users. You can restrict access to individual sites or OneDrive.
Learn more about more features to prevent oversharing, control access, and enhance your content governance with SharePoint Advanced Management [here](/sharepoint/get-ready-copilot-sharepoint-advanced-management).

### With Microsoft Purview Data Loss Prevention (DLP)

You can prevent selected files from being used by agents by using sensitivity labels along with [Microsoft Purview Data Loss Prevention (DLP)](/purview/dlp-learn-about-dlp). You [do this](/purview/dlp-create-deploy-policy#scenario-2-block-sharing-of-sensitive-items-via-sharepoint-and-onedrive-in-microsoft-365-with-external-users) by creating a DLP custom policy with the **Content contains** > **Sensitivity labels** condition to exclude items from being processed. Identified items are available in the citations of the response, but the content of the item isn't used in the response.
We don’t yet support adding a sensitivity label directly to the [.agent file](https://support.microsoft.com/office/create-and-edit-an-agent-d16c6ca1-a8e3-4096-af49-67e1cfdddd42#where-agent-file). If you want to govern your *.agent* file with DLP, instead of using the sensitivity labels as the condition, you can use conditions based on the *.agent* extension. We'll support the ability of adding a sensitivity label directly to a *.agent* file in the future.

## Manage where agents are available

### Site owner controls in SharePoint

Agents created in SharePoint aren't automatically listed or published anywhere. Users can manually navigate to *.agent* files to use them just like how they would discover or use Word or Excel files. Site owners can choose to designate specific agents from their sites as 'approved' ones. These agents would be guaranteed to show up on the picker for that particular site, and users can differentiate them from the ones that are recommended to them. Learn more [here](https://support.microsoft.com/en-us/office/manage-agents-in-sharepoint-bcab837a-835c-4a1a-8ad4-d53a353c369f).

### Turn off agents on sites with restricted content discovery

You as a SharePoint Admin can turn off all agent-related features on individual sites with the [restricted content discovery](/sharepoint/restricted-content-discovery). Once a site is flagged with restricted content discovery, users can't see the Copilot icon on the upper right of the site. Therefore, they don’t have access to use the ready-made agent, create new agents, or add content from that site to any other agents. The restricted content discovery policy leaves site access unchanged but prevents the site's content from being surfaced in Microsoft 365 Copilot or organization-wide search for all users.

### Block agents from being used in Copilot Chat

Tenant admins and AI admins can manage actively used SharePoint agents right from the Microsoft 365 admin center, under the Agents section of the Copilot Control System (formerly known as integrated apps). This gives them a clear overview of all agents ever used in Copilot Chat, with the ability to view details and block or unblock any agent for use in M365 Copilot, all from one place. Learn more [here](/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps).

![Agent Inventory](media/agents-sharepoint/agent-inventory.png)


>[!NOTE]
> At the moment, blocking an agent only affects its availability in Copilot Chat. It doesn’t yet apply to OneDrive, SharePoint, or Teams.


## More resources

- [SharePoint site roles and permissions](/sharepoint/site-permissions)
- [Permission levels in SharePoint](/sharepoint/understanding-permission-levels)
- [SharePoint and Microsoft 365 Groups integration](/microsoft-365/solutions/groups-sharepoint-governance)
- [Microsoft Teams, SharePoint, and Microsoft 365 Groups integration](/microsoft-365/solutions/groups-sharepoint-teams-governance)
- [Get ready for Microsoft 365 Copilot with SharePoint Advanced Management](/sharepoint/get-ready-copilot-sharepoint-advanced-management)
- [Learn about data loss prevention](/purview/dlp-learn-about-dlp)
