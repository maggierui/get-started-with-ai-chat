---
ms.date: 10/20/2025
title: "Restrict SharePoint site access with Microsoft 365 groups and Microsoft Entra security groups"
ms.reviewer: nibandyo
recommendations: true 
ms.author: ruihu
author: maggierui
manager: dansimp
audience: Admin
customer-intent: As a SharePoint administrator, I want to restrict access to specific SharePoint sites and content by security groups.
f1.keywords: 
- NOCSH 
ms.topic: how-to
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.custom:
  - has-azure-ad-ps-ref
ms.collection: 
- M365-collaboration
- M365-SAM
- Highpri
- Tier2
- ContentEngagementFY24
- trust-pod
search.appverid:
description: "Learn how to restrict access to SharePoint sites to members of a Microsoft 365 or Microsoft Entra security group."
---

# Restrict SharePoint site access with Microsoft 365 groups and Microsoft Entra security groups

Restricted site access control lets you prevent oversharing by designating access of SharePoint sites and its content to users in a specific group. Users not in the specified group can't access the site or its content, even if they had prior permissions or a shared link. This policy can be applied on Microsoft 365 group-connected, Teams-connected, and nongroup connected sites using Microsoft 365 groups or Microsoft Entra security groups.

Site access restriction policies are applied when a user attempts to open a site or access a file. Users with direct permissions to the file can still view files in search results. However, they can't access the files if they're not part of the specified group.

:::image type="content" source="media/sam-overview/3-restricted-access-control-sharepoint-sites.png" alt-text="Screenshot of saved changes for restricted access control for SharePoint sites." lightbox="media/sam-overview/3-restricted-access-control-sharepoint-sites.png":::

Restricting site access via group membership can minimize the risk of oversharing content. For insights into data sharing, see [Data access governance reports](data-access-governance-reports.md).

## What do you need to restrict site access?

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

## Enable site-level access restriction for your organization

You must enable site-level access restriction for your organization before you can configure it for individual sites.

To enable site-level access restriction for your organization in SharePoint admin center:

1. Expand **Policies** and select **Access control**.
2. Select **Site-level access restriction**.
3. Select **Allow access restriction** and then select **Save**.

   :::image type="content" source="media/rac-spac/1-RAC-SPAC-dashboard-feb-2024.png" alt-text="screenshot of site access restriction in sharepoint admin center dashboard." lightbox="media/rac-spac/1-RAC-SPAC-dashboard-feb-2024.png":::

To enable site-level access restriction for your organization using PowerShell, run the following command:

```Powershell
Set-SPOTenant -EnableRestrictedAccessControl $true
```

It might take up to one hour for the command to take effect.

> [!NOTE]
> For Microsoft 365 Multi-Geo users, run this command separately for each desired geo-location.

## Restrict access to all SharePoint sites using Microsoft 365 group or Microsoft Entra security groups

You can restrict access to a SharePoint site by specifying Microsoft Entra security groups or Microsoft 365 groups as the Restricted Access Control group. The control group should have the users who should be allowed access to the site and its content.

For a site, you can configure up to 10 Microsoft Entra security groups or Microsoft 365 groups. Once the policy is applied, users in the specified group who have access permission to the content are allowed access.

> [!IMPORTANT]
> Adding people to the Restricted Access Control group (Microsoft Entra security group or Microsoft 365 group) doesn't automatically give the users access permission to the site or the content. For a user to be able to access the content protected with this policy, the user would need to have both the site or content access permission AND be a member of the Restricted Access Control group.

> [!NOTE]
> You can also use dynamic security groups as a Restricted Access Control group if you want to base group membership on user properties.

### Manage site access for a site

To manage site access for a site:

1. In SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select the site you want to manage and the site details panel appears.
3. In **Settings** tab, select **Edit** in the Restricted site access section.
4. Select the **Restrict SharePoint site access to only users in specified groups** check box.
5. Add or remove your security groups or Microsoft 365 groups and select **Save**.

In order for site access restriction to be applied to the site, you must add at least one group to the site access restriction policy.

