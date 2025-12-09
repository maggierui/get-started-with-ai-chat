---
ms.date: 04/03/2025
title: "Migration Manager Google FAQs"
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
description: Migration Manager Google FAQs
---

# Frequently Asked Questions: Migration Manager Google

**Question: Are there any other tools available to migrate my Google accounts?**

Answer: Currently, Migration Manager is the tool to use to for migrating Google content.
</br> </br>

**Question: Is Migration Manager Google available for GCC, GCCHigh, DoD tenants?**

Answer: For the latest updates, refer to [specialty environments support](mm-specialty-environments-support.md).
</br> </br>

**Question: What gets transferred?**

Answer: All accessible files and folders within a Google user (Personal Drive or Shared Drive) are copied. Any items the user doesn't have permission to access are excluded from the migration.

As to the permissions, when [identities are fully mapped](mm-google-step5-map-identities.md), content is automatically reshared after migration, ensuring that each user retains access to their content exactly as before.
</br> </br>

**Question: Does Migration Manager sync files from Google after first migration?**

Answer: After you complete a migration task for the first time, triggering the **Migrate** button again initiates a delta sync (incremental migration run). During this process, by default the destination directory is compared to the source, and only new or modified files are transferred. Here are a few examples of how we deal with changes to files and folders:

- **Content changes**: If you edit a document in your source or you add a few new files, we copy them to your destination on the next incremental run, overwriting the previously existing files in the destination.
- **Name changes**: If the name of a file or folder changes in Office 365, we treat it as a brand new object. This change can lead to duplicate files being migrated to Office 365, or entire folders worth of data could be duplicated from the changed folder down.
  - **Example**: Changing the path **/Sales/Clients** to **/Global Sales/Clients** results in two copies of your **Sales** folder after the **Global Sales** folder is also copied during an incremental pass.

Learn more about how to change the file transfer behavior during a [delta sync](mm-delta-sync.md).
</br> </br>

**Question: Does Migration Manager delete my files?**

Answer: No. We never delete your data from any source. We take your data from one place and copy it to another; akin to *copy and paste* rather than *cut and paste*. We also don't retain any of your cloud storage data for any reason.
</br> </br>

**Question: Can I rearrange content during a migration?**

Answer: Not recommended. Any major changes in directory structure should happen before or after your migration. It's also not a good idea to use our app to rearrange content. The risks that come with rearranging content during the migration are primarily in the form of data duplication; our incremental process sees all changes as new data. So, for example, if you change a folder name at the root, we detect that as a new folder, and all of the contents is retransferred, including all subfolders. When sharing permissions are transferred, both owners and collaborators receive duplicate data if content is rearranged or renamed.
</br> </br>

**Question: What happens to external sharing links?**

Answer: We don't recreate external sharing links. After migration, the links have to be set in the destination manually.
</br> </br>

**Question: What about external collaborators?**

Answer: We don't share content with external collaborators. This policy is in place to protect your organization, and industry best practice is to never automatically share sensitive internal data with guests.
</br> </br>

**Question: Does Migration Manager preserve file versions?**

Answer: Migration Manager now supports migrating version histories along with each of the files.[Learn more about version migration](file-versions.md).
</br> </br>

**Question: Does Migration Manager automatically notify users?**

Answer:  Migration Manager allows you to customize email notifications to track your migration progress. [Learn more about email notification](mail-notification.md).
</br> </br>

**Question: Does Migration Manager transfer permissions for shared drives?**

Answer: Yes. To correctly migrate the Google Shared Drive permissions, we recommend you do the following before starting the Shared Drive migration:
- Recreate a Microsoft 365 group that has the same memberships as the Google Drive group. You can either create a new group, or edit the group linked to the Team site you designate as the migration destination of the Google Shared Drive.
- In the [Map identities](mm-google-step5-map-identities.md) setting, map the original Google Drive group of the shared Drive to the Microsoft 365 group recreated in the previous step.
</br> </br>

**Question: What can't Migration Manager migrate from Google?**

Answer: Google doesn't allow us to export sites and maps from Google Drive. [Learn more about what isn't migrated](/sharepointmigration/mm-unsupported-files).
</br> </br>

**Question: Does Migration Manager migrate Google Forms?**

Answer: Yes. Migration Manager now migrates Google Forms. Forms destinations are required to make it work. [Learn more about Forms destination editing](/sharepointmigration/mm-google-step4-review-destinations).
</br> </br>

**Question: Does Google calculate the size of their proprietary files?**

Answer: Google only started calculating the size of its proprietary files, including Google Docs, Sheets, Forms, and Slides, on May 2, 2022. Any Google proprietary files created and modified **before** May 2, 2022 don't include file size in the metadata info we get from the API calls. As a result, all Google proprietary files created before May 2, 2022 default to a scanned size of 1 byte and are reported as such in our *ScanSummary report*.
</br> </br>

**Question: What happens to the files with the same name in the same folder after they are migrated to Microsoft 365?**

Answer: Files with the same name are renamed with suffixes (1), (2), and so on.
</br> </br>

**Question: Does Migration Manager support migrating two Google Drives with the same name?**

Answer: No, it doesn't. Only the first discovered Drive is migrated.
</br> </br>

**Question: Can I migrate Drives with "/" in their names?** </br>

Answer:  No, Google Drive with "/" in its name isn't supported. The **Source location** field in either the scan list or migration list shouldn't include "/", even if you configured invalid character replacement in the Project settings.
</br> </br>

**Question: Why I can’t see some of my SharePoint sites while assigning destinations on the UI?**

Answer: If SharePoint or Teams sites in your tenant aren't visible in the UI while assigning destinations, there could be a few reasons for this lack of visibility:
- SharePoint admins only see sites where they're at least a member, as sites are searched using a user-scoped delegated token.
- Admins might not see sites for a multi-geo tenant due to limitations in the graph API.
- Sites that are recently created might take a couple of hours to sync and appear in the UI.
- SharePoint site search in the UI might not work in some special cases (for example, when there are special characters in the destination path).

If you can't locate a destination in the "Edit destination" panel, [upload the destination using a CSV file](/sharepointmigration/mm-google-step4-review-destinations#upload-destinations-using-a-csv-file).
</br> </br>


**Question: Why am I receiving the "MEXPORTFILERESTRICTED" failure code in Migration detailed report when attempting to migrate a specific file?**

Answer: This error typically occurs due to incorrect settings in Google. To resolve it, ensure the following configurations are enabled:

Overall setting in Google Admin Console:
1. Go to Google Admin Console.
2. Select Apps -> Google Workspace -> Settings for Drive and Docs -> Features and Applications.
3. Enable the following settings by selecting the checkboxes:
   - **Allow users to create and upload any file**
   - **Allow users to create new Docs, Sheets, Slides, Drawings, Forms and Vids files**

File level setting in Google Drive:
1. Navigate to the **Share** panel for the file in Google Drive.
1. Click on the **Settings Icon** located at the top right corner.
1. Select the checkbox for the setting **Viewers and commenters can see the option to download, print, and copy**.

</br> </br>

**Question: Why am I receiving the "MAUTHACCESSTOKENINVALID" or "MAUTHREFRESHTOKEN" failure code in Migration detailed report when attempting to migrate a specific file?**

Answer: This failure occurs when the "Drive and Docs" service status isn't set to "On for everyone". To resolve the issue, go to the Google Admin Console, select Apps -> Google Workspace -> Service Status, and change the service status of "Drive and Docs" to **ON for everyone**.

</br> </br>

