---
ms.date: 04/03/2025
title: "Migration Manager FAQs"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: faq
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
- m365initiative-migratetom365
ms.custom: admindeeplinkSPO
search.appverid: MET150
description: Migration Manager FAQs
---

# Frequently Asked Questions: Migration Manager File Share

### File Share migration questions

**Question:** Does the file share I'm migrating need to be on a Windows computer?

Answer: No. As long as you can access the file share from the migration agent, you can migrate it.

**Question:** Can I manually assign a task to a migration agent I set up?

Answer: No. Migration Manager does it for you by automatically distributing tasks to the next available agent. However, you can target migration tasks to a group of agents.

**Question:** How many tasks can an agent perform simultaneously?

Answer: An agent can perform 5 to 10 tasks simultaneously, depending on the size of each of the tasks.

**Question:** What happens when you "pause" a task?

Answer: Pausing a task doesn't release the agent to another task. The agent remains unavailable to accept a new task until the task is resumed and completed, or if the task is deleted.

**Question:** How long does an agent stay connected to Migration Manager?

Answer: The connection between an agent and Migration Manager stays active as long as the computer is still running and the SharePoint admin credentials that were used to sign into the agent are still valid. If the agent does becomes disconnected, the agent holds the token to the Migration Manager for up to seven days. After which the agent needs to be reinstalled.

**Question:** How do I remove the Migration Manager agent from a computer? 

Answer: Rerun the Migration Manager agent installer and select the **Uninstall** button.

**Question:** How do I update the Migration Manager agent?

Answer: The agent is set to automatically update to the latest version by default.

**Question:** Does adding more agents linearly increase the throughput? Is there a cap on the max number of agents?

Answer: Based on our current data, the average speed of migration scales linearly to the number of agents, unless the overall throughput hits the upper limit of your network bandwidth. Multiple agents reading from the same source file share path can also impact throughput. There’s no limit on how many agents you can install. We have many customers who perform migrations using 20+ agents. **Note:** A single agent can process up to 10 tasks at a given time.

**Question:** Where are local Migration Manager logs stored?

Answer: The logs are stored here: `C:\Users\<Username>\AppData\Roaming\Microsoft\SPMigration`.

**Question:** Can I rename my temporary working folder?

Answer: Yes. By default the name of the folder is `%appdata%\Microsoft\SPMigration`. Through the Migration Manager UI, you can configure the physical location of the folder where logs and reports are stored on the agent's machine including renaming your working folder.

**Question:** What should I do if I don't have enough storage space?

Answer: When you are in Manager Manager, you can see the available disc space. Choose a drive that has enough storage before starting your migration.

**Question:** What happen during incremental migration if I rename, move or delete a destination file or folder?

Answer: After a file or fold is migrated to destination, user **renames or moves** the file or folder, then remigrate,

- The source file or folder is migrated to the destination.
- The renamed/moved file or folder is kept.

After a file or folder is migrated to destination, user **deletes** the file or folder, then remigrate,

- The source file or folder is migrated to the destination.

**Question:** In file share migrations, what is the content type of a migrated document?

Answer: In file share migrations, files are transferred to the SharePoint document library with the default "Document" content type. This process doesn't take into account any content type configurations that may be set on the library.

### General questions on Migration Manager

**Question:** Is there a Tenant to Tenant (T2T) migration solution?

Answer: Yes. Cross-tenant OneDrive migration is now available outside of Migration Manager. A cross tenant migration solution for **SharePoint** is currently available. [Learn more about the cross-tenant OneDrive migration](/microsoft-365/enterprise/cross-tenant-onedrive-migration).

**Question:** Can I migrate content from SharePoint Server?

Answer: At this time, Migration Manager supports the migration of file shares and cloud sources including Google, Dropbox, and Box. It doesn't support the migration of content from SharePoint Server. See SPMT (SharePoint Migration Tool) for SharePoint Server migration.

**Question:** Can I run the SharePoint Migration Tool (SPMT) on the same computer that I have the Migration Manager agent installed?

Answer: Yes.

**Question:** Is multifactor authentication supported by Migration Manager?

Answer: Microsoft multifactor authentication is supported; however third party multifactor authentication isn't.

**Question:** Can Migration Manager migrate content to non-English SharePoint sites?

Answer: Yes, Migration Manager can migrate content to non-English sites as long as the site title doesn’t include non-EN characters.

**Question:** Is Migration Manager available for Government clouds?

Answer: Yes. Here's how you configure it: [Government cloud settings](./mm-gov-cloud.md).

**Question:** What’s the retention policy for the blog storage?

Answer: Customers and ISVs use the [SharePoint-provided blob containers/queues](/sharepoint/dev/apis/migration-api-azure-container-and-queue) when they used the Migration API. [SAS URIs](/azure/storage/common/storage-sas-overview) are provided to access the container and queues. The SAS URIs are valid for three days from creation for containers and 21 days for queues. After the SAS expires, the content in the blob containers and queues isn't accessible. SharePoint backend jobs delete the content in the container/queues within 30 to 90 days of the creation.
 
**Question:** Is the data in the SharePoint-provided containers encrypted?

Answer: Yes. We mandate that the data uploaded to SharePoint provided containers must be encrypted using Advanced Encryption Standard (AES) Cypher Block Chaining (CBC) to ensure the data is secure. To learn more, see: [OneDrive for Business and SharePoint Online Migration API encryption](/sharepoint/dev/apis/migration-api-encryption).

**Question:** Can my migration succeed if the temporary storage expires before content migration is complete?

Answer: Yes. If your migration task was successful, your data is migrated to SharePoint even if the temporary storage expired.

**Question:** Does running a migration slowdown the tenant or impact SharePoint site performance while migrating?

Answer: In general, site performance shouldn't be impacted by running a migration. There are many factors that prevent migration impacting site performance:
- Migration runs as a background activity and doesn't compete with end-user traffic.
- SharePoint and OneDrive infrastructure has built-in throttling rules that project the reliability and availability of the system. To learn more about migration throughput and factors that affect migration speed, learn more at: [General migration performance guidance](./sharepoint-online-and-onedrive-migration-speed.md).

**Question:** Does Migration Manager do incremental migrations?

Answer: Yes. The jobs created in Migration Manager do perform incremental migrations.

**Question:** The date and time in Migration Manager isn't my local time. How can I change the setting to my local time zone?
Answer: Migration Manager uses the time zone setting in the SharePoint Admin center to convert to your time zone. To update the timezone of the SharePoint Admin Center, browse to `https://<your host url>-admin.sharepoint.com/_layouts/15/regionalsetng.aspx` to change the setting.

**Question:** What does **% complete** mean?

Answer: The % complete indicates the progress of the overall task migration, including the number of files migrated and the preparation work required for the remaining files to be migrated. *Note:* The **%** isn't linearly proportional to the number of files remaining to be migrated.

**Question:** What is the maximum file size that can be migrated?

Answer: For file share and cloud migrations, a file size of 250 GB is supported.

**Question**: How many task rows can I run at once when migrating content from a cloud provider?

Answer: At a maximum, only 50 task rows can run simultaneously. This total includes both scanning and migrating. This limit doesn't apply to file share migration.

**Question:** In the Migration Manager tool, is there a limit to the number of path characters you can enter?

Answer: Yes. When entering the **source path** into the text box, you're allowed a maximum of 255 characters. However, during migration the **file path** can be up to 32,767 characters in length. The path is limited to 400 characters after migration.
