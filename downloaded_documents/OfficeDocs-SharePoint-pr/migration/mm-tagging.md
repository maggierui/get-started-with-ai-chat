---
ms.date: 04/04/2025
title: "Importing tags with Migration Manager"
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
- M365-collaboration
- SPMigration
- m365initiative-migratetom365
ms.custom: admindeeplinkSPO
search.appverid: MET150
description: "Importing tags with Migration Manager"
---

# Importing and using tags with Microsoft Manager

Use tags to better organize, plan, and schedule your content migrations in Migration Manager. Tags let you filter tasks and easily navigate through a large quantity of sources and users to find what you need.

If you have a large migration project, you likely migrate the content in phases or need to identify them by groupings. Apply tags to indicate department, region, wave, or any other collection relevant to your organization. With tags, you can filter, group, and keep organized.
 
Tags can be updated anytime during your project. If you scan a group of sources and they're ready to migrate, you can apply new tags to identify their status quickly. Or if a group of tasks need to be run again, you may tag them with "Incremental run" to make that group stand out.

## Using and managing tags

While you can create as many tags as you wish, we strongly recommend limiting the number of tags you use to simplify your projects. Making tags like "Ready for migration" or "Incremental run" reusable is one way of limiting the number of tags you use.

You can enter one or more tags per source, separating them with a semi-colon in the CSV file. Keep in mind that tags are case-sensitive and filter on an exact string match. Tags are part of the metadata associated with the content and are preserved even after you copy tasks to the migration tab. The Summary reports and scans also include tags.

### Examples of tags

As you plan your overall migration project, plan your tag strategy to align with it.

|Category      |Tag examples                                 |Importance                                              |
|:-------------|:--------------------------------------------|:-------------------------------------------------------|
|Business unit |Sales, Finance                               |Helpful if you're migrating by division or department   |
|Phase         |Wave 1, Wave 2, Pilot                        |Manage by phases                                        |
|Extra work    |Incremental run                              |Tag a batch to be run again                             |
|Readiness     |Ready to migrate                             |Quickly view if the task is ready to copy to migrations |
|Regional      |German Data Center, Oslo division, Australia |Group by geography                                      |

>[!Note]
>Only tags can be updated using this CSV file. The ID, source name, and source path are included for reference only.

## Import and update tags

1. In the SharePoint admin center, select [Migration center](https://go.microsoft.com/fwlink/?linkid=2185075).
2. Select and connect to your migration source. Your sources are automatically scanned.
3. Highlight one or more tasks, and then select **Import tags** from the menu bar.

![Import tags option on the menu bar.](media/mm-tagging.png)

4. Select **Download current source paths**. The downloaded CSV file contains the Task ID, Source Name, Source Path, and Tags. If no tags were associated with the source, the value is blank.
5. Enter the name of the tag associated with each source. If you want to apply more than one tag to a single source, separate the values using a semi-colon. Save the revised file.
6. Browse for the updated CSV file and then select **Apply**.

![Import tags entering CSV file name.](media/mm-import-tag-csv.png)

7. View the tags on the scan list and filter as needed.

![Results from import tags.](media/mm-import-tag-results.png)

> [!NOTE]
> For file share migration, the import tag limit is set at 1,000 tasks. If you need to apply tags to more than 1,000 tasks, you must divide them into multiple CSV files, each containing fewer than 1,000 tasks. Proceed to apply these files sequentially.
