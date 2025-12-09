---
ms.date: 11/21/2025
title: "Manage inactive sites using inactive site policies"
ms.reviewer: nvasudevan
manager: dansimp
recommendations: true
ms.author: ruihu
author: maggierui
audience: Admin
customer-intent: As a SharePoint admin, I want to ensure all inactive sites are properly managed so that resources are optimized.
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

search.appverid:
description: "Learn how to manage inactive SharePoint sites using inactive site policies at scale and automate compliance."
---

# Manage inactive sites using inactive site policies

The site lifecycle management features from [Microsoft SharePoint Advanced Management](/sharepoint/advanced-management) let you improve site governance by having automated policies configured in the [SharePoint admin center](get-started-new-admin-center.md). Inactive site policies, part of SharePoint's site lifecycle management features, help you automate this process. You can set up an inactive site policy to automatically detect inactive sites and notify site owners via email. Owners can then confirm if the site is still active.

## What do you need to create an inactive site policy

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

## How do inactive site policies work

### Scope of inactive site policies

You can configure parameters for an inactive site policy like inactive time period, template type, site creation source, sensitivity labels, and exclusion of up to 100 sites.

#### In-scope site activities

Inactive site policies analyze activity across SharePoint and connected platforms like Teams, Viva Engage (formerly Yammer), and Exchange to detect a site's last activity.

|Platform type | Activities  |
|---------|---------|
|**SharePoint**     |Viewed files, edited files, shared files internally and externally, synced files, viewed pages, visited pages          |
|**Viva Engage (formerly Yammer)**     |Posted messages, read conversations, liked messages         |
|**Teams**     |Posted channel messages in a team across standard channels, posted messages in Teams and standard channels, replied to messages, mentioned in messages, reacted to messages, sent urgent messages, conducted meetings (recurring, ad hoc, one-time)          |
|**Exchange**     | Received emails in the Exchange mailbox       |

#### Scope of app activities

Inactive site policies do not consider app activity via app token. App activity via user token is considered only when a user agent involved and meets the following criteria.

|Activity source| Condition when activity is considered|
| -------- | -------- |
|PnP PowerShell activity via user token|Is not considered|
|SharePoint Online PowerShell activity via user token|Is considered only when UserAgent parameter value is passed       |
|CSOM scripting activity via user token|Is considered when script explicitly sets UserAgent value|
|Any other app activity via user token| Is considered when UserAgent exists, except in the following scenarios when<br> - UserAgent starts with "client-request=id"/"ACTIVEMONITORING"/SPORUNNERS" **OR**<br> - UserAgent ends with "MSDEMO"/"MSDPLATFORM"/"SystemUsage" **OR**<br> - UserAgent contains "GomezAgent"/"bingbot.htm"/"ms search 6.0 robot"/"http://www.monitis.com"/"ISV"|
|App activity via app token| Is not considered     |

#### In-scope site templates

Site lifecycle management reviews the activity of communication sites, classic sites, Teams-connected sites, and group-connected sites with the following site template types:

|Site type|Template type|
|---|---|
|Communication site|SitePagePublishing#0|
|Classic sites|STS#0, STS#1, STS#2, WIKI#0, BLOG#0, SGS#0, SPS#0, SPSNEWS#0, ENTERWIKI#0, COMMUNITY#0, DEV#0, EXPRESS#0, EHS#1, EHS#2|
|Teams-connected site|STS#3 or Group#0|
|Group-connected site|STS#3 or Group#0|

#### Out-of-scope sites

The following sites are considered out-of-scope and excluded from site activity detection:

- OneDrive sites
- Sites created by system users
- App catalog sites
- Root sites
- Home sites
- Tenant admin sites

- Sites associated with Shared and Private Teams channels


### Policy modes

When setting up a site lifecycle policy, you can choose between a simulation policy and an active policy. 

#### Simulation mode

The simulation policy runs once and generates a report based on the set parameters. If it fails, you need to delete it and create a new one. Once you validate a simulation policy, you can convert it to an active policy.

