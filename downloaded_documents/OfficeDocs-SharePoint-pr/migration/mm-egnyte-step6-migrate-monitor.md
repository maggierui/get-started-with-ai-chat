---
ms.date: 04/08/2025
title: "Step 6: Migrate and monitor Egnyte migration"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
ms.localizationpriority: medium
ms.collection: 
- m365solution-migratefileshares
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
search.appverid: MET150
ROBOTS: NOINDEX
description: "Step 6: Migrate and monitor Egnyte migration"
---
# Step 6:  Migrate and monitor your Egnyte migration

Once you review the tasks (Egnyte folders), confirm the destinations, and correctly map identities, you're ready to migrate.

>[!Important]
>We strongly recommend you don't rename or move migrated files before the final migration has been completed. Doing so results in files being overwritten.

1. Select the accounts to migrate.
2. Select **Migrate**.
3. A confirmation panel displays. Select **Migrate**.
4. Once the migration starts, monitor the migration status, and the table summary at the top. Depending on how large your migration, this step can take hours or days.
>[!Note]
> Starting your migration only copies content from your Egnyte account to the location you have specified in Microsoft 365. Make sure the destinations are correct. Once migration starts, they can't be modified.

## Download reports

**Migration summary report** and **Migration detailed reports** are available to assist you in troubleshooting. [Download the generated reports](/sharepointmigration/mm-cloud-reports#download-migration-reports) to investigate any possible issues that occurred during the migration. 

Check the [status code](/sharepointmigration/mm-cloud-reports#status-codes) in **Migration summary report** to address task-level errors. For file-level errors, refer to the [failure code (*ResultCode*)](/sharepointmigration/mm-cloud-reports#failure-codes) in the **Migration detailed report**.

After resolving the issues related to warnings or failed tasks, migrate the tasks again to ensure the successful migration of all required files.

## Delta sync
When a migration task is conducted for the first time, we call it an initial migration or new migration. After the initial migration, the destination can't be changed. If the task is migrated again, we call it a delta sync. We may also call it an incremental sync, or incremental migration. Learn more about [file transfer behaviors in a delta sync](mm-delta-sync.md).


## Migration lanes

At a maximum, only 50 task rows can run simultaneously. This total includes both scanning and migrating.

If you select more than that total combined number and start scanning or migrating, only 50 randomly chosen rows run. The remaining rows are queued.

As a task row completes, another from the queue starts migrating or scanning automatically. The maximum allowed is 50 task rows. However, if a migration experiences any slowdowns or back-off requests, it can drop lower than this number to keep the migration stable.

## Schedule a migration
Migration Manager allows you to schedule a migration for one or multiple tasks. This migration is a one-time migration event. When the scheduled time arrives, Migration Manager starts queuing the scheduled tasks. The queued tasks begin migrating immediately if the migration lane limit isn't reached.
