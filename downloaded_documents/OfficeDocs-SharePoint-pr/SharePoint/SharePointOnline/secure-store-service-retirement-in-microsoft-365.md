---
ms.date: 04/08/2025
title: Secure Store Service (SSS) retirement in Microsoft 365
ms.reviewer: troys
ms.author: ruihu
author: maggierui
manager: jtremper
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.custom: admindeeplinkSPO
ms.collection:
- Tier3
search.appverid:
- SPO160
- MET150
description: Microsoft is announcing its plan to retire Secure Store Service (SSS) in Microsoft 365 and focus on Azure Key Vault as its replacement technology.
---

# Secure Store Service (SSS) retirement in Microsoft 365

SharePoint has a long history of helping users securely work with external data inside the SharePoint user experience, starting with the Business Data Catalog feature in SharePoint Server 2007. SharePoint has been evolving into a cloud-first service and along with it the options for managing credentials and secrets for external data access have also evolved. To simplify these options and provide the best experience for these scenarios going forward, Microsoft is announcing its plan to retire Secure Store Service (SSS) in Microsoft 365 and focus on Azure Key Vault as its replacement technology.

This announcement follows the discontinuation of [Business Connectivity Services](/sharepoint/business-connectivity-services-retirement) (BCS), which was the primary use case for Secure Store Service.

## Impact on SharePoint Server

This announcement has no immediate impact on Secure Store Service in SharePoint Server 2016, 2019, and Subscription Edition.

Until  SharePoint Server 2016 and SharePoint Server 2019 reach their end of support date of July 14, 2026, SSS will be supported. For SharePoint Server Subscription Edition, there are no current and immediate plans to retire SSS. For any deprecation or feature support removal announcements, see [What's deprecated or removed from SharePoint Server Subscription Edition](/sharepoint/what-s-new/what-s-deprecated-or-removed-from-sharepoint-server-subscription-edition)

## Impacted features and scenarios

All Secure Store Service features will be retired in SharePoint in Microsoft 365. This includes features such as:

- Secure Store Target Applications
- Credential storage
- Mapping for external data sources

## Retirement schedule

| Date | Milestone |
|---------|---------|
| **April 10, 2025** | Retirement is announced and transition period begins. |
| **May 31, 2025** | Adding new Target Applications or credentials in Secure Store Service is restricted. |
| **September 30, 2025** | Secure Store Service is fully retired in Microsoft 365. |

## Automatic retirement

Microsoft will manage the retirement process automatically. Administrators don't need to take any manual steps to disable Secure Store Service. Once retired, the service will no longer be available, and any existing configurations will be removed.

## Recommended replacement technology: Azure Key Vault

We encourage you to explore using Azure Key Vault to replace Secure Store Service solutions in SharePoint in Microsoft 365. Although there's no direct migration from Secure Store Service to Azure Key Vault, it supports a modern, cloud-first credential and secret management experience. Azure Key Vault can integrate with various Microsoft 365 services and external data sources through its secure and scalable architecture.

To learn more about Azure Key Vault, see the links in the [More information](#more-information-about-azure-key-vault) section.

## More Information about Azure Key Vault

For more information about Azure Key Vault and its capabilities, see:

- [Azure Key Vault (AKV) Documentation](/azure/key-vault/keys/)
