---
ms.date: 12/11/2024
title: Connect organizational asset libraries to PowerPoint for an on-brand experience
ms.reviewer:
ms.author: ruihu
author: maggierui
manager: jtremper
audience: Admin
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: sharepoint
ms.localizationpriority: medium
search.appverid:
- MET150
ms.collection:
- M365-collaboration
ms.custom:
- admindeeplinkSPO
- onedrive-toc
description: "Learn how to enable PowerPoint to provide an on-brand asset experience by specifying organization asset libraries for users to query images, logos, or illustrations directly from chat."
---
# Connect organizational asset libraries to PowerPoint for an on-brand experience

PowerPoint can now search and retrieve enterprise assets directly from your organizational asset libraries (OALs). This new workflow helps organizations democratize access of approved brand assets and simplifies retrieval through “Brand Images” feature. Create on-brand documents with quick access to company stock images, logos, icons, and illustrations.

## How does it work?

- Assigning an organization image library allows PowerPoint to search and download content directly from the library.

- Instantly access your Brand Images right inside PowerPoint by going to __Insert → Pictures → Brand Images__

- Search in Brand Images utilizes image metadata stored within the OAL. Image tags, file name, description, and location are used to help users find the most relevant results. 

![Screenshot 2025-11-17 104723.](media/connect-organizational-asset-libraries-to-copilot/screenshot-2025-11-17-104723.png)

## Use Microsoft PowerShell to specify an organization image document library to be searchable

First, if you haven't, [download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

> [!NOTE]
> If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

Connect to SharePoint as a [SharePoint Administrator or higher](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

Run the following command to designate a document library as an organization image library and enable Brand Images in PowerPoint. 

```PowerShell
Add-SPOOrgAssetsLibrary -LibraryUrl <URL> [-ThumbnailUrl <URL>] [-OrgAssetType ImageDocumentLibrary] [-CdnType <Public or Private>] [-CopilotSearchable <$True or $False>] 
```
- *LibraryURL* is the absolute URL of the library to be designated as a central location for organizational assets. 

- *ThumbnailURL* is the URL for the image file that you want to appear in the card's background in the file picker; this image must be on the same site as the library. The name publicly displayed for the library is the organization's name. 

- *OrgAssetType* must be ImageDocumentLibrary. For now, search functionality only supports ImageDocumentLibrary. 

- _CopilotSearchable_ should be set to True only when you intend to make this organization’s image library available for Copilot features, such as creating presentations with Copilot.

- If you don't specify the *CdnType*, it enables a private CDN by default.

Example:


```PowerShell
Add-SPOOrgAssetsLibrary -LibraryURL https://contoso.sharepoint.com/sites/branding/Assets -ThumbnailURL https://contoso.sharepoint.com/sites/branding/Assets/contosologo.jpg -OrgAssetType ImageDocumentLibrary -CopilotSearchable $True
```

> [!NOTE]
> - You can only use image document libraries.
> - Ensure SharePoint Management Shell version is 16.0.24915.12000 or later.
 >  - Brand Images feature is currently available on PowerPoint on both desktop and web.
 >  - If you don’t already have an organization asset library created, use Microsoft PowerShell to specify an existing library as an organization asset library.
 >  - For a user to see the organization's asset library in PowerPoint for the web, they must have an Office 365 E3 or E5 license.
 >  - Allow up to 24 hours for the organization assets library to appear to a user in the desktop apps.
 >  - Users need at least read permissions on the root site for your organization for the organization assets library to appear in the desktop apps.

## Best Practices

Follow these guidelines to improve the organization asset library image search experience:
- Avoid Multiple formats and resolutions of the same image. Search may return multiple versions of the same image reducing the breadth of search results. 
- Avoid exceptionally large images. Images over 10 MB result in search latency and slow downloads, host application limits may also apply.
- Remove any files that aren’t image based. Non-image files may be included in search results but fail on insertion.
- Insufficient tagging and descriptions. Successful search results require meaningful file names, image tags, location, and descriptions to be included with the content in the organization image asset library. Insufficient metadata reduces search hit rates and lower result relevancy.
- The following image formats are supported: JPEG, PNG, SVG, BMP, GIF, TIFF, WEB P, HEIF, ICO.

## Reference

- [Create an organization assets library](/sharepoint/organization-assets-library) 
- [Add-SPOOrgAssetsLibrary](/powershell/module/sharepoint-online/add-spoorgassetslibrary)

- [Set-SPOOrgAssetsLibrary](/powershell/module/sharepoint-online/set-spoorgassetslibrary)
