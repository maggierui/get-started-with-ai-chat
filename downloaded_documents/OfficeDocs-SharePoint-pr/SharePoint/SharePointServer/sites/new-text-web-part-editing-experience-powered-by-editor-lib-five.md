---
title: "New web part editing experience powered by CKEditor lib v5"
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
description: "Learn about the new web part editing experience powered by CKEditor v5, which replaces the end-of-life CKEditor4 in SharePoint Server Text and Events web parts."
---

# New web part editing experience powered by CKEditor lib v5

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

The CKEditor4 (CK4), which was the core text editor in SharePoint Server, reached its end-of-life as of 2023. This means that it no longer receives updates, security patches, or technical support. Given the increasing reliance on modern web technologies and the need for enhanced security, performance, it is important to migrate to a newer, supported version of the text editor. CKEditor5 (CK5) is the natural successor, offering significant improvements over its predecessor.

In this upgrade, we replaced CK4 with CK5 as the core text editor in both the Text Web Parts and the Events Web Parts. The functional interface remains unchanged, ensuring a seamless transition for users.

> [!NOTE]
> Currently, we only replace the text editor to CK5 in new-create web parts, and stay using CK4 in the old web parts. In the future, we will replace all the web parts based on CK4 to CK5.

## How to Use

### Text web part

1. Create a modern site page.

2. Click "+" to add new web part, choose Text.

3. Verify that this web part is based on CK5.

![Text web part interface showing the CKEditor 5 text editor](../media/text-webpart-with-editor-core.png)

### Events web part

1. Create a modern site page.

2. Click "+" to add new web part, choose Events.

3. Fill the title in this web part, then publish this page.

4. Click "Add event".

5. Verify that in the "About this event" area, the Text Editor is based on CK5.

![Event description form showing the CKEditor 5 text editor in the About this event section](../media/event-description-with-editor-core.png)

## The Impact on User Interface/Interaction

The upgrade to CK5 introduces the following changes:

### Format toolbar position

In text web part based on CK4, the position of the toolbar changes with the text you select.
![CKEditor 4 toolbar appearing near selected text](../media/toolbar-display-in-old-editor.png)

If you select text in the text web part based on CK5, the toolbar appears in the upper left corner of the editor's viewable area.
![CKEditor 5 toolbar positioned in the upper left corner of the editor](../media/toolbar-display-in-new-editor.png)

### Table

When you create table in CK4 web part, the width of this table column is fixed and does not change as the width of the editor changes.
![Table in CKEditor 4 with fixed column widths](../media/table-display-in-old-editor.png)

When you create a table in CK5 web part, the width of the table column varies proportionally with the width of the editor. And you can manually adjust the width of the table column.
![Table in CKEditor 5 with responsive column widths and manual adjustment capabilities](../media/table-display-in-new-editor.png)

### Image paste

When you paste an image in CK4 web part, it splits this web part to three web parts: text web part 1 with the content before the position you paste, image web part with the image you paste, text web part 2 with the content after the position you paste.

When you paste an image in CK5 web part, it pastes into the editor directly. See [New enhancements for the Text web part](../sites/new-enhancements-for-the-text-web-part.md).
