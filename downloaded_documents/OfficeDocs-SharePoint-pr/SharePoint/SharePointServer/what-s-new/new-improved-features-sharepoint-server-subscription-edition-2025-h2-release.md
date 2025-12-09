---
ms.date: 01/08/2025
title: "New and improved features in SharePoint Server Subscription Edition Version 25H2"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: overview
ms.service: sharepoint-server-itpro
ms.localizationpriority: high
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition Version 25H2."
---

# New and improved features in SharePoint Server Subscription Edition Version 25H2

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn about the new features and updates introduced in the SharePoint Server Subscription Edition Version 25H2 feature update.

## Summary of the features

The following table provides a summary of the new features introduced in the SharePoint Server Subscription Edition Version 25H2 feature update.

|**Feature**|**Release ring**|**More information**|
|:-----|:-----|:-----|
| **Support for automatic machine key rotation**  |  Standard release   | For more information, see [Support for automatic machine key rotation](new-and-improved-features-in-sharepoint-server-subscription-edition-25h1-release.md#support-for-automatic-machine-key-rotation).<p> This was part of Early release in the Version 25H1 feature update.<p>|
| **Dynamic customer survey by One Customer Voice**  | Standard release  | For more information, see [Dynamic customer survey by One Customer Voice](new-and-improved-features-in-sharepoint-server-subscription-edition-25h1-release.md#dynamic-customer-survey-by-one-customer-voice).<p> This was part of Early release in the Version 25H1 feature update.<p>|
| **Create new Office files in client apps**   |Standard release   |For more information, see [Create new Office files in client apps](new-and-improved-features-in-sharepoint-server-subscription-edition-25h1-release.md#create-new-office-files-in-client-apps).<p> This was part of Early release in the Version 25H1 feature update.<p>|
| **Support for request body scan in AMSI**   |Standard release   |For more information, see [Support for request body scan in AMSI](new-and-improved-features-in-sharepoint-server-subscription-edition-25h1-release.md#support-for-request-body-scan-in-amsi).<p> This was part of Early release in the Version 25H1 feature update.<p>|
| **Cloud Hybrid Search upgrade**   |Standard release   |For more information, see [Cloud Hybrid Search upgrade](new-and-improved-features-in-sharepoint-server-subscription-edition-25h1-release.md#cloud-hybrid-search-upgrade).<p> This was part of Early release in the Version 25H1 feature update.<p>|
| **Support JWE encrypted tokens from Entra ID**   |Early release   |For more information, see [Support JWE encrypted tokens from Entra ID](#support-jwe-encrypted-tokens-from-entra-id).|
| **Drag and drop functionality for web parts in publishing sites**   |Early release   |For more information, see [Drag and drop functionality for web parts in publishing sites](#drag-and-drop-functionality-for-web-parts-in-publishing-sites).|
| **Modern People Card**   |Early release   |For more information, see [Modern People Card](#modern-people-card).|
| **Per-Database Connection Encryption Settings**   |Standard release   |For more information, see [Per-Database Connection Encryption Settings](#per-database-connection-encryption-settings).|
| **Document Intelligence**   |Early release   |For more information, see [Document Intelligence](#document-intelligence).|
| **AMSI Body Scan Defaults to “Full Mode”**   |Early release   |For more information, see [AMSI Body Scan Defaults to “Full Mode”](#amsi-body-scan-defaults-to-full-mode).|
| **Enhance Document Virus Check with AMSI Option**   |Early release   |For more information, see [Enhance Document Virus Check with AMSI Option](#enhance-document-virus-check-with-amsi-option).|
| **New web part editing experience powered by CKEditor lib v5**   |Standard release   |For more information, see [New web part editing experience powered by CKEditor lib v5](#new-web-part-editing-experience-powered-by-ckeditor-lib-v5).|
| **New enhancements for the Text web part**   |Early release   |For more information, see [New enhancements for the Text web part](#new-enhancements-for-the-text-web-part).|
| **New PowerShell Cmdlet to Validate Defender and AMSI Integration**   |Standard release   |For more information, see [New PowerShell Cmdlet to Validate Defender and AMSI Integration](#new-powershell-cmdlet-to-validate-defender-and-amsi-integration). <br>**Note:** This feature is included in the September 2025 Public Update (PU) for SharePoint Server Subscription Edition (SPSE), SharePoint Server 2019 (SP2019), and SharePoint Server 2016 (SP2016).|

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition Version 25H2.

> [!NOTE]
> Features previously introduced in the Version 25H1 feature update won't be described here. For more information on Version 25H1, see [New and improved features in SharePoint Server Subscription Edition Version 25H1](new-and-improved-features-in-sharepoint-server-subscription-edition-25h1-release.md).

### Support JWE encrypted tokens from Entra ID  

JSON Web Tokens (JWT) are widely used for authentication. While JWTs are typically signed (JWS), JSON Web Encryption (JWE) tokens provide encryption for sensitive claim information. As Entra ID adopts JWE, SharePoint Server must support it to maintain compatibility. JSON Web Encryption (JWE) is a standard that enables the encryption of JSON data structures (known as claims) to produce a compact, URL-safe token.
This feature will enable SharePoint Server Subscription Edition (SPSE) to consume and process encrypted tokens issued by Entra ID, ensuring compatibility with modern authentication standards and enhancing security.  JWE offers the following benefits:

- **Enhanced Security**

  JWE tokens provide an additional layer of security by encrypting sensitive information. This ensures that the data within the token is protected from unauthorized access and tampering.

- **Compliance with Standards**

  Using JWE tokens aligns with industry standards for secure data transmission. This can help organizations comply with regulatory requirements and best practices for data protection.

- **Improved Privacy**

  By encrypting the token payload, JWE helps protect user privacy. Sensitive claims are not exposed to intermediaries during transmission, reducing the risk of data leakage.

### Drag and drop functionality for web parts in publishing sites

Users can now move web parts between page sections or change web part order within page sections when editing pages in SharePoint Server publishing sites using modern browsers. This drag and drop functionality enhances the page editing experience by allowing intuitive repositioning of web parts through a simple hover, click, and drag operation.

The feature works by hovering over the header/title bar of any web part, where the mouse cursor changes to a 4-way arrow, then clicking and holding to drag the web part to any other section on the page. This same functionality can be used to reorder web parts within a page section.

For more information, see [Use Drag and Drop to move web parts in publishing sites](../sites/use-drag-and-drop-to-move-web-parts-publishing-sites.md).

### Modern People Card

Modern People card enhances the user experience in Lists and Document Libraries by displaying essential user information directly within the interface.

For more information, see [Modern People Card](../sites/modern-people-card.md).

### Per-Database Connection Encryption Settings

Previously, the encryption settings of the database connection were configured at the farm level, meaning every database in the farm shared the same encryption settings as the configuration database. With this new feature, users can now select different connection encryption settings per database, which can be particularly useful when databases are stored on different SQL servers or serve different purposes. This feature is applicable to both content databases and service application databases.

For more information, see [Transport Layer Security (TLS) 1.3 Support](../security-for-sharepoint-server/tls-support-1.3.md).

### Document Intelligence

Document Intelligence represents a significant advancement in SharePoint Server's document management capabilities, combining AI with traditional document handling to provide intelligent insights and automation. This feature transforms how organizations interact with their document libraries by using AI to enable smarter, more efficient content engagement.

For more information, see [Document Intelligence](../sites/document-intelligence.md).

### AMSI Body Scan Defaults to “Full Mode”

This enhances security by making Full Mode body scanning the default behavior in the AMSI integration for SharePoint Server. In Full Mode, the entire request body is scanned by AMSI, rather than relying on partial scans. This ensures more comprehensive detection of malicious payloads, including zero-day threats that may be embedded deeper in the request stream.

For more information, see [AMSI Body Scan Defaults to “Full Mode”](../security-for-sharepoint-server/configure-amsi-integration.md).

### Enhance Document Virus Check with AMSI Option

The Enhance Document Virus Check with AMSI Option feature enables SharePoint Server to scan documents for malware using the Antimalware Scan Interface (AMSI). This allows SharePoint to leverage Windows Defender or any AMSI-compatible antimalware solution to scan documents uploaded to or downloaded from SharePoint Server.

For more information, see [Enhance Document Virus Check with AMSI Option](../security-for-sharepoint-server/document-virus-check-with-amsi-option.md).

### New web part editing experience powered by CKEditor lib v5

SharePoint Server now uses CKEditor5 (CK5) as the core text editor in both Text web parts and Events web parts, replacing the end-of-life CKEditor4 (CK4). This upgrade provides significant improvements in security, performance, and modern web technology support while maintaining a seamless transition for users with an unchanged functional interface.
 
Key improvements include enhanced format toolbar positioning, improved table functionality with responsive column widths and manual adjustment capabilities, and direct image paste functionality. The upgrade currently applies to newly created web parts, with existing CK4-based web parts to be migrated in future updates.
 
For more information, see [New web part editing experience powered by CKEditor lib v5](../sites/new-text-web-part-editing-experience-powered-by-editor-lib-five.md).

### New enhancements for the Text web part

This feature introduces significant improvements to the Text web part, including enhanced table accessibility features and improved image insertion capabilities. The table accessibility enhancements allow users to mark the first column and first row as headers and set custom alternative text for tables, ensuring that screen readers like Narrator can accurately announce table headers and descriptions for users with visual impairments.
 
The image enhancement feature adds the ability to easily add images to a text web part using either upload or copy and paste functionality. Users can use the "Insert Image" button in the web part editing sidebar to select images from recently used files, site images, upload new images, or add images from links. The feature also supports copy and paste operations (Ctrl+C and Ctrl+V) from the local file system or image editing applications.
 
For more information, see [New enhancements for the Text web part](../sites/new-enhancements-for-the-text-web-part.md).

### New PowerShell Cmdlet to Validate Defender and AMSI Integration

A new PowerShell cmdlet has been introduced to help administrators verify that Windows Defender components and SharePoint AMSI (Antimalware Scan Interface) integration are properly installed and functioning correctly. The `Test-DefenderAndAmsiWorkProperly` cmdlet performs comprehensive checks to ensure that the security infrastructure is operational and can protect SharePoint Server from malicious content.
 
This diagnostic cmdlet validates both the Windows Defender antimalware engine and the AMSI integration that allows SharePoint to scan content for potential threats. It provides detailed information about the current state of security components without making any changes to the system configuration. The cmdlet requires administrator privileges and supports verbose output for detailed diagnostic information.
 
For more information, see [Test-DefenderAndAmsiWorkProperly](/powershell/module/sharepointserver/test-defenderandamsiworkproperly).
