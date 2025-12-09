---
ms.date: 06/11/2025
title: Microsoft Entra B2B integration for SharePoint & OneDrive
ms.reviewer: srice
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- CSH
ms.topic: integration
ms.service: sharepoint-online
ms.localizationpriority: medium
search.appverid:
- MET150
ms.collection: M365-collaboration
ms.custom:
 - Adm_O365
 - seo-marvel-apr2020
description: In this article, you learn about the SharePoint and OneDrive integration with Microsoft Entra B2B.
---

# SharePoint and OneDrive integration with Microsoft Entra B2B 

> [!Important]
> After enabling Microsoft Entra B2B integration, external users attempting to access previously shared links (One Time Passcode) will encounter access issues. They receive error 'This organization has updated its guest access settings'. To restore access, your users need to reshare files/folders/sites to external users.

This article describes how to enable Microsoft SharePoint and Microsoft OneDrive integration with [Microsoft Entra B2B](/entra/external-id/what-is-b2b).

Microsoft Entra B2B provides authentication and management of guests. Authentication happens via one-time passcode when they don't already have a work or school account or a Microsoft account.

With SharePoint and OneDrive integrated with Azure B2B Invitation Manager, you can share files, folders, list items, document libraries, and sites with external people. This feature provides an upgraded experience from the existing secure external sharing recipient experience. Additionally, Azure B2B Invitation Manager offers a one-time passcode feature. This feature allows users without Work, School, or Microsoft accounts to authenticate using a code, instead of creating a new account.

Enabling this integration doesn't change your sharing settings. For example, if you have site collections where external sharing is turned off, it remains off.

SharePoint and OneDrive integration with the Microsoft Entra B2B one-time passcode feature is enabled by default for new tenants.

Advantages of Microsoft Entra B2B include:
- Invited people outside your organization are each given an account in the directory and are subject to Microsoft Entra ID access policies such as multifactor authentication.
- Invitations to a SharePoint site use Microsoft Entra B2B and no longer require users to have or create a Microsoft account.
- If you have Google federation in Microsoft Entra ID, federated users can now access SharePoint and OneDrive resources that you shared with them.
- SharePoint and OneDrive sharing is subject to the Microsoft Entra organizational relationships settings, such as **Members can invite** and **Guests can invite**. As with Microsoft 365 Groups and Teams, if a Microsoft Entra organizational relationship setting is more restrictive than a SharePoint or OneDrive setting, the Microsoft Entra setting prevails.

> [!NOTE]
> Microsoft Entra B2B doesn’t support Microsoft accounts in Microsoft 365 operated by 21Vianet.

## Enabling the integration

 > [!NOTE]
 > When the integration is enabled, people outside the organization are invited via the Azure B2B platform when sharing from SharePoint. They'll sign in based on the [Microsoft Entra B2B redemption policy](/azure/active-directory/external-identities/redemption-experience#invitation-redemption-flow). When the integration isn't enabled, people outside the organization continue to use their existing accounts created when previously invited to the tenant. Any sharing to new people outside the organization may result in either Microsoft Entra ID-backed accounts or SharePoint-only email auth guests that use a SharePoint One Time Passcode experience to sign in.

To enable SharePoint and OneDrive integration with Microsoft Entra B2B

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

2. Connect to SharePoint with permissions of a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) or [more](/microsoft-365/admin/add-users/about-admin-roles) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following cmdlets:

   ```PowerShell
   Set-SPOTenant -EnableAzureADB2BIntegration $true
   ```

 >[!NOTE]
 > Review any custom [domain sharing restrictions in SharePoint and OneDrive](/sharepoint/restricted-domains-sharing) and decide if they should be moved to the [Microsoft Entra B2B Allow/Deny list](/azure/active-directory/external-identities/allow-deny-list). The Microsoft Entra ID Allow/Deny list also affects other Microsoft 365 services like Teams and Microsoft 365 Groups.

## Disabling the integration

You can disable the integration by running [`Set-SPOTenant`](/powershell/module/sharepoint-online/Set-SPOTenant) `-EnableAzureADB2BIntegration $false`.

> [!Important]
> Once disabled, previously shared users remain Microsoft Entra Guest Users for future shares. To convert a user from a Microsoft Entra Guest User back to a SharePoint OTP user, you need to [delete the guest](/sharepoint/remove-users#delete-a-guest-from-the-microsoft-365-admin-center) in Microsoft Entra ID and remove all SPUser objects in your organization that reference that guest user.

## Frequently Asked Questions: 

The following questions address a change that requires resharing content with external users when considering enabling Microsoft SharePoint integration with Entra B2B.

**1. How can I check if my tenant has enabled SharePoint and OneDrive integration with Entra B2B?**

**Answer:** You can verify this using the SharePoint Online Management Shell. Run the following PowerShell cmdlet: Get-SPOTenant. In the output, look for the EnableAzureB2BIntegration property. If it is set to True, Entra B2B integration is enabled. If it is False, the integration is not enabled.

**2. Is there an impact of previously shared links on tenants which do not have Entra B2B integration enabled?**

**Answer:** No, there is no impact on tenants that have not enabled Entra B2B integration. This change only affects tenants that have already enabled or will enable the integration in the future.

**3. What happens to previously shared links if a tenant has enabled or plans to enable Entra B2B integration?**

**Answer:** For tenants that have enabled or will enable SharePoint integration with Entra B2B, users will need to reshare files, folders, and sites with external collaborators starting July 1, 2025. Tenants provisioned after June 2023 have Entra B2B integration enabled by default and are not impacted by this change.

**4. Is there a way to report which previously shared links and external users are affected?**

**Answer:** Yes. You can use audit logs to assess the impact. Refer to the documentation on [Use sharing auditing in the audit log](/purview/audit-log-sharing?tabs=microsoft-purview-portal). Additionally, site sharing reports available through Microsoft Graph Data Connect can help identify affected content and users. Details are provided in the [Microsoft Graph Data Connect for SharePoint Blog](https://techcommunity.microsoft.com/blog/microsoft_graph_data_connect_for_sharepo/mgdc-for-sharepoint-faq-what-is-in-the-permissions-dataset/4075447). You could also report on file and folder sharing in a SharePoint site using [this sharing report](/sharepoint/sharing-reports?WT.mc_id=M365-MVP-9501).

**5. Can we proactively invite existing users to join via Entra B2B before this change takes effect?**

**Answer** Yes. You can add guests in advance using Microsoft Entra B2B; however, resharing is still required. Guidance is available in the [Add and manage B2B collaboration users](/entra/external-id/add-users-administrator).

**6. Can exceptions be made to this change?**

**Answer:** No. This update is part of Microsoft’s ongoing efforts to enhance security.

**7. Can this change be applied at the site level?**

**Answer:** No. The change applies at the tenant level and cannot be scoped to individual sites.

## See also

[Set-SPOTenant](/powershell/module/microsoft.online.sharepoint.powershell/set-spotenant)

[External sharing overview](./external-sharing-overview.md)
