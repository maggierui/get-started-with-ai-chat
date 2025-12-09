---
ms.date: 04/21/2025
title: Deploy Restrict Known Folder Move from Office Group Policy
ms.reviewer: nirupama.m
manager: jtremper
recommendations: true 
ms.author: v-mactran
author: MachelleTranMSFT
audience: Admin
f1.keywords: 
- NOCSH 
ms.topic: how-to
ms.service: onedrive
ms.localizationpriority: medium
ms.custom:
  - has-azure-ad-ps-ref
ms.collection: 
- M365-collaboration
- Highpri
- Tier2
search.appverid:
description: "Learn how to deploy the Restrict Known Folder Move from Office Group Policy to prevent Office apps from prompting users to back up files to OneDrive."
---

# Deploy Restrict Known Folder Move from Office Group Policy

The Restrict Known Folder Move from Office (Restrict KFM from Office) Group Policy allows administrators to control whether Office apps display prompts encouraging users to back up their files to Microsoft OneDrive.

When this policy is enabled and deployed, Office doesn't display the message bar, even if users are eligible for the Known Folder Move (KFM) feature. This policy applies only to Office apps and doesn't affect other OneDrive or KFM configurations. It's available in the [Administrative Template files for Microsoft Office](https://www.microsoft.com/download/details.aspx?id=49030) (version 5497.1000 or newer).

> [!TIP]
>
> - Enable this policy if you don’t want users to see prompts to back up their files.
> - If KFM is blocked in your organization, the message bar doesn't appear, even if users are eligible.
> - Microsoft respects existing policies that block KFM and doesn't display prompts in those environments.

## What users see when eligible

When the policy isn't enabled, eligible users might see a message bar in Microsoft Word, Excel, and PowerPoint (Windows desktop versions) prompting them to enroll in [OneDrive Known Folder Move (KFM)](/sharepoint/redirect-known-folders). The message bar allows users to select folders to back up to OneDrive.

> [!IMPORTANT]
> If users aren't enrolled in KFM, they might see the message:  
> **"BACK UP THIS DOCUMENT: Share and work with others in this and other files using OneDrive."**  
>
> Selecting **Open OneDrive** lets users choose which folders to back up.

By enabling and deploying the **Restrict KFM from Office** Group Policy, administrators can prevent these prompts and maintain control over KFM adoption.

## When the Message Bar isn't displayed

The message bar doesn't appear under the following conditions:

- The user is already enrolled in KFM.
- OneDrive isn't provisioned, installed, or running.
- The policy [Prevent users from moving their Windows known folders to OneDrive](/sharepoint/use-group-policy#prevent-users-from-moving-their-windows-known-folders-to-onedrive) is enabled.
- The **Restrict KFM from Office** policy is enabled.

## Deployment methods

### Option 1: Deploy via Group Policy (Active Directory or hybrid environments)

If you're using Active Directory, Microsoft Entra, or a hybrid environment, you can deploy the policy using [Group Policy Objects (GPOs)](/previous-versions/windows/desktop/policy/group-policy-objects).

1. Download the [Administrative Template files (ADMX/ADML) for Microsoft Office](https://www.microsoft.com/download/details.aspx?id=49030).
2. Select **Download**, then choose the 32-bit (x86), 64-bit (x64), or both versions.
3. Select **Next**, then choose a location to save the file.
4. Run the downloaded **admintemplates_XXXXXXX_en-us.exe** and follow the prompts to extract the files.
5. After extracting, you'll see **admin** and **admx** folders.
6. On your Active Directory server:
   - Copy the `.admx` files into **%SYSTEMROOT%\PolicyDefinitions**
   - Copy the corresponding language `.adml` files into **%SYSTEMROOT%\PolicyDefinitions\[Language-CountryRegion]**
     - For example, copy U.S. English `.adml` files into the `en-us` folder.
7. Open **Group Policy Management**.
8. Under **Domains**, select the appropriate policy (for example, **Default Domain Policy**) and choose **Edit**.
9. In the Group Policy Management Editor, go to:  
   **User Configuration** > **Policies** > **Administrative Templates: Policy Definitions** > **All Settings**
10. Locate **Restrict KFM from Office**, right-click it, and select **Edit**.
11. Change the setting from **Not Configured** to **Enabled**, then select **Apply** and **OK**.
12. The policy setting should now display as **Enabled**.

:::image type="content" source="media/restrict-kfm-from-office/0-restrict-kfm-from-office-group-policy-editor.jpg" alt-text="Screenshot shows comment being added to the Restrict KFM from Office tool." lightbox="media/restrict-kfm-from-office/0-restrict-kfm-from-office-group-policy-editor.jpg":::

:::image type="content" source="media/restrict-kfm-from-office/1-restrict-kfm-from-office-group-policy-editor-all-settings.jpg" alt-text="Screenshot that shows the disabling KFM pop ups via the Group Policy Management editor." lightbox="media/restrict-kfm-from-office/1-restrict-kfm-from-office-group-policy-editor-all-settings.jpg":::

> [!NOTE]
> It might take up to 24 hours for the policy to take effect.

### Option 2: Deploy via Cloud Policy service

You can also deploy this policy using the [Cloud Policy service for Microsoft 365](https://config.office.com/officeSettings/officePolicies). This method works even if the device isn't domain-joined. When a user signs into Microsoft 365 Apps for Enterprise on a device, the policy settings roam to that device. See [Overview of Cloud Policy](/microsoft-365-apps/admin-center/overview-cloud-policy) to learn more about cloud policies for Microsoft 356 Apps.

To deploy the policy:

1. Sign in to the [Microsoft 365 Apps admin center](https://config.office.com/) with administrative credentials.
2. Under **Customization**, select **Policy Management**.
3. On the **Policy configurations** page, select **Create**.
4. On the **Start with the basics** page, enter a **Name** (required) and **Description** (optional), then select **Next**.
5. On the **Choose the scope** page, select whether the policy applies to:
   - All users
   - Specific groups
   - Users accessing Office for the web anonymously
6. If applying to specific groups, select **Add Groups** and choose the relevant groups.

> [!NOTE]
>
> Adding multiple groups to a single policy configuration allows for the same group to be included in multiple policy configurations, facilitating a more streamlined and efficient policy management process.

7. Select **Next**.
8. On the **Configure Settings** page:
   - Search for **Restrict KFM from Office** or use a filter.
   - Set the configuration to **Enabled**, then select **Apply**.
9. Review your selections and choose **Create**.
10. Select **Done**.

:::image type="content" source="media/restrict-kfm-from-office/2-restrict-kfm-from-office-group-policy-configure-cloud-policy.jpg" alt-text="screenshot of KFM configuration settings" lightbox="media/restrict-kfm-from-office/2-restrict-kfm-from-office-group-policy-configure-cloud-policy.jpg":::

Once configured, the policy will apply to eligible users the next time they sign in to Microsoft 365 Apps on any device.

## Related topics

- [Redirect and move Windows known folders to OneDrive](redirect-known-folders.md)
- [Use OneDrive policies to control sync settings](use-group-policy.md)
- [Group Policy Objects](/previous-versions/windows/desktop/policy/group-policy-objects)
