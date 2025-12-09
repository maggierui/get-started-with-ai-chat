---
ms.date: 03/31/2025
title: "SPMT Workflow migration report and error codes"
ms.reviewer:
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: error-reference
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
ms.assetid:
description: "Learn about the report generated when migrating SharePoint Server workflows using the SharePoint Migration Tool (SPMT) and the error codes that may surface."
---

# Migration workflow report and error codes

When migrating SharePoint Server workflows to Microsoft 365 using the SharePoint Migration Tool (SPMT), reports are automatically generated. Any error codes encountered are listed in the following table.

## Workflow migration reports

The work migration task generates two reports, one for scans and the other for the migration. These reports are saved to the *WF_xxx/Report/TaskReport_xxx/* folder.

- Workflow scans: **WorkflowScanReport.csv**
- Workflow migrations: **WorkflowMigrationReport.csv**

|Report column name |Notes |
:-----|:-----|
|Source association URL |The source SharePoint object URL associated with the workflow. It can be the URL of a list, a library, or a site |
|Destination association URL|The destination SharePoint object URL associated with the migrated Power Automate flow. It can be the URL of a list or a library. |
|Source workflow URL |The location of the source workflow. |
|Destination workflow URL |The location where the workflow is migrated. |
|Source workflow ID ||
|Destination flow ID ||
|Source workflow name ||
|Destination flow name ||
|Solution name |The name of the Power Automate solution that contains migrated flows. The flow owner can find migrated flows in the solution. |
|Source workflow owner |The creator of source workflow instance. |
|Destination flow owner |The owner or owners of the migrated Power Automate flow. |
|Association type |Possible values: List, Site, or Content type. |
|Workflow version |Possible values: Workflow 2010, Workflow 2013. |
|Workflow template name ||
|Workflow accessed date |The latest execution or modification date of the workflow. |
|Total action count |The count of actions for SPD workflow. |
|Unsupported actions |A list of actions not supported by migration tool. |
|Status |Possible values: Migrated, Failed, Skipped, Scan Finished. |
|Result category |Possible values: Migrated, Scan Finished, SCAN FILTER, MIGRATION SKIP, SCAN FAILURE, FLOW CREATE FAILURE. |
|Message |Error message. |
|Error code ||

## Workflow migration errors

When a scan or migration fails with either a *SCAN FAILURE* or *FLOW CREATE FAILURE*, the error message and code are provided in the report.

|Error message |Error code |Suggested action |
|:-----|:-----|:-----|
|SharePoint workflow scan unknown error. |0x02110001 ||
|SharePoint workflow subscription found without a workflow definition. |0x02110002 |Confirm the workflow has valid definition. |
|SharePoint workflow parse unknown error. |0x02110011 ||
|SharePoint workflow parse initial variables failed. |0x02110012 ||
|SharePoint workflow parse activities failed. |0x02110013 ||
|SharePoint workflow definition can't be loaded. |0x02110014 |Confirm the workflow has valid definition. |
|SharePoint workflow association data can't be loaded. |0x02110015 |Check your workflow and associate it with a list or library. |
|SharePoint workflow parse initial operator failed. |0x02110016 ||
|SharePoint workflow template isn't supported. |0x02110021 ||
|SharePoint workflow associated with a site or site level content type isn't supported. |0x02110022 ||
|SharePoint workflow can't convert to cloud flow because some variables aren't supported. |0x02110023 ||
|SharePoint workflow can't convert to cloud flow because some actions aren't supported. |0x02110024 ||
|Workflow migration failed because of unsupported variables or activities. |0x02110024 ||
|Workflow stage isn't supported. It may contain circle stage dependency in the flow definition. |0x02110025 ||
|SharePoint Workflow definition contains unsupported actions. |0x02110026 |You can select "Convert to compose action" in settings, and try migration again to convert unsupported action to compose. |
|Not all dependencies used in SharePoint workflow are resolved. |0x02110041 |Resolve dependencies (user or list), then retry migration. |
|Lookup list used in SharePoint workflow can't be mapped to target list. |0x02110042 |Migrate the lookup list to SPO, then retry migration. |
|Can't get flow owner's AAD ID. |0x02110044 |Map the flow owner to a valid Entra ID user, then retry the migration. |
|SharePoint workflow is filtered out because its association list or content type is out of migration scope. |0x02210031 |If you migrate workflows of a single list, try to perform workflow migration of its site. If the workflow is associated to a content type, manually create the content type on SPO list or library and try workflow migration again. |
|SharePoint workflow is filtered out because no new instances are allowed. |0x02210032 |Confirm the workflow is still in use. If you want to continue the migration, reactivate the workflow. |
|SharePoint workflow is filtered out because no SharePoint object is associated. |0x02210033 |Check your workflow and associate it with a list or library. |
|SharePoint workflow is filtered out because no triggers are configured. |0x02210034 |Confirm the workflow is still in use. If you want to continue the migration, reactivate the workflow. |
|SharePoint workflow is filtered out because it is a draft, please publish it and try to migrate it again. |0x02210035 |Publish your workflow and try migration again. |
|Workflow migration failed. |0x02810051 ||
|Workflow migration failed because flow owner isn't found. |0x02810052 |To make sure the workflow owner can be mapped to an Entra ID user, check the user mapping file or Entra ID lookup. |
|Workflow migration failed because flow approvers aren't found. |0x02810053 |To make sure the workflow owner can be mapped to an Entra ID user, check the user mapping file or Entra lookup. |
|Workflow migration failed because association data is missing. |0x02810054 |Check your workflow and associate it with a list or library and check that the out of the box (OOTB) workflow includes necessary data. |
|SharePoint workflow is skipped because it has been migrated before. |0x02810055 ||
|Unable to create flow. |0x02810061 ||
|Can't find the Flow owner in CDS |0x02810062 |Make sure the flow owner existed in Power Platform. |
|Invalid parameters to create flows. Contact with Microsoft for details. |0x02810063 ||
|No flow is going to be created. Contact with Microsoft for details. |0x02810064 ||
|Fails to detect the endpoints of the BAP environment. |0x02810065 |Make sure your custom endpoint file is valid. |
|Can't access BAP environment. |0x02810066 |Make sure the migrator user can access Business Applications Platform. |
|Unable to get Power Platform's default environment. |0x02810067 |Check if the tenant has a Power Automate license and if the database is created. |
|Can't access CDS. |0x02810068 |Make sure the migration user can access the Common Data Service. |
|Unable to create CDS user because we can't fetch the business unit in CDS. |0x02810070 |You can create the flow owner user manually in the power platform admin center. Assign Basic User and Environment Maker security roles to this user. Then migrate the workflow again. |
|Unable to create CDS user because we can't detect the built-in roles in CDS. |0x02810071 |Retry migration. |
|Unable to fetch existing flows from the environment. |0x02810072 |You can create flow owner user manually in power platform admin center. Assign Basic User and Environment Maker security role to this user. Then migrate the workflow again. |
|Unable to create user in Power Platform's default environment. |0x02810073 |You can create the flow owner user manually in the power platform admin center. Assign Basic User and Environment Maker security roles to this user. Then migrate the workflow again. |
|Unable to get the publisher. |0x02810074 |Retry migration. |
|Unable to publish solution. |0x02810075 |Retry migration. |
Workflow migration failed possibly because flow owner missing environment maker role. |0x02810076 |The flow owner didn't meet the role prerequisites. Make sure the flow owner has Basic User and Environment Maker roles. |
