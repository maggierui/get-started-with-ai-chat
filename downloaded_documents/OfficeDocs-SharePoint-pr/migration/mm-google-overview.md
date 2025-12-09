---
ms.date: 09/15/2025
title: "Overview: Migrate Google Workspace to Microsoft 365 with Migration Manager"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
ms.custom: admindeeplinkSPO
search.appverid: MET150
description: Overview of how to migrate from Google Workspace to Microsoft 365 with Migration Manager.
---

# Migrate Google Workspace to Microsoft 365 with Migration Manager

Collaborate all in one place by migrating your Google Workspace files, metadata, and permissions to OneDrive and SharePoint in Microsoft 365.

## How does it work?
For a standard Migration Manager workflow, the migrator typically follows six key steps:

- **Step 1:** [Connect to Google](mm-google-step1-connect.md). Sign in to your Google account and install Microsoft 365 migration app in Google Workspace Marketplace. 
- **Step 2:** [Scan and assess](mm-google-step2-scan-assess.md). Add Google Drives for scanning. Once the scans are complete, download [Scan reports](/sharepointmigration/mm-cloud-reports) to investigate any possible issues that might block your migration.
- **Step 3:** [Copy to Migrations list](mm-google-step3-copy-to-migrations.md). After a Google Drive is scanned as **Ready to migrate**, you can add them to your migration list.
- **Step 4:** [Review destination paths](mm-google-step4-review-destinations.md). We automatically map source paths to any exactly matching destination paths. Ensure content is being copied to the right place by reviewing and modifying as needed for each destination path.
- **Step 5:** [Map identities](mm-google-step5-map-identities.md). Map your domains, groups, and users in Google Drive to the domains, groups, and users in Microsoft 365. This mapping lets you migrate metadata and permissions correctly.
- **Step 6:** [Migrate and Monitor](mm-google-step6-migrate-monitor.md). After reviewing your [migration setup](/sharepointmigration/mm-project-settings), migrate your Google Drives and monitor the progress.

>[!Tip]
>Watch this video to help get started:  [Migrate Google files to Microsoft 365 with Migration Manager](https://youtu.be/GZ4kTX31U-A).


## Migration Manager Lite
Migration Manager Lite is a simplified version of standard Migration Manager rolled out to help SMB (small and medium business) customers easily migrate their content from Google Drive to Microsoft 365. It's **enabled by default** for SMB tenants with fewer than 100 licenses in Microsoft 365 at the time the migration project is created.

| Migration workflow   | Standard Migration Manager | Migration Manager Lite |
|----------------------|-----|---------|
| **Step 1:** [Connect to Google](mm-google-step1-connect.md) | ✔   | ✔       |
| **Step 2:** [Scan and assess](mm-google-step2-scan-assess.md) | ✔   | ✖       |
| **Step 3:** [Copy to Migrations list](mm-google-step3-copy-to-migrations.md) | ✔   | ✖       |
| **Step 4:** [Review destination paths](mm-google-step4-review-destinations.md) | ✔   | ✖       |
| **Step 5:** [Map identities](mm-google-step5-map-identities.md)| ✔    | ✖       |
| **Step 6:** [Migrate and Monitor](mm-google-step6-migrate-monitor.md)| ✔    | ✔       |


## Get started

To get started, navigate to [Microsoft 365 Admin Center Home - Setup - Migration and imports](https://admin.microsoft.com/#/featureexplorer/collections/Migrations) and select **Google Drive** or **Google Workspace** to create a migration project. Make sure that you have:

- **Access to the destination**: You must be one of the following roles in the Microsoft 365 tenant where you want to migrate your content: 

  - Global admin
  - OneDrive/SharePoint admin
  - User that is granted with the "[Microsoft 365 Migration Administrator](/sharepointmigration/mm-migration-admin-role)" role

  >[!IMPORTANT]
  >Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization.

- **Access to the source**: Have Google account credentials that have **Read** access to any Google user account you plan to migrate.

- **Prerequisites installed:** Make sure you have the necessary prerequisites installed.

Once a migration project is created, you can start connecting to the source as described in the next step.

> [!NOTE]
> - There are [file size limitations](/sharepointmigration/mm-file-size-limitations) and [unsupported files](/sharepointmigration/mm-unsupported-files) in Migration Manager.
> - Learn more about [frequently asked questions for Google migration](mm-faqs-google.md).

## [**Step 1: Connect to Google Workspace**](mm-google-step1-connect.md)