:::image type="content" source="media/rac-spac/non-group-connected-sites/restricted-access-control-non-group-connected-site-page.png" alt-text="screenshot showing site access restriction security groups being added to nongroup connected sites." lightbox="media/rac-spac/non-group-connected-sites/restricted-access-control-non-group-connected-site-page.png":::

For a group connected site, the Microsoft 365 group connected to the site is added as the default Restricted Access Control group. You can choose to keep this group and add more Microsoft 365 or Microsoft Entra Security groups as Restricted Access Control group.

:::image type="content" source="media/rac-spac/7-rac-group-connected.png" alt-text="screenshot showing site access restriction security groups being added to connected sites." lightbox="media/rac-spac/7-rac-group-connected.png":::

> [!NOTE]
> There's a tag labeled as **Default group** marked against the Microsoft 365 group connected to the site as shown in the previous image.

To manage site access restriction for a SharePoint site using PowerShell, use the following commands:

| Action  | PowerShell command |
|---------|---------|
|Enable site access restriction     |`Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true`|
|Add group |`Set-SPOSite -Identity <siteurl> -AddRestrictedAccessControlGroups <comma separated group GUIDS>`         |
|Edit group     |`Set-SPOSite -Identity <siteurl> -RestrictedAccessControlGroups <comma separated group GUIDS>`         |
|View group     |`Get-SPOSite -Identity <siteurl> Select RestrictedAccessControl, RestrictedAccessControlGroups`         |
|Remove group     |`Set-SPOSite -Identity <siteurl> -RemoveRestrictedAccessControlGroups <comma separated group GUIDS>`         |  
|Reset site access restriction  |`Set-SPOSite -Identity <siteurl> -ClearRestrictedAccessControl`         |

### Site admin and site owner experience

Once you apply the policy to the site, the policy status and all configured control groups are displayed for site owners and site admins on the **Site access** panel in addition to the **Site Information** and **Permissions** panels.

:::image type="content" source="media/rac-spac/8-rac-site-access-panel.png" alt-text="screenshot showing site access restriction panel." lightbox="media/rac-spac/8-rac-site-access-panel.png":::

## Shared and private channel sites

Shared and private channel sites are separate from the Microsoft 365 group-connected site that standard channels use. Because shared and private channel sites aren't connected to the Microsoft 365 group, site access restriction policies applied to the team don't affect them. You must enable site access restriction for each shared or private channel site separately as nongroup connected sites.

For shared channel sites, only internal users in the resource tenant are subject to site access restriction. External channel participants are excluded from site access restriction policy and only evaluated per the site's existing site permissions.

> [!IMPORTANT]
> Adding people to the security group or Microsoft 365 group doesn't give users access to the channel in Teams. We recommend adding or removing the same users of the Teams channel in Teams and the security group or Microsoft 365 group, so users have access to both Teams and SharePoint sites.

## Auditing

Audit events are available in the Microsoft Purview portal to help you monitor site access restriction activities. Audit events are logged for the following activities:

- Applying site access restriction for site
- Removing site access restriction for site
- Changing site access restriction groups for site

## Reporting

### Restricted site access policy insights

As an IT administrator, you can view the following reports to gain more insight about SharePoint sites protected with restricted site access policy:

- Sites protected by restricted site access policy (RACProtectedSites)
- Details of access denials due to restricted site access (ActionsBlockedByPolicy)

> [!NOTE]
> It can take a few hours to generate each report.

### Sites protected by restricted site access policy report

You can run the following commands in SharePoint PowerShell to generate, view, and download the reports:

| Action  | PowerShell command | Description |
|---------|---------|---------|
|Generate report     |`Start-SPORestrictedAccessForSitesInsights -RACProtectedSites`| Generates a list of sites protected by restricted site access policy|
|View report |`Get-SPORestrictedAccessForSitesInsights -RACProtectedSites -ReportId <Report GUID>`| The report shows the top 100 sites with the highest page views that are protected by the policy.|
|Download report   |`Get-SPORestrictedAccessForSitesInsights -RACProtectedSites -ReportId <Report GUID> -Action Download`| This command must be run as an administrator. The downloaded report is located on the path where the command was run.|
|Percentage of site protected with restricted site access report|`Get-SPORestrictedAccessForSitesInsights -RACProtectedSites -ReportId <Report GUID> -InsightsSummary`|This report shows the percentage of sites that are protected by the policy out of the total number of sites|

