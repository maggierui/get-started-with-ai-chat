---
ms.date: 11/17/2025
title: Create SharePoint site ownership policy
ms.reviewer: anupam.francis
ms.author: ruihu
author: maggierui
manager: dansimp
audience: Admin
customer-intent: As a SharePoint admin, I want to ensure all sites have proper ownership so that content is managed effectively.
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection: 
- M365-collaboration
- M365-sam
ms.custom:
search.appverid:
ms.assetid: 0ecb2cf5-8882-42b3-a6e9-be6bda30899c
description: Learn how to create a SharePoint site ownership policy to manage site ownerships at scale and automate compliance.
---

# Monitor SharePoint site ownership automatically with site ownership policies

The site lifecycle management features from [Microsoft SharePoint Advanced Management](/sharepoint/advanced-management) let you improve site governance by having automated policies configured in the [SharePoint admin center](get-started-new-admin-center.md). Site ownership policies, part of SharePoint's site lifecycle management features, help you automatically monitor and enforce site ownership requirements across your organization. These policies allow you to define who should be responsible for each site, set minimum owner or admin counts, and automate notifications when sites do not meet your criteria. By regularly identifying noncompliant sites and prompting users to take action, site ownership policies support effective site management, reduce the risk of ownerless sites, and help maintain security and compliance in your SharePoint environment.

## What do you need to create a site ownership policy

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

## How does site ownership policies works?

### Scope of site ownership policies

You can create different policies with different scopes based on your organization's requirements.

You can choose the sites to be scoped under the policy based on site templates, creation sources, sensitivity labels and include sites under retention policies and retention holds. If you wish to exclude specific sites, you can add the site URLs of up to 100 sites in the Exclude sites section while configuring the policy.

> [!NOTE]
>
> - OneDrive sites, sites created by system users, app catalog sites, root sites, home sites, tenant admin sites are excluded from site ownership policies.
>
> - Sites marked as read-only by site ownership policies will be detected and added to the report if they are not compliant as per policy configurations. All other sites locked with no access or read-only access are excluded from site ownership policies.  

### Policy modes

When setting up a site lifecycle policy, you can choose between a simulation policy and an active policy. 

#### Simulation mode

The simulation policy runs once and generates a report based on the set parameters. If it fails, you need to delete it and create a new one. Once you validate a simulation policy, you can convert it to an active policy.

#### Active mode

The active policy runs monthly, generating reports and sending notifications to site owners to confirm the site's status. If it fails during a particular month, it will run again on the next schedule. The active policy enforces actions on inactive sites that remain uncertified by the site owner or admin, provided you configured it to take enforcement actions.

### Ownership criteria

Different organizations have different needs. Site ownership policies allow you to customize how ownership is determined by allowing you to:

- Choose who is considered responsible for managing a site in your organization - site owners or site admins or both.  

- Define the minimum number of owners or admins a site should have, currently up to 2.

The policy identifies all sites that aren't compliant with the configured ownership criteria and generate the report. If your policy is active, email notifications would then be sent for identified sites.  

We recommend choosing 2 as the minimum owner count so that sites with a single owner are identified and another owner is added immediately. Having more than one site owner can help to reduce the risk of sites becoming ownerless.

### How can you resolve user ID mismatches before running the site ownership policy?

Before running the site ownership policy, it's important to resolve any user ID mismatches to ensure accurate ownership outcomes for each site. Sometimes, if a site owner was deleted and later recreated, ownership references may point to an old, non-existent PUID. As a tenant admin, you should fix these mismatches by running the [Site User ID Mismatch diagnostic](/troubleshoot/sharepoint/sharing-and-permissions/fix-site-user-id-mismatch).

## Create a site ownership policy

To create a site ownership policy, go to the SharePoint admin center.

1. Expand **Policies** and select **Site lifecycle management**.

    :::image type="content" source="media/site-ownership-policy/1-create-site-ownership-policy.png" alt-text="Screenshot of ownership policy being created in SharePoint admin center dashboard." lightbox="media/site-ownership-policy/1-create-site-ownership-policy.png":::

2. Select **+ Create policy** and select **Next**.

    :::image type="content" source="media/site-ownership-policy/2-create-site-ownership-policy.png" alt-text="Screenshot of ownership policy created in SharePoint admin center dashboard." lightbox="media/site-ownership-policy/2-create-site-ownership-policy.png":::

