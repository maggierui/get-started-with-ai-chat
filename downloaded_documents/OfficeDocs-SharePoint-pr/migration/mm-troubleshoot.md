---
ms.date: 04/02/2024
title: "Troubleshooting Migration Manager"
ms.reviewer:
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting-general
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection:
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
ms.custom: admindeeplinkSPO
description: "Troubleshoot common errors in Migration Manager."
---

# Troubleshoot Migration Manager file migrations

This article describes how to resolve issues and errors you may experience when using Migration Manager for file share migration.

- [Prerequisites and settings](#check-prerequisites-and-settings)
- [Agent error messages](#agent-error-messages)
- [Destination site URL issues](#destination-site-url-issues)
- [Common error messages](#frequently-seen-error-messages)
- [Agent installation failure](#agent-installation-failure)
- [Agent disconnected](#agent-disconnected)
- [Task stuck in "Queued" state](#task-stuck-in-queued-status)
- [A Task report can't be downloaded](#a-task-report-cant-be-downloaded)
- [Migration errors in task reports](#migration-errors-in-task-reports)
- [Google migration error reports contain HTML](#google-error-report-shows-html-code-in-report)
- [Error codes](#error-codes)
- [Geo admins can't access full functionality of Migration Manager](#geo-admins-not-supported)
- [Group-inherited SharePoint admins can't access the full functionality of Migration Manager](#group-inherited-sharepoint-admins-unable-to-access-the-scans-and-migrations-tabs)
- [The site collection "XXXX" can't be created or updated](#the-site-collection-xxxx-cant-be-created-or-updated)
- [Scan task stuck in "queued" status](#scan-task-stuck-in-queued-status)

## Check prerequisites and settings

Make sure you meet the prerequisites for agent installation, and review the required endpoints. Government cloud customers should confirm the configuration is set correctly.

- [Agent installation prerequisites](mm-prerequisites.md).
- [Required endpoints](mm-prerequisites.md#required-endpoints).
- [Government cloud settings](mm-gov-cloud.md).
- [Pre-provision OneDrive accounts](/onedrive/pre-provision-accounts) If you're migrating to OneDrive accounts, make sure the accounts are provisioned before you migrate. You can do this using a script, as shown here: [Pre-provision OneDrive for users in your organization](/onedrive/pre-provision-accounts).

## Agent error messages

|Message |Action |
|--------|-------|
|*Migration agent couldn't be installed. Close setup and try again.* |You may be using an out-of-date version of the agent setup file to install the agent. For more information, see the [Agent installation failure](#agent-installation-failure) section. |
|*Current user doesn't have access to source file share* |Make sure the source file share is a network file share. Verify that the Windows account associated with the agent has **Read** permissions to the file share you want to migrate. |
|*The source file share doesn't exist* |Make sure the source file share is an existing network file share. Confirm that the Windows account associated with the agent has **Read** permissions to the file share you want to migrate. |

## Destination site URL issues

|Message                                |Recommended action |
|---------------------------------------|-------------------|
|Destination site or web doesn't exist  |Confirm the destination site or subsite exists. If it's a OneDrive account, make sure that it's been pre-provisioned. |
|Failed to check site or web existence. |Confirm the destination site or subsite exists. |

## Frequently seen error messages

|Message |Recommended action |
|--------|-------------------|
|*Invalid source folder* |Confirm the path you entered is correct and follows the proper format. </br>Confirm you have **Read** access to the folder. |
|*The site can't be created or updated* |Make sure that you have permissions to create the site and that the URL is valid. </br>If the site exists, confirm you're the site collection administrator. </br>If it still fails, create the site manually and point the migration tool to this newly created site.|
|*Scan file failure: The folder name is invalid* |See [Invalid file names and file types in OneDrive and SharePoint](https://support.office.com/article/64883a5d-228e-48f5-b3d2-eb39e07630fa). |
|*Scan file failure: Target path is too long* |See [Invalid file names and file types in OneDrive and SharePoint](https://support.office.com/article/64883a5d-228e-48f5-b3d2-eb39e07630fa). </br>The entire path, including the file name, must contain fewer than 400 characters for OneDrive and SharePoint. |
|*Scan File Failure: Not enough disk space to pack the file* |The disk space available for the migration working folder is too small for the size of your source file. Enlarge your size of your working folder and try again. |
|*Packaging failure: Can't open file* |Packaging failed due to a nonexistent source. Check if you can access the source root folder. |
|*A duplicate task has already been created.* |The CSV file used to do bulk migration can't have duplicate entries. Remove the duplicate line or lines and try again. |
|*The parent folder wasn't migrated* |The parent folder wasn't migrated, therefore all items under the folder fail to migrate. Check your parent folder and retry your migration. |

## Agent installation failure

**Issue:** The migration agent fails to install when using an old version of agent setup file to install agent.

![Screen agent installation failure](media/mm-agent-install-failure-old-setup.png)

**Diagnosis / Investigation**:

An outdated *clientsetup.exe* file could cause this problem.

**Mitigation**:

1. Go to the [Migration center](https://go.microsoft.com/fwlink/?linkid=2185075) in the SharePoint admin center, and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.
2. Select **Download agent setup file**.
3. Run the *clientsetup.exe* file on the computer or virtual machine you want to install the agent on. Follow the instructions to complete the agent installation.

**Issue:** The migration agent doesn't install successfully, or the clientsetup.exe can't be opened.

Example:

![Migration Manager agent installation failure screenshot.](media/mm-agent-installation-failure.png)

**Diagnosis / Investigation**:

If the *clientsetup.exe* can't be opened:

- Sign in to Windows as Administrator, or provide the Administrator username and password upon opening the application. The Administrator account should already be added to the domain.

If errors occurred during installation process:

- The error message should already include the failure reason, and the appropriate actions to take if possible.
- If errors don't suggest actions to resolve, temporary network failure could cause this problem, or other unknown issues.

**Mitigation**:

If the clientsetup.exe can't be opened:

1. Sign in to Windows as Administrator.
2. Reopen the clientsetup.exe application, or provide the Administrator username and password upon opening the application.

If errors occurred during the installation process:

- For errors with specific stated actions, take the corresponding action and then reopen the clientsetup.exe.
- For other nonspecific errors, make sure your Administrator account is added to the domain. Close the application window and then retry installation.

## Agent disconnected

**Issue**: The state of the agent displays "Disconnected" and never changes.

![Agent disconnected](media/mm-agent-disconnect-ts.png)

**Diagnosis / Investigation**:

- Check the network health on the computer on which the agent is installed.
- If the password of the logged-in Tenant Administrator account is changed, or any other similar, critical changes are applied to the Tenant Admin account that would require you to sign in again, all of the agents are disconnected. Reinstallation is required on all of them.
- If the agent failed to autoupgrade, the version is likely too old. Reinstall the agent.
- Token expiration can also cause the agent to disconnect.

**Mitigation**:

- If there's a network issue, fix that. The agent should reconnect soon after.
- If there are critical changes to the Tenant Admin account that require you to sign in again: Reinstall the agent on all the computers.
- If neither of these options applies, start by reinstalling the agent first.

## Task stuck in "Queued" status

**Issue**: The status of a task stays at "Queued" and never gets scheduled on an agent to run.

![Task stuck in Queued status.](media/mm-task-stuck-in-queued-status.png)

**Diagnosis / Investigation**:

- Make sure there are agents installed for this tenant. They should be listed in the Agents list.
- Check the state of each agent. They should be set to "Enabled".
- A status of "In use" indicates the agent is already processing another task. The agent isn't able to be assigned more tasks without finishing the current one.
- If an agent is listed as "Disabled", enable it.
- If they appear to be "Disconnected" for a long time, check Agent Disconnected.

**Mitigation**:

- If there are available, *enabled agents* in the list, but the tasks haven't been scheduled for a long time: Create another task that is the same. Sometimes it fixes the problem.

## A Task Report can't be downloaded

**Issue**: The Task report can't be downloaded from the link on the task details panel.

- The Download task report link is disabled.
- The Download task report link displays active, but nothing happens after clicking on it.

![Task report can't be downloaded screenshot.](media/mm-task-report-cant-download.png)

**Diagnosis / Investigation**:

- The link, "Download task report", is disabled until the task is finished. Reports are only available after the status of the task has a "Complete" or "Failed" status. Tasks that failed due to time-out also have a disabled task report link.
- If no reports can be downloaded for finished, non-timed-out tasks, most likely there are errors that occurred during the migration process which interrupted the uploading of the reports to SharePoint. However, they can be found locally as long as they exist.

**Mitigation**:

On the computer that completed the task, try to retrieve the reports.

- In folder **%AppData%\Microsoft\SPMigration\Logs\Migration\MigrationTool\[tenant_site]**, or **< Your-Customized-Working-Folder >\Migration\MigrationTool[tenant_site]**, sort the subfolders by their modified time. Find the subfolder whose modified time is the closest to the task's start time. If the task reports exist, it's in the "Report" folder within this subfolder.

Or

- If the task failed, navigate to the folder **%AppData%\Microsoft\SPMigration\Logs**, then sort the subfolders by their modified time. Find the subfolder whose modified time is the closest to the task's start time. The error report is in this subfolder.

## Migration errors in task reports

**Issue**: Migration tasks fail due to various reasons and are detailed in the task reports.

![Migration manager error](media/mm-migration-error-ts.png)

**Diagnosis / Investigation**:

- The failure reasons should already be written in detail to the reports along with suggested solutions.
- If you can't download the task reports, refer to [A Task Report Can't Be Downloaded](#a-task-report-cant-be-downloaded).

**Mitigation**:

Find the specific error here for more information: [Error codes](#error-codes).

If you receive an error similar to this one: *SUBMITTING FAILURE Failed to Submit the Job to Server: Unknown failed reason when submitting a job. 0x01610002*, check the settings on any antivirus application installed on the agent machine. Add our two migration applications as exceptions so that the migration traffic isn't interrupted:

- microsoft.sharepoint.migration.clientservice.exe
- microsoft.sharepoint.migration.mthost.exe

## Google error report shows HTML code in report

**Issue**: Error reports generated for a Google migration sometimes have an HTML code embedded in the report.

![Google error report includes HTML code.](media/mm-troubleshoot-google-error-report-html.png)

**Details**:

Google APIs return HTML errors that are included in the generated reports. This issue may happen when there's a Google server load error.

**Mitigation**:

Run less concurrent transactions.

**Status**:

This issue is a known issue. ETA not set.

## Geo admins not supported

Migration Manager currently doesn't support the Geo admin role for specific scenarios. For file share migrations, these users can't access the **Scans** tab. For cloud migrations, these users can't access the **Scans** tab or the **Migrations** tab.

**Workaround**. Assign the Geo user either a SharePoint admin or Global admin role.

> [!IMPORTANT]
> Microsoft recommends that you use roles with the fewest permissions, helping to improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

1. In the admin center, go to the **Users** > [Active users](https://go.microsoft.com/fwlink/p/?linkid=850628) page.
2. On the **Active users** page, select the user whose admin role you want to change. In the flyout pane, under **Roles**, select **Manage roles**.
3. Select the admin role that you want to assign to the user. If you don't see the role you're looking for, select **Show all** at the bottom of the list.

## Group inherited SharePoint admins unable to access the Scans and Migrations tabs

Migration Manager doesn't fully support SharePoint admin roles created as a result of joining an Azure group. For file share migrations, these users can't access the **Scans** tab. For cloud migrations, these users can't access the **Scans** tab or the **Migrations** tab.

**Workaround**. Assign the user either a SharePoint admin or Global admin role.

> [!IMPORTANT]
> Microsoft recommends that you use roles with the fewest permissions, helping to improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

1. In the admin center, go to the **Users** > [Active users](https://go.microsoft.com/fwlink/p/?linkid=850628) page.
2. On the **Active users** page, select the user whose admin role you want to change. In the flyout pane, under **Roles**, select **Manage roles**.
3. Select the admin role that you want to assign to the user. If you don't see the role you're looking for, select **Show all** at the bottom of the list.

## The site collection "XXXX" can't be created or updated

The User Principal Name (UPN) referenced is invalid. In order to create or update a OneDrive site collection, Microsoft Entra ID must contain the referenced UPN. Check your destination URL and validate that the user exists in Microsoft Entra ID.

## Scan task stuck in "queued" status

**Issue**: The status for a file share scan stays at "Queued" and never gets scheduled on an agent to run.

:::image type="content" source="media/mm-scan-task-issue-1.png" alt-text="Scan task issue stuck in queued phase.":::

**Diagnosis / Investigation**  

- Check the Agent group column for scan tasks. Only agents in the **Default** agent group can be scheduled.

:::image type="content" source="media/mm-scan-task-isssue-2.png" alt-text="Scan task issue troubleshooting.":::

**Mitigation**

- If there's no agents in the **Default** agent group, change the existing agent's group to **Default**. Any scan tasks that were stuck should now move out of this state.

 :::image type="content" source="media/mm-scan-task-issue-3.png" alt-text="Scan task issue edit agents.":::

## Error codes

|**Error Code**|**Recommended action**|
|:-------------|:---------------------|
|0x00000000 |Unexpected error. |
|0x01110001 |Unknown reason. |
|0x0111000B |Path is too long. |
|0x0111000F |The parent folder wasn't migrated. Check the failure report to determine the file and then try again. |
|0x01110003 |Can't access source folder. |
|0x01110009 |Cound not retrieve the file metadata. |
|0x01110010 |Invalid characters in the file name. Check report for files names with <>:"?*/\, |
|0x01110011 |The item "created time" or "modified time" isn't supported. |
|0x0201000D |Check if the list exists or if you can access it in the source site and target site. |
|0x02050008 |Unable to access your local storage. Restart your migration. |
|0x02010023 |Your source list template isn't supported. Try another. |
|0x0201000C |Check your credentials and then reenter your username and password. |
|0x02010017 |You must be a site collection admin. |
|0x02060009 |1 - The site collection can't be created because the URL is already in use or an invalid URL. |
||2 - The site collection can't be created because the URL contains invalid character. |
||3 - The site collection can't be created or updated. |
|0x02060007 |1 - The site collection can't be created because the URL is already in use or an invalid URL. |
||2 - The site collection can't be created because the URL contains invalid character. |
|0x02010018 |1 - Check your credentials and then try again. |
||2 - A problem occurred accessing SharePoint. Check your credentials and try again. |
||3 - A problem occurred accessing SharePoint. Check your credentials and your network connection and try again. |
||4 - A problem occurred accessing SharePoint. Check your credentials and your site URL for accuracy and try again. |
||5 - A problem occurred accessing SharePoint. Check your credentials and the format of your URL. Retry. |
||6 - A problem occurred accessing SharePoint. Check your credentials and try again. If the problem continues, create a support case. |
||7 - A problem occurred accessing SharePoint. Check your credentials and try opening your site in a browser. |
|0x0204000A |Can't create package file. All files and folders in the Migration Manager working folder, *%appdata%\Microsoft\SPMigration\Logs\Migration\MigrationToolStorage*, must be closed. Restart your migration. |
|0x02030001 |1 - Check your credentials. Restart your migration. |
||2 - Check your credentials. Restart your migration. |
||3 - Check your credentials and your network connection. Restart your migration. |
||4 - Check your credentials and your site URL. Restart your migration. |
||5 - Check your credentials and the format of your URL. Restart your migration. |
||6 - Check your credentials and restart your migration. If this problem continues, create a support case. |
||7 - Check your credentials and try opening your site in a browser. Restart your migration. |
|0x02010008 |Confirm the path and format of the user-mapping file and that you have permission to access it. |
|0x02050001 |All files and folders in the Migration Manager working folder, *%appdata%\Microsoft\SPMigration\Logs\Migration\MigrationToolStorage*, must be closed. Restart your migration. |
|0x02010002 |Check your network status. If you can access the source sites from a browser, then create a support case. |
|0x02010010 |Make sure the source list and target list have the same template. |
|0x0204000D |All files and folders in the Migration Manager working folder, *%appdata%\Microsoft\SPMigration\Logs\Migration\MigrationToolStorage*, must be closed during migration. Restart your migration. |
|0x02040012 |The temporary storage on your local computer is too low. Migration Manager caches the package on the working folder. Expand your temporary storage and retry. |
|0x02030003 |There are too many items with unique permissions. Simplify your permissions list by reducing the number of unique permissions. aRetry your migration. |
|0x02050001 |Local storage file is corrupted. The working folder was touched or modified during the migration. Retry your migration. |
|0x02080001 |The file in the package was changed or deleted while uploading. All files and folders in the Migration Manager working folder, *%appdata%\Microsoft\SPMigration\Logs\Migration\MigrationToolStorage*, must be closed. Restart your migration. |
|0x02040009 |The package can't be created because the directory can't be found. All files and folders in the Migration Manager working folder, *%appdata%\Microsoft\SPMigration\Logs\Migration\MigrationToolStorage*, must be closed. Restart your migration. |
|0x02010020 |Disable migrating version history in Migration Manager settings or enable versioning in SharePoint. |
|0x0201000E |Check if the global setting is filtering out special characters in the target path or if the path has unsupported characters. |
|0X0201000F |Invalid site URL. Check if the site URL is valid. Try to access the URL via a browser. If this account is a OneDrive account, make sure it's pre-provisioned before you migrate. |
|0x0207001 |You don't have access to the task folder. Check if you can access *%appdata%\Microsoft\SPMigration\Logs\Migration\MigrationToolStorage*. |
|0x01410010 |A failure occurred because of missing dependencies on list items. Check the FailureSummaryReport.csv for details. Check if the dependencies are included in your migration scope. |
|0x01510001 |Packages failed to upload. If you have a customized Azure storage, check if you can access the Azure storage and check if you can access the target site. Try migrating again. |
|0x01510001 |Failed to Upload the Job to Server: Upload file failed during migration. |
|0x02070009 |Several packages failed to upload. Pause the task and check your network connection. |
|0x01710009 |A failure occurred due to job end failures; some items failed in the package. Restart migration. |
|0x01710009 |Errors or time-out for Server Processing the file: Not all the items in the package were migrated. |
|0x01610001 |The Azure container is expired. Retry migration task. |
|0x01710006 |Errors or time-out for server processing the file: Job Fatal Error. |
|0x01710004 |Errors or time-out for server processing the file. Fail to look up folder name. The item may exist in other list or site in the same site collection. Or the item is in the recycle bin. |
|0x0131000F |Failed to Read the file. File is checked out. |
