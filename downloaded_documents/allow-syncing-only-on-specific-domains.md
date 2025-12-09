---
ms.date: 04/04/2025
title: "Allow syncing only on computers joined to specific domains"
ms.reviewer: gacarini
ms.author: v-mactran    
author: MachelleTranMSFT
manager: jtremper
audience: Admin
f1.keywords:
- CSH
ms.topic: how-to
ms.service: onedrive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- M365-collaboration
search.appverid:
- ODB160
- ODB150
- MET150
ms.assetid: a3b03efd-ccd0-4d3c-b9ae-7f8f3f9485bc
ms.custom:
- admindeeplinkSPO
- onedrive-toc
description: "Learn how to restrict syncing to only devices on the domains you specify."
---

# Allow syncing only on computers joined to specific domains

To ensure users sync OneDrive files only on managed computers, you can configure OneDrive to sync only on PCs that are joined to specific domains.
  
## To allow syncing only on PCs joined to specific domains

> [!NOTE]
> These settings apply to SharePoint sites and OneDrive.
> In a multi-geo environment, this setting can be configured separately for each geo location to apply to users with that preferred data location.

1. Go to [Settings in the SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185072){:target="_blank"}, and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

   > [!NOTE]
   > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Sharing page.

2. Select **Sync**.

    ![Sync settings in the SharePoint admin center](media/sp-sync-settings.png)
  
3. Select the **Allow syncing only on computers joined to specific domains** check box.

4. Add the [GUID of each domain](/powershell/module/activedirectory/get-addomain) for the member computers that you want to be able to sync.

   > [!NOTE]
   > Make sure to add the domain GUID of the computer domain membership. If users are in a separate domain, the only requirement is adding the domain GUID the computer account is joined to.

   > [!IMPORTANT]
   > This setting is only applicable to Active Directory domains. It doesn't apply to Microsoft Entra domains. If you have devices that are only Microsoft Entra joined, consider using a [Conditional Access Policy](/azure/active-directory/conditional-access/overview) instead. For details, see [Enable conditional access support in the OneDrive sync app](enable-conditional-access.md).

5. Select **Save**.

For info about setting this sync app restriction by using PowerShell, see [Set-SPOTenantSyncClientRestriction](/powershell/module/sharepoint-online/set-spotenantsyncclientrestriction).

For information about blocking or limiting access to SharePoint and OneDrive content from unmanaged devices, see [SharePoint and OneDrive unmanaged device access controls for administrators](control-access-from-unmanaged-devices.md).
