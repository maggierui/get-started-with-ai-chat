---
title: "Enhance Document Antivirus with AMSI Option"
ms.reviewer: 
ms.author: xiaolongchen
author: xiaolongchen
manager: guoqingli
ms.date: 08/16/2025
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: [GENERATE-NEW-GUID]
description: "Learn how to configure the Document Antivirus feature with AMSI option in SharePoint Server."
---


# Enhance Document Antivirus with AMSI Option in SharePoint Server

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn how to configure and manage the Document Antivirus feature with AMSI option in SharePoint Server. This article describes the feature, prerequisites, configuration steps, and troubleshooting guidance.

## Overview

The **Enhance Document Antivirus with AMSI Option** feature enables SharePoint Server to scan documents for malware using the Antimalware Scan Interface (AMSI). This allows SharePoint to leverage Windows Defender or any AMSI-compatible antimalware solution to scan documents uploaded to or downloaded from SharePoint Server.

This feature enhances the legacy document virus scanning capability by providing an AMSI-based option that integrates with modern Windows security.

> [!TIP]
> This feature is distinct from the AMSI Filter feature. AMSI Filter scans incoming HTTP requests for SharePoint Server, while Document Antivirus with AMSI scans documents during upload, download, or online editing.

## Prerequisites

Before you configure this feature, ensure the following:

- You are running SharePoint Server Subscription Edition with the latest updates.
- Windows Server 2016 or later is installed.
- An AMSI-compatible antimalware solution (such as Microsoft Defender Antivirus) is installed and enabled on all SharePoint servers.
- You must be a member of the **Farm Administrators** group.

## Available Document Malware Scanning Options

You can configure SharePoint Server to use one of the following document scanning options:

- **Automatic (default):** Attempts to use the legacy VSAPI (Virus Scanning API) first. If VSAPI is unavailable, AMSI is used.
- **AMSI:** Forces SharePoint to use AMSI for document scanning, even if VSAPI-compatible software is present.
- **VSAPI:** Forces SharePoint to use VSAPI for document scanning, even if AMSI-compatible software is present.

## Configure Document Antivirus with AMSI

To configure the document antivirus scanning:

1. Open **SharePoint Central Administration**.
2. Select **Security** in the left navigation.
3. Click **Manage antivirus settings**.
4. Under **Antivirus Settings**, select the document antivirus option you need:
	- Select **Scan documents on upload** to scan files as users upload them to libraries.  
	- Select **Scan documents on download** to scan files before users download them.  
5. Under **Scan Interface Type**, select one of the following:
	- **Automatically choose the available scan interface** – This is recommended option. SharePoint will attempt to use the legacy VSAPI (Virus Scanning API) first. If VSAPI is unavailable, AMSI is used.
	- **Use the Antimalware Scan Interface (AMSI) API for scanning** – Only use the newer Antimalware Scan Interface, even if VSAPI-compatible software is present. If you have both VSAPI and AMSI compatible software, then you may want to select this to ensure the document antiviurs feature uses AMSI.
	- **Use the legacy Microsoft Office SharePoint Virus Scan Engine (VSE) API for scanning.** – Only use the legacy VSAPI integration, even if AMSI-compatible software is present.

6. Click **OK** to save your changes.

## How It Works

When a user uploads, downloads, or edits a document in SharePoint, the selected scanning engine (AMSI or VSAPI) is invoked to check the file for malware. If malware is detected, the action is blocked and an error is logged.
