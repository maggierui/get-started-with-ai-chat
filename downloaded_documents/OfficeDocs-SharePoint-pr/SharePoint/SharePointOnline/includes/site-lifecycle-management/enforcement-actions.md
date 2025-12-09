---
author: maggierui
manager: dansimp
ms.author: ruihu
ms.service: sharepoint-online
ms.topic: include
ms.date: 11/11/2025
---
For sites that aren't certified or attested after 3 monthly notifications for any of the site lifecycle management policies, you can take one of the following enforcement actions. 

|Enforcement action|Policy behavior|
|---|---|
|**Do nothing**|Site owners or site admins receive monthly notifications for three months. After this period, no notifications are sent for the next three months. If the site remains unattested after six months, monthly notifications resume. The policy execution report lists unattested sites as unactioned by the site owner. You can download this report and filter out sites marked as unactioned.|
|**Read-only access**|Site owners or site admins receive monthly notifications for three months. If the notification recipients don't mark the site as attested during this period, the site goes into read-only mode.|
|**Archive sites after mandatory read-only period**|Site owners or site admins receive monthly notifications for three months. If the notification recipients don't mark the site as attested during this period, then the site goes into a read-only mode for a configurable duration (3, 6, 9, or 12 months). After the configured number of months, the site gets archived through [Microsoft 365 Archive](/microsoft-365/archive/archive-setup). Archival is subject to the tenant enabling Microsoft 365 Archive on the Microsoft Admin center.|

The following screenshot shows an example of configuring enforcement actions for a site attestation policy:
:::image type="content" source="../../media/site-lifecycle-management/enforcement-actions.png" alt-text="Screenshot of enforcement actions configuration for site lifecycle management policies." :::

> [!NOTE]
> If you configure the policy to take an enforcement action:
>  - The notifications won’t be sent after policy action is successful.
>  - The site and it’s status are included in the monthly report.
