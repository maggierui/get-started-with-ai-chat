---
ms.date: 09/18/2025
ms.update-cycle: 180-days
title: Automate workflows in a SharePoint document library
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
description: Learn how to use rules to automate workflows in a SharePoint document library.
---

# Automate workflows in a SharePoint document library

> [!NOTE]
> This article applies to the preview version of Knowledge Agent in SharePoint.

Knowledge Agent in SharePoint enables you to set up automations in your document library simply by describing what you want to happen, using natural language. You don’t need to know technical terms or navigate complex menus—just tell the agent your intent, and it will suggest and configure the appropriate workflow rule.

## Launch the quick action

1. In the lower-right corner of your document library, select the **Knowledge Agent** icon.

2. From the **quick actions** menu, select **Set up rules**.

3. The chat panel opens and displays a list of suggested actions related to the creation of rules.

    > [!NOTE]
    > If this is the first time using the agent on the library, Knowledge Agent will automatically suggest up to three columns based on the available files. These columns are auto populated with metadata about your files and useful when creating rules.

## Use a suggested action

1. From the chat panel, select an action. For this example, we use **Send notification**.

2. In the chat box, review the instruction provided. If needed, you can modify the text to better suit your intent. Once you're ready, select **Send** (![Screenshot of the send icon in the chat box.](media/knowledge-agent/chat-box-send-icon.png)) to submit your action.

3. The agent uses your prompt to generate a rule. Review the rule created and select **Create** to set up the rule.

   ![Screenshot of the Create a rule page.](media/knowledge-agent/knowledge-agent-create-a-rule.png)

4. The rule conditions are summarized in the chat panel.  

   ![Screenshot showing a summary of the rules conditions.](media/knowledge-agent/knowledge-agent-rule-conditions.png)

## Enter a custom action

1. In the chat panel’s text box, enter your own automation instruction. When requesting a rule, specify the condition in which it should run and the action that should happen. This helps ensure the rule meets your needs.

   ![Screenshot of the chat box showing a requested action.](media/knowledge-agent/knowledge-agent-chat-box-requested-action.png)

    > [!TIP]
    > The agent can do four actions: email, move, copy, and set the value. Here are some sample prompts:
    >
    > •	Send an email (for example, “Email me when a contract is approved” or “Notify me when new files are added and the release date is in 2025”)
    >
    > •	Move a file (for example, “Move reviewed invoices to the Verified Expenses folder”)
    >
    > •	Copy a file (for example, “Copy all Northwind Traders invoices to the Northwind folder”)

2. Select **Send** (![Screenshot of the send icon in the chat box.](media/knowledge-agent/chat-box-send-icon.png)) to submit your action.

3. The agent uses your prompt to generate a rule. Review the rule created and select **Create** to set up the rule.

   ![Screenshot of the Create a rule page showing the generated rule.](media/knowledge-agent/knowledge-agent-generated-rule.png)

4. The rule conditions are summarized in the chat panel.

   ![Screenshot of the chat box showing the generated rule.](media/knowledge-agent/knowledge-agent-chat-box-generated-rule.png)

    > [!TIP]
    > The agent can set up a rule using your existing columns and, when needed, it can create new columns. Prompt for the automation you want and the agent will first create the required column and next configure the automation.
    >
    >![Screenshot of the chat box showing the prompt for automation.](media/knowledge-agent/knowledge-agent-chat-box-prompt-for-automation.png)

## Save your changes

1. When you're ready to save the rule you created and any other changes you made, select **Save changes**.

2. On the **Save changes to library?** confirmation screen, verify that you want to update the **current library view** or save as a **new view**, and then select **Apply changes**.

    > [!TIP]
    > If you create a new view, it will be the name of the library appended with a numerical value. The naming experience will be improved in future updates, but for now you can rename the view from the library command bar.

3. You're returned to the updated library, and the agent will run the rule you created whenever the conditions are met.

    > [!TIP]
    > If you want to see all of rules in your document library, from the header select **Automate** > **Rules** > **Manage rules**.
    >
    >![Screenshot showing the path to view all rules in your library.](media/knowledge-agent/knowledge-agent-rules-path.png)

## Requirements and limitations

- **Supported rule triggers**: A new item is created, an item is modified, or an item is deleted.

- **Supported rule actions**: Email, move, copy, and set value.

- **Supported languages**: All languages supported through [Microsoft 365 Copilot](https://support.microsoft.com/topic/26de43a1-c176-4908-bef7-29c8c37ac7ce) for text-based prompts and responses, but can only process files in English.

- **Limitations**:

    - Encrypted files can't be analyzed to run rules.

    - The "date approaches" trigger for rules isn't yet supported in Knowledge Agent.

    - The translate and delete rules actions aren't yet supported in Knowledge Agent. Organizations with [pay-as-you-go billing](/microsoft-365/documentprocessing/syntex-azure-billing) set up can ask the agent to translate files, but will incur costs on their pay-as-you-go meter.

    - Multi-step prompts to create new columns and configure a rule in one step do not yet work for the set value action.

    - A maximum of 15 rules can be created per list or library.

    - Rules can't be applied to multi-line text columns.

    - Rules don't support email-enabled security groups for notifications.

- **Notifications**: Emails are sent from *no-reply@sharepointonline.com* to specified individuals.
