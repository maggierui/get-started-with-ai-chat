---
title: "Document Intelligence"
ms.reviewer: 
ms.author: lanruowu
author: lanruowu
manager: kaibchen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: overview
ms.date: 08/08/2025
ms.service: sharepoint-server-itpro
ms.localizationpriority: high
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn about the Document Intelligence feature, which is one of the newly introduced features in SharePoint Server Subscription Edition Version 25H2."
---

# Document Intelligence

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

This article describes the "Document Intelligence" feature, which is one of the new features introduced in the SharePoint Server Subscription Edition Version 25H2 feature update.

> [!NOTE] 
> Document Intelligence was first introduced in SharePoint Server Subscription Edition Version 25H2, but it was initially available only for SharePoint farms in Early release. Starting with SharePoint Server Subscription Edition Version 26H1, it's available regardless of whether your SharePoint farm is in Early release or Standard release.

## Document Intelligence

Document Intelligence represents a significant advancement in SharePoint Server's document management capabilities, combining AI with traditional document handling to provide intelligent insights and automation. This feature transforms how organizations interact with their document libraries by using AI to enable smarter, more efficient content engagement.

The Document Intelligence feature integrates seamlessly with SharePoint's existing document management infrastructure while introducing powerful AI-driven capabilities that help users work more efficiently with their content.

> [!IMPORTANT]
> As of the current release (SharePoint Server Subscription Edition Version 25H2), Document Intelligence is limited to Document AI Summarization functionality.

### Deployment and Configuration

To enable Document Intelligence, you must first complete deployment and configuration steps. These steps include provisioning required Azure resources and configuring SharePoint Server to support AI-powered document intelligence.
You can use a PowerShell script to deploy the required Azure resources and configure SharePoint Server. [Download the PowerShell deployment script](https://download.microsoft.com/download/9abfe128-15c8-4e47-a317-b5e7874049ff/DeployAzureAndConfigSPServer.ps1) and run it in Administrator mode.

Before executing the script, ensure the following requirements are met:
- **SharePoint Server** 
  - Ensure that at least one certificate exists in the **SharePoint Certificate Manager** End Entity store for Microsoft Entra ID authentication, and that it complies with the required certificate policy.
- **Azure**
  - Ensure you have the necessary permissions to create Azure resources and assign roles.
  - Verify that your subscription has sufficient quotas and resources to support the **Azure OpenAI** service.

When executing the script, you're prompted to enter your **tenant ID**, **resource location**, **subscription ID**, and select a **certificate** from SharePoint Certificate Manager for Azure authentication. During this process, you sign in to your tenant, create Azure resources, and upload the selected certificate to the Azure App registration.

**Sign in:**
 
![Login](../media/document-intelligence-login.png)

**Select a certificate:**

![ChooseCertificate](../media/document-intelligence-choose-certificate.png)
Once the certificate is selected, the deployment begins. The script checks for existing resources with the same name to avoid duplication. At the end of the process, it configures SharePoint Server and tests the connection between SharePoint and Azure.

If the configuration is successful, you see the following confirmation message:

![SuccessMessage](../media/document-intelligence-success-message.png)

### Feature Activation and Deactivation
After completing deployment and configuration, you can activate or deactivate the Document Intelligence feature as needed.

To manage this feature, the following minimum permissions are required:
- Site Collection level: Site Collection Administrator
- Document Library level: ManageLists permission

#### Site Collection Level
Site Collection Administrators can enable the Document Intelligence feature for all document libraries within a site collection by activating it in Site Collection Features. This approach is ideal when you want the AI summarization capability to be available across the entire site collection.

**Steps:**
1.	Go to **Site Settings**. Select **Site Collection Features.**

    ![SiteSettings](../media/document-intelligence-site-settings.png)

2.	Locate **Document Intelligence.**

    ![SiteCollectionFeatures](../media/document-intelligence-site-collection-features.png)

3.	Activate it.

    ![ActivateFeature](../media/document-intelligence-activate.png)

    Once activated, Document AI Summarization is enabled by default in all document libraries within the site collection, unless individual library settings are customized. The default library behavior follows the site collection configuration.

---

#### Document Library Level
For more granular control, you can enable or disable Document Intelligence at the individual document library level. This setting allows you to override the default site collection setting.

**Steps:**
1. Navigate to the desired document library, then go to **Library Settings** > **Advanced Settings**.

   ![AdvancedSettings](../media/document-intelligence-advanced-settings.png)

2.	Locate the **Document Intelligence** option and choose your preferred setting:

    ![OptionInLibrarySettings](../media/document-intelligence-option-in-library-settings.png)

    - Use the site default: Inherits the site collection setting.
    - Enable or Disable: Overrides the site collection setting for this library.
  
    > [!NOTE]
    > Changes made here apply only to the selected library and don't affect other libraries within the site collection.

---

### Document AI Summarization
The SharePoint **Document AI Summarization** feature uses Azure OpenAI services to automatically generate concise summaries, helping users quickly understand document content and improve productivity.

####  Activation and Deactivation
Document AI Summarization is automatically enabled when the **Document Intelligence** feature is activated. To disable AI summarization across the **entire farm**, use the following PowerShell command:
```PowerShell
Disable-SPDocSummary
```
To enable AI summarization across the farm, use:
```PowerShell
Enable-SPDocSummary
```
> [!NOTE]
> - This command has no effect if the Document Intelligence feature isn't activated.  
> - Farm administration permission is required.

---

#### Supported File Types

Document AI Summarization currently supports the following file formats:
- .doc, .docx, .pdf, .txt, .rtf, .html, .pptx, .md

#### Document Library Experience

AI Summarization is available in the following locations within the Document Library:

- Command bar

  ![CommandBar](../media/document-intelligence-command-bar.png)

- Contextual menu

  ![ContextualMenu](../media/document-intelligence-contextual-menu.png)

- Share dialog

  ![DocLibShareDialog](../media/document-intelligence-doc-lib-share-dialog.png)

When you select the **Summarize** button from the command bar or contextual menu, a dialog appears:
- You can keep the dialog open while the summary is being generated, or close it and allow the process to continue in the background.

  ![WaitForSummary](../media/document-intelligence-wait-for-summary.png)

- When a summary exists, it appears in the dialog. To generate a new one, select **Regenerate** button.

  ![RegenerateSummary](../media/document-intelligence-regenerate-summary.png)

In the Share Dialog, the generated summary appears in the message editor:

- You can edit the summary before sharing the document.

  ![ShareDialogSummary](../media/document-intelligence-share-dialog-summary.png)

- Recipients receive the document along with the summary in the email body.

  ![EmailWithSummary](../media/document-intelligence-email-with-summary.png)

#### Document Library WebPart

The Document Library Web Part supports AI summarization only within the Share Dialog.

![DocLibWebPartShareDialog](../media/document-intelligence-doc-lib-webpart-share-dialog.png)
