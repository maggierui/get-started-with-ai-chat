---
ms.date: 04/11/2025
title: "SharePoint Server Team Sites Migration Guide"
audience:  ITPRo
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
ms.audience: ITPro
f1.keywords:
- NOCSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
- m365initiative-migratetom365
search.appverid: MET150
description: "This guide helps you prepare to migrate content from SharePoint Server team sites to SharePoint in Microsoft 365."
---

# SharePoint Server team sites Migration Guide

This guide helps you prepare to migrate from SharePoint Server team sites to SharePoint in Microsoft 365.

Most migrations fall into regular phases as described in this article. Proven success factors for migration include planning, assessing and remediating, preparing your target environment, migrating, and onboarding your users.

**Note:**</br>The SharePoint Migration Tool (SPMT) is a Microsoft developed migration tool available at no cost. To download: [SharePoint Migration Tool](https://aka.ms/spmt-ga-page).

![A screenshot of the migration process flow, showing the planning, assess and remediate, prepare your environment, migrate, and user onboarding stages.](media/migration-process-SPonly.png)

|**Planning** |**Assess and remediate** |**Prepare your SharePoint environment** |**Migrate** |**User onboarding** |
|:------------|:------------------------|:---------------------------------------|:-----------|:-------------------|
|What to expect before and after </br>Migration and network performance considerations </br>Change management and communications </br>Plan for Modern team sites |Run SMAT </br>Assess key areas </br>Remediate issues </br>Workflows </br> |User creation </br>Site creation </br>Tenant settings </br>Hybrid </br> |Migration service providers </br>Let users know how they're impacted </br> |Send regular emails to users </br>Provide training </br>Provide documentation for making the switch </br> |

## Planning

Before beginning your migration, it's important that you plan your outcome by performing an assessment of your current source environment.

Plan your User Onboarding efforts to prepare your users for change and how it impacts them. See the [User Onboarding](#user-onboarding) section.

We recommend you consider setting up a hybrid environment at the beginning.

- Learn more at: [SharePoint Hybrid Configuration Roadmaps](/sharepoint/hybrid/configuration-roadmaps).

What you discover influences your overall strategy and timing, including:

- The mapping of content from your source site to the destination site.

- The amount of content you migrate. Determine if content is redundant, out of date, or still relevant. See this article for more info on speed [Best practices for improving SharePoint and OneDrive migration performance](./sharepoint-online-and-onedrive-migration-speed.md) 

- The permissions you set so IT can read/write from source to target destination.

### Understanding the modern architecture
New features and enhancements are continually being rolled in SharePoint in Microsoft 365 before being included in SharePoint Server. As a result, features and functionality available in SharePoint Server may be different than features and functionalities in SharePoint in Microsoft 365.

As you plan your migration strategy, it's important to understand the modern architecture. Begin by reading:

- **[Guide to the Modern experience in SharePoint](/sharepoint/guide-to-sharepoint-modern-experience)**

### Planning a modern framework before you migrate

**Modern team sites, pages and hubs**

When moving your team site, we recommend that you create team sites in SharePoint that are **modern**. While this action doesn't automatically make them group or **Microsoft Teams** connected, you can connect them in the future. You can either create them using:

- The user interface
- PowerShell
- A migration tool such as the SharePoint Migration Tool (SPMT), which can create these sites for you.

As you plan your migration, we recommend that a **hub site** the best way to create relationships between sites. We recommend taking this opportunity to bring those subsites to be their own site collections in order to connect them through a hub.

- [What is a SharePoint hub site?](https://support.office.com/article/fe26ae84-14b7-45b6-a6d1-948b3966427f)

- [Planning your SharePoint hub sites](/sharepoint/planning-hub-sites)

Decide how your team sites map to a modern hub architecture. You don't need to group connect every site you're moving, but strategize your site plan to optimize the structure to be flexible for continuous change.

#### More guidance on modernization

- [Modernize your classic SharePoint sites](/sharepoint/dev/transform/modernize-classic-sites) 
- [Transform classic pages to modern client-side pages](/sharepoint/dev/transform/modernize-userinterface-site-pages)

### Workflows and planning for the future

In Microsoft 365, **Power Automate** is the product that allows you to easily create and manage workflow. If you're currently using SharePoint workflows, we recommend that you consider "future-proofing" your environment by identifying the workflows you want to keep and recreate them using **Power Automate** to allow for better platform integration.

To learn more:
- [Get started with Power Automate](/power-automate/getting-started)

> [!NOTE]
> Classic workflow is supported and available until 2026. We recommend taking this information into consideration as you plan for your workflow lifetime. For more information, see [SharePoint 2010 workflow retirement](https://support.microsoft.com/office/sharepoint-2010-workflow-retirement-1ca3fff8-9985-410a-85aa-8120f626965f).

## Assess and remediate your content

Before beginning your migration, it's important that you perform an analysis of your current environment. Only you know your data and how and who uses it. Think about how and what My Sites features you use in production.

An initial assessment can begin with working with your users in two main areas:

- Identify older content.
- Determine if content is obsolete or redundant and can be deleted.

### Using the SharePoint Migration Assessment Tool (SMAT)

The SharePoint Migration Assessment Tool (SMAT) is a simple command-line executable that scans the contents of your SharePoint Server 2013 farm to help identify any issues before you migrate your content.

After the scan completes, SMAT generates summary and detailed reports showing the areas that could impact your migration. Not everything in the report needs to be remediated; but the important scans for your business needs should be looked at.

Also included is the SharePoint Migration Identity Management Tool. This tool does identity mapping by scanning SharePoint Active Directory and Microsoft Entra ID.

## Prepare your SharePoint environment

Before migrating your team site content, you must first pre-provision your users in Microsoft 365.

For guidance on pre-provisioning see:

- [Prepare to provision users through directory synchronization to Microsoft 365](/office365/enterprise/prepare-for-directory-synchronization)

Create modern hub sites based on how you mapped your sites to a system of hub sites.

- [Create a hub site](/sharepoint/create-hub-site)
- [Associate a SharePoint site with a hub site](https://support.office.com/article/ae0009fd-af04-4d3d-917d-88edb43efc05)

## Migration process

The following is a typical migration process that follows Microsoft's best practices guidance:

1. Select a small set of users for a pilot migration. The goals of the pilot are to validate the process, including performance and user communication, and to get a sample of user feedback.
1. Run the pilot migration. Use an incremental migration method that runs in the background with no user impact. Follow this incremental migration with a cutover event in which you disable SharePoint Server team sites. Direct users to use the SharePoint environment. This method is preferred, as it reduces user impact.
1. Assess the data from the pilot migration to determine the rest of your migration schedule, and make any needed changes. For example, you may update your user communication template to address questions you received from pilot users.
1. Do the rest of the migration. Use an incremental migration method, just like the pilot. We recommend a single cutover event for all users to switch to using their SharePoint sites. This approach helps prevent users from updating duplicate copies of content.

### Migration offerings

Currently, you have these migration offerings available to you:

**Self service**

The benefit for self-service migration is that you have full control over your process and timing, and you determine the pace of migration. Microsoft provides the [SharePoint Migration Tool](https://aka.ms/spmt-ga-page) free of charge and you can use your own IT resources rather than having to invest in outside expertise.

**Migration service providers**

You may decide that your organization has specific business needs that require you to use third-party services or applications to help you execute your migration. Explore the professional services and applications available from partners in the Microsoft Partner Center. There you can find experts to help you in your enterprise content migration to Microsoft 365. For more info, see [Microsoft Partner Center](https://partnercenter.microsoft.com/partner/home).

## User Onboarding

Develop a plan to prepare your users for the upcoming change. Consideration factors to include in your plan:

- **Evangelize the move**. Underscore the benefits, the collaborative capabilities, and the reasons for making the move.
- **End user training**. Provide training to your users on the features in SharePoint.
- **Train your helpdesk**. Before the cutover, train your helpdesk in key features and common user questions.
- **Prepare for any possible downtime** the migration may incur.

Develop a plan for sending communications to your user base, providing clear statements of timing, expectations, and impact to the individual. Include:

- The migration timeline and how it impacts them. Include any end user calls to action. 
- Assurances that if they have content already in SharePoint, their content is safe and not overwritten. 
- Awareness about whether or not individuals can opt out of the migration process.