### Access denials due to restricted site access policy report

You can run the following commands to create, fetch, and view report for access denials due to restricted site access reports:

| Action  | PowerShell command | Description |
|---------|---------|---------|
|Create access denials report    |`Start-SPORestrictedAccessForSitesInsights -ActionsBlockedByPolicy`| Creates a new report for fetching access denial details|
|Fetch access denials report status |`Get-SPORestrictedAccessForSitesInsights -ActionsBlockedByPolicy`| Fetches the status of the generated report.|
|Latest access denials in the past 28 days|`Get-SPORestrictedAccessForSitesInsights -ActionsBlockedByPolicy -ReportId <Report ID> -Content AllDenials`| Gets a list of the most recent 100 access denials that occurred in the past 28 days|
|View list of top users who were denied access| `Get-SPORestrictedAccessForSitesInsights -ActionsBlockedByPolicy -ReportId <Report ID> -Content TopUsers`|Gets a list of the top 100 users who received the most access denials|
|View list of top sites that received the most access denials|`Get-SPORestrictedAccessForSitesInsights -ActionsBlockedByPolicy -ReportId <Report ID> -Content TopSites`| Gets a list of the top 100 sites that had the most access denials|
|Distribution of access denials across different types of sites|`Get-SPORestrictedAccessForSitesInsights -ActionsBlockedByPolicy -ReportId <Report ID> -Content SiteDistribution`|Shows the distribution of access denials across different types of sites|

> [!NOTE]
> To view up to 10,000 denials, you must download the reports. Run the download command as an administrator and the downloaded reports are located on the path from where command was run.

## Sharing of site and content with users outside of Restricted Access Control Groups (opt-in capability)

Sharing of SharePoint sites and its content doesn't honor restricted site access policy by default. The SharePoint administrator can choose to restrict sharing of site and its content with users who aren't members of the Restricted Access Control group.

To restrict sharing capability with users outside of the Restricted Access Control group, enable it, run the following PowerShell command in SharePoint Online Management Shell as an Administrator:

```powershell
Set-SPOTenant -AllowSharingOutsideRestrictedAccessControlGroups $false
```

### Sharing with users

Once sharing restriction is applied, sharing is blocked for users who aren't members of the Restricted Access Control group.

:::image type="content" source="media/rac-spac/rac-share-with-users.png" alt-text="screenshot of sharing with users message." lightbox="media/rac-spac/rac-share-with-users.png":::

### Sharing with groups

Sharing is allowed with Microsoft Entra Security or Microsoft 365 groups which are part of the Restricted Access Control groups list. Thus, sharing with all other groups including Everyone except external users or SharePoint groups aren't allowed.

:::image type="content" source="media/rac-spac/rac-share-with-groups.png" alt-text="screenshot of sharing with groups message." lightbox="media/rac-spac/rac-share-with-groups.png":::

> [!NOTE]
> Sharing of a site and its content isn't allowed for the nested security groups that are part of the Restricted Access Control groups. This support will be added in the next release iteration.

## Configure the Learn more link for access denial error page (opt-in capability)

Configure the **Learn more** link to inform users who were denied access to a SharePoint site due to the restricted site access control policy. With this customizable error link, you can provide more information and guidance to your users.

> [!NOTE]
> The **Learn more** link is a tenant-level setting that applies to all sites with Restricted Access Control policy enabled.  

To configure the link, run the following command in SharePoint PowerShell:

```powershell
Set-SPOTenant -RestrictedAccessControlForSitesErrorHelpLink “<Learn more URL>” 
```

To fetch the value of the link, run the following command:

```powershell
Get-SPOTenant | select RestrictedAccessControlForSitesErrorHelpLink 
```

The configured learn more link is launched when the user selects the **Know more about your organization’s policies here** link.

![Screenshot that shows learn more link for Restricted Access Control.](media/rac-spac/2-rac-learn-more-link.png)

## Related articles

[Conditional access policy for SharePoint sites and OneDrive](authentication-context-example.md)

[Data Access Governance reports](data-access-governance-reports.md)