3. Enter your policy scope parameters that determine which sites the policy would act on and select **Next**.

    :::image type="content" source="media/site-ownership-policy/3-create-site-ownership-policy.png" alt-text="Screenshot of site ownership policy with set policy scope in SharePoint admin center dashboard." lightbox="media/site-ownership-policy/3-create-site-ownership-policy.png":::

    [!INCLUDE[Upload a CSV list of sites](includes/site-lifecycle-management/upload-csv-list-sites.md)]

4. Define the ownership criteria, who should be notified if a site doesn't meet these criteria and what action to take if the site fails to meet these criteria for three months. Select **Next**.

    :::image type="content" source="media/site-ownership-policy/4-create-site-ownership-policy.png" alt-text="Screenshot of ownership policy configuration page in SharePoint admin center dashboard." lightbox="media/site-ownership-policy/4-create-site-ownership-policy.png":::


5. Name your policy, add a description (optional) and select a policy mode. Select **Finish**.

    :::image type="content" source="media/site-ownership-policy/5-create-site-ownership-policy.png" alt-text="Screenshot of ownership policy with notifications options selected." lightbox="media/site-ownership-policy/5-create-site-ownership-policy.png":::

6. Select **Done**. Your policy is now created and can be viewed and managed by selecting Site ownership policies in the Site lifecycle management dashboard.


## Inactive site notifications

Each policy runs every month to identify noncompliant sites. Email notifications are then sent to the configured set of recipients as per the policy.  
Notifications are triggered only if the policy is running in Active mode.

> [!IMPORTANT]
> Site lifecycle policies leverage Outlook Actionable Messages to enable recipients take necessary actions within email. 
> - For notifications to render properly, ensure [Outlook version requirements](/outlook/actionable-messages/) are met in your organization.   
> - To troubleshoot rendering issues, refer to [frequently asked questionnaire](/outlook/actionable-messages/actionable-messages-faq).

The potential recipients of these email notifications, if configured in the policy, are:

- **Current site owners:** If the minimum owner or admin count is set to 2 and the site has an existing site owner, they receive an email notification asking them to add another owner.  

- **Current site admins:** If the minimum owner or admin count is set to 2 and the site has an existing site admin, they receive an email notification asking them to add another owner.  

- **Managers of previous owners or admins:** If an owner or admin of a site leaves the organization, their managers are informed that the site needs an owner for effective management. If managers are members of a site, they can accept ownership. If they're visitors or don't have access to the site, they can coordinate with SharePoint admins to find the next best owner.  

  - As a user's details are deleted from the system 30 days after leaving the organization, managers might get only one notification about the site.

  - If the policy runs after 30 days of a user's leaving the organization, manager information won't be available, and notifications can't be sent.
  - For a Teams site, the "manager of the previous site owner" notification works only for users added directly to the SharePoint site owner. If the user was added from the M365 Group, the notification won't be sent. This is a system limitation due to how user information is retained after an account is deleted. Therefore, to improve the chances of successfully sending notifications, we recommend selecting at least three options.

- **Active site members:** Based on policy configuration, emails are sent to the most recent active members of a site to accept ownership. 

  - To ensure relevance and recency, read or write activity performed by a site member on a site in the last 180 days is considered as an activity. 
  
  - Any user with last activity beyond 180 days is not considered for these notifications.
  
  - External and guest users will NOT be considered for these notifications to accept ownership.
  
    > [!NOTE]
    > If a site has no one to be notified as per the email recipients provided during policy configuration, the count is provided in the summary. You can triage the sites and determine the next course of action. 
  
### Sites managed by multiple site lifecycle management policies

For each type of site lifecycle management policy—[site ownership policy](/sharepoint/create-sharepoint-site-ownership-policy), [inactive site policy](/sharepoint/site-lifecycle-management), and [site attestation policy](/sharepoint/request-site-attestations)—if multiple policies are created under the same type, notification emails aren't repeated. If a notification was sent within the last 30 days from any policy of that type, and the site remains uncertified, no further notifications are sent. The policy execution report shows the site's status as "Notified by another policy."

For example, if a site is covered by two different site ownership policies and receives a notification email from the first policy, no additional notifications will be sent from the second policy within the next 30 days if the site remains uncertified.

