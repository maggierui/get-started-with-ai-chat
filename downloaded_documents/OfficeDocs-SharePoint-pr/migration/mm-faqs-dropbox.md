---
ms.date: 04/04/2025
title: "Migration Manager Dropbox FAQs"
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
description: Migration Manager Dropbox FAQs
---

# Frequently Asked Questions: Migration Manager Dropbox

**Question: Is Migration Manager Dropbox available for GCC, GCCHigh, DoD tenants?**

Answer: For the latest updates, refer to [specialty environments support](mm-specialty-environments-support.md).
</br> </br>

**Question: What gets transferred?**

Answer: All accessible files and folders within a Dropbox user (Member folder or Team folder) are copied. Any items the user doesn't have permission to access are excluded from the migration.

As to the permissions, when [identities are fully mapped](mm-dropbox-step5-map-identities.md), content will be automatically reshared after migration, ensuring that each user retains access to their content exactly as before.
</br> </br>

**Question: Does Migration Manager sync files from Dropbox after first migration?**

Answer: After you complete a migration task for the first time, triggering the **Migrate** button again will initiate a delta sync (incremental migration run). During this process, by default the destination directory is compared to the source, and only new or modified files are transferred. Here are a few examples of how we deal with changes to files and folders.

- **Content changes**: If you edit a document in your source or you add a few new files, we copy them to your destination during the next incremental run, replacing the previous versions. If new files are added in the source, they're also migrated in the next incremental run.
- **Name changes**: If the name of a file or folder changes in Office 365, we treat it as a brand new object. This change can lead to duplicate files being migrated to Office 365, or worse in that entire folders worth of data would be duplicated from the changed folder downwards.
- **Example**: Changing the path `/Sales/Clients` to `/Global Sales/Clients` results in two copies of your `Sales` folder after the `Global Sales` folder is also copied during an incremental pass.

Learn more about how to change the file transfer behavior during a [delta sync](mm-delta-sync.md).
</br> </br>

**Question: Can I rearrange content during a migration?**

Answer: Not recommended. Any major changes in directory structure should happen before or after your migration. It's also not a good idea to use our app to rearrange content. The risks that come with rearranging content during the migration are primarily in the form of data duplication; our incremental process sees all changes as new data. So, for example, if you change a folder name at the root, we detect that as a new folder, and all of the contents is retransferred, including all subfolders. When sharing permissions are transferred, both owners and collaborators receive duplicate data if content is rearranged or renamed.
</br> </br>

**Question: What happens to external sharing links?**

Answer: We don't recreate external sharing links. After migration, the links have to be set in the destination manually.
</br> </br>

**Question: What about external collaborators?**

Answer: We don't share content with external collaborators. This policy is in place to protect your organization, and industry best practice is to never automatically share sensitive internal data with external collaborators.
</br> </br>

**Question: Does Migration Manager preserve file versions?**

Answer: No. During a Dropbox migration, only the most recent version of a file is transferred.
</br> </br>

**Question: Does Migration Manager automatically notify users?**

Answer:  Migration Manager allows you to customize email notifications to track your migration progress. [Learn more about email notification](mail-notification.md).
</br> </br>

**Question: Why I can’t see some of my SharePoint sites while assigning destinations on the UI?**

Answer: If SharePoint or Teams sites in your tenant aren't visible on the UI while assigning destinations, there could be a few reasons:
- SharePoint admins only see sites where they are at least a member, as sites are searched using a user-scoped delegated token.
- Admins might not see sites for a multi-geo tenant due to limitations in the graph API.
- Sites that are recently created might take a couple of hours to sync and appear in the UI.
- SharePoint site search in the UI might not work in some special cases (for example, when there are special characters in the destination path).

If you can't locate a destination in the "Edit destination" panel, [upload the destination using a CSV file](/sharepointmigration/mm-dropbox-step4-review-destinations#upload-destinations-using-a-csv-file).
</br> </br>
