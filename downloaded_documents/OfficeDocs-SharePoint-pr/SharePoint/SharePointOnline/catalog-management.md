---
ms.date: 11/14/2025
title: "Catalog management in SharePoint Advanced Management"
ms.reviewer: nvasudevan
manager: dansimp
recommendations: true
ms.author: ruihu
author: maggierui
audience: Admin
customer-intent: As a SharePoint admin, I want to gain insights into content distribution across my organization to optimize resource management.
f1.keywords: 
- NOCSH 
ms.topic: how-to
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- Highpri
- Tier2
- M365-sam
- M365-collaboration
- essentials-manage

search.appverid:
description: "Learn how to use Catalog management in SharePoint Advanced Management to gain insights into content distribution across your organization."
---
# Catalog management in SharePoint Advanced Management

Catalog management is included inSharePoint Advanced Management, designed to provide organizations with a comprehensive view of content distribution across regions, departments, users, information barriers, and custom properties defined by you. By leveraging built-in Microsoft 365 site and user metadata, catalog management allows organizations to group related sites into logical categories for targeted actions such as content monitoring, policy enforcement, and Copilot grounding. This structured approach streamlines processes like billing, reporting, and access management, resulting in consistent governance, reduced administrative overhead, and precise targeting for lifecycle management and security controls throughout the organization.

## What you need for Catalog management

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

## Get started with Catalog management

To get started with Catalog management, log into in the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219): 

1. Select **Reports** > **Catalog management**. 

2. See how your content is distributed across your organization. Currently, you can view the distributions by five default properties: *locale*, *department*, *user type*, *preferred data location (PDL)*, and *Information barriers segment*.

Here are what these properties mean:

   - **Locale**: The region of where the content is hosted. (e.g., North America vs. Europe).
   - **Department**: The organizational units associated with the site (e.g., finance department).
   - **User type**: Guest or not Guest.
   - **Preferred data location (PDL)**: The [multigeo setup](/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365) for your sites.
   - **Information barriers segment**: The segment defined by [information barriers policies](/purview/information-barriers-sharepoint) (for organizations that have implemented information barriers).



## How can you change property names in Catalog management?

You can customize property names to better align with your organization's terminology. For example, you might rename "Locale" to "Location" for clarity.
You can change display name of the property by selecting the property name and typing in the display name you prefer.

![Screenshot showing the option to change property names in Catalog management.](media/sam-catalog-management/change-property-name.jpg "Change property name in Catalog management")

Changing property names only affects how properties are displayed in Catalog management and doesn't alter the underlying metadata or impact site grouping logic.
