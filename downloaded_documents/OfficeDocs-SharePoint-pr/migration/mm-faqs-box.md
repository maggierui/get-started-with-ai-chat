---
ms.date: 04/03/2025
title: "Migration Manager Box FAQs"
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
search.appverid: MET150
description: Migration Manager Box FAQs
---

# Frequently Asked Questions: Migration Manager Box

**Question: What gets transferred?**

Answer: All accessible files and folders within a Box user are copied. Any items the user doesn't have permission to access are excluded from the migration.

**Question: What happens to Box Notes?**

Answer: Box Notes are converted during migration to a .docx format.

**Question: Is Migration Manager Box available for GCC, GCCHigh, DoD tenants?**

Answer:  For the latest updates, refer to [specialty environments support](mm-specialty-environments-support.md).

**Question: Does Migration Manager Box sync files?**

Answer: There's a source-to-destination delta for files. When you run a transfer, we compare the destination directory to the source, and only transfer new or modified files over. We call this functionality our incremental feature. We compare the timestamps of the files in both the source and destination and transfer the newest versions only. The incremental feature is always on. Here are a few examples of how we deal with changes to files and folders.

- **Content changes**: If you edit a document in your source or you add a few new files, we copy them to your destination on the next incremental run, overwriting the previously existing files in the destination.
- **Name changes**: If the name of a file or folder changes in Office 365, we treat it as a brand new object. This circumstance can lead to duplicate files being migrated to Office 365, or worse in that entire folders worth of data would be duplicated from the changed folder downwards.
- **Example**: Changing the path `/Sales/Clients` to `/Global Sales/Clients` results in two copies of your `Sales` folder after the `Global Sales` folder is also copied during an incremental pass.

**Question: Does Migration Manager delete my files?**

Answer: No. We never delete your data from any source. We take your data from one place and copy it to another; akin to *copy and paste* rather than *cut and paste*. We also don't retain any of your cloud storage data for any reasons.

**Question: Can I rearrange content during a migration?**

Answer: It isn't recommended. Any major changes in directory structure should happen before or after your migration. It's also not a good idea to use our app to rearrange content. The risks that come with rearranging content during the migration are primarily in the form of data duplication; our incremental process sees all changes as new data. So, for example, if you change a folder name at the root, we detect that as a new folder, and all of the contents is retransferred, including all subfolders. When sharing permissions are transferred, both owners and collaborators receive duplicate data if content is rearranged or renamed.

**Question: What happens to external sharing links?**

Answer: We don't recreate external sharing links. After migration, these links have to be set in the destination manually.

**Question: What about external collaborators?**

Answer: We don't share content with external collaborators. This policy is in place to protect your organization, and industry best practice is to never automatically share sensitive internal data with external collaborators.

**Question: Does Migration Manager preserve file versions?**

Answer: No. During a migration, only the most recent version of a file is transferred.

**Question: Does Migration Manager automatically notify users?**

Answer: No. We automatically suppress all emails to users so they aren't bombarded with excessive notifications about the data they now have access to.

**Question: Why I can’t see some of my SharePoint sites while assigning destinations on the user interface (UI(?**

Answer: If SharePoint or Teams sites in your tenant aren't visible in the UI while assigning destinations, there could be a few reasons for this lack of visibility:
- SharePoint admins only see sites where they are at least a member, as sites are searched using a user-scoped delegated token.
- Admins might not see sites for a multi-geo tenant due to limitations in the graph API.
- Sites that are recently created might take a couple of hours to sync and appear in the UI.
- SharePoint site search in the UI might not work in some special cases (for example, when there are special characters in the destination path).
