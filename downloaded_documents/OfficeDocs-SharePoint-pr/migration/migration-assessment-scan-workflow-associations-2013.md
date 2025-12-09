---
title: "Migration Assessment Scan Workflow Associations 2013"
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
ms.assetid: 59e80c9a-2543-43b4-9d4d-d758465c2e71
description: "Learn how to fix issues with that occur with Workflow Associations 2013 during migration."
---

# Migration Assessment Scan: Workflow Associations 2013

Learn how to fix issues that occur with Workflow Associations 2013 during migration.

## Overview

When content is migrated from the SharePoint source environment to the new target environment there are two types of workflows that could be involved, depending on their use in the current farm.

Workflows created using the workflow service available in SharePoint 2010 and are still in use on the source environment migrate to the new farm and continue to work as expected.

SharePoint source farms may run Workflow 2013 using a version of the Workflow Manager. As a result, when content is moved from the source environment to the target environment, there's a process to migrate Workflow 2013 over to the Azure instance of the Workflow Manager.

## Data Migration

Workflow Data is divided into two parts:

- **Workflow Definition:** The definition describes the overall workflow process, for example, a three stage approval workflow with custom routing rules for each stage. This data lives in Office 365 and is migrated with the rest of the Office 365 data and is available in your target environment.
- **Workflow Instances:** Each running instance of a workflow definition maintains the state of the workflow, for example, this document is in Stage Two of the approval process and is assigned to John Doe. This data lives in the Azure Workflow Manager. Unfortunately, the Azure team doesn't have the technology to migrate Workflow Manager data from the current source environments to Azure instances. This situation results in the loss of all running workflow instances. For example, a document that was in Stage Two of a workflow in the source environment is set back to Stage Zero (workflow not started) post migration to the target environment.

> [!IMPORTANT]
> Any site configured as "No Access" (locked) in SharePoint is skipped. To see a list of locked site collections see the Locked Sites scan output.

## Preparing for Migration

To avoid unnecessary workflow restarts, it's best to complete in-flight workflows before the migration event when your content is moved to the target environment. If the feature is in use in the source environment today, you can receive a list of running instances of workflows before migration. You can communicate this status to your site owners.

## Post Migration

Once the migration is complete, all users need to restart any workflows that were still in flight. In some extreme cases, it may be necessary to recreate a workflow if the tooling is unable to migrate it.

## Scan Result Report

**WorkflowAssociations2013-detail.csv** This scan report contains source workflow definitions and where they're associated in the site. Workflow definitions come across in the migration, which gives some visibility into the workflow footprint in the farm. 

|**Column**|**Description**|
|:-----|:-----|
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
|Scope |Either List or Site. Scope is the level the workflow runs at. It should help the site owner locate the impacted workflow definitions. |
|RunningInstances |Number of running instances linked to this workflow association. |
|WebUrl |Url to the subsite. |
|ListTitle |If the workflow is associated with a list, this row displays the title of that list. |
|ListUrl |If the workflow is associated with a list, this row displays the url to the root of the list. |
|IsReusable |True/False. Identifies which workflows were published as reusable workflows. |
|WorkflowAssociationName |Display name given to the workflow association. |
|WorkflowDescription |Description given to the workflow association. |
|WorkflowPublishedBy |Identity of the account used to publish the workflow. |
|WorkflowAssociationID |Unique identifier for the workflow association. |
|EmailActivityExists |True if there are email activities contained in the workflow. It may be necessary to fix up the identities in the email activities post migration. |
|ConditionalRuleExists |True if there are conditional rules contained in the workflow. It may be necessary to fix up the identities in the conditional rules post migration. |
|WorkflowFileCheckedOut |True if the workflow files are checked out. Checked out files don't migrate. |
|ScanID |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |
