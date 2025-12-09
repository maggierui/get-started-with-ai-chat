---
ms.date: 7/14/2025
ms.update-cycle: 180-days
title: Microsoft 365 Copilot - best practices with SharePoint
ms.reviewer: 
ms.author: ruihu
author: maggierui
manager: dansimp
recommendations: true
audience: Admin
ROBOTS: NOINDEX, NOFOLLOW
f1.keywords:
- NOCSH
ms.topic: best-practice
ms.service: sharepoint-online
ms.collection: 
- M365-collaboration
- m365copilot
- magic-ai-copilot
- Tier2
- trust-pod
ms.localizationpriority: medium
search.appverid:
- MET150
description: "Learn about the best practices with SharePoint for content sharing when enabling Microsoft 365 Copilot."
---
# Microsoft 365 Copilot with SharePoint

## Copilot and SharePoint

Your organization is preparing to enable Microsoft 365 Copilot, an AI-driven productivity tool that enhances creativity, productivity, and skills in real-time.  As the SharePoint admin, it’s crucial to govern your organization's SharePoint data properly to ensure Copilot's results are appropriate, accurate, and compliant. Understanding the significance of content governance in SharePoint for Copilot begins with knowing [how Copilot works through three components](/copilot/microsoft-365/microsoft-365-copilot-overview#copilot-integration-with-graph-and-microsoft-365-apps):

- Large language models (LLMs)
- The Microsoft 365 productivity apps that you use every day, such as Word, Excel, PowerPoint, Outlook, Teams, and others.
- Content in Microsoft Graphs

Content in Microsoft Graph includes emails, files, meetings, chats, calendars, and contacts. A significant portion of them is stored as SharePoint files. When you share documents with others, these documents become data stored on SharePoint sites, document libraries and OneDrive. These documents can be: Word document shared by your colleagues, a presentation that you're working with your team, meeting recordings, project notes you created in Loop and OneNote, and more. When a user makes a request to Copilot, it processes the request using large language models (LLMs). It then generates a response with LLMs by leveraging content from Microsoft Graph and web content (optional).

Microsoft 365 Copilot only surfaces organizational data to which individual users have *at least view permissions*. It's important to use the permission models in SharePoint to ensure the right users or groups have the right access to the right content within your organization. To get ready for your organization's Microsoft 365 Copilot adoption, there are a few [highly recommended steps](/sharepoint/get-ready-copilot-sharepoint-advanced-management) you can take with SharePoint and OneDrive using [SharePoint advanced management](/sharepoint/advanced-management). In addition, as a SharePoint administrator, here are some steps you can take using regular SharePoint settings to prepare your organization for Microsoft 365 Copilot:

## Step 1 - Optimize search in SharePoint

✅ **Optimize your SharePoint content for search**

As mentioned before, when a user makes a request to Copilot, it processes the request and then generates a response with LLMs. Copilot leverages content from Microsoft Graph and web content (optional). 
So how does Copilot get content from SharePoint? It is the same way when a user searches for content via [SharePoint Search](/sharepoint/overview-of-search).

To get the most out of Copilot and get the best results, optimize your SharePoint content for search:

- [Make sure the content can be found](/sharepoint/make-sure-content-can-be-found)
- [Make sure the search results look great](/sharepoint/make-search-results-look-great)
- [Plan your content](/microsoftsearch/plan-your-content)

## Step 2 - Prevent oversharing and control access with SharePoint and OneDrive

To prevent oversharing and control access with SharePoint and OneDrive, there are a few [highly recommended steps you can take with SharePoint and OneDrive](/sharepoint/get-ready-copilot-sharepoint-advanced-management). In addition, you can use some SharePoint built-in features to reduce oversharing and check permissions and site access in the SharePoint admin center. 

To start, you can:

✅ **Reduce accidental oversharing with SharePoint sharing settings**

To minimize accidental content oversharing with Copilot results, implement sharing settings at the organization and site levels:

1. At the organization level:

    - Update [sharing settings for SharePoint and OneDrive](/sharepoint/turn-external-sharing-on-or-off) for your tenant from organization-wide sharing to specific people links.
    - Consider hiding broad-scope permissions from your end users. For example, use the SharePoint `Set-SPOTenant` PowerShell cmdlet to [hide "Everyone Except External Users" in the People Picker control](/powershell/module/microsoft.online.sharepoint.powershell/set-spotenant) so end users can't use it.
    - Use [Restricted SharePoint Search (RSS)](/sharepoint/restricted-sharepoint-search) to temporarily restrict Copilot results up to 100 selected SharePoint sites. Child sites of Hub sites aren't counted toward the 100 limit.

      RSS gives you time to review & audit site permissions. It should be used only as a temporary solution to give your organization time to adopt Copilot.

2. At the site level:

    - Educate site admins on the site-level controls they can use to [restrict members from sharing](/sharepoint/change-external-sharing-site).
    - Make sure that [Site Owners receive a request to access the site](https://support.microsoft.com/office/set-up-and-manage-access-requests-94b26e0b-2822-49d4-929a-8455698654b3).
    - [Change the external sharing setting for a user's OneDrive](/sharepoint/user-external-sharing-settings). When a user saves a file to OneDrive, it's in the end user's personal storage. The user has full control over the file and can share it with others. To ensure data security, review OneDrive sharing features.

✅ **Check permissions and site access in SharePoint admin center**

To ensure data is secure, review SharePoint site access and permissions. Prioritize sites that contain sensitive information.

1. In the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219), see **Active Sites** > select a site > **Edit** > **Settings**.

    **Private** means that only users in your organization with access to the site can find it. **Public** (default) means anyone in your organization can find the site and access its content.

    :::image type="content" source="media/sharepoint-active-sites-setting.png" alt-text="Screenshot showing the SharePoint admin center active sites panel." lightbox="media/sharepoint-active-sites-setting.png":::

1. In the **Membership** tab, review access to site owners, members, and visitors. Ensure that only the necessary users have access to the site.

> [!IMPORTANT]
> This article mainly introduces using SharePoint built-in settings to reduce oversharing and check permissions and site access. To further enhance your organization's data governance with efficiency and at scale, consider using [SharePoint advanced management](/sharepoint/advanced-management) to monitor and manage your organization's SharePoint data.
