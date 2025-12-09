---
ms.date: 09/18/2025
ms.update-cycle: 180-days
title: Create views in a SharePoint document library
ms.reviewer: jseto
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
description: Learn how to use rules to create custom views in a SharePoint document library.
---

# Create views in a SharePoint document library

> [!NOTE]
> This article applies to the preview version of Knowledge Agent in SharePoint.

Knowledge Agent in SharePoint helps you create custom views of your document libraries to organize them. By showing and hiding columns, sorting, and filtering, the agent can set up your Library to show what’s most important to you.

## Launch the quick action

1. In the lower-right corner of your document library, select the **Knowledge Agent** icon.

2. From the **quick actions** menu, select **Create new view**.

3. The chat panel opens and displays a list of suggested actions related to custom views.

    > [!NOTE]
    > If this is the first time using the agent on the library, Knowledge Agent will automatically suggest up to three columns based on the available files. These columns are auto populated with metadata about your files and useful when creating views.

## Use a suggested action

1. From the chat panel, select an action. For this example, we use **Show recently updated files first**.

2. In the chat box, review the instruction provided. If needed, you can modify the text to better suit your intent. Once you're ready, select **Send** (![Screenshot of the send icon in the chat box.](media/knowledge-agent/chat-box-send-icon.png)) to submit your action.

3. The agent uses your prompt to generate a view. The view parameters are summarized in the chat panel.

   ![Screenshot of a summary of the view parameters in the chat panel.](media/knowledge-agent/knowledge-agent-view-parameters.png)

## Enter a custom action

1. In the chat panel’s text box, enter your own custom view instruction. When describing a view, consider what you want to see (filters) and how you want it grouped or sorted. This helps ensure the view meets your needs.

   ![Screenshot of the chat box showing a custom view instruction.](media/knowledge-agent/knowledge-agent-chat-box-custom-view.png)

    > [!TIP]
    > The agent can show and hide columns, sort, filter, and group. Here are some sample prompts that could be used on libraries containing different document types:
    >
    > •	**Invoices**: Show me past due invoices, grouped by vendor and sorted by amount due.
    >
    > •	**Product specs**: Show me products with a release date in 2020 and sort by market positioning.
    >
    > •	**HR policy documents**: Display HR policies by category showing only those that are already in effect.
    >
    > •	**Project plans**: I want to see project plans grouped by phase and sorted by start date. Show the owner column and hide the location column.

2. Select **Send** (![Screenshot of the send icon in the chat box.](media/knowledge-agent/chat-box-send-icon.png)) to submit your action.

3. The agent uses your prompt to create a view and summarizes the view in the chat panel.

   ![Screenshot of the chat box showing a summary of the view.](media/knowledge-agent/knowledge-agent-summary-view.png)

    > [!TIP]
    > Select the chevron in the view summary card in the chat panel to expand it and see a full description of the view created. The view will also be reflected in the document library.
    >
    >![Screenshot of the document library showing the view summary in the chat box.](media/knowledge-agent/knowledge-agent-chat-box-and-library-view.png)

    > [!TIP]
    > The agent can create a view using your existing columns and, when needed, it can create new columns. Prompt for the view you want and the agent will first create the required column and next configure the view.
    >
    >![Screenshot of the document library showing the next view configuration in the chat box.](media/knowledge-agent/knowledge-agent-chat-box-prompt-for-new-columns.png)

## Save your changes

1. When you're ready to save the view you created and any other changes you made, select **Save changes**.

2. On the **Save changes to library?** confirmation screen, verify that you want to update the **current library view** or save as a **new view**, and then select **Apply changes**.

    > [!TIP]
    > If you create a new view, it will be the name of the library appended with a numerical value. The naming experience will be improved in future updates, but for now you can rename the view from the library command bar.

3. You're returned to the updated library and the view you created. Views created by the agent are public views for everyone who uses the document library to see.

## Requirements and limitations

- **Supported view actions**: Show column, Hide column, Sort, Filter, and Group-By.

- **Supported column types for filtering**: Choice, Number, Text, DateTime, Boolean, Currency, and MMD.

- **Supported column types of column creation**: Choice, Number, Text, DateTime, Boolean, Note, Currency, URL, and MMD.

- **Supported languages**: All languages supported through [Microsoft 365 Copilot](https://support.microsoft.com/topic/26de43a1-c176-4908-bef7-29c8c37ac7ce) for text-based prompts and responses, but can only process files in English.

- **Limitations**:

    - Encrypted files can't be analyzed to generate metadata for views.

    - Column ordering, column width changes, and conditional formatting of views are not yet supported in Knowledge Agent.

    - Knowledge Agent doesn't yet support the creation of personal views (views created by the agent are public views for everyone who uses the document library to see).
