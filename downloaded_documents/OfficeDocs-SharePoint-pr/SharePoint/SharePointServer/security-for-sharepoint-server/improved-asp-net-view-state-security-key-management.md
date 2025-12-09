---
ms.date: 03/11/2025
title: Improved ASP.NET view state security and key management
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5cdce2aa-fa6e-4888-a34f-de61713f5096
description: "Learn how to set up improved ASP.NET view state security and key management"
---

# Improved ASP.NET view state security and key management

[!INCLUDE[appliesto-xxx-2016-2019-SUB-xxx-md](../includes/appliesto-xxx-2016-2019-SUB-xxx-md.md)]

> [!NOTE]
> SharePoint Server Subscription Edition encrypts the `machineKey` section of its `web.config` files by default. This prevents attackers from reading your ASP.NET view state encryption and validation keys, even if they gain access to those `web.config` files.

If you are running SharePoint Server Subscription Edition or SharePoint Server 2016/2019 editions, the platform secures your sensitive data by regularly updating the machine encryption keys. This process is done manually using PowerShell cmdlets, which updates the decryption and validation keys within a web application. This security practice helps to mitigate potential vulnerabilities if a key is compromised. For more information, see [PowerShell cmdlets](#powershell-cmdlets).

Starting from SharePoint Server Subscription Edition Version 25H1 and the September 2025 Public Update for SharePoint Server 2016 and 2019, you would be able to automatically update machine keys without manual intervention. For more information, see [Automatic machine key rotation](#automatic-machine-key-rotation).

## Automatic machine key rotation

Automatic machine key rotation feature aims to improve security by automating the periodic updating of machine keys, thereby minimizing the risk of key compromise. This feature ensures seamless and automatic rotation of machine keys while maintaining high availability and reliability of SharePoint services during key rotation.

The feature incorporates a Key Management Service that handles storage, retrieval and distribution of machine keys using a timer job called **Machine Key Rotation Job**. The timer job is configured to run automatically on the Sunday of every week by default.

If you need to update the machine keys manually, you can trigger the Machine Key Rotation timer job by performing the following steps:

1. Navigate to the **Central Administration** site.
1. Go to **Monitoring** -> **Review job definition**.
1. Search for **Machine Key Rotation Job** and select **Run Now**.

When the job is completed, there should be no noticeable change to the administrators of the farm.

Using the following new PowerShell cmdlets, you can change the ASP.NET view state decryption and validation keys of a SharePoint web application, thus allowing you to rotate those keys in your farm.

## PowerShell cmdlets

 1. `Set-SPMachineKey`
 
    Configures the ASP.NET view state decryption and validation keys of a web application.

    #### Syntax
   
    ```PowerShell
    Set-SPMachineKey -WebApplication <SPWebApplicationPipeBind> [-DecryptionKey <String>] [-ValidationKey <String>] [-Local] [<CommonParameters>]
    ```

    #### Parameters
   
     - `-WebApplication <SPWebApplicationPipeBind>`
   
         Specifies the name, URL, or GUID of the Web application.

     - `-DecryptionKey [<String>]`
   
         Specifies the new ASP.NET view state decryption key. The key should be represented as a 64-character long hexadecimal string (0-9 and A-F).

         If this parameter isn't specified, a random decryption key is generated and used.

     - `-ValidationKey [<String>]`
   
         Specifies the new ASP.NET view state validation key. The key should be represented as a 64-character long hexadecimal string (0-9 and A-F).

         If this parameter isn't specified, a random validation key is generated and used.
     
     - `-Local`
   
         Deploy the new decryption and validation keys only to the local server. Other servers in the farm continue to use the previous decryption and validation keys. Web sessions that are load balanced across multiple servers in the farm will fail if these keys are not synchronized on every server in the farm. Use the `Update-SPMachineKey` cmdlet to deploy the keys to additional servers in the farm.

       If this parameter isn't specified, the new decryption and validation keys is deployed to all servers in the farm.
    
 2. `Update-SPMachineKey`
 
    Deploys ASP.NET view state decryption and validation keys to servers in the farm.

    #### Syntax
   
    ```PowerShell
    Update-SPMachineKey -WebApplication <SPWebApplicationPipeBind> [-Local] [<CommonParameters>]
    ```
    
    #### Parameters
    
     - `-WebApplication <SPWebApplicationPipeBind>`
    
       Specifies the name, URL, or GUID of the Web application.

     - `-Local`
    
       Deploys the new decryption and validation keys only to the local server. Other servers in the farm continue to use the previous decryption and validation keys. Web sessions that are load balanced across multiple servers in the farm will fail if these keys are not synchronized on every server in the farm.

       If this parameter is not specified, the decryption and validation keys is deployed to all servers in the farm.
  

