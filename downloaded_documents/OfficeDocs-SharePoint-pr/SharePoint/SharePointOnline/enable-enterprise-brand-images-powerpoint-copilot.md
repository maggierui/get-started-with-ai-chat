---
# Required metadata
# For more information, see https://learn.microsoft.com/en-us/help/platform/learn-editor-add-metadata
# For valid values of ms.service, ms.prod, and ms.topic, see https://learn.microsoft.com/en-us/help/platform/metadata-taxonomies

title: How to Enable Enterprise Brand Images with PowerPoint Copilot
description: Self-Serve Setup Guide for Enterprise Customers to enable Brand Images with PowerPoint Copilot
author:      EH560 # GitHub alias
ms.author:   eleanl # Microsoft alias
manager: yvhsieh
ms.service: powerpoint
ms.topic: how-to
ms.date:     09/03/2025
---
# How to Enable Enterprise Brand Images with PowerPoint Copilot

Copilot in PowerPoint can now create on-brand presentations using your company-approved images stored in OAL or Templafy. Here’s how you can set up Copilot in PowerPoint to use your brand images.

### Option 1: SharePoint Organizational Asset Library (OAL)

Copilot can generate on-brand presentations using images from your OAL.

__Steps to Enable:__

1.     Ensure your Image OAL contains at least 1,000 images

2.     [Run the setup script](/sharepoint/connect-organizational-asset-libraries-to-copilot) to allow Copilot access to folders

3.     Add robust [image metadata (tags)](/copilot/microsoft-365/microsoft-365-copilot-search-image-tagging-integration) for better results

4.     A user in your organization can then include branded images from OAL when creating presentations with Copilot

### Option 2: Templafy Image Library

Copilot can generate on-brand presentations using images from your Templafy library.

__Steps to Enable:__

1.     Ensure your Templafy library has at least 1,000 images

2.     Confirm image metadata is in place

3.     Your administrator should [enable the Microsoft Graph Connector for Templafy](https://support.templafy.com/hc/en-us/articles/24656260075549-How-to-enable-Microsoft-Graph-Connector-for-Templafy-Image-Library)

4.     A user in your organization can then [include branded images from Templafy when creating presentations with Copilot](https://support.templafy.com/hc/en-us/articles/29041436032413-How-to-include-branded-images-from-Templafy-when-creating-presentations-with-Copilot)    

### Tips for Success

- Use Copilot’s ‘Create a presentation’ feature to generate presentations with your brand images. Use the [image source toggle](https://support.microsoft.com/en-us/topic/keep-your-presentation-on-brand-with-copilot-046c23d5-012e-49e0-8579-fe49302959fc) to control where Copilot pulls the presentation’s images from. You can verify the image source in the Notes pane of a slide.

- Ensure your OAL or Templafy library contains at least 1,000 brand-approved images with robust metadata (name, descriptions, tags for both Templafy and OAL, plus [folder structure for Templafy](https://support.templafy.com/hc/en-us/articles/24656260075549-How-to-enable-Microsoft-Graph-Connector-for-Templafy-Image-Library#h_01JJSG6CYF63YGME313C4VSKTP)) to improve Copilot’s ability to retrieve relevant visuals.

- To further enhance image relevancy, consider expanding the quantity of images provided to Copilot and refining your image tags to optimize search results.

### Related Articles 

- [Keep your presentation on-brand with Copilot - Microsoft Support](https://support.microsoft.com/en-gb/topic/keep-your-presentation-on-brand-with-copilot-046c23d5-012e-49e0-8579-fe49302959fc)

#### OAL Connector

- [Create an organization assets library - SharePoint in Microsoft 365 | Microsoft Learn](/sharepoint/organization-assets-library)

- [Connect organizational asset libraries to Copilot for an on-brand experience - SharePoint in Microsoft 365 | Microsoft Learn](/SharePoint/connect-organizational-asset-libraries-to-copilot)

- [Find and manage images using enhanced image tagging | Microsoft Learn](/microsoft-365/documentprocessing/image-tagging)

- [Overview of image tagging with Syntex | Microsoft Learn](/microsoft-365/documentprocessing/image-tagging-overview)

#### Templafy Connector

- [About the Templafy connector](/connectors/templafy/)

- [How to Enable Microsoft Graph connector for Templafy Image Library](https://support.templafy.com/hc/en-us/articles/24656260075549-How-to-enable-Microsoft-Graph-Connector-for-Templafy-Image-Library) for administrators

- [How to include branded images from Templafy when creating presentations with Copilot](https://support.templafy.com/hc/en-us/articles/29041436032413-How-to-include-branded-images-from-Templafy-when-creating-presentations-with-Copilot) for users in your organization

