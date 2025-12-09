---
ms.date: 11/21/2025
title: "Restrict OneDrive access by security group"
ms.reviewer: nibandyo
ms.author: ruihu
author: maggierui
manager: dansimp
audience: Admin
customer-intent: As a SharePoint administrator, I want to restrict all OneDrive access to specific security groups.
f1.keywords:
- CSH
ms.topic: how-to
ms.service: onedrive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- Highpri
- Tier2
- M365-sam
- M365-collaboration
- essentials-compliance
- essentials-security
search.appverid:
ms.assetid: 
ms.custom:
- admindeeplinkSPO
- onedrive-toc
description: "Learn how to allow only users in specified security groups to access the OneDrive service."
---

# Restrict OneDrive access by security group

You can restrict access and sharing of OneDrive content to users in specified Microsoft Entra ID security groups. Even if other users outside of these security groups are licensed for OneDrive, they won’t have access to their own OneDrive or any shared OneDrive content when this policy is in effect. OneDrive access restriction at tenant level is applied when a user attempts to open a OneDrive or a file.

You can use this to prevent new users from accessing any OneDrive content. For example, you can restrict OneDrive access and sharing to your new users, guest or frontline users.

Users who aren't members of the specified security group can still see files in organization-wide search and Copilot experiences if they have existing permissions to the file prior to the policy configuration. However they won't be able to open the file or OneDrive if they aren't part of the specified security group.

:::image type="content" source="media/sam-overview/4-restricted-access-control-onedrive.png" alt-text="Screenshot of restricted access control for OneDrive." lightbox="media/sam-overview/4-restricted-access-control-onedrive.png":::

> [!NOTE]
> If you want to prevent oversharing of OneDrive content also for users with existing permissions, we recommend you to enforce OneDrive site access restriction to an individual user's OneDrive. For more information, see [Restrict access to a user's OneDrive content to people in a security group](onedrive-site-access-restriction.md).

## What you need to restrict OneDrive access?

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

## Specify security groups for OneDrive access

To enable this feature:

1. Go to [Access control in the SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185071), and sign in with an account that has [admin permissions](sharepoint-admin-role.md) for your organization.

2. Select **Restrict OneDrive access**.

3. Select **Restrict OneDrive access to only users in specified security groups**.

    :::image type="content" source="media/restrictonedriveaccess.png" lightbox="media/restrictonedriveaccess.png" alt-text="Restrict OneDrive access on the Access control page in the SharePoint admin center":::

4. Add the security groups (maximum of 10) you want to be able to use OneDrive.

5. Select **Save**.

> [!IMPORTANT]
> Users who aren't members of the specified security groups lose access to their own OneDrive and any shared OneDrive content. Sharing of content is allowed only for the specified security group or members of the specified security group.

## Configure learn more link for access denial error page

Configure your learn more link to inform users who were denied access to a OneDrive site due to the OneDrive access restriction policy. With this customizable error link, you can provide more information and guidance to your users.

> [!NOTE]
> The learn more link is a tenant-level setting that applies to all OneDrive sites.

To configure the link, run the following command in SharePoint PowerShell:

```powershell
Set-SPOTenant -RestrictedAccessControlForOneDriveErrorHelpLink "<Learn more URL>"
```

To fetch the value of the link, run the following command:

```powershell
Get-SPOTenant | select RestrictedAccessControlForOneDriveErrorHelpLink 
```

The configured learn more link is launched when the user selects the **Know more about your organization’s policies here** link.

![Screenshot that shows learn more link for restricted access control](media/rac-spac/2-rac-learn-more-link.png)

## Audit events

[Audit events](/microsoft-365/compliance/audit-log-activities) are available in Microsoft Purview portal to help you monitor restricted access control activities. Audit events are logged for the following activities:

- Enabled Restricted OneDrive access and sharing
- Disabled Restricted OneDrive access and sharing

## Related topics

[Restrict access control for SharePoint sites](restricted-access-control.md)

[Data access governance insights for SharePoint sites](data-access-governance-reports.md)
