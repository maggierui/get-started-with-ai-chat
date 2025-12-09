---
ms.date: 11/17/2025
title: "Request recurring site attestations for SharePoint sites"
ms.reviewer: nibandyo
recommendations: true 
ms.author: ruihu
author: maggierui
manager: dansimp
audience: Admin
customer-intent: As a SharePoint administrator, I want to request recurring site attestations for SharePoint sites to ensure compliance with organizational policies.
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
search.appverid:
description: "Learn how to request recurring site attestations for SharePoint sites to ensure compliance with organizational policies."
---
# Request recurring site attestations for SharePoint sites

The site lifecycle management features from [Microsoft SharePoint Advanced Management](/sharepoint/advanced-management) let you improve site governance by having automated policies configured in the [SharePoint admin center](get-started-new-admin-center.md). Site attestation policies, part of SharePoint's site lifecycle management features, help you manage periodic attestation of sites at scale. This attestation involves regular reviews by site owners or admins to check and confirm the accuracy of site information, including the site's necessity, its owners, members, permissions, and sharing settings. For sites that remain unattested, you can choose to automate enforcement actions, to prevent risks of content over exposure. This approach ensures ongoing site compliance and actively reduces risks such as information oversharing.  

## What do you need to create a site attestation policy

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

## How does site attestation policy work?

### Scope of site attestation policies

You can create site life cycle policies with different scopes based on your organization's requirements. You can choose the sites to be scoped under the policy based on:

-	Site templates
-	Creation sources
-	Sensitivity labels
-	And whether to include sites under retention policies and retention holds

If you wish to exclude specific sites, you can add the site URLs of up to 100 sites in the Exclude sites section while configuring the policy.
 
### Policy modes

When setting up a site lifecycle policy, you can choose between a simulation policy and an active policy. 

#### Simulation mode

The simulation policy runs once and generates a report based on the set parameters. If it fails, you need to delete it and create a new one. Once you validate a simulation policy, you can convert it to an active policy.

> [!NOTE]
> Site lifecycle policies in simulation mode are now available in GCCH and DoD environments as of November 17, 2005.

#### Active mode

The active policy runs monthly, generating reports and sending notifications to site owners to confirm the site's status. If it fails during a particular month, it will run again on the next schedule. The policy enforces actions on inactive sites that remain unattested by the site owner or admin, provided you configured it to take enforcement actions.

## Create site attestation policies

To create a site attestation policy, start with these steps:

1. Sign in to the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219) with the [SharePoint administrator](sharepoint-admin-role.md) credentials for your organization.
2. In the left pane, expand **Policies** and select **Site lifecycle management**.

![Screenshot of the Site lifecycle management page showing the Site attestation option.](media/site-lifecycle-management/site-attestation-on-site-lifecycle-page.png "Site lifecycle management page with Site attestation")

3. Under **Site attestation policies**, select **Open**.
4. Select **Create a policy**.
5. On the **Overview** page of **Manage site attestation**, select **Next**.

On the next page, you will define the scope of the policy.

## Define the scope of the site attestation policy

To define the scope of the site attestation policy, on the **Select policy scope** page, you can start by selecting the sites for the policy with one of the following approaches:

   - Upload a CSV file with a list of up to 10,000 URLs
   - Select sites at scale 

  :::image type="content" source="media/site-lifecycle-management/scope-options.png" alt-text="Screenshot showing scope options for site attestation policy in SharePoint admin center." lightbox="media/site-lifecycle-management/scope-options.png":::

### Upload a csv file with the list of sites

If you select **Upload a CSV file with a list of up to 10,000 URLs**, you can upload a list of site URLs of select sites for the policy.  

:::image type="content" source="media/site-lifecycle-management/upload-csv-site-list.png" alt-text="Screenshot showing the option to upload a CSV file with site URLs for site attestation policy in SharePoint admin center." lightbox="media/site-lifecycle-management/upload-csv-site-list.png":::

> [!TIP]
> - You can export the site list from the SharePoint active sites page 
> - Ensure the CSV file use the same format of the sample CSV file and has no duplicate URLs and those URLs are valid and complete. 
> - Ensure the URLs listed in CSV file belong to your tenant’s domain.  

### Select sites at scale

If you choose **Select sites at scale**, you can then select site templates to include in this policy, and filter them by:

-	Sensitivity label
-	Site creation source

You can also choose whether to:
- Include sites with retention policies and retention holds
- Exclude specific sites from this policy

