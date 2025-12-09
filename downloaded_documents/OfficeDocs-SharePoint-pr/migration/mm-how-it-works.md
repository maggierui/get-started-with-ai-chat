---
ms.date: 04/02/2025
title: How does Migration Manager work for file share migrations
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
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
search.appverid: MET150
description: "Learn how File share migration works, for a computer or a VM (virtual machine) when using Migration Manager in Microsoft 365 SharePoint admin center."
---

# How does Migration Manager work for file share migrations

The Migration Manager centralizes the management of large file share migrations by configuring one or more computers or virtual machines (VMs) as migration "agents". Each computer or VM can be running migration tasks simultaneously.

## User process

**Agent setup**

From the SharePoint admin center, select <a href="https://go.microsoft.com/fwlink/?linkid=2185075" target="_blank">**Migration center**</a> and then **File Shares**. Download the agent setup file and install it on each Windows computer or virtual machine you want to use as a migration agent. The agent setup file prompts for two sets of credentials: the SharePoint Admin credentials to access your destination and the Windows credentials that have **Read** access to any network file shares you plan to migrate.

This pair of credentials creates a trust with Migration Manager. Migration Manager now sees it as an available agent to which it can automatically distribute migrations tasks.

**Task creation**

After you configure the agent, anyone with the permission to go into the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a> can create tasks.

When you add a task, Migration Manager authenticates to the destination tenant and then prompts for the source file location and destination location. Selecting **Migrate** submits the task. The scanning, packaging, uploading, and importing steps are then performed in parallel across all the files chosen for migration.

## Migration Process

**Authentication**

Sign in to your <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a> as a either a Global Administrator or SharePoint admin user in the destination where you want to migrate content. The tenant associates the migration jobs you submit to this account.

> [!IMPORTANT]
> Microsoft recommends that you use roles with the fewest permissions. It helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

**Scan**

After selecting Migrate, a scan is always performed on every file, even if you decide not to migrate your files. The scan verifies that there's access to the data source and write access to the destination. It also scans the files for known potential issues.

**Packaging**

In the packaging stage, a content package is created that contains a manifest.

**Upload**

In the upload stage, the content package is uploaded to Azure with the manifest. Before a migration job can be accepted from a SharePoint-provided Azure container, the files and manifest are encrypted at rest using the AES-256-CBC standard.

**Import**

During the import phase, the key is provided to SharePoint SAS. Only Azure and SharePoint are interacting to fetch and migrate the data to the destination. This process is a timer job-based but doesn't prevent other jobs from being queued up. A report is created in the working folder, and live updates are made during the import.

After the migration job completes, reports are generated and can be downloaded. Report files are cleared when you delete the tasks.

**Sessions**

The session's information, including the tasks and settings, is saved in the Tenant Admin site hidden list. When you select **Run** to resume a paused task, Migration Manager issues a command to the agent. If the migration task completes, clicking **Run** restarts the task with the same source, destination, and settings.

## Encryption and security

During the upload and import phases, data is encrypted and Azure containers and keys are generated.

>[!Important]
>The SharePoint service and a select number of engineers can run maintenance commands against them, but they don't have direct access to the accounts. Datacenter technicians aren't prepped with how data is laid out on disk and don't have ready access to equipment to mount disks. All drives are physically destroyed before leaving the datacenter. Physical security is also in place across all of our datacenters.

Each container is dedicated to the customer and not reused. The data is stored in the Azure blob from 4 to 30 days, after which it's deleted. When the data is deleted, the files are delinked and later soft-deleted from disk. A file in an account and on-disk may be shared across many servers. The same process is used for replicas, including backup copies (geo-replicated data if applicable).

The random, single-use default container key is generated programmatically and is only valid for three days. This key is the only way to gain access to the container. SharePoint never stores the key.

The container itself lives longer than the key. The container is purged anywhere from 30 to 90 days from its creation date. The container is housed in a shared Microsoft storage outside the tenant but within the region. The container key protects it. For multi-Geo customers, the containers are generated based on the destination URL, and dictate the Geo it's stored in.

If your key is lost or someone else obtains it, there are two defenses in place that protect you. First, the container only enables read/write operations. And, as the container has no list, you need to know the details of the files stored in the container to read or write. Secondly, the files are encrypted at rest with AES-256-CBC.

>[!Important]
>Only those who have the key have access to the container. Other users in the subscription or the tenant do not have access.