#### Active mode

The active policy runs monthly, generating reports and sending notifications to site owners to confirm the site's status. If it fails during a particular month, it will run again on the next schedule. The active policy enforces actions on inactive sites that remain uncertified by the site owner or admin, provided you configured it to take enforcement actions.

:::image type="content" source="media/site-lifecycle-management/1-inactive-site-policy-dashboard.png" alt-text="Screenshot of Site lifecycle management dashboard." lightbox="media/site-lifecycle-management/1-inactive-site-policy-dashboard.png":::

## How to create an inactive site policy

To create an inactive site policy, expand **Policies** and select **Site lifecycle management** in the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219):

1. Select **+ Create policy** and then select **Next**.
   
   :::image type="content" source="media/site-lifecycle-management/overview.png" alt-text="Screenshot of Overview page." lightbox="media/site-lifecycle-management/overview.png":::

3. Choose your policy scope option and select **Next**.

 [!INCLUDE[Upload a CSV list of sites](includes/site-lifecycle-management/upload-csv-list-sites.md)]
     

> [!NOTE]
> - When you select **Include sites with retention policies and retention holds**, read-only sites and locked sites are included in the scope of the policy.
> - All inactive ownerless sites are automatically included in the scope of the policy.

   :::image type="content" source="media/site-lifecycle-management/scope-scale.png" alt-text="Screenshot of Scope page when selecting the option of sites at scale." lightbox="media/site-lifecycle-management/scope-scale.png":::

      
5. Define the configuration of the policy by selecting the inactivity period, the email recipients and the enforcement actions. Select **Next.**

   During the configuration step, you can:
   - Choose to send emails to site owners or site admins, or both.
   - Customize the email content to provide more context and instructions to the email recipients.
   - Choose enforcement actions if there's no response from site owners or admins after three notifications.
 
   **Choose enforcement actions**
    [!INCLUDE[Enforcement actions](includes/site-lifecycle-management/enforcement-actions.md)]
   :::image type="content" source="media/site-lifecycle-management/configuration.png" alt-text="Screenshot of Configuration page." lightbox="media/site-lifecycle-management/configuration.png":::
   
   
6. Name the policy, add a description (optional), and select a policy mode. Select **Finish**. Your policy is now created and can be viewed and managed from the Site lifecycle management > Inactive site policy dashboard.

   :::image type="content" source="media/site-lifecycle-management/finish.png" alt-text="Screenshot of Finish page." lightbox="media/site-lifecycle-management/finish.png":::

## Inactive site notifications to site owners or site admins

Notifications inform SharePoint site owners or site admins when a site is inactive for a specified number of months. To keep the site, the notification recipients should select the **Certify site** button in the notification email. Once certified, Site lifecycle management doesn't check the site's activity for one year.

### Sites managed by multiple site lifecycle management policies

For each type of site lifecycle management policy—[site ownership policy](/sharepoint/create-sharepoint-site-ownership-policy), [inactive site policy](/sharepoint/site-lifecycle-management), and [site attestation policy](/sharepoint/request-site-attestations)—if multiple policies are created under the same type, notification emails aren't repeated. If a notification was sent within the last 30 days from any policy of that type, and the site remains uncertified, no further notifications are sent. The policy execution report shows the site's status as "Notified by another policy."

For example, if a site is covered by two different inactive site policies and receives a notification email from the first policy, no additional notifications will be sent from the second policy within the next 30 days if the site remains uncertified.

It's recommended to ensure that policies of the same type do not have overlapping scopes. If sites fall under the scope of multiple policies of the same type, the notification schedule and enforcement actions on the site could become unpredictable.

## Enforcement actions

The following table summarizes how the inactive site policy behaves based on the selected enforcement action:

