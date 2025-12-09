---
ms.date: 04/01/2025
title: Email notification
ms.reviewer: heidip
ms.author: kbchen
author: MetMS2023
manager: DAPODEAN
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: microsoft-365-migration
ms.localizationpriority: medium
mscollection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
description: "Email notification settings of Migration Manager."
---

# Email Notification

Migration Manager allows you to customize email notifications for all cloud migration scenarios to track your migration progress.

## Configure email notification

To set up email notification for your cloud migration project:

1. Select **Project settings** in the top-right toolbar.
2. Select the **Advanced** tab.
3. Enable **Email notification** and configure the following settings:
    - **Recipients**: Enter email addresses, separated by commas
    - **Frequency**: Select notification frequency:
      - **Do not repeat**
      - **Daily** (3-month limit, multiple notifications per day available)
      - **Weekly** (3-month limit)
      - **Monthly** (12-month limit)
    - **Start date**
    - **Start time** (in your local time zone)
    - **End date**

>[!NOTE]
> Ensure notifications are sent to authorized recipients only to maintain project confidentiality.

## Notification content

You receive the following email notifications based on your configured schedule:

**Email details**:
- **Subject**: Your latest migration progress
- **From**: SharePoint Online (no-reply@sharepointonline.com)

**Content includes**:
- Project Information: Project ID and name.
- Migration Overview: Total, completed, and running tasks.
- Task Status: Completed, warning, and failed tasks.
- Migration Statistics: Number of files and data volume (migrated and failed).

>[!NOTE]
> - Scheduled tasks aren't included in the Migration Overview.
> - Migration Statistics show cumulative results from all migration transactions.
