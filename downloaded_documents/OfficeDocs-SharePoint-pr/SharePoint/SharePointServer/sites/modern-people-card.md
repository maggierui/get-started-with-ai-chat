---
title: "Modern People Card"
ms.reviewer: 
ms.author: lanruowu
author: lanruowu
manager: kaibchen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: overview
ms.date: 08/14/2025
ms.service: sharepoint-server-itpro
ms.localizationpriority: high
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn about the Modern People Card feature, which is one of the newly introduced features in SharePoint Server Subscription Edition Version 25H2."
---

# Modern People Card

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

This article describes the "Modern People Card" feature, which is one of the new features introduced in the SharePoint Server Subscription Edition Version 25H2 feature update.

> [!NOTE]
> The Modern People Card was initially introduced in SharePoint Server Subscription Edition Version 25H2, with availability limited to SharePoint farms configured for the Early release ring. Beginning with Version 26H1, the feature is available to all farms, regardless of whether they're configured for Early release or Standard release.

## Modern People Card

This feature enhances the user experience in Lists and Document Libraries by displaying essential user information directly within the interface.
When you hover over or select a user field, the People Card appears, offering a compact and informative view.

![UserInfo](../media/modern-people-card-user-info.png)

### Displayed Information
The Modern People Card presents the following details (fields not populated are omitted):
- Basic Information
  - Avatar
  - Name (for example, user01)
  - Job (for example, software engineer)
  - Department (for example, SharePoint Server)
- Contact Information
  - Sip Address (for example, user01-sip-address)
  - Phone (for example, 123456789)
  - Email (for example, user01​@microsoft.com)
- Reporting Structure
  - Manager Avatar
  - Manager name (for example, user03)
  - Manager job (for example, leader)

When a user selects a contact item (such as an email address or phone number), the default application launches or prompts the user to choose one. For example, clicking on the email address might open Outlook with the recipient prefilled.

## How to Configure User Information
User data displayed in the Modern People Card is sourced from:
- **User Profile Service Application (UPA)**
- **Active Directory (AD)**

### User Profile Service Application

To configure user profiles:

1. Navigate to **Central Admin > Application Management > Manage service applications > User Profile Service Application > Manage User Profiles**.

   :::image type="content" source="../media/modern-people-card-manage-user-profiles.png" lightbox="../media/modern-people-card-manage-user-profiles.png" alt-text="ManageUserProfiles":::

1. Add or edit User Profiles.
   ![EditUserProfile](../media/modern-people-card-edit-user-profile.png)

   The following table maps User Profile properties to People Card fields:

    | User Profiles Properties | Information in People Card |
    |------------------------|----------------------------|
    | AccountName            | Name (without domain)      |
    | SPS-JobTitle           | Job                        |
    | SPS-Department         | Department                 |
    | PictureURL             | Avatar                     |
    | WorkPhone              | Phone                      |
    | SPS-SipAddress         | Sip Address                |
    | WorkEmail              | Email                      |
    | Manager                | Manager                    |

    > [!NOTE]
    > - Manager details (for example, job title) must be configured in the manager's own profile.
    > - Set visibility to "Show to Everyone" for fields like SPS-Department to ensure they appear on the card.

### Active Directory
If a user exists in AD but not in User Profile Service Application, the user's email is shown on the People Card if it's set in Active Directory. This email is also be used as the SIP address.
