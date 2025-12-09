---
ms.date: 03/31/2025
title: "Migrate SharePoint workflows with the SharePoint Migration Tool (SPMT) to Power Automate"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom: admindeeplinkSPO
ms.assetid: 
search.appverid: MET150
description: "Overview of how to migrate your SharePoint Server workflows to Power Automate using the SharePoint Migration Tool (SPMT)."
---

# Overview: Migrate SharePoint Server workflows to Power Automate

Workflows created with SharePoint Server or SharePoint Server Designer can be migrated to Power Automate using the SharePoint Migration Tool (SPMT).

## What is supported

Using the SharePoint Migration Tool (SPMT), you can now migrate:

- **SharePoint Server 2010 out-of-the-box (OOTB) workflows** to Power Automate, including: Approval, Collect Feedback, Collect Signature, and Three-state workflows.
- **SharePoint Server 2010 and 2013 Designer (SPD) workflows** to Power Automate.
- List, library workflows, and content-type workflows (not site workflows).
- Workflow definitions and associations (not workflow history data).

>[!Note]
>Microsoft removed **SharePoint Server 2010** workflow services from existing tenants on November 1, 2020. We recommend that you move your classic SharePoint Server workflows to Power Automate flows.

## Steps

|Step |What happens |
|:----|:------------|
|[Step 1: Configure endpoints and Power Automate](spmt-workflow-step1.md) |Configure required endpoints. If your tenant has never used Power Automate, configure it before you begin migration. |
|[Step 2: Migrate workflows](spmt-workflow-step2.md) |Using SPMT, migrate your SharePoint Server workflows. |
|[Step 3: Activate workflows](spmt-workflow-step2.md) |Sign in to Power Automate to activate the newly migrated workflows. |

## Prerequisites

Go to the [Migration Center](https://microsoft-admin.sharepoint-df.com/?page=migration&modern=true) in the SharePoint admin center and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

Make sure you have:

- **Access to the destination**: The user account you use to migrate must:
  - Be a OneDrive or SharePoint admin, or a SharePoint site admin on the Microsoft 365 tenant.
  - Be a Power Automate admin who can manage the solution.
  - Be assigned the *Environment Maker* role, as this user account is set as the owner of migrated flow. [Learn more about Environment Maker role](/power-platform/admin/database-security).
- **Access to the source**: Your SharePoint Server account credentials must have **Read** access to any workflow you plan to migrate.
- **Prerequisites installed:** Make sure you have the necessary prerequisites installed.

## General process

- **Scan workflow**
  Workflow scans generate a report that lets you review your workflow inventory and plan the migration. Select "Only perform scanning" on the **Choose your settings** page to start a scan.
- **Migrate workflow**
  Review your scan and determine if you're ready to migrate your SharePoint Server workflows. Choose to either use SPMT to step through the process or use the PowerShell method.
- **Re-run migration**
  SPMT skips a workflow if it's been migrated successfully. If you want to run a new migration to override the migrated flow, delete it from the destination before starting the migration.
