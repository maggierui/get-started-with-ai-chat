---
title: "Migration Assessment Scan Secure Store"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
ms.date: 04/10/2025
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
ms.localizationpriority: medium
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
ms.assetid: 8c63518d-4977-4bea-a376-09ec71b7ff56
description: "Learn how to mitigate issues with Secure Store during migration."
---

# Migration Assessment Scan: Secure Store

Learn how to mitigate issues with Secure Store during migration.

## Overview

Secure Store Service is a shared service that provides storage and mapping of credentials, such as account names and passwords. It lets you securely store data in the Secure Store Service to provide required credentials. You can connect to external systems and associate those credentials to a specific identity or group of identities.

## Data Migration

Secure Store applications aren't migrated to the target environment.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

Determine if the Secure Store applications listed in the scan results are required on the target platform. If they're required, you need to create them in Tenant Administration on the new platform during the migration testing.

> [!NOTE]
> The target environment only supports the Group Restricted type.

## Post Migration

If you created Secure Store applications in the target environment, ensure they work as expected.

## Scan Result Reports

**SecureStoreApplications-detail.csv** This scan report contains the Secure Store applications configured in the source environment. The information provided should be enough for you to recreate the applications in the target environment, if necessary.

> [!NOTE]
> If you see Secure Store application entries related to user profile, you should view the CustomProfilePropertyMappings output and remediation file to determine if the Secure Store applications are in use and how to remediate.

|**Column** |**Description** |
|:----------|:---------------|
|ApplicationID |Secure Store application ID. |
|Name |The name of the Secure Store application. The name typically matches the Application ID. |
|FriendlyName |Friendly name for the Secure Store application. |
|ContactEmail |Contact email address associated with the Secure Store application. |
|ApplicationType |The type of the Secure Store application. The only supported option on vNext is Group Restricted. |
|CredentialManagementURL |URL associated with managing credentials. The user doesn't typically set this URL. We provide this data for informational purposes. |
|TicketTimeout |Ticket time-out associated with the Secure Store application. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