:::image type="content" source="media/site-lifecycle-management/scope-scale.png" alt-text="Screenshot showing scale options for site attestation policy in SharePoint admin center." lightbox="media/site-lifecycle-management/scope-scale.png":::

#### Select site template types

You can select site template types from the following:

-	All sites
-	Classic sites
-	Communication sites
-	Group connected sites without teams
-	Team sites without Microsoft 365 group
-	Teams-connected sites
 
#### Filter sites by sensitivity labels

You can set policy scope by filtering sites with their sensitivity labels. 

> [!NOTE]
> If your tenant hasn’t set up sensitivity labels, this option will be greyed out.

#### Filter sites by creation source

You can filter sites for the policy scope by site creation source:
-	SharePoint Home
-	SharePoint admin center
-	PowerShell
-	PnP
-	Teams
 
#### Include sites with retention policies and retention holds

By default, the box of **Include sites with retention policies and retention holds, read-only sites and locked sites** is selected, meaning sites in a read-only state or locked states are included in the scope of the policy, with whatever other filters applied.

#### Exclude specific sites from the policy

You can enter up to 100 sites that you want to exclude from the policy. Be sure to separate each URL by new lines.

:::image type="content" source="media/site-lifecycle-management/exclude-sites.png" alt-text="Screenshot showing the option to exclude specific sites from a site attestation policy in SharePoint admin center." lightbox="media/site-lifecycle-management/exclude-sites.png":::

After setting the policy’s scope, select **Next**. You will then configure the site attestation policy settings.

## Configure site attestation policy settings

On the Configure policy page, you can:

-	Choose how often you want the sites to be attested (3 months, 6 months, and 12 months)
-	Identify who is responsible for attesting the site (site owners, site admins or both)
-	Exclude site owners or admins from receiving requests
-	Specify what action should the policy take after 3 notifications

### Exclude site owners or admins from receiving requests

You can exclude up to 100 users or Microsoft 365 or security groups from receiving attestation requests even if they are the site owners or site admins for the sites included in the policy. 

### Actions to take on unattested sites after three notifications

For sites that are unattested after 3 monthly notifications, you can choose to either do nothing, or take one of the following enforcement actions. The following table summarizes how the inactive site policy behaves for each selected enforcement action:

|Enforcement action|Policy behavior|
|---|---|
|**Do nothing**|Site owners or site admins receive monthly notifications for three months. After this period, no notifications are sent for the next three months. If the site remains unattested after six months, monthly notifications resume. The policy execution report lists unattested sites as unactioned by the site owner. You can download this report and filter out sites marked as unactioned.|
|**Read-only access**|Site owners or site admins receive monthly notifications for three months. If the notification recipients don't mark the site as attested during this period, the site goes into read-only mode.|
|**Archive sites after mandatory read-only period**|Site owners or site admins receive monthly notifications for three months. If the notification recipients don't mark the site as attested during this period, then the site goes into a read-only mode for a configurable duration (3, 6, 9, or 12 months). After the configured number of months, the site gets archived through [Microsoft 365 Archive](/microsoft-365/archive/archive-setup). Archival is subject to the tenant enabling Microsoft 365 Archive on the Microsoft Admin center.|

:::image type="content" source="media/site-lifecycle-management/enforcement-actions.png" alt-text="Screenshot showing enforcement actions available for unattested SharePoint sites in site attestation policy." lightbox="media/site-lifecycle-management/enforcement-actions.png":::

> [!NOTE]
> If you configure the policy to take an enforcement action:
>
>  - The notifications won’t be sent after policy action is successful.
>  - The site and it’s status are included in the monthly report.



After configuring the policy settings, select **Next** to finish your policy. Name the policy, add a description (optional), and select a policy mode.

Select **Finish**. Your policy is now created and can be viewed and managed from the **Site lifecycle management** > **Site attestation policy** dashboard.

### Site set as read-only mode

An unattested site policy configured with the read-only enforcement action sends additional notifications to inform site owners or site admins when the site goes into read-only mode.

:::image type="content" source="media/site-lifecycle-management/9-inactive-site-policy-read-only-mode.png" alt-text="Screenshot of Site lifecycle management read-only mode notification." lightbox="media/site-lifecycle-management/9-inactive-site-policy-read-only-mode.png":::

Once the site is in read-only mode, the following banner is added to the site:

