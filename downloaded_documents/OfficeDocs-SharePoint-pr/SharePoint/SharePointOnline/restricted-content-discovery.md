---
ms.date: 11/21/2025
title: "Restrict discovery of SharePoint sites and content"
ms.reviewer: nibandyo
recommendations: true 
manager: dansimp
ms.author: ruihu
author: maggierui
audience: Admin
customer-intent: As a SharePoint administrator, I want to restrict the discovery of specific SharePoint sites and content.
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
- Tier2
- trust-pod
search.appverid:
description: "Learn how to restrict the discovery of SharePoint sites from Microsoft 365 Copilot and tenant-wide search."
---

# Restrict discovery of SharePoint sites and content

For organizations onboarding to Microsoft 365 Copilot, maintaining strong data governance controls for SharePoint content is critical to deploying Copilot in a safe manner. Sites identified with the highest risk of oversharing can use Restricted Content Discovery to protect content while taking time to ensure that permissions are accurate and well-managed.

With Restricted Content Discovery, organizations can limit the ability of end users to search for files from specific SharePoint sites. Enabling Restricted Content Discovery for each site prevents the sites from surfacing in organization-wide search and Microsoft 365 Copilot Business Chat, unless a user had a recent interaction.

Restricted Content Discovery is a site-level setting that needs to be propagated to the search index, a large number of transactions could lead to a long queue in the ingestion pipeline and higher update latency times.

While child content is hidden by default, users in your organization can still discover files they own or recently interacted with. End users can still find relevant content they need for their day-to-day tasks, even if Restricted Content Discovery is applied to the parent site.

Restricted Content Discovery doesn't affect searches originating from a site context or other intelligent features such as Microsoft 365 Feed and Recommendations.

> [!NOTE]
> - Restricted Content Discovery doesn't affect existing permissions on sites. Users with access can still open files on sites with Restricted Content Discovery toggled on.
> - This feature can't be applied to OneDrive sites.

> [!CAUTION]
> Overuse of Restricted Content Discovery can negatively affect performance across search, SharePoint, and Copilot. Removing sites or files from tenant-wide discovery means that there's less content for search and Copilot to ground on, leading to inaccurate or incomplete results.

## Use cases for Restricted Content Discovery

Restricted Content Discovery can be applied to any SharePoint site in your organization. The key use case for this feature is to prevent accidental discovery of high-risk sites.

We recommend using tools such as Data access governance reports and SharePoint admin center's **Active sites** tab to first compile a selective list of targeted sites.

## What you need to restrict a specific SharePoint access?

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

