---
title: "New enhancements for the Text web part"
ms.reviewer: 
ms.author: yanyanmu
author: yanyanmu
manager: kaibchen
ms.date: 8/11/2025
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
description: "Learn about new enhancements for the Text web part including improved table accessibility features and enhanced image insertion capabilities."
---

# New enhancements for the Text web part

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

## New table features for the Text web part

This feature improves table accessibility in the Text web part by allowing users to mark the first column and first row as headers, and to set custom alternative text for tables. These enhancements ensure that screen readers like Narrator can accurately announce table headers and descriptions, making tabular data easier to navigate and understand for users with visual impairments.

### Usage

1. Create a page in SharePoint site, then text web part, then add table in the property pane. In the property pane, it displays the "Table accessibility" section.
![Table accessibility section in the property pane showing options for first row header, first column header, and alternative text.](../media/table-accessibility-section.png)

2. Click the first row header, the first row of this table becomes bold.
![Table with the first row formatted as bold headers.](../media/first-row-header.png)

3. Click the first column header, the first column of this table becomes bold.
![Table with the first column formatted as bold headers.](../media/first-column-header.png)

4. Click the Alternative text, change the alternative text of this table.
![Dialog box for entering alternative text for the table.](../media/table-alternative-text.png)

5. Using screen readers like Narrator, it can accurately announce table headers and alternative text.

## Image enhancements for the Text web part

The ability to easily add images to a text web part using either upload or copy and paste has been added. Users can use the "Insert Image" button in the web part editing side bar to select an image to add to the web part.

![Text web part property pane showing the Insert Image button.](../media/image-upload-section.png)

From there, users can select a recently-used image, an image already on the site, upload an image, or add an image from a link.

![Image upload dialog showing options for recent images, site images, upload, and link.](../media/image-upload.png)

Users can also use copy and paste, including the ctrl+c and ctrl+v shortcuts to add an image to the text web part. An image file can be copied from the local file system, or from an image display or editing app like MSPaint or the Windows "Photos" app.

Once added to the web part, users can add a caption or alternate text for the image by using those controls.
![Image controls showing caption and alternative text buttons for an inserted image.](../media/image-caption-and-alternative-text-button.png)
