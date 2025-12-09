---
ms.date: 04/11/2025
title: "Migrate your file share content to SharePoint using the Azure Data Box"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
search.appverid: MET150
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.localizationpriority: medium
description: "Learn how to migrate your file share content, preserving file metadata and NTFS (NT File System) information, to SharePoint in Microsoft 365 by using the Azure Data Box."
---

# Migrate your file share content to Microsoft 365 using the Azure Data Box

The Microsoft Azure Data Box is a service that lets you order a device from the Microsoft Azure portal. You can then copy terabytes of data from your servers to the device. After you ship it back to Microsoft, your data is copied into Azure.

This article specifically talks about how to use the Azure Data Box to migrate your file share content to SharePoint in Microsoft 365.

## Is Azure Data Box right for my migration?

Most of our large enterprise customers don't use Azure Data Box to migrate to OneDrive and SharePoint. Those enterprise customers with more than 500 TB of data achieved their migration goal using multiple computers and tools such as [Migration Manager](mm-get-started.md).

The most important thing to understand when deciding if you should use Azure Data Box is your migration's current bottleneck. We recommend running a performance test using multiple computers. Use a test size that pushes your migration boundaries so you can evaluate your bottleneck. Unfortunately, customers often attempt a test pilot that's too small and fail to see accurate results.

Another factor to consider is the added complexity involved in using the Azure Data Box. After loading the data onto the Data Box, you must allow for the delay caused by shipment time before the data can be copied into an Azure file share. Then you still need to perform the same migration steps on the copied data.

**Wrong reasons for using Data Box:**

- I have a large amount of data.
- I ran a test with one computer, and it wasn't fast enough.

**Correct Reasons for using Data box**

- My data is in a remote location with poor connectivity to Microsoft 365.
- My source is low on resources, and I can scale up my migration by using the Azure Data Box.

To learn more about our migration performance, see [General migration performance guidance.](./sharepoint-online-and-onedrive-migration-speed.md).

## Migrate your file share content using Azure Data Box

You can use your Azure Data Box and the SharePoint Migration Tool (SPMT) to migrate file share content to Microsoft 365. By using the Data Box, you can remove dependency on your WAN link to transfer the data.

Depending on the size of data you intend to transfer, you can choose from:

- [Data Box Disk](/azure/databox/data-box-disk-overview) with 35-TB usable capacity per order for small-to-medium datasets.
- [Data Box](/azure/databox/data-box-overview?pivots=dbx) with 80-TB usable capacity per device for medium-to-large datasets.
- [Data Box Next-Gen](/azure/databox/data-box-overview?pivots=dbx-ng) with either 120-TB and 525-TB usable capacity per device for medium-to-large datasets.
- [Data Box Heavy](/azure/databox/data-box-heavy-overview) with 770-TB usable capacity per device for large datasets.

## Requirements and costs

#### For Data Box

- Data Box is only available for Enterprise Agreement (EA), Cloud solution provider (CSP), or Pay-as-you-go subscription offers. If you don't have one of these subscriptions, contact Microsoft Support to upgrade your subscription, or see [Azure subscription pricing](https://azure.microsoft.com/pricing/).
- Data Box has a fee for use. Make sure to review the [Data Box pricing](https://azure.microsoft.com/pricing/details/databox/).

#### For SharePoint

- Review the minimum requirements for the [SharePoint Migration Tool (SPMT)](./how-to-use-the-sharepoint-migration-tool.md).

## Workflow overview

This workflow requires you to perform steps on Data Box and on SharePoint:

1. Order Data Box.
2. Receive and set up your Data Box.
3. Copy data from your on-premises file share to folder for Azure Files on your device.
4. After the copy is complete, ship the device back as per the instructions.
5. Wait for the data to completely upload to Azure.

The following steps relate to SharePoint:

1. Create a VM in the Azure portal and mount the Azure file share on it.
2. Install SPMT on the Azure VM.
3. Using the Azure file share as the SOURCE, run SPMT.
4. Complete the final steps of SPMT.
5. Verify and confirm your data.

## Use Data Box to copy data

Take the following steps to copy data to your Data Box.

1. [Order your Data Box](/azure/databox/data-box-deploy-ordered).
2. After you receive your Data Box, [Set up the device](/azure/databox/data-box-deploy-set-up). You cable and configure your device.
3. [Copy data to Data Box](/azure/databox/data-box-deploy-copy-data). While copying, make sure to:
    - Copy the data using only the *StorageAccountName_AzFile* folder in the Data Box. This location is important because you want the data to end up in an Azure file share, not in block blobs or page blobs.
    - Copy files to a folder within *StorageAccountName_AzFile* folder. A subfolder within *StorageAccountName_AzFile* folder creates a file share. Files copied directly to *StorageAccountName_AzFile* folder fail, and are uploaded as block blobs. This location is the file share you mount on your VM in the next step.
4. Run [Prepare to ship](/azure/databox/data-box-deploy-picked-up#prepare-to-ship) on your device. A successful 'prepare to ship' ensures a successful upload of files to Azure.
5. [Return the device](/azure/databox/data-box-deploy-picked-up#ship-data-box-back).
6. [Verify the data upload to Azure](/azure/databox/data-box-deploy-picked-up#verify-data-upload-to-azure).

## Migrating your data to Microsoft 365 using SPMT

After you receive confirmation from the Azure data team that your data copy completes, you can now proceed to migrate your data to Microsoft 365. For best performance and connectivity, we recommend you create an Azure Virtual Machine (VM).

1. Sign into the Azure portal, and then create a virtual machine. To learn how, see [Quickstart: Create Windows virtual machine in the Azure portal](/azure/virtual-machines/windows/quick-create-portal).
2. [Mount the Azure file share onto the VM](/azure/storage/files/storage-how-to-use-files-windows).
3. [Download the SharePoint Migration Tool](https://spmt.sharepointonline.com/install/default.htm), and install it on your Azure VM. 
4. Start SPMT. Select **Sign in**, and enter your Microsoft 365 username and password.

:::image type="content" source="media/spmt-opening-screen.png" alt-text="A screenshot of the SPMT launch page.":::

5. Select **File share**. Enter the path to your Azure file share where your data is located.
6. Follow the remaining prompts, including setting your target location. For more info, see [How to use the SharePoint Migration Tool](./how-to-use-the-sharepoint-migration-tool.md).

> [!IMPORTANT]
> - Several factors impact the speed at which data is ingested into SharePoint, regardless if you have your data already in Azure. By understanding these factors, you can plan your migration and maximize its efficiency. For more info, see [SharePoint and OneDrive Migration Speed](./sharepoint-online-and-onedrive-migration-speed.md).
> - File metadata and NTFS permissions can be preserved when the data is uploaded to Azure Files. To learn more, see [Preserving file ACLs, attributes, and timestamps with Azure Data Box](/azure/databox/data-box-file-acls-preservation).
