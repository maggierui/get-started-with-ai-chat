---
ms.date: 11/17/2025
title: "Restrict OneDrive and SharePoint site creation by apps"
ms.reviewer: vgaddam
recommendations: true 
ms.author: ruihu
author: maggierui
manager: dansimp
audience: Admin
customer-intent: As a SharePoint administrator, I want to restrict apps from creating specified types of SharePoint and OneDrive sites.
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
- essentials-manage
- trust-pod
search.appverid:
description: "Learn how to restrict apps from creating specified types of OneDrive and SharePoint sites using restricted site creation."
---

# Restrict OneDrive and SharePoint site creation by apps

**Restricted Site Creation by Apps** lets SharePoint Administrators use [SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/introduction-sharepoint-online-management-shell#getting-started-with-sharepoint-online-powershell) to designate which third party apps can create SharePoint sites in the organization.  

You can choose between two ways to manage site creation for apps within your tenant: deny mode (the specified apps are unable to create sites) and allow mode (only the specified apps are allowed to create sites).  Once you enable restricted site creation for apps in your tenant, the default mode is **deny**. 

Keep in mind, these policies only control which apps can create new sites—they don't affect site access permissions for users or apps.

> [!NOTE]
>
> - The Restrict OneDrive and SharePoint site creation by apps feature is currently in preview.
> - Admins can create separate configurations for the following categories of sites: All sites (including OneDrives), all SharePoint sites (not including OneDrives), OneDrives, Team sites (Group connected and classic), and Communication sites. 
> - The Restricted site creation for apps feature has a simulation mode parameter to test hypothetical scenario for policy configuration. 
> -The Restricted site creation for apps feature only affects 3rd party apps. First party apps currently aren’t affected. 

 ## What do you need to restrict OneDrive and SharePoint site creation by apps?

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

In addition, to use Restricted site creation for apps, you need to: 

- Download and install the [latest version](https://www.microsoft.com/download/details.aspx?id=35588) of Microsoft SharePoint Online Management Shell.  

- Make sure you can configure apps that are allowed to create SharePoint sites. 

## Manage restricted site creation for apps with SharePoint Online Management Shell 

You must be a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) or have equivalent permissions in Microsoft 365 to run the SharePoint Online Management Shell admin scripts. 

Before you use the scripts in this article, you need to do the following steps: 

1. If you haven't, [download the latest SharePoint Online Management Shell](https://www.microsoft.com/download/details.aspx?id=35588). 

> [!NOTE]
> If you installed a previous version of the SharePoint Online Management Shell, go to **Add or remove programs** and uninstall "SharePoint Online Management Shell" first. Then, install the latest version.

1. Connect to SharePoint as a SharePoint Administrator or with equivalent permissions in Microsoft 365 in Microsoft 365. To learn how, see Getting started with SharePoint Online Management Shell. 

## Overview of the PowerShell commands 

| Function                        | Command                                                                                   |
|----------------------------------|------------------------------------------------------------------------------------------|
| Enable site access restriction   | `Set-SPORestrictedSiteCreationForApps –Enabled $true`                                    |
| Specify mode as Allow or Deny     | `Set-SPORestrictedSiteCreationForApps –Mode Allow`  <br> `Set-SPORestrictedSiteCreationForApps –Mode Deny`               |
| Add/reconfigure App ID list      | `Set-SPORestrictedSiteCreationForApps -SiteType <SiteType> -RestrictedSiteCreationApps <comma separated app IDs>` |
| View App ID list                 | `Get-SPORestrictedSiteCreationForApps -SiteType <SiteType>`                                  |

To get App IDs, follow these steps:  

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) as at least a [Cloud Application Administrator](/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator).

1. Browse to **Entra ID** > **Enterprise apps** > **All applications**. 

1. Select the application you want, and view its Application ID.  

> [!NOTE]
> This feature only restricts third party apps; it doesn't affect [first party apps](/power-platform/admin/apps-to-allow).

## Site types for restricted site creation for apps

You need to specify the SiteType parameter when you update and view the App ID list. Here's the SiteType parameter list: 

|Site type|Applies to|
|---|---|
|All|OneDrive and all SharePoint sites|
|SharePoint|All SharePoint sites (but not OneDrive)|
|OneDrive|Only OneDrive|
|Team|Only SharePoint team sites (group-connected and classic)|
|Communication|Only SharePoint communication sites|