|Enforcement action|Policy behavior|
|---|---|
|**Do nothing**|Site owners or site admins receive monthly notifications for three months. After this period, no notifications are sent for the next three months. If the site remains inactive after six months, monthly notifications resume. The policy execution report lists inactive sites as unactioned by the site owner. You can download this report and filter out sites marked as unactioned.|
|**Read-only access**|Site owners or site admins receive monthly notifications for three months. If the notification recipients don't mark the site as certified during this period, the site goes into read-only mode.|
|**Archive sites after mandatory read-only period**|Site owners or site admins receive monthly notifications for three months. If the notification recipients don't mark the site as certified during this period, then the site goes into a read-only mode for a configurable duration (3, 6, 9, or 12 months). After the configured number of months, the site gets archived through [Microsoft 365 Archive](/microsoft-365/archive/archive-setup). Archival is subject to the tenant enabling Microsoft 365 Archive on the Microsoft Admin center.|

> [!IMPORTANT]
>
> - Site lifecycle policies leverage Outlook Actionable Messages to enable site owners or site admins take necessary actions within email.
> - For notifications to render properly, ensure **[Outlook version requirements](/outlook/actionable-messages/)** are met in your organization.
> - To troubleshoot rendering issues, refer to **[frequently asked questionnaire](/outlook/actionable-messages/actionable-messages-faq)**.
> - When a site owner or site admin selects the site URL in the notification email, this action does **not** count as site activity. The site remains inactive. Additionally, any **read actions** done on the site within one hour of visiting from the email aren't considered activity. However, any **edits** made to the site count as activity and reset the inactivity status.

> [!TIP]
> Before creating an inactive site policy, check for any site access restriction policies that could disrupt site attestation by the respective site owner.

## Read-only mode

An inactive site policy configured with the read-only enforcement action sends additional notifications to inform site owners or site admins when there's no response.

[!INCLUDE[Read-only and archived sites](includes/site-lifecycle-management/read-only-archived-sites.md)]



## Reporting

Sites with inactivity for six months are listed in the policy execution report. The report is available for download as a .csv file and lets you filter out sites that are considered unactioned by site owners.

:::image type="content" source="media/site-lifecycle-management/8-inactive-site-policy-downloaded-csv-report.png" alt-text="Screenshot of inactive site policy downloaded csv report." lightbox="media/site-lifecycle-management/8-inactive-site-policy-downloaded-csv-report.png":::

The following table describes the information included in the policy execution report:

| Column                   | Definition |
|----------------------|--------------------|
| **Site name**                  | Name of the site  |
| **URL**                        | URL of the site  |
| **Template**                   | Template of the site |
| **Connected to Teams**         | Is it a Teams-connected site or not   |
| **Sensitivity label**          | Sensitivity label of the site                |
| **Retention policy**           | Is any retention policy applied to the site or not    |
| **Site lock state**            | State of site access **before** the policy is run (Unlock/Read-Only/No access)                                                                                                                                                      |
| **Last activity date (UTC)**   | Date of last activity detected by inactive site policy across SharePoint site and connected workloads (Exchange, Viva Engage (formerly Yammer), or Teams)                                                                        |
| **Site creation date (UTC)**   | Date when the site was created     |
| **Storage used (GB)**          | Storage consumed by the site  |
| **Number of site owners**      | Total count of site owners for the site   |
| **Email address of site owners**| Email addresses of all site owners  |
| **Number of site admins**      | Total count of site admins for the site    |
| **Email address of site admins**| Email addresses of all site admins    |
| **Action status**              | Status of the site (First/second/third notification sent, Site in read-only mode, Site archived, Action taken by another policy: read-only/archive/notified by another policy)                                                  |
| **Total notifications count**  | Total notifications sent so far by any policy under the same policy template                                                                                                                                                    |
| **Action taken on (UTC)**      | Date on which the enforcement action was taken (date when site was archived or put in read-only mode)                                                                                                                           |
| **Duration in read-only**      | Number of days the site is in the enforced read-only state  |

## Related articles

- [Microsoft 365 group expiration policy](/microsoft-365/solutions/microsoft-365-groups-expiration-policy)

- [Restore deleted sites](restore-deleted-site-collection.md)

- [Overview of Microsoft 365 Archive](/microsoft-365/archive/archive-setup)

