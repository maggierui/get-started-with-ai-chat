---
title: "Connect to Box with Migration Manager"
ms.date:  04/07/2025
ms.reviewer: kbchen
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
ms.custom: admindeeplinkSPO
search.appverid: MET150
description: "Steps to connect to Box when using Migration Manager in the SharePoint Admin center."
---

# Step 1:  Connect your Box account to Microsoft 365

Sign in to your Box account and add the Microsoft 365 migration app to your Box account custom apps.

1. Select **Connect to Box** on the project page.
2. Select **Authenticate account**.
3. Sign in to grant access to Box. Enter your Box email and password, then select **Authorize**.
4. Select **Grant Access to Box**. You're returned to the SharePoint Admin center. Select **Next**.
5. Select **Go to custom Apps Manager**. Sign in to the Box admin console.
6. Return to SharePoint and select **Copy the client ID**.
7. In the Box Custom Apps Manager, select **Add app** to authorize. Paste in the client ID and select **Next**.
8. Select **Authorize**.
9. You're now connected to Box. Select **Finish** to close the window.

>[!Important]
>For security reasons, you have 10 minutes to complete the steps to connect to Box. After 10 minutes of inactivity, the session will expire.

## [**Step 2: Scan and assess**](mm-box-step2-scan-assess.md)
