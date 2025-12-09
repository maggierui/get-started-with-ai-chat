---
ms.date: 10/07/2025
ms.update-cycle: 180-days
title: Get started with Knowledge Agent (preview)
ms.reviewer: ssquires
ms.author: chucked
author: chuckedmonson
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ROBOTS: 
ms.topic: how-to
ms.service: sharepoint-online
ms.collection: 
- M365-collaboration
- m365copilot
ms.localizationpriority: medium
search.appverid:
- MET150
description: Learn how to set up Knowledge Agent in SharePoint.
---

# Get started with Knowledge Agent (preview)

> [!NOTE]
> This article applies to the preview version of Knowledge Agent in SharePoint.
> 
> Knowledge Agent isn't currently supported in Microsoft 365 Government - GCC, GCC High, DoD, or Office 365 air-gapped cloud environments.

Knowledge Agent is a built-in SharePoint capability designed to help your organization prepare content for AI. It enriches, organizes, and maintains SharePoint content in a structured, authoritative format—optimized for Microsoft 365 Copilot agents.

For eligible tenants, a new agent button appears in the lower-right corner of SharePoint surfaces, giving qualifying users access to advanced AI capabilities. These include automated content enrichment, metadata optimization, and intelligent page summarization.

## Prerequisites

- A [SharePoint Administrator](/entra/identity/role-based-access-control/permissions-reference#sharepoint-administrator) (or [Global Administrator](/entra/identity/role-based-access-control/permissions-reference#global-administrator)) must first [enable Knowledge Agent (preview)](#enable-knowledge-agent).

    > [!IMPORTANT]
    > Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. To learn more, see [About admin roles in the Microsoft 365 admin center](/microsoft-365/admin/add-users/about-admin-roles).

- To use the feature, users must have a [Microsoft 365 Copilot license](/copilot/microsoft-365/microsoft-365-copilot-licensing) assigned and be site owners or members to see the agent button. Usage is included with Microsoft 365 Copilot.

### Role definitions for site access

- **Site Owner**: A user with full Site Owner permissions.
- **Content Manager**: A user with read, write, and list permissions.
- **Content Creator**: A user with read and write permissions to site contents or at least Site Members group access.
- **Content Consumer**: Any user with at least Read permissions to site contents or at least Site Visitors group access.

## Enable Knowledge Agent

For preview, you configure availability using PowerShell. You use `KnowledgeAgent` parameters in `Set-SPOTenant` to enable Knowledge Agent across all sites, selectively include sites, or selectively exclude sites. 

For multi-geo tenants, the PowerShell script must be run in each geo to enable Knowledge Agent in that region.

The enablement process will change for general availability.

Use the [SharePoint Online Management Shell version 16.0.26615.12013 or later](https://www.microsoft.com/download/details.aspx?id=35588) to manage access to the Knowledge Agent preview for users with Copilot licenses. For setup instructions, see [Get started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

If you already have the SharePoint Online Management Shell installed, make sure you're running the latest version by running the following command in administrative mode: `Update-Module -Name Microsoft.Online.SharePoint.PowerShell`.

### To resolve versioning errors

If you get the following error, it might indicate that you have multiple or conflicting versions of the SharePoint Online Management Shell installed:

`Set-SPOTenant : A parameter cannot be found that matches parameter name 'KnowledgeAgentScope'`

To resolve the issue, follow these steps:

1. Remove the conflicting SharePoint modules by opening **Add or remove programs**, and searching for *SharePoint*. Uninstall any SharePoint admin modules you find.

2. Check the installed modules by running the following command:

    `Get-Module -Name *SharePoint* -ListAvailable`

    If multiple versions are listed, remove them using:

    `Uninstall-Module -Name <ModuleName>`

3. Manually delete the remaining modules. If you encounter exceptions during uninstall, use this command to locate the module path:

    `(Get-Module -Name *SharePoint* -ListAvailable).Path`

    Navigate to the parent folder and manually delete it.

4. Restart PowerShell. Close the terminal and reopen it to clear any modules loaded in memory.

5. Repeat cleanup. Repeat steps 2 and 3 until no SharePoint Online PowerShell modules remain.

6. To install the latest SharePoint Online PowerShell module, run:

    `Install-Module -Name Microsoft.Online.SharePoint.PowerShell`

    > [!NOTE]
    > To verify the installed version, use the following command:
    >
    >`(Get-Module -Name Microsoft.Online.SharePoint.PowerShell -ListAvailable).Version`
    >
    >If multiple versions appear, repeat the previous cleanup steps.

<!---

If you get the error **Set-SPOTenant : A parameter cannot be found that matches parameter name 'KnowledgeAgentScope'** it can be an indicator that you have multiple or conflicting versions. Here are some steps to resolve this:

1. Go to add or remove programs, search for SharePoint, and remove possible SharePoint admin module.

2. Run `get-module -name *SharePoint* -ListAvailable` in terminal. If you get still versions listed there, remove them by using the `uninstall-module` cmdlet.

    - If you have exceptions on doing that, use `(get-module -name *SharePoint* -ListAvailable).Path` to resolve the location of module, and then and manually delete the parent folder.

3. Restart PowerShell, close terminal, and open again. It's all loaded in memory.

4. Repeat steps 2 and 3 until you have no SPO PowerShell available.

5. Install the latest version of the SPO PowerShell using this command: `Install-Module -Name Microsoft.Online.SharePoint.PowerShell`.

> [!NOTE]
> You can always check the version details by using following command to ensure that you have the right version locally installed: `(get-module -name Microsoft.Online.SharePoint.PowerShell -ListAvailable).Version`. If you get multiple versions, you have multiple modules installed and you need to repeat the previous steps to clean up.
--->

### KnowledgeAgentScope

- **Description**: Allows administrators to control which SharePoint sites the Knowledge Agent feature is available on.
- **Valid values**:
  - `AllSites`: Knowledge Agent is available on all sites.
  - `IncludeSelectedSites`: Knowledge Agent is available only on sites specified in KnowledgeAgentSelectedSitesList 
    
  - `ExcludeSelectedSites`: Knowledge Agent is available on all sites except those specified in KnowledgeAgentSelectedSitesList.
  - `NoSites`: Knowledge Agent isn't available on any sites. (This is the Default value.)
    
- **Note**: Requires Microsoft 365 Copilot license.

### KnowledgeAgentSelectedSitesList

- **Description**: Allows administrators to pass a list of SharePoint site URLs to include or exclude from the Knowledge agent feature.
- When KnowledgeAgentScope = **ExcludeSelectedSites**: the list is treated as sites to **EXCLUDE** (site opt-out list).
  - When  KnowledgeAgentScope = **IncludeSelectedSites**: the list is treated as sites to **INCLUDE** (site opt-in list).
    
- By default, this overwrites any existing list with the provided list.

- This parameter can only be called when `KnowledgeAgentScope` is set to `IncludeSelectedSites` or `ExcludeSelectedSites`.
- The list of site URLs can't exceed 100 items.
- **Note**: Requires Microsoft 365 Copilot license.

### KnowledgeAgentSelectedSitesListOperation

- **Description**: Specifies the operation to perform on the Knowledge Agent feature's current sites list.

- **Valid values**:
  - `Overwrite`: Overwrite the existing sites list (default).
    
  - `Append`: Append the input list of sites to the existing sites list.
    
  - `Remove`: Remove the input list of sites from the existing sites list.
    
- **Note**: Calling this parameter without `KnowledgeAgentSelectedSitesList` has no effect.

### Example usage

#### Enable Knowledge Agent on all sites

```PowerShell
# Connect to SharePoint Online admin center
Connect-SPOService https://yourtenant-admin.sharepoint.com

# Enable Knowledge Agent for all sites in the tenant
Set-SPOTenant -KnowledgeAgentScope AllSites

# Verify the configuration
Get-SPOTenant | Select-Object KnowledgeAgentScope
```

#### Enable Knowledge Agent on specified sites


```PowerShell
# Connect to SharePoint Online admin center 
Connect-SPOService https://yourtenant-admin.sharepoint.com 

# Set Knowledge Agent to be available only on the included sites 
Set-SPOTenant -KnowledgeAgentScope IncludeSelectedSites 

# Specify sites to enable Knowledge Agent (initial inclusion list) 
Set-SPOTenant -KnowledgeAgentSelectedSitesList @("https://yourtenant.sharepoint.com/sites/site5", "https://yourtenant.sharepoint.com/sites/site7") 

# Add additional sites to the existing inclusion list (if needed) 
Set-SPOTenant -KnowledgeAgentSelectedSitesList @("https://yourtenant.sharepoint.com/sites/site3") -KnowledgeAgentSelectedSitesListOperation Append 

# Verify the inclusion configuration 
Get-SPOTenant | Select-Object KnowledgeAgentScope, KnowledgeAgentSelectedSitesList 
```

#### Enable Knowledge Agent on all sites except specified sites

```PowerShell
# Connect to SharePoint Online admin center
Connect-SPOService https://yourtenant-admin.sharepoint.com

# Set Knowledge Agent to be available on all sites except selected sites
Set-SPOTenant -KnowledgeAgentScope ExcludeSelectedSites

# Specify sites to exclude from Knowledge Agent (initial exclusion list)
Set-SPOTenant -KnowledgeAgentSelectedSitesList @("https://yourtenant.sharepoint.com/sites/site1", "https://yourtenant.sharepoint.com/sites/site2")

# Add additional sites to the existing exclusion list (if needed)
Set-SPOTenant -KnowledgeAgentSelectedSitesList @("https://yourtenant.sharepoint.com/sites/site3") -KnowledgeAgentSelectedSitesListOperation Append

# Verify the exclusion configuration
Get-SPOTenant | Select-Object KnowledgeAgentScope, KnowledgeAgentSelectedSitesList
```

#### Disable Knowledge Agent

```PowerShell
# Connect to SharePoint Online admin center
Connect-SPOService https://yourtenant-admin.sharepoint.com

# Disable Knowledge Agent for all sites in the tenant
Set-SPOTenant -KnowledgeAgentScope NoSites

# Verify Knowledge Agent is disabled
Get-SPOTenant | Select-Object KnowledgeAgentScope
```
