---
ms.date: 11/11/2025
title: "Service prioritization in SharePoint"
ms.reviewer: 
ms.author: sibourda
author: SimonBourdages
manager: fraga
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.custom: admindeeplinkSPO
ms.localizationpriority: medium
search.appverid:
- SPO160
- MET150
ms.assetid: 
description: "What is service prioritization in SharePoint and How to Leverage It"
---


# Service Prioritization in SharePoint

Service prioritization in SharePoint is a powerful service designed to prioritize apps within your SharePoint Online tenants, particularly those considered business-critical. By using service prioritization, organizations can ensure optimal performance, scalability, and reliability for key applications without requiring code modifications. Next, we explore what service prioritization entails and how to effectively use it within your organization.

## What is Service Prioritization in SharePoint?

Service prioritization in SharePoint enables businesses to assign a higher priority to their critical applications within a SharePoint environment. This prioritization ensures that these apps are the last to experience throttling in their tenant during periods of high resource usage. It allows the app to scale resource usage limits ([aka.ms/SPO429](https://aka.ms/spo429)) significantly—ranging from a minimum of 2x up to 10x when there are available resources. Additionally, these apps receive dedicated resource units that are separate from the general tenant limits, enhancing their reliability and performance.
> [!NOTE]
> Sharing limits are excluded from this offering at this time.

### Key Benefits of Service Prioritization in SharePoint

- **Scalable Resources**: Application resource limits can exceed [normal thresholds](https://aka.ms/spo429), offering up to 10 times more capacity when available.
- **No Code Changes Required**: Any app can be prioritized without requiring development or code modifications as long as they can be registered on Microsoft Graph metered APIs.
- **Pay-As-You-Go Model**: Organizations only pay for the resources they consume.

## Metered API Classification

Service prioritization in SharePoint integrates with Azure's standard cost management experience, enabling organizations to monitor and control expenses associated with prioritized apps. For detailed reporting, refer to Microsoft’s Cost Management documentation.

To support prioritization, service prioritization in SharePoint operates on a metered API model with defined costs:

- **Standard APIs**: charged at $0.02 per 1,000 requests.
- **Heavy APIs**: charged at $0.14 per 1,000 requests.

> [!NOTE]
> All API calls to SharePoint and OneDrive are included. Price varies based on the API used per pricing above in effect as of 11/11/2025.

## How to Leverage Service Prioritization in SharePoint

Administrators can onboard and manage service prioritization policies and app registrations using the SharePoint Online PowerShell module. Below are some key cmdlets: 

### 1. Onboard on Service Prioritization in SharePoint Using PowerShell

- **[New-SPOServicePrioritizationBillingPolicy]**: Creates a new billing policy for service prioritization. This policy defines the billing structure for prioritized apps.
- **[Add-SPOServicePrioritizationAppRegistration]**: Registers an app for service prioritization. Requires details such as App ID, Azure Subscription ID, and Quota Multiplier.

### 2. Manage Service Prioritization in SharePoint Using PowerShell

- **[Get-SPOServicePrioritizationBillingPolicies]**: Retrieves all existing billing policies for service prioritization in the tenancy.
- **[Get-SPOServicePrioritizationAppRegistrations]**: Retrieves all app registrations for service prioritization in the tenancy.
- **[Set-SPOServicePrioritizationAppRegistration]**: Updates an existing app registration for service prioritization, such as modifying the Quota Multiplier or enabling/disabling the registration.
- **[Remove-SPOServicePrioritizationAppRegistration]**: Deletes an existing app registration for service prioritization.

### 3. Best Practices and Considerations

- Prioritize apps that are critical to your business operations to maximize the value of service prioritization in SharePoint.
- Take time to understand the limits of the service at [https://aka.ms/spo429](https://aka.ms/spo429).
- Regularly review resource usage and adjust quotas or policies as necessary to balance performance with cost efficiency.

## Related articles

- [Microsoft Cost Management Documentation](/azure/cost-management)
- [Understanding SharePoint Throttling Limits](https://aka.ms/spo429)
