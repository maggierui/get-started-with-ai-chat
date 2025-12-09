---
# Required metadata
# For more information, see https://learn.microsoft.com/en-us/help/platform/learn-editor-add-metadata
# For valid values of ms.service, ms.prod, and ms.topic, see https://learn.microsoft.com/en-us/help/platform/metadata-taxonomies

title:       User PowerShell to automate migration
description: PowerShell cmdlet is used to management migration manager tasks and download reports.
author:      zacsun-ms # GitHub alias
manager:     dapodean
ms.author:   zhaosu # Microsoft alias
ms.service:  microsoft-365-migration
# ms.prod:   # To use ms.prod, uncomment it and delete ms.service
ms.topic:    upgrade-and-migration-article
ms.date:     11/11/2025
---

# User PowerShell to automate migration

The PowerShell cmdlet is designed to manage file share migration tasks running in Migration Manager service, and download scan and migration reports.

Refer to this [link](/sharepointmigration/overview-spmt-ps-cmdlets) to make sure your computer meet the system requirements.

## Before you start

To start Migration Manager file share migration:

1. Install Migration Manager Agents, then connect them to the destination tenant with an admin account.
2. Sign into the SharePoint Admin Center as an admin and navigate to **Migration/File Share**.

 Download the PowerShell zip file [here](https://aka.ms/MMPowerShellModule), and unzip the build into a working folder

## Use the PowerShell cmdlet

__Launch PowerShell as Administrator__

Run the following commands:

`> Get-ChildItem -Path "working_folder" -Recurse | Unblock-File`

`> Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force`

__Close the first PowerShell window and launch PowerShell as Administrator__

Run the following commands:

`> Import-Module "working_folder\Microsoft.SharePoint.MigrationManager.PowerShell.dll"`

> [!NOTE]
> Provide an absolute file path in the Import-Module cmdlet.

### Connect to the Migration Manager service

`> Connect-MigrationService`

This cmdlet connects to the Migration Manager service. After a connection is established, you can add migration tasks and start migration.

### Add a migration task

`> Add-MigrationTask`

Use this cmdlet to create a new migration task. After creation, the task appears on the Migration Manager page.

The following parameters are required:

- __TaskName__: Specifies the name of the migration task.

- __SourceUri__: Defines the source file path.

- __TargetSiteUrl__: Indicates the destination SharePoint site URL.

- __TargetListName__: Specifies the name of the destination SharePoint list.

Optional parameters:

- __ScheduleStartTime__: Specifies the time the task starts to execute. By default, a task starts right after you add it.

- __AgentGroup:__ Assign an agent group to execute the task. By default, "Default" group is assigned.

- __Tags:__ Assign tags to the task. To assign more than one tag, semi-colon is used to separate the tag values.

Output message:

- "Migration task is created with task ID *taskId*" if the task is successfully added into the migration service.

- "Failed to add migration task. *errorMessage*" if the cmdlet errors out.

For a complete list of supported parameters, run: 

`> Get-Help Add-MigrationTask -Full`

### Get migration reports

`> Get-MigrationReport`

Use this cmdlet to retrieve reports of completed migration tasks based on the specified parameters:

- __OutputPath__: Specifies the directory path where the generated reports are saved.

- __StartTime__: Filters migration tasks that started after the specified date and time.

- __EndTime__: Filters migration tasks that started before the specified date and time.

- __TaskNameContains__: Filters migration tasks whose names contain the specified keyword.

- __Tags__: Filters migration tasks whose tag is same as the given parameter. If more than tags are given, separated by a semicolon (;), all tasks whose tag is same as one in the tags parameter should be returned.

- __Status__: Filters migration tasks whose status is same as the given parameter. Supported values are **Completed** and **Failed**. By default, reports of **Completed** and **Failed** tasks are downloaded.

If no parameters are specified, the cmdlet defaults to downloading all **Completed** and **Failed** reports.

Output message:

- "Report downloaded for task _taskeId_" for each task if the report zip file is downloaded. And the last message is a summary line "Migration reports downloading completed, check the output folder: _outputPath_"

- "Failed to download migration report. _errorMessage_" if the cmdlet errors out.

For a complete list of supported parameters, run:

`> Get-Help Get-MigrationReport -Full`

### Get scan reports

`> Get-ScanReport`

Use this cmdlet to retrieve reports of completed scan tasks based on the specified parameter
- __OutputPath__: Specifies the directory path where the generated reports are saved.

- __StartTime__: Filters migration tasks that started after the specified date and time.

- __EndTime__: Filters migration tasks that started before the specified date and time.

- __Tags__: Filters migration tasks whose tag is same as the given parameter. If more than tags are given, separated by a semicolon (;), all tasks whose tag is same as one in the tags parameter should be returned.

- __Status__: Filters migration tasks whose status is same as the given parameter. Supported values are **Ready**, **Warning**, and **Error**. By default, reports of **Ready to migrate**, **Warning**, and **Error** tasks are downloaded.

If no parameters are specified, the cmdlet defaults to downloading all **Ready to migrate**, **Warning**, and **Error** reports.

Output message:

- "Scan log downloaded for task _taskeid_" for each task if the report zip file is downloaded. And the last message is a summary line "Scan logs downloading completed,  check the output folder: _outputPath_".

- "Failed to download scan log. _error_message_" if the cmdlet errors out.

For a complete list of supported parameters, run:

`> Get-Help Get-ScanReport -Full`
