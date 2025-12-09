---
title: Translate documents in OneDrive
ms.author: chucked
author: MachelleTranMSFT
manager: jtremper
ms.reviewer: karlha
ms.date: 08/01/2025
audience: admin
ms.topic: how-to
ms.service: onedrive
search.appverid: 
ms.collection: 
    - enabler-strategic
ms.localizationpriority:  medium
description: Learn about the document translation service in OneDrive.
---

# Translate documents in OneDrive

> [!NOTE]
> Through December 2025, you can try out document translation and other selected services at no cost if you have [pay-as-you-go billing](/microsoft-365/documentprocessing/syntex-azure-billing) set up.
>
> For details on how to get started and the limitations, see [Try out pay-as-you-go services](/microsoft-365/documentprocessing/promo-syntex).

OneDrive, with the document translation service, allows you to manually translate documents while preserving the original format and structure. With this feature, you can create a translated copy of a single file or a set of files. The translation feature is available for all supported languages and dialects, and supports up to 10 languages per translation request.

:::image type="content" source="media/onedrive-document-translation/1-onedrive-translation.png" alt-text="screenshot of OneDrive document translate feature." lightbox="media/onedrive-document-translation/1-onedrive-translation.png":::

---

## Key features

- **Multiple points of access**: OneDrive document translation can be accessed via **My files** in OneDrive or using the viewer after opening the document. If you want to access the document translation feature for SharePoint Online libraries, you can also access that feature through OneDrive's **Quick access** section. For more information about document translation for SharePoint Online, see [Overview of document translation](/microsoft-365/documentprocessing/translation-overview).
- **Request multiple languages per translation**: You can select up to 10 languages per document translation.
- **Translation of different file types**: Translate various file types. [Supported file types](#supported-file-types) include .docx, .pdf, .pptx, and more.
- **Video transcripts and captions**: The translation feature also supports translating video transcripts and closed caption files. For more information, see [Transcript translations in Stream for SharePoint](https://support.microsoft.com/office/microsoft-syntex-pay-as-you-go-transcript-translations-in-stream-for-sharepoint-2e34ad1b-e213-47ed-a806-5cc0d88751de).

---

## Prerequisites

To enable document translation for your tenant, you must:

- Link an Azure subscription to [pay-as-you-go billing](/microsoft-365/documentprocessing/syntex-azure-billing#connect-the-service-to-an-azure-subscription-for-billing).
- Be a [SharePoint Administrator](sharepoint-admin-role.md) or have credentials to access the Microsoft 365 admin center.

## Enable document translation for your tenant

> [!NOTE]
> Once an Azure subscription is linked to pay-as-you-go billing, the translation feature is automatically set up and turned on for all [SharePoint](/microsoft-365/documentprocessing/translation-setup#set-up-translation) and OneDrive sites.

## Manage document translation for OneDrive

Even though OneDrive document translation is enabled by default, you can also turn off the feature.

To disable document translation for OneDrive:

1. Sign in to the Microsoft 365 admin center and select **[Setup](https://go.microsoft.com/fwlink/p/?linkid=2171997)**.
2. Expand **Files and content** and select **Automate content processes with Syntex**.
3. On the **Automate content processes with Syntex** page, select **Go to Syntex settings**.
4. On the Syntex page, in the **Document & image services** section, select **Document translation**.
5. In the OneDrive section, select **Edit**. On the **Where can document translation be used?** panel, clear the **Available in OneDrive** checkbox.

For more information about managing document translation for SharePoint sites, see [Set up and manage document translation](/microsoft-365/documentprocessing/translation-setup#manage-sites).

## Translate a document

Sign in to [OneDrive](https://go.microsoft.com/fwlink/p/?LinkID=2119709) with your Microsoft account credentials.

1. Select **My files**.

2. Select the file you want to translate and select the **More commands (...)** button in the ribbon.

    Alternatively, you can get to this feature by selecting **More Actions (...)** beside the file name or opening the document in the viewer.

3. Select **Translate**.

4. Choose up to 10 languages and select **Translate**.

    :::image type="content" source="media/onedrive-document-translation/3-onedrive-translation-max-languages.png" alt-text="Screenshot of OneDrive document translate feature with maximum of 10 languages selected." lightbox="media/onedrive-document-translation/3-onedrive-translation-max-languages.png":::

The translated file is saved in the same location as the file you selected to translate.

> [!NOTE]
> It might take up to several hours to generate the translated files.

---

## Requirements and limitations

### Supported file types

Document translation is available for the following file types:

- `.csv`, `.docx`, `.htm`, `.html`, `.markdown`, `.md`, `.msg`, `.pdf`, `.pptx`, `.txt`, `.xlsx`

For legacy file formats, the translated copy is created in the modern equivalent:

- `.doc` → `.docx`
- `.xls` → `.xlsx`
- `.ppt` → `.pptx`

> [!NOTE]
> SharePoint site pages aren't supported for translation at this time.

### Supported file size

The maximum file size for translation is 40 MB.

### Supported languages

Translation for the service is available for all [supported languages and dialects](/azure/ai-services/translator/language-support#translation).

:::image type="content" source="media/onedrive-document-translation/2-onedrive-translation.png" alt-text="Screenshot of OneDrive document translate feature with supported languages." lightbox="media/onedrive-document-translation/2-onedrive-translation.png":::

---

## Current limitations

- **Images**: Text embedded in images within documents isn't translated.
- **Encrypted files**: Encrypted files can't be translated.
- **Password-protected files**: Password-protected files aren't eligible for translation.

---

## Frequently asked questions

For more information, see the following resources:

- [Document Translation: FAQ](/azure/ai-services/translator/document-translation/faq#document-translation-faq)
- [How does Translator count characters?](/azure/ai-services/translator/translator-faq#how-does-translator-count-characters)

## Related topics

- [Overview of document translation](/microsoft-365/documentprocessing/translation-overview)
- [Set up and manage document translation](/microsoft-365/documentprocessing/translation-setup)
- [Translate a document](/microsoft-365/documentprocessing/translation)
- [Configure pay-as-you-go billing](/microsoft-365/documentprocessing/syntex-azure-billing)
