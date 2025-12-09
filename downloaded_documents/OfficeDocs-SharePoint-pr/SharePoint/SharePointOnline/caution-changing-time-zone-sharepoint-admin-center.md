---
title: Best practices for changing site creation time zone display in SharePoint admin center
description: "Learn the best practices for changing the displayed creation time zone of the Active sites page in the SharePoint admin center."
author: maggierui
manager: dansimp
ms.author: ruihu
ms.service: sharepoint-online
ms.topic: best-practice #Don't change
ms.date: 10/22/2025
audience: Admin
customer intent: As a SharePoint admin, I want to change the displayed creation time zone of the Active sites page in the SharePoint admin center so that it reflects the correct time zone for my organization.
f1.keywords: NOCSH
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- Highpri
- Tier2
- M365-sam
- M365-collaboration
search.appverid:
---

# Best practices for changing site creation time zone display in SharePoint admin center

As a SharePoint admin, sometimes you may have the need to change the displayed creation time zone of the **Active sites** page in the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219). Instead of changing the time zone setting of the SharePoint admin center itself, we recommend using [user-level settings](https://support.microsoft.com/office/change-your-personal-language-and-region-settings-caa1fccc-bcdb-42f3-9e5b-45957647ffd7) for time zone and locale change.

[![Screenshot showing creation dates in SharePoint admin center.](media/spac/creation-dates-sharepoint-admin-center.png "Creation dates displayed in SharePoint admin center")](media/spac/creation-dates-sharepoint-admin-center.png#lightbox)

## What can happen when you change the time zone in SharePoint admin center

You can change the time zone for the SharePoint admin center by adding `"_layouts/15/regionalsetting.aspx"` to the end of your admin center URL. For example: `https://contoso-admin.sharepoint.com/_layouts/15/regionalsetting.aspx`.

By default, the SharePoint admin center uses Pacific Time (PST). When you create a new SharePoint site, it inherits the current time zone setting from the admin center. If you change the time zone of the SharePoint admin center after sites have already been created, new sites will use the updated time zone, but existing sites will keep their original time zone for creation dates. This can lead to confusion and reporting issues, as older sites may display creation timestamps based on the previous time zone, while newer sites reflect the new setting.

## What we recommend: use user-level settings for Time Zone and Locale

To avoid time stamp misalignments on the **Active sites** page in SharePoint admin center, we recommend using [user-level settings](https://support.microsoft.com/office/change-your-personal-language-and-region-settings-caa1fccc-bcdb-42f3-9e5b-45957647ffd7) for time zone and locale instead of directly changing the SharePoint admin center's time zone settings. User-level time zone and locale settings affect how times are displayed in Outlook, SharePoint, and other Microsoft 365 services. 
> [!NOTE]
> If your organization enforces tenant-level time zone settings, personal changes may be overridden. Changes may take a few minutes to propagate across services.

## Related content

- [Change your personal language and region settings](https://support.microsoft.com/office/change-your-personal-language-and-region-settings-caa1fccc-bcdb-42f3-9e5b-45957647ffd7)
- [Change regional settings for a SharePoint site](https://support.microsoft.com/office/change-regional-settings-for-a-site-e9e189c7-16e3-45d3-a090-770be6e83c1a)
