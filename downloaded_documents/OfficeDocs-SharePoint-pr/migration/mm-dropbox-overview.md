---
ms.date: 03/26/2025
title: "Overview: Migrate Dropbox using Migration Manager"
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
description: Overview of migration from Dropbox to Microsoft 365 using Migration Manager.
---

# Migrate Dropbox to Microsoft 365 with Migration Manager

Collaborate all in one place by migrating your Dropbox documents, data, and users to OneDrive, SharePoint, and Teams in Microsoft 365.

## How does it work?

- **Step 1:** [Connect to Dropbox](mm-Dropbox-step1-connect.md). Sign in to your Dropbox administrator account to connect to your Microsoft 365 migration.
- **Step 2:** [Scan and assess](mm-Dropbox-step2-scan-assess.md). Add Dropbox accounts for scanning. Once the scans are complete, download the generated reports to investigate any possible issues that might block your migration.
- **Step 3:** [Copy to Migrations list](mm-Dropbox-step3-copy-to-migrations.md). After Dropbox is scanned and determined to be ready, add them to your migration list.
- **Step 4:** [Review destination paths](mm-Dropbox-step4-review-destinations.md). We automatically map source paths to any exactly matching destination paths. Ensure content is being copied to the right place by reviewing and modifying as needed for each destination path.
- **Step 5:** [Map identities](mm-Dropbox-step5-map-identities.md). Map your domains, groups, and users in Dropbox to domains, groups, and users in Microsoft 365 to migrate metadata and permissions correctly.
- **Step 6:** [Migrate and Monitor](mm-Dropbox-step6-migrate-monitor.md). After reviewing your migration setup, migrate your Dropbox accounts and monitor the progress.

## Get started

To get started, navigate to [Microsoft 365 Admin Center Home - Setup - Migration and imports](https://admin.microsoft.com/#/featureexplorer/collections/Migrations), select **Dropbox** to create a migration project. Make sure you have:

- **Access to the destination**: You must be one of the following roles in the Microsoft 365 tenant where you want to migrate your content: 
  - Global admin
  - OneDrive/SharePoint admin
  - User that is granted with the "[Microsoft 365 Migration Administrator](/sharepointmigration/mm-migration-admin-role)" role

  >[!IMPORTANT]
  >Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. 

- **Access to the source**: Have Dropbox account credentials that have **Read** access to any Dropbox user account you plan to migrate.
- **Prerequisites installed:** Make sure you have the necessary prerequisites installed.

Once a migration project is created, you can start connecting to the source as described in the next step.

> [!NOTE]
> - There are [file size limitations](/sharepointmigration/mm-file-size-limitations) and [unsupported files](/sharepointmigration/mm-unsupported-files) in Migration Manager.
> - Learn more about [frequently asked questions for Dropbox migration](mm-faqs-dropbox.md).

## [**Step 1: Connect to Dropbox**](mm-dropbox-step1-connect.md)