:::image type="content" source="media/site-lifecycle-management/10-inactive-site-policy-read-only-mode-banner.png" alt-text="Screenshot of Site lifecycle management read-only mode banner at the top of a SharePoint site." lightbox="media/site-lifecycle-management/10-inactive-site-policy-read-only-mode-banner.png":::

#### Remove site from read-only mode

To remove a site from read-only mode in [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219), go to the **Active sites** page, select the site, and then select **Unlock** from the site page panel.

Site owners can't remove a site from read-only mode and must contact the tenant admin to remove read-only mode.

:::image type="content" source="media/site-lifecycle-management/11-inactive-site-policy-read-only-mode-site-page.png" alt-text="Screenshot of Site lifecycle management site page in SharePoint admin center." lightbox="media/site-lifecycle-management/11-inactive-site-policy-read-only-mode-site-page.png":::

### Unarchive a site

To unarchive a site in [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219), expand **Sites** and select **Archived sites**. Select the site you want to unarchive and select **Reactivate**.

> [!NOTE]
> Only tenant admins can reactivate an archived site.

### Sites managed by multiple site attestation policies

For each type of site lifecycle management policy—[site ownership policy](/sharepoint/create-sharepoint-site-ownership-policy), [inactive site policy](/sharepoint/site-lifecycle-management), and [site attestation policy](/sharepoint/request-site-attestations)—if multiple policies are created under the same type, notification emails aren't repeated. If a notification was sent within the last 30 days from any policy of that type, and the site remains unattested or uncertified, no further notifications are sent. The policy execution report shows the site's status as "Notified by another policy."

For example, if a site is covered by two different site attestation policies and receives a notification email from the first policy, no additional notifications will be sent from the second policy within the next 30 days if the site remains unattested.

It's recommended to ensure that policies of the same type do not have overlapping scopes. If sites fall under the scope of multiple policies of the same type, the notification schedule and enforcement actions on the site could become unpredictable.

## Reporting

After each run of the configured policy, you can view a detailed report about the sites it identifies.
In the **Site attestation policies** page, select the desired policy from the list.
The panel outlines the numbers of:
- Sites to be attested
- Sites that didn't have anyone to notify
- Sites attested
- Sites set to ready-only
- Archived sites
You can also view the policy’s scope, configuration, and general information on the report. 

:::image type="content" source="media/site-lifecycle-management/attestation-report-detail.png" alt-text="Screenshot showing the detailed attestation report for SharePoint site lifecycle management." lightbox="media/site-lifecycle-management/attestation-report-detail.png":::

You can also view the policy’s scope, configuration, and general information on the panel. Select the **Download detailed report** option to download the report in CSV containing the following details for each of the sites identified due for attestation:

| Column                      | Definition                                                                                   |
|-----------------------------|----------------------------------------------------------------------------------------------|
| Site name                   | Name of the site                                                                             |
| URL                         | URL of the site                                                                              |
| Template                    | Template of the site                                                                         |
| Connected to Teams          | Indicates if it is a Teams-connected site                                                    |
| Sensitivity label           | Sensitivity label assigned to the site                                                       |
| Retention policy            | Indicates if any retention policy is applied to the site                                     |
| Site lock state             | State of site access **before** the policy runs (Unlock/Read-Only/No access)                 |
| Notified site admins        | Email addresses of site admins receiving attestation notifications                           |
| Notified site owners        | Email addresses of site owners receiving attestation notifications                           |
| Last attested by            | Email address of the person who last attested the site                                       |
| Last attestation date (UTC) | Date when the site was last attested                                                         |
| Number of site owners       | Total count of site owners for the site                                                      |
| Email address of site owners| Email addresses of all site owners                                                           |
| Number of site admins       | Total count of site admins for the site                                                      |
| Email address of site admins| Email addresses of all site admins                                                           |
| Total notifications count   | Total notifications sent so far by any policy under the same policy template                 |
| Action status of policy     | Status of the site (First/second/third notification sent, Site in read-only mode, Site archived, Action taken by another policy such as read-only/archive/notified by another policy) |
| Action taken on (UTC)       | Date on which the enforcement action was taken (date when site was archived or put in read-only mode) |
| Last activity date (UTC)    | Date of last activity detected across SharePoint site and connected workloads                |
| Site creation date (UTC)    | Date when the site was created                                                               |
| Storage used (GB)           | Storage consumed by the site                                                                 |
| Duration in read-only (days)| Number of days the site is in the enforced read-only state                                   |