> [!NOTE]
> **All Sites** includes all sites except for any template listed in the following table. The *All Sites* SiteType overrides all others.

 | Type           | Template Name   | Template ID | Reason                              |
|----------------|-----------------|-------------|-------------------------------------|
| SharePoint Embedded           | CSPCONTAINER    | 70          | SharePoint Embedded experience is managed separately|
| Redirect site  | REDIRECTSITE    | 301         | Critical SharePoint functionality   |
| My Site Host   | MYSITEHOST      | 54          | Core site                           |
| Tenant Admin   | TENANTADMIN     | 16          | Core site                           |

## How restricted site creation for apps deny and allow modes work

The restricted site creation for apps mode is shared across all site type policies. It isn't possible to use deny mode for one site type and allow mode for a different site type.

When restricted site creation for apps is in **deny** mode, an app is blocked from creating a site if its App ID is in any list configured with any site type, which applies to the site it's attempting to create. For example, an app is blocked from creating a SharePoint communication site if its App ID is in any list configured with the All, SharePoint, or Communication site types. 

When restricted site creation for apps is in **allow** mode, an app is only allowed to create a site if its App ID is in a list configured with a site type, which applies to the site it's attempting to create. For example, an app can create a OneDrive if its App ID is in a list configured with the All or OneDrive site types.

## Enable restricted site creation for apps 

The `Set-SPORestrictedSiteCreationForApps –Enabled $true` cmdlet in the SharePoint Online Management Shell allows the admin to enable the restricted site creation feature and policies for the tenant. 

Example: `Set-SPORestrictedSiteCreationForApps –Enabled $true`

## Specify mode as Allow or Deny 

You can specify Apps that are allowed (use the parameter `Allow`) or not allowed (use the parameter `Deny`) to create a certain type of sites. 

Example: Set the mode of restricted site creation for apps as Allow 

`Set-SPORestrictedSiteCreationForApps –Enabled:$true –Mode Allow` 

> [!NOTE]
> Flipping from deny to allow mode prompts a message: “Are you sure you want to switch from Deny to Allow? Switching will remove all current configuration of restrictions.” A similar message appears when you switch from allow to deny mode as well.  

## Set App IDs in the app list

When you set App IDs in the Restricted Sites App list, the command replaces the current list with the app IDs you specify. You can't add or remove individual app IDs—each run of the command replaces the previous list with a new list for that site type. To avoid removing access for other apps, always include all app IDs you want to allow in your command.

Example 1: To allow only the app with ID `281e395b-7316-4cb2-b5bb-8881426ee411` to create all sites, run the following command in SharePoint Online Management Shell:

```powershell
Set-SPORestrictedSiteCreationForApps –SiteType "All" -RestrictedSiteCreationApps "281e395b-7316-4cb2-b5bb-8881426ee411"
```

This command replaces the existing list with just the specified app ID. Only this app is able to create sites of type "All".

Example 2: To update the list of app IDs that are allowed to create Team sites, use the following command in SharePoint Online Management Shell:

```powershell
Set-SPORestrictedSiteCreationForApps –SiteType "Team" -RestrictedSiteCreationApps "78159241-04a9-41d2-8dd4-ac568e9766a3,1f95829b-e1c8-4406-b2be-508c36f4bca5"
```

This command replaces the current list of allowed apps for Team sites with only the specified app IDs.

Example 3: To control which apps can create Communication sites, use an empty App ID list (`""`) with the `Set-SPORestrictedSiteCreationForApps` command:

```powershell
Set-SPORestrictedSiteCreationForApps –SiteType "Communication" -RestrictedSiteCreationApps ""
```

- **Allow mode:** No apps can create Communication sites.
- **Deny mode:** All apps can create Communication sites.

This command sets the policy based on the current mode (Allow or Deny) and applies it to Communication sites. Add app IDs "" to the list of apps that are allowed to create Communication sites- this means: 

## View the App ID list 

You can view restricted or allowed Apps in the Restricted Sites App list by running a Get command. This command by default includes all configurations. 

You can run `Get-SPORestrictedSiteCreationForApps` without any parameters to return the value of:`Enabled`, `Mode`, and a dictionary matching each site type to its configured app IDs.

You can also run this command filtered by `-SiteType` to return the app IDs for a specific site type:

`Get-SPORestrictedSiteCreationForApps -SiteType <SiteType>` 

 Example: View all app IDs that can create All sites. 

`Get-SPORestrictedSiteCreationForApps –SiteType All`
