---
title: "Configure feedback for SharePoint Server"
ms.author: ruihu
author: maggierui
manager: jtremper
ms.date: 10/22/2024
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
description: "Learn how to configure feedback for SharePoint server."
---

# Configure feedback for SharePoint Server

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

> [!Note]
> Feedback collection is available in the SharePoint Server Subscription Edition Version 24H1 feature update. This feature is only available in the *Early release* feature release ring. For more information, see [Feature release rings](feature-release-rings.md).

Microsoft aspires to bring the best possible experiences for users around the world through its innovative product offerings. Play a key role in helping Microsoft build the features that you need as we develop our products or services.

The SharePoint Server asks farm administrators to provide feedback through a feedback pop-up dialog when each admin launches the Central Administration page either locally or remotely through a browser. Your feedback goes directly to our engineers and helps us shape the future of SharePoint Server and services for our users.

> [!Note]
> By default, this feature is enabled.

An example of the "Survey" feature that was introduced in Version 24H1 is depicted in the following screenshot:

:::image type="content" source="../media/feedback-microsoft-ocv.png" alt-text="Screenshot that shows the feedback to Microsoft survey." lightbox="../media/feedback-microsoft-ocv.png":::

Starting from Version 25H1, SharePoint Server has introduced an enhancement that overwrites the feature introduced in Version 24H1. This enhancement allows the dynamic configuration and display of surveys to gather administrator feedback in a more effective manner based on current needs.

This Version 25H1-enhancement provides scope for making the following types of surveys as configurable and customizable:

- Survey type
- Rating question
- Survey rating scale and options
- Comment Question
- Whether to collect user email

The enhancement's significance is the changes in the "pop-up" frequency that follows the following rules:

- **User-level cooldown: 14 days** - This is the waiting period after triggering a survey during which a user can't see another survey. Unlike the earlier feature in which the survey form used to appear 2 weeks after the farm administrator signed in to the Central Administration portal, the Dynamic Survey features displays the survey immediately on the farm administrator signing in to the Central Administration portal and provides a cooldown period of 14 days to the user to fill the survey form, during which the farm administrator can't see any other survey form.
- **Survey-level cooldown: configurable** - This is the waiting period after triggering a survey during which a user can't see the same survey.
- A survey won't appear again for users who have already submitted.

You can also disable the survey feature for the farm administrators or specific users. For information on how to disable the survey feature, see:

- [To disable feedback for current Farm Administrator](#to-disable-feedback-for-current-farm-administrator)
- [To disable feedback for current Farm](#to-disable-feedback-for-current-farm)

You can disable or enable the feedback function using one of the following options:

## To disable feedback for current Farm Administrator

  1. Use the following cmdlet in SharePoint Management Shell to get to the current admin Sid:  

     ```
     $user = Get-SPUser -Identity <Login Name of the admin> -Web <The Central Admin Site URL>
     ```

     **For example:**
     
     ```
     $user = Get-SPUser -Identity 'contoso\domain_admin' -Web http://spse-sps:5000 
     ```

  2. Use the following cmdlet to disable the feedback for current admin:

     ```
     Disable-SPCustomerFeedbackForUser -UserSid $user.Sid 
     ```

  This `$user` is obtained from Step 1.
  
## To enable feedback for current Farm Administrator

  1. Use the following cmdlet in SharePoint Management Shell to get to the current admin Sid:  

     ```
     $user = Get-SPUser -Identity <Login Name of the admin> -Web <The Central Admin Site URL>
     ```

     **For example:**
  
     ```
     $user = Get-SPUser -Identity 'contoso\domain_admin' -Web http://spse-sps:5000 
     ```

  2.  Use the following cmdlet to enable the feedback for current admin: 

      ```
      Enable-SPCustomerFeedbackForUser -UserSid $user.Sid
      ```
    
  This `$user` is obtained from Step 1. 
  
## To disable feedback for current Farm 

Use the following cmdlet to disable feedback for current farm:  
  
  ```
  Disable-SPCustomerFeedbackForFarm
  ```
  
## To enable feedback for current Farm 

Use the following cmdlet to enable feedback for current farm:
  
  ```
  Enable-SPCustomerFeedbackForFarm
  ```
