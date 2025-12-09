---
title: "Connect to Google with Migration Manager"
ms.date:  09/15/2025
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: microsoft-365-migration
ms.localizationpriority: medium
mscollection:
- m365solution-migratefileshares
- m365solution-migratetom365
- m365solution-scenario
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
ms.custom: admindeeplinkSPO
description: "Steps to connect to Google when using Migration Manager in the SharePoint Admin center."
---

# Step 1:  Connect to Google Workspace

Sign in to your Google account and add the Microsoft 365 migration app to your Google account custom apps.

1. **Install Microsoft 365 migration app**
   - Select **Install and authorize**. Sign in to the Google Workspace Marketplace with a super admin, groups admin, user management admin, or help desk admin account.
   - Select **Domain install**. On the *Domain wide install* screen, select **Continue**. Agree to the terms of service by checking the box, then select **Allow**. Click **Done** to complete the installation.
   - Go back to Migration Manager in Microsoft Admin Center and select **Next**.
2. **Authenticate Google Workspace**
   - Select **Sign in to Google Workspace** to authenticate and complete the connection.
   - Select **Next**/**Finish** to proceed.

>[!Important]
>For security reasons, you have 10 minutes to complete the steps to connect to Google. After 10 minutes of inactivity, the session expires.

## Standard Migration Manager

For general customers, after connecting to Google Workspace, you're directed to the **Configure project settings** page to review key migration options. If you prefer to skip this step, select **Skip and finish**.

You can then proceed to [Step 2: Scan and assess](mm-google-step2-scan-assess.md).

## Migration Manager Lite

For SMB (small and medium business) customers with fewer than 100 Microsoft 365 licenses, once you connect to Google Workspace, you enter the Migration Manager Lite’s **First Run Experience** wizard:
1. **Select migration tasks**. Select the tasks discovered from Google Drive that you wish to migrate.
2. **Assign destinations**. Review and confirm that each selected task has the correct destination. You can make [single destination edits or bulk updates via CSV upload](mm-google-step4-review-destinations.md).
3. **Map identities**. Map your Google domains, groups, and users to their Microsoft 365 counterparts. Learn more about [Map identities](mm-google-step5-map-identities.md).
4. **Configure migration settings**. Adjust migration preferences as needed.
5. **Review and finish**. Finalize your setup and start migration.

> [!NOTE]
> - The migration of selected tasks begins automatically once the wizard is completed.
> - Next, you can download migration reports, rerun migrated tasks, or add new migration tasks from the main migration UI. Learn more about [Migration and monitor](mm-google-step6-migrate-monitor.md).

## Go to [**Step 2: Scan and assess**](mm-Google-step2-scan-assess.md)
