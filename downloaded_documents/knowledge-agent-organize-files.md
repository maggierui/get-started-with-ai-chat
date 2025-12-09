---
ms.date: 10/06/2025
ms.update-cycle: 180-days
title: Organize files in a SharePoint document library
ms.reviewer: ssquires
ms.author: chucked
author: chuckedmonson
manager: jtremper
recommendations: true
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
description: Learn how to organize files, automate columns, and classify documents in a document library in SharePoint.
---

# Organize files in a SharePoint document library

> [!NOTE]
> This article applies to the preview version of Knowledge Agent in SharePoint.

Knowledge Agent in SharePoint empowers you to build richer, more intelligent document libraries for streamlined content management. By simplifying the configuration process, it ensures consistent and accurate data capture across your organization. 

The agent’s "Organize this library" skill analyzes library file content to suggest or create columns and prompts to automate metadata extraction and generation. With recommended metadata columns, the agent improves library-scoped chat experiences and enables rule-based automation flows that support efficient business processes. This approach keeps your SharePoint libraries organized, relevant, and continuously up to date—making document management smarter and more scalable.

## Get suggested columns and metadata

To get suggested columns and metadata based on the first 20 files in your document library, follow these steps.

1. [Launch the quick action](#launch-the-quick-action).
2. [Use a suggested action](#use-a-suggested-action) or [enter a custom action](#enter-a-custom-action).
3. [Save your changes](#save-your-changes).

### Launch the quick action

1. In the lower-right corner of your document library, select the **Knowledge Agent** icon.

2. From the **quick actions** menu, select **Organize this library**.

3. The chat panel opens and displays a list of [suggested actions](#use-a-suggested-action) related to the creation of columns.

    > [!NOTE]
    > If this is the first time using the agent on the library, it will automatically suggest up to three columns based on the available files.

4. You can also request your own column in the chat panel.

### Use a suggested action

1. From the chat panel, select an action. For this example, we use **Suggest more columns**.

2. In the chat box, review the instruction provided. If needed, you can modify the text to better suit your intent. Once you're ready, select **Send** (![Screenshot of the send icon in the chat box.](media/knowledge-agent/chat-box-send-icon.png)) to submit your action.

3. The agent analyzes your library and suggests new columns, which appear highlighted and marked as **AI-generated**. This might take a few moments.

   ![Screenshot of a document library with the suggested columns highlighted.](media/knowledge-agent/knowledge-agent-suggested-columns-added.png)

   The suggested column information is summarized in the chat panel.

   ![Screenshot of the chat panel showing the suggested columns.](media/knowledge-agent/knowledge-agent-suggested-columns-chat-panel.png)

4. Review the suggested columns and the associated metadata to make sure they're appropriate for your content.

5. To remove a suggested column:

   - From the document library page, select the column name, and then select **Remove column**.

   - From the chat panel, on the column card, select **Remove**.

6. To rename the column or to refine the metadata in a suggested column:

    - From the document library page, select the column name, and then select **Edit column**.

    - From the chat panel, on the column card, select **Edit**.

7. On the **Edit column** panel, you can change the column name or modify the instruction that generates the metadata. After you edit the instruction, test it on up to 10 files to make sure gives you the information you want. When you're done making changes for that column, select **Save**.

8. You can also ask the agent to suggest an additional three columns by selecting the lightbulb icon in the header menu. If you want these suggestions based on a specific file, select the file before submitting the request.

   ![Screenshot of the chat panel showing the lightbulb icon to suggested additional columns.](media/knowledge-agent/knowledge-agent-suggest-additional-columns.png)

### Enter a custom action

1. In the chat panel’s text box, enter your own instruction.

    > [!TIP]
    > When requesting a column, be sure to specify a clear name and what type of information you would like to capture (for example, reason for document creation or project rationale), as well as any specifics around format and length. This helps ensure the column meets your needs.

   ![Screenshot of the text box showing a custom instruction has been entered.](media/knowledge-agent/knowledge-agent-custom-prompt.png)

2. Select **Send** (![Screenshot of the send icon in the chat box.](media/knowledge-agent/chat-box-send-icon.png)) to submit your action.

### Save your changes

1. When you're ready to save all of the column changes, select **Save changes**.

2. On the **Save and apply your changes?** confirmation screen, verify that you want to update the **current library view** or save as a **new view**, and then select **Apply changes**.

    > [!TIP]
    > If you create a new view, it will be the name of the library appended with a numerical value. The naming experience will be improved in future updates, but for now you can rename the view from the library command bar.

3. You're returned to the updated library, and the agent will begin processing the first 20 files. You can verify and monitor the progress in the [activity panel](knowledge-agent-file-processing-status.md#view-the-activity-panel).

4. After these prompts are saved on a column, any new files uploaded to the library are automatically processed, and the extracted information is saved to the corresponding columns.

<!---This section for classification needs to be added on Sept 25. Farreltin to edit; Chuck to review/confirm placement--->

## Classify documents  

You can add a classification column to automatically tag documents with predefined terms. Currently, only **Choice** values are supported, which means categories and descriptions must be entered manually. Future updates will introduce support for enterprise term sets and content types, enabling organization-wide reuse and consistency.

There are two ways to create a classification column: [directly within the document library](#create-a-classification-column-within-the-document-library) or [by using Knowledge Agent](#create-a-classification-column-by-using-knowledge-agent).

### Create a classification column within the document library

1. From the document library, select **+ Add column**.

   ![Screenshot showing how to add a classification column.](media/knowledge-agent/knowledge-agent-add-classification-column.png)

2. Select **Next** to open Knowledge Agent. The **Add column** panel opens, and the classification column is visible in the agent preview.

   ![Screenshot of the Add column panel and agent preview.](media/knowledge-agent/knowledge-agent-add-column-panel.png)

3. Name your classification column, and then select **+ Add categories** to begin adding categories. Descriptions for each category are optional but providing them might help improve agent classification accuracy.

   ![Screenshot of the Add categories panel.](media/knowledge-agent/knowledge-agent-add-categories-panel.png)

4. To test the prompt, select the files from preview to test. You can select 10 files to test at once. The result shows up in the classification column in the preview.

   ![Screenshot showing how to test your prompt.](media/knowledge-agent/knowledge-agent-test-your-prompt.png)

5. To save the classification column, select **Save** in the **Add column** panel, and then select **Save changes** in Knowledge Agent. This process adds a new classification column to the library.

### Create a classification column by using Knowledge Agent

1. From the chat panel, select **Classify documents**.

   ![Screenshot showing the Classify documents starter prompt.](media/knowledge-agent/knowledge-agent-classify-documents-starter-prompt.png)

2. In the chat box, edit the prompt, and then select **Send** (![Screenshot of the send icon in the chat box.](media/knowledge-agent/chat-box-send-icon.png)). The agent automatically creates a classification column, classifies the documents, and displays the results in the preview.

   ![Screenshot showing the classification results.](media/knowledge-agent/knowledge-agent-classification-results-screen.png)

3. In the chat box, tell the agent you want to create a classification column.

   ![Screenshot showing an example of a prompt to create a classification column.](media/knowledge-agent/knowledge-agent-classification-prompt-example.png)

4. The agent adds a classification column as required and displays the result in the preview.

   ![Screenshot showing the added column in the preview.](media/knowledge-agent/knowledge-agent-added-column-in-preview.png)

You can edit or delete the classification column in the chat panel. Select **Save changes** at the bottom of the preview to update.

## Requirements and limitations

- **Supported file types**: .csv, .docx, .pdf, .xlsx, and other Microsoft 365-compatible formats.

- **Supported languages**: All languages supported through [Microsoft 365 Copilot](https://support.microsoft.com/topic/26de43a1-c176-4908-bef7-29c8c37ac7ce) for text-based prompts and responses, but can only process files in English.

- **Supported column types**: Text, Multiple lines of text, Number, Yes/No, Date and time, Choice, Hyperlink, Currency, and Managed metadata.

- **Limitations**:  

    - Person or Group, Location, Image, and Lookup column types are currently unsupported.  

    - For optimal performance, we recommend adding no more than 10 columns per library and processing files no larger than 65 pages.

    - The agent can only process files, not folders. If files from a folder are used to configure the library, the changes are applied to the entire library.  

    - The agent only processes the first 20 files during initial configuration. Additional files can be selected manually and processed.  

    - If a managed metadata column type is used, it can only use the first 100 terms of a mapped term set. If a preferred term or synonym matches, the agent saves the preferred term to the column.  

    - Encrypted files can't be analyzed or the metadata included in the results.

    - The agent can only configure document libraries currently. The following library types aren't supported: FormServerTemplates, SitePages, Style Library, and SiteAssets.
