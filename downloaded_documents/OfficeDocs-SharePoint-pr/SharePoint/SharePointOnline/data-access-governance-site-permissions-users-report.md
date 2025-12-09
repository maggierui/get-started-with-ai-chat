---
ms.date: 11/16/2025
title: "Data access governance reports - get site permission report for given users"
ms.reviewer: pullabhk
ms.author: ruihu
author: maggierui
manager: dansimp
recommendations: true
audience: Admin
customer_intent: As a SharePoint administrator, I want to determine which sites are accessible by the given user and determine the extent of their access so that I can take necessary actions to modify permissions for sensitive content.
f1.keywords: NOCSH
ms.topic: how-to
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- Highpri
- Tier2
- M365-sam
- M365-collaboration
- trust-pod
ms.custom:
- admindeeplinkSPO
search.appverid: 
description: "In this article, you learn how to get a snapshot report to view the list of sites accessible by a given user."
---

# Discover sites accessible by a given user with the snapshot report

Site permissions for users report is one of the [Data access governance snapshot reports](/sharepoint/data-access-governance-reports#what-are-snapshot-reports) available with [SharePoint Advanced Management](advanced-management.md). This report lists all sites a user can access and allows admins to determine whether they can access the entire site or specific sections, granted directly to the user or indirectly through groups. This approach helps you quickly assess your overall security posture and identify sites that need immediate attention.

## What does the site permissions for users report show me?
 
The site permissions for users report captures the permission state of given user(s) at a specific point in time, giving you a complete overview of sites accessible to these users along with the extent of access. You can determine whether the entire site is shared with the user or only few files/items are shared. For the complete list of metrics captured in the report, see the [Download the site permissions for users](#download-the-site-permissions-for-users-report) section below.
 
## When to use the site permissions for users report?
 
You can use the report when you would like to review permissions for users before assigning them a Copilot license or if you want to clean up permissions when the user is about to leave the organization or changed departments.


## Run the site permissions for users report

> [!IMPORTANT]
> Review these important details before creating your first report:
>
> - Make sure that the site permissions for your organization report is generated at least once.
> - Reports capture data from up to 48 hours before generation
> - Maximum of 5 reports are allowed
> - You can run reports again every 30 days

Here's how to run the site permissions for users report:

1. From the Data access governance landing page, select **View reports** under **Site permissions for users**.
2. Select **Create report** to generate your report.
3. Select **Add users to report** to select the users for whom you want to generate the report. Select **Save** to save the selections. You can also edit the selection and remove users or add new users, if required.
4. Specify the **Scope** - either SharePoint or OneDrive.
5. Provide the **Report name** - a unique name to identify this report.
6. Select **Create and run** to trigger the creation of report.
7. Check the **Status** column to see if a report is ready or when it was last updated.

### How to view the site permissions for users report?

1. From the Data access governance landing page, select **View reports** under **Site permissions for users**.
2. View all the available reports and their corresponding status, the list of users for whom report is generated, how many sites are present in the report and a button to download the entire report.
3. Select the relevant **Report name**
4. You can view all the users as a list to the left. The right side shows the list of sites accessible to the selected user. The right side also displays whether the user can access the entire site or has access to few specific items directly or indirectly.

:::image type="content" source="media/data-access-governance/user-permission-report.png" alt-text="Report to list all sites accessible to the selected user":::

## Download the site permissions for users report

There are three ways to download the report for a given user or for all users for whom the report was generated

1. Select **Download report for** the selected user option to download the report as a CSV file. The file has a limit of 1 million sites.
2. Select **Download detailed report** to get CSV files for all the users given as input, as a Zip file.
3. On the previous page where all the reports are listed, select **Download report** to get CSV files for all the users given as input, as a Zip file.

The downloaded report contains the following information:

|Column  |Description  |
|---------|---------|
|TenantID     |   GUID identifying the organization     |
|Site ID     |  GUID identifying the organization       |
|Site Name     |   Name of the site      |
|Site URL     |  URL of the site       |
|Site Template     |   Specifies the type of site. Has values such as Communication site, Team site, Team site (no Microsoft 365 Groups), Other sites     |
|Primary admin     |    Site administrator marked as Primary in Active sites page     |
|Primary admin email     |    Email of primary site administrator     |
|ExternalSharing |  Specifies whether content can be shared with external guests. Yes or No.    |
|Site Privacy |   Applicable in Microsoft 365 connected team sites. Specifies the privacy setting of the group. Has values Public or Private   |
|Site Sensitivity |   Specifies the sensitivity label applied to the site   |
|Files |  Approximate number of all files in the site |
|Is site shared  |  Specifies if the user is part of one or more SharePoint groups with site-level access. Yes or No. |
|Items with direct access count |   Number of files or folders shared directly with the user   |
|Items with indirect access count |   Number of files or folders the user can access by being part of a group.   |
|Microsoft Entra object ID |   GUID identifying the user in Microsoft Entra   |
|User principle name |   Unique name identifying the user in Microsoft Entra  |
|Display name |   Name as displayed in people selection/search related experiences  |
|Report Date |  Time of generation of report. It might take up to 48 hours to reflect any changes in the report    |