It's recommended to ensure that policies of the same type do not have overlapping scopes. If sites fall under the scope of multiple policies of the same type, the notification schedule and enforcement actions on the site could become unpredictable.  

## Enforcement actions

The following table summarizes how the inactive site policy behaves based on the selected enforcement action:

|Enforcement action|Policy behavior|
|---|---|
|**Do nothing**|The specified recipients receive monthly notifications for three months. After this period, no notifications are sent for the next three months. If the site remains ownerless after six months, monthly notifications resume. The policy execution report lists ownerless sites as unactioned. You can download this report and filter out sites marked as unactioned.|
|**Read-only access**|The specified recipients receive monthly notifications for three months. If the notification recipients don't mark the site as certified during this period, the site goes into read-only mode.|
|**Archive sites after mandatory read-only period**|The specified recipients receive monthly notifications for three months. If the notification recipients don't mark the site as certified during this period, then the site goes into a read-only mode for the configured number of months. After the configured number of months, the site gets archived through [Microsoft 365 Archive](/microsoft-365/archive/archive-setup). Archival is subject to the tenant enabling Microsoft 365 Archive on the Microsoft Admin center.|

If a site is identified as not meeting the ownership criteria for three consecutive months, one of the following actions is taken depending on what is configured:

**Do nothing**: There's no change to access, but subsequent notifications are paused and will resume after three months.

**Set access to read-only**: Site members and visitors can view content but no longer make edits. No further notifications are sent.

- If option is chosen and no one can be notified during the three months, the site continues to have its access set to read-only.


## Read-only mode

A site ownership policy configured with the read-only enforcement action sends additional notifications to inform the specified recipients when there's no response.

[!INCLUDE[Read-only and archived sites](includes/site-lifecycle-management/read-only-archived-sites.md)]

## Reporting

After each run of the configured policy, you can view a report about the sites it identifies.  

In the **Site ownership policies** page, select the desired policy from the list.

The report outlines the number of sites identified as not meeting the ownership criteria, along with the number of sites that didn't have anyone to notify.

:::image type="content" source="media/site-ownership-policy/6-create-site-ownership-policy-reporting.png" alt-text="Screenshot of ownership policy report." lightbox="media/site-ownership-policy/6-create-site-ownership-policy-reporting.png":::

Select **Download report** to download the detailed report in a .csv format. The following table describes the information included in the policy execution report:


| **Column**                              | Definition                                                                                                                      |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| **Site name**                            | Name of the site                                                                                                                 |
| **URL**                                  | URL of the site                                                                                                                  |
| **Template**                             | Template of the site                                                                                                             |
| **Sensitivity label**                    | Sensitivity label of the site                                                                                                    |
| **Retention policy**                     | Is any retention policy applied to the site or not                                                                               |
| **Site lock state**                      | State of site access **before** the policy is run (Unlock/Read-Only/No access)                                                       |
| **Minimum owners or admins configured**  | Minimum owner or admin count configured by you while creating the policy                                                         |
| **Number of site owners**                | Total count of site owners for the site                                                                                          |
| **Email address of site owners**         | Email addresses of all site owners                                                                                               |
| **Number of site admins**                | Total count of site admins for the site                                                                                          |
| **Email address of site admins**         | Email addresses of all site admins                                                                                               |
| **Managers of previous owners or admins**| Email addresses of the managers of previous owners or admins (if this option was configured during policy set-up)                |
| **Active members**                       | Email addresses of the active site members (if this option was configured during policy set-up)                                  |
| **Total notifications count**            | Total notifications sent so far by any policy under the same policy template                                                     |
| **Action status**                        | Status of the site [First/second/third notification sent, Site in read-only mode, Site archived, Action taken by another policy] |
| **Action taken on (UTC)**                | Date on which the enforcement action was taken (date when site was archived or put in read-only mode)                            |
| **Last activity date (UTC)**             | Date of last activity detected across SharePoint site and connected workloads                                                    |
| **Site creation date (UTC)**             | Date when the site was created                                                                                                   |
| **Storage used (GB)**                    | Storage consumed by the site                                                                                                     |
| **Duration in read-only (days)**         | Number of days the site is in the enforced read-only state                                                                       |

