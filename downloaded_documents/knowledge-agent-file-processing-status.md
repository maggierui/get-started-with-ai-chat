---
ms.date: 09/18/2025
ms.update-cycle: 180-days
title: Monitor file processing status
ms.reviewer: ssquires
ms.author: chucked
author: chuckedmonson
manager: jtremper
recommendations: 
audience: Admin
f1.keywords:
- NOCSH
ROBOTS: 
ms.topic: how-to
ms.service: sharepoint-online
ms.collection: 
- M365-collaboration
- m365copilot
ms.localizationpriority: medium
search.appverid:
- MET150
description: Learn how to monitor the processing status of files in a SharePoint document library.
---

# Monitor file processing status

> [!NOTE]
> This article applies to the preview version of Knowledge Agent in SharePoint.

You can monitor real-time updates on files processed in a SharePoint library. This feature lets you:

- See when a file is being processed.
- Check the status of the file: **In progress**, **Completed**, or **Failed**.
- Understand what worked, what didn’t, and why.

You can view the processing status for a [file that is being processed](#monitor-the-status-of-a-file-being-processed), for a [selected file](#monitor-the-status-of-any-file) or for [all files](#monitor-the-status-of-all-files) in a document library.

<!---
> [!NOTE]
> For autofill, the **Status** column is hidden by default in the document library view. If you don’t see it, you can unhide it by customizing the library view.
--->

## Prerequisites

To use this feature, you need:

- [Microsoft 365 Copilot license](/copilot/microsoft-365/microsoft-365-copilot-licensing)

- [Knowledge Agent (preview) enabled](knowledge-agent-get-started.md)

## Monitor the status of a file being processed

When you submit an on-demand request to process a file:

1. A message bar appears at the top of the library, indicating the action is in progress.

2. On the right side of the message bar, select **View status** to open the activity panel.

3. The [activity panel](#view-the-activity-panel) shows the current action being processed.

<!---
## Monitor the status of a file being processed

When you submit an on-demand request for autofill or translation:

1. A message bar appears at the top of the library, indicating the action is in progress.

    - For autofill:

        ![Screenshot of the message bar showing that the action is in progress for autofill.](../media/content-understanding/processing-status-message-bar-columns.png)

    - For translation:

        ![Screenshot of the message bar showing that the action is in progress for translation.](../media/content-understanding/processing-status-message-bar-translation.png)

2. On the right side of the message bar:

    - For autofill: Select **View autofill status** to open the **Autofill activity** panel.

    - For translation: Select **View translation status** to open the **Translation activity** panel.

3. The [activity panel](#view-the-activity-panel) shows the current action being processed.

4. The message bar disappears once the request is completed or failed.
--->

## Monitor the status of any file

To view the processing status of one or more files:

1. In a SharePoint document library, select the file or files.

2. From the **More options** (**...**) menu either next to the file name or on the command bar, select the service, and then select **View recent activity**.

3. The [activity panel](#view-the-activity-panel) shows the current action being processed.

<!---
## Monitor the status of any file

To view the processing status of one or more files:

1. In a SharePoint document library, select the file or files.

    > [!NOTE]
    > If no files or more than 30 files are selected, the activity panel shows the status for the entire library.

2. From the **More options** (**...**) menu either next to the file name or on the command bar:

    - For autofill: Select **Autofill columns** > **View recent activity**.

        ![Screenshot of the More options menu showing Autofill columns and View recent activity.](../media/content-understanding/processing-status-view-recent-activity-columns.png)

    - For translation: Select **Translate** > **View recent activity**.

        ![Screenshot of the More options menu showing Translate and View recent activity.](../media/content-understanding/processing-status-view-recent-activity-translation.png)

3. Depending on the service you selected, the corresponding [activity panel](#view-the-activity-panel) opens.
--->

## Monitor the status of all files

To view the processing status of all files in the library:

1. In a SharePoint document library, on the command bar, select **More options** (**...**), select the service, and then select  **View recent activity**.

2. The [activity panel](#view-the-activity-panel) shows the current actions being processed.

<!---
## Monitor the status of all files

To view the processing status of all files in the library:

1. In a SharePoint document library, on the command bar:

    - For autofill: Select **More options** (**...**) > **Autofill columns** > **View recent activity**.

    - For translation: Select **Translate** > **View recent activity**.

2. Depending on the service you selected, the corresponding [activity panel](#view-the-activity-panel) opens.
--->

## View the activity panel

The activity panel displays a list of file processing events, including:

- File name
- Summary of the action that was performed, or information about why it failed
- Processing status: **In progress**, **Completed**, or **Failed**
- Date and time of the event

> [!NOTE]
> If no files or more than 30 files are selected, the activity pane displays the processing status for the entire library, rather than for individual files.

<!---
## View the activity panel

The activity panel displays a list of file processing events, including:

- File name
- Summary of the action that was performed, or information about why it failed
- Processing status: **In progress**, **Completed**, or **Failed**
- Date and time of the event

    ![Screenshot of the activity panel in a SharePoint library.](../media/content-understanding/processing-status-activity-panel-columns.png)

> [!NOTE]
> If no files or more than 30 files are selected, the activity pane displays the processing status for the entire library, rather than for individual files.
--->

### Filter activity options

By default, the panel shows activity for the last 60 days.

- To filter by date: **Filter** > **Date range**

- To show only failed files: **Filter** > **Failed status**

### Status definitions

| Status       | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| In&nbsp;progress  | The service has started processing the file. A timestamp is displayed.           |
| Completed    | The service has finished processing successfully. A description of the completed actions is provided. |
| Failed       | The service has encountered an error. A description of the cause of the failure is provided. |