In addition to above, you also need the latest version of [Microsoft SharePoint Online Management Shell](https://www.microsoft.com/download/details.aspx?id=35588).

## Configure Restricted Content Discovery

By default, Restricted Content Discovery is off for all sites. As an IT administrator, you can enable or disable this feature, and check the current state of a given site. You can also delegate Restricted Content Discovery setting to all the site admins of your organization.

### Enable Restricted Content Discovery for a site

You can enable Restricted Content Discovery from the SharePoint admin center or via PowerShell.

To enable Restricted Content Discovery for a site using SharePoint admin center:

1. In SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select the site you want to restrict the content discovery, and the site details panel appears.
3. In the **Settings** tab, toggle on or off in the **Restrict content from Microsoft 365 Copilot** section.
4. Select **Save**.

:::image type="content" source="./media/restricted-content-discovery/1-rcd-enable-spac.png" alt-text="Screenshot of site details panel showing ability to restrict a site from being discovered in Microsoft 365 Copilot." lightbox="./media/restricted-content-discovery/1-rcd-enable-spac.png":::

> [!NOTE]
> Changes can take time to be effective.

To enable Restricted Content Discovery for a site using PowerShell, run the following command:

```powershell
Set-SPOSite –identity <site-url> -RestrictContentOrgWideSearch $true
```

### Check status of Restricted Content Discovery

To check the status of Restricted Content Discovery, run the following command:

```powershell
Get-SPOSite –identity <site-url> | Select RestrictContentOrgWideSearch
```

### Remove Restricted Content Discovery from a site

To remove Restricted Content Discovery on a SharePoint site, run the following command:

```powershell
Set-SPOSite –identity <site-url> -RestrictContentOrgWideSearch $false
```

### Delegate Management of Restricted Content Discovery to Site Admins

As a SharePoint administrator, you can also delegate management of Restricted Content Discovery control to site admin. Upon managing the policy, the site admins would need to provide appropriate justification on why the policy is being updated. 

By default, the delegation is turned off.  If you decide to enable it, run the following command:

```powershell
Set-SPOTenant -DelegateRestrictedContentDiscoverabilityManagement $true
```

### Check status of Delegate management of Restricted Content Discovery to site admins

To check the delegation status, run the following command:

```powershell
Get-SPOTenant | Select-Object DelegateRestrictedContentDiscoverabilityManagement
```


Once the Restricted Content Discovery setting is delegated to all the site admins, they can manage the policy. 

![RCD configuration by site admin](media/restricted-content-discovery/configuration-by-site-admin.png)

The site admins would need to provide justification whenever the Restricted Content Discovery setting is updated by them, as shown below:

![RCD justification by site admin](media/restricted-content-discovery/justification-by-site-admin.png)

Once the policy is enabled on the site, the **Restricted** tag will be visible on the Home tab of the site as shown below:

## ![Restricted marker](media/restricted-content-discovery/restricted-marker.png)

## Auditing

Audit events are available in the Microsoft’s Unified Audit log to help you monitor activities related to managing of Restricted Content Discovery. Audit events are logged are: 

- Turning on the Restricted Content Discovery setting for site 

- Turning off the Restricted Content Discovery setting for site 

- Justification for updating Restricted Content Discovery setting for site

## Restricted Content Discovery policy insights

You can view the following reports to gain insights on the SharePoint sites protected with Restricted Content Discovery:

### Generate insights report

To generate a list of sites with Restricted Content Discovery enabled, run the following command:

```powershell
Start-SPORestrictedContentDiscoverabilityReport
```

### View insights report

To view a report displaying the Report GUID, created DateTime stamp, and status of the report generation, run the following command:

```powershell
Get-SPORestrictedContentDiscoverabilityReport
```

### Download insights report

To download a Restricted Content Discovery insights report, you must run the following command as an administrator:

```powershell
Get-SPORestrictedContentDiscoverabilityReport –Action Download –ReportId <Report GUID>
```

The downloaded report is located on the path where the command was run.

## Next steps

Restricted Content Discovery gives organizations time to review and/or audit permissions and deploy access controls while onboarding Copilot in a safe manner.

Ultimately for sites that are overshared, the goal is to ensure that proper controls are in place to manage access. SharePoint Advanced Management has a suite of features, such as advanced site content lifecycle management, to help site owners and admins create a robust SharePoint governance framework.

## Frequently Asked Questions

**Is my organization eligible to use Restricted Content Discovery?**

Customers who are licensed for Copilot and have SharePoint Advanced Management available to them can configure Restricted Content Discovery.

**What search scenarios enforce Restricted Content Discovery?**

Restricted Content Discovery only affects tenant-wide search (SharePoint home, Office.com, Bing) and Microsoft 365 Copilot. Only Copilot Discovery scenarios are in scope; Copilot experiences that use data-in-use, such as "summarize the current document" in Word aren't impacted.  

**Does Restricted Content Discovery impact other features with dependencies on the search index, such as the Microsoft Purview product suite?**

No, Restricted Content Discovery doesn't remove content from the tenant search index, which means Microsoft Purview features such as eDiscovery and autolabeling aren't impacted.

**How soon can I expect Search and Copilot to reflect an update made to the Restricted Content Discovery configuration of a site?**

Restricted Content Discovery is a site-level property. Index update latency is highly dependent on the number of items in the site and the number of sites getting updated at the same time. For sites with more than 500,000 items, the Restricted Content Discovery update could take more than a week to fully process and reflect in search and Copilot.

**How does Restricted Content Discovery affect the end user experience in Copilot?**

Based on usage of this feature, Copilot has less information available to reference, which could negatively affect its ability to provide accurate and comprehensive responses.

**How does Restricted Content Discovery fit into an overall approach to prepare SharePoint data for Microsoft 365 Copilot?**

Restricted Content Discovery is designed to limit the ability of end users to search for content from specific SharePoint sites. For a more comprehensive guidance on preparing your data for Copilot, check out this [blueprint](https://aka.ms/Copilot/OversharingBlueprintLearn).
