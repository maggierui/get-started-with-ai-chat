---
ms.date: 03/25/2025
title: "Migrate to Microsoft 365"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- CSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
ms.localizationpriority: Low
search.appverid: MET150
msCollection: 
- SPMigration
- M365-collaboration
- m365solution-migratetom365
- m365solution-overview
- m365initiative-migratetom365
ms.custom:
- seo-marvel-apr2020
- intro-overview
- intro-get-started
description: "This article helps you understand which tool to use when migrating content to SharePoint and OneDrive in Microsoft 365."
---

# Migrate your content to Microsoft 365

Moving to Microsoft 365? **Migration Manager** helps you migrate your content easily and securely.

### Announcing the new Migration Admin role

A Microsoft 365 Migration Administrator role is now available to provide access to Migration Manager within the Microsoft 365 Admin Center. Previously, your migration teams must be assigned the SharePoint admin role, giving more access than needed. This new role is limited to the permissions required to migrate your content, reserving SharePoint Admin access to only users who need it.

Learn more:  [**Migration Admin role**](mm-migration-admin-role.md).

## What's new

- See what's new and coming soon to [Migration Manager](mm-whats-new.md).

- See what's new and coming soon to the [SharePoint Migration Tool (SPMT)](new-and-improved-features-in-the-sharepoint-migration-tool.md).

#### Mover retirement

**Mover is now retired for all Admin led migrations**. The ability to migrate from Google Drive, Box, Dropbox, and Egnyte is fully integrated into Migration Manager. All FastTrack-led migrations are transitioned to Migration Manager. Migration Manager doesn't support the migration of Amazon S3 or Azure blob storage.

**Mover will be retired and not available for individual and students use after October 31, 2024.**

- For migrating from Google Drive and Dropbox to your OneDrive (personal) account, download the OneDrive mobile app from [here](https://www.microsoft.com/microsoft-365/onedrive/download) and follow the [guidance](https://support.microsoft.com/office/import-other-cloud-files-using-the-onedrive-mobile-app-0e769bf6-934f-46f5-b57e-032d41210343).

- For migrating from OneDrive (work or school) to your OneDrive (personal) account, follow the [guidance](https://support.microsoft.com/office/copy-transfer-or-import-files-to-your-personal-onedrive-7dbda93c-71e6-483f-8914-ad445554cd31).

- For other migration scenarios to migrate your content to Microsoft 365, check Migration Manager [learn more](/sharepointmigration/migrate-to-sharepoint-online).

### Cross-tenant migration

Tenant to tenant migration for OneDrive is now available outside of Migration Manager. To learn more:

- [**Cross-tenant OneDrive migration**](/microsoft-365/enterprise/cross-tenant-onedrive-migration).

A cross tenant migration solution for SharePoint is currently in private preview. To learn more, see:

-  [**How to participate in the Cross-tenant SharePoint migration preview**](/microsoft-365/enterprise/cross-tenant-sharepoint-migration).

### Transform your classic SharePoint Server pages

If you're onboarding your classic on-premises SharePoint Server pages to Microsoft 365, we have assistance available. Learn more at: [**Transform classic pages to modern pages**](/sharepoint/dev/transform/modernize-userinterface-site-pages).

##  Where are you migrating from?

|Migrate from|Description|
|:-----|:-----|
|![Get started **Box**](/office/media/icons/get-started-blue.png)</br> [**BOX**](mm-box-overview.md)|Collaborate all in one place by migrating your Box documents, data, and users to OneDrive, SharePoint, and Teams in Microsoft 365. |
|![Get started File share](/office/media/icons/get-started-blue.png) </br> [**FILE SHARES**](mm-get-started.md)|With a centralized way of connecting servers, creating tasks, and managing your migration tasks, migrate your file shares to Microsoft 365.|
|![Get started Google Workspace](/office/media/icons/get-started-blue.png) </br> [**GOOGLE WORKSPACE**](mm-google-overview.md)|Migrate your Google Drives to Microsoft 365. |
|![Get started Dropbox](/office/media/icons/get-started-blue.png) </br> [**DROPBOX**](mm-dropbox-overview.md)|Collaborate all in one place by migrating your Dropbox documents, data, and users to OneDrive, SharePoint, and Teams in Microsoft 365. |
|![Get started SharePoint Server](/office/media/icons/get-started-blue.png)</br>  [**SHAREPOINT SERVER**](introducing-the-sharepoint-migration-tool.md)|Migrate your SharePoint Server sites and content to take advantage of the latest collaboration, intelligence, and security solutions in Microsoft 365. SharePoint Server 2010, 2013, and 2016 environments only.|
|![Get started SharePoint Server workflows](/office/media/icons/get-started-blue.png)</br>  [**SHAREPOINT SERVER WORKFLOWS**](spmt-workflow-overview.md)|Microsoft removed **SharePoint Server 2010** workflow services from existing tenants on November 1, 2020. We recommend that you move your classic SharePoint Server workflows to Power Automate flows. With SPMT, you can migrate your **SharePoint Server 2010** out of the box (OOTB) approval and collect feedback workflows to Power Automate, List and library "out-of-box" (OOTB) approval workflows, and Workflow definitions and associations.|
|![Get started classic SharePoint Server pages](/office/media/icons/get-started-blue.png)</br>[**SHAREPOINT SERVER CLASSIC PAGES**](/sharepoint/dev/transform/modernize-userinterface-site-pages)|Are you onboarding your classic on-premises SharePoint Server content to Microsoft 365? Here's how: [Transform classic pages to modern pages](/sharepoint/dev/transform/modernize-userinterface-site-pages)|

## Other resources

- **Cross-tenant OneDrive migration**. During mergers or divestitures, you commonly need the ability to move your users OneDrive accounts into a new Microsoft 365 tenant. With Cross-tenant OneDrive migration, tenant administrators can use PowerShell to transition users into their new organization. To learn more, see [**Cross-tenant OneDrive migration**](/microsoft-365/enterprise/cross-tenant-onedrive-migration)

- **Microsoft FastTrack**. Microsoft FastTrack services can help you get started with your migration to the cloud. When you need assistance to help you get started on your migration project.

- **Azure Data Box**. Want to remove the dependency on your WAN link to transfer data? The Microsoft Azure Data Box is a service that lets you order a device from the Microsoft Azure portal. You can then copy terabytes of data from your servers to the device, ship it back to Microsoft, and your data is copied into Azure. Once your data's in Azure, use SPMT to migrate content to SharePoint. To learn more, see [Migrate using the Azure Data Box](how-to-migrate-file-share-content-to-SPO-using-AzureDataBox.md).

- **OneDrive sync app** To migrate users' Windows known folders (Desktop, Documents, Pictures, Screenshots, and Camera Roll) to OneDrive, you can use [Known Folder Move](/onedrive/redirect-known-folders). If users want to move other files from their local computer or a network file share to OneDrive or SharePoint, it's often easiest for them to use the OneDrive sync app. Users drag their files or folders to a folder they're syncing.

>[!Note]
>When you migrate your content to Microsoft 365, you are copying the files.  Your source files are not deleted.
