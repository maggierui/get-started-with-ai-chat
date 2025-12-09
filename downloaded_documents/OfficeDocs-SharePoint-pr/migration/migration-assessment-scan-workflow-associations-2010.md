---
title: "Migration Assessment Scan Workflow Associations 2010"
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
ms.localizationpriority: high
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
ms.assetid: ebf375f6-588f-4d5e-9126-e945aa31f7e2

---

# Migration Assessment Scan: Workflow Associations 2010

## Overview

The migration tooling is typically able to migrate the Workflow Definitions from the SharePoint source to the target environment. However, any in progress workflow instances aren't migrated. As a result, in progress workflows are reset to appear as if they were never started on the destination.

## Data Migration

Workflow Data is divided into the following two parts:

- **Workflow Definition:** The definition describes the overall workflow process, for example, a three stage approval workflow with custom routing rules for each stage. This data is typically migrated with the rest of the site collection data and is available in your target environment.
- **Workflow Instances:** Each running instance of a workflow definition maintains the state of the in progress workflow, for example, this document is in Stage 2 of the approval process and is assigned to John Doe. Unfortunately, this information can't be migrated to the new platform. The result is the loss of all running workflow instances. For example, a document that was in Stage Two of a workflow in the source environment is set back to Stage Zero (workflow not started) post migration to the target environment.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

To avoid unnecessary workflow restarts, it's best to complete in-flight workflows before the migration event when your content is moved to the target environment.

## Post Migration

Once the migration to the target environment is complete, users need to restart any workflows that were still in flight. If the workflow contained identities, it may be necessary to republish the workflow using SharePoint Designer.

## Scan Result Reports

**WorkflowAssociations2010-detail.csv** This scan report provides a list of all the 2010 workflow associations in the environment along with how many running instances at the time the scan was executed.

|**Column** |**Description** |
|:----------|:---------------|
|SiteId |Unique identifier of the impacted site collection. |
|SiteURL |URL to the impacted site collection. |
|SiteOwner |Owner of the site collection. |
|SiteAdmins |List of people listed as site collection administrators. |
|SiteSizeInMB |Size of the size collection in megabytes (MB). |
|NumOfWebs |Number of webs that exist in the site collection. |
|ContentDBName |Name of the content database hosting the site collection. |
|ContentDBServerName |SQL Server hosting the content database. |
|ContentDBSizeInMB |Size of the content database hosting the site collection. |
|LastContentModifiedDate |Date/Time the site collection had content modified. |
|TotalItemCount |Total number of items found in the site collection. |
|Hits |Number of requests logged for the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DistinctUsers |Number of distinct users who accessed the site collection. Relies on data from the usage logging service. This row shows N/A if the usage logging service is disabled. |
|DaysOfUsageData |Number of days the usage logging service retains data. This information provides context for Hits and DistinctUsers. For example, if this number is 14 days, the Hits and DistinctUsers data is for the last 14 days. |
|Scope |Either List, ContentType, or Site. This entry is the level that associated with the workflow. |
|RunningInstances |Number of workflows actively running at that scope. |
|WebURL |URL to the web that the workflow is associated with. |
|ListTitle |Title of the list the workflow is associated with. The value is N/A if the scope is Site. |
|ListUrl |Url to the list with the workflow association. |
|ContentTypeName |Name of the content type if the scope is ContentType. |
|IsReusable |True if the workflow association was published as a reusable workflow. |
|ReusableScope |Specifies the scope of the reusable workflow. Reusable or GlobalReusable. |
|WorkflowName |Name of the workflow association. The text that displays in SharePoint when starting the workflow. |
|WorkflowDescription |Description of the workflow association. |
|HasCustomWorkflowActivity |True if the workflow uses a custom workflow activity deployed using full trust solutions. |
|WorkflowReferencedAssemblies |Name of the assembly associated with a custom activity. Populated if HasCustomWorkflowActivity is True. |
|SolutionNames |Name of the full trust solution package associated with a custom activity. Populated if HasCustomWorkflowActivity is True. |
|WorkflowPublishedBy |Name of the person who published the workflow. |
|WorkflowID |Unique identifier associated with the workflow. |
|AddListItemPermissionsExist |True if the workflow contains an action that adds list permissions. The activity embeds a user's identity and may not function post migration without manual republish of the workflow. |
|RemoveListItemPermissionsExists |True if the workflow contains an action that removes list permissions. The activity embeds a user's identity and may not function post migration without manual republish of the workflow. |
|ReplaceListItemPermissionsExists |True if the workflow contains an action that replaces list permissions. The activity embeds a user's identity and may not function post migration without manual republish of the workflow. |
|EmailActivityExists |True if the workflow contains an action that sends email. The activity embeds a user's identity and may not function post migration without manual republish of the workflow. |
|ImpersonationExists |True if the workflow contains an action that impersonates an account to perform an action. The activity embeds a user's identity and may not function post migration without manual republish of the workflow. |
|RulesFileExists |True if the workflow contains conditional rules that contain identities. The activity embeds a user's identity and may not function post migration without manual republish of the workflow. |
|ContentAppovalExists |True if the workflow contains content approval activities. The activity embeds a user's identity and may not function post migration without manual republish of the workflow. |
|WorkflowFileCheckedOut |If the workflow file is checked out, it doesn't migrate as expected. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
