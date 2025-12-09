---
ms.date: 04/07/2025
title: "Overview: Migrate Box using Migration Manager"
ms.reviewer: kbchen
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.custom: admindeeplinkSPO
ms.collection: 
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
search.appverid: MET150
description: Overview of migration from Box to Microsoft 365 using Migration Manager.
---

# Migrate Box to Microsoft 365 with Migration Manager

Collaborate all in one place by migrating your Box documents, data, and users to OneDrive, SharePoint, and Teams in Microsoft 365.

## How does it work?

- **Step 1:** [Connect to Box](mm-box-step1-connect.md). Sign in to your Box account and add the Microsoft 365 migration app to your Box account custom apps.
- **Step 2:** [Scan and assess](mm-box-step2-scan-assess.md). Add tasks for scanning. Once the scans are complete, download Scan reports to investigate any possible issues that might block your subsequent migration. You can skip this step in Box migration.
- **Step 3:** [Copy to Migrations list](mm-box-step3-copy-to-migrations.md). After a Box user is scanned and determined to be ready, add them to your migration list.
- **Step 4:** [Review destination paths](mm-box-step4-review-destinations.md). Review destinations before migrating as destinations can't be modified once migration starts.
- **Step 5:** [Map identities](mm-box-step5-map-identities.md). Align your domain, users, and groups in the source with those domains, users, and groups in Microsoft 365 to ensure accurate migration of file metadata and permissions.
- **Step 6:** [Migrate and Monitor](mm-box-step6-migrate-monitor.md). After reviewing your migration setup, migrate your Box accounts and monitor the progress.

## Get started

To get started:

Navigate to [Microsoft 365 Admin Center Home - Setup - Migration and imports](https://admin.microsoft.com/#/featureexplorer/collections/Migrations). Select **Box** to create a migration project. Make sure that you have:

- **Access to the destination**: You must be one of the following roles in the Microsoft 365 tenant where you want to migrate your content:

  - Global admin
  - OneDrive/SharePoint admin
  - A user granted the "[Microsoft 365 Migration Administrator](/sharepointmigration/mm-migration-admin-role)" role

  >[!IMPORTANT]
  >
  > Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization.

- **Access to the source**: Have Box account credentials that have **Read** access to any Box user account you plan to migrate.
- **Prerequisites installed:** Make sure you have the necessary prerequisites installed.

Once a migration project is created, you can start connecting to the source as described in the next step. 

> [!NOTE]
> There are [file size limitations](/sharepointmigration/mm-file-size-limitations) and [unsupported files](/sharepointmigration/mm-unsupported-files) in Migration Manager.

## [**Step 1: Connect to Box**](mm-box-step1-connect.md)
