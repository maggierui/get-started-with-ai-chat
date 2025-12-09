---
ms.date: 08/27/2025
title: "Site policy comparison reports for SharePoint sites"
ms.reviewer: pullabhk
ms.author: ruihu
author: maggierui
manager: dansimp
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- Highpri
- Tier2
- M365-sam
- M365-collaboration
- trust-pod
ms.custom:
- admindeeplinkSPO
search.appverid: 
description: "In this article, you learn about reports that can help you compare site policies of input or reference sites against target sites in SharePoint."
customer-intent: As a SharePoint admin, I want to compare site policies across multiple sites to ensure consistency and compliance.
---

# Compare site policies with the site policy comparison reports for SharePoint sites

As a best practice, SharePoint admins should use the same security policies for similar sites. Usually, admins organize sites by department, location, or nature of content, and then apply consistent security settings. For example, a site containing legal contracts should have strict security measures, such as [preventing external sharing](/microsoft-365/solutions/microsoft-365-limit-sharing), applying [conditional access](/sharepoint/authentication-context-example), [restricting access to specific groups](/sharepoint/restricted-access-control), and [blocking downloads](/sharepoint/block-download-from-sites). However, when there are hundreds or thousands of sites, it can be challenging for SharePoint admins to find sites with similar content and ensure they all have the right security policies.

Now with the power of AI, you can select one or more reference sites as your baseline and compare them against up to 10,000 target sites. The AI identifies sites with similar content and highlights any differences in their policy settings compared to your reference sites. This report is called the "site policy comparison report."

## What do you need to create site policy comparison reports?

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

## How to create site policy comparison reports

To create site policy comparison reports, follow these steps:

1. **Locate the report**: Sign in to the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219) with the [SharePoint administrator](sharepoint-admin-role.md) credentials for your organization. In the left pane, expand **Reports** and then select **Site Policy configuration**.
:::image type="content" source="media/sam-site-policy-comparison/site-policy-comparison-create.png" alt-text="Screenshot showing the Site Policy creation page in SharePoint admin center." lightbox="media/sam-site-policy-comparison/site-policy-comparison-create.png":::

1. **Start creating the new report**: Select the **New report** button to bring up the report wizard. You'll be guided through two steps to create your report. Watch for the callout that explains what "Similarity of content" means—the system looks at up to 5 of the most recently used files in your chosen site or sites and compares them semantically to files in the target sites.
:::image type="content" source="media/sam-site-policy-comparison/site-policy-comparison-overview.png" alt-text="Screenshot showing the site policy comparison report overview with step 1 of reference sites, step 2 of target sites, and the similarity of content call-out." lightbox="media/sam-site-policy-comparison/site-policy-comparison-overview.png":::
1. **Select the reference sites**: On the **Reference sites** page, pick up to 5 reference (input) sites that will serve as the basis for your comparison. Choose a site that contains files with similar types of content, such as contracts, agreements, statements of work, or project specifications. If the files in your reference site aren't alike, the matching results may not be as accurate. 
:::image type="content" source="media/sam-site-policy-comparison/site-policy-comparison-reference-site.png" alt-text="Screenshot showing the reference site selection page where administrators can choose one or more sites to serve as the baseline for policy comparison." lightbox="media/sam-site-policy-comparison/site-policy-comparison-reference-site.png":::
1. **Select the scope of comparison**: On the **Scope** page, pick which sites to compare, known as the "target" sites. You can compare up to 10,000 target sites. There are two ways to provide information about the target sites.
    1. As the first option, the admin can select specific site properties, and only the top sites that match those properties will be included in the comparison.
    :::image type="content" source="media/sam-site-policy-comparison/site-policy-comparison-scope.png" alt-text="Screenshot showing the scope selection page where administrators can filter target sites by properties like site type, creation date, and sensitivity label." lightbox="media/sam-site-policy-comparison/site-policy-comparison-scope.png":::
    1. Another option is to upload a CSV file with site URLs. The CSV file should have a header named "SiteURL" and contain the URLs of the target sites you want to compare. You can download a sample CSV file from the **Set scope** page.
    :::image type="content" source="media/sam-site-policy-comparison/site-policy-comparison-scope-csv.png" alt-text="Screenshot showing the option to upload a CSV file containing site URLs for target sites." lightbox="media/sam-site-policy-comparison/site-policy-comparison-scope-csv.png":::

> [!NOTE]
> For comparison, only the top 10 recently used files in a site for both reference sites and target sites.

1. **Name the report**: On the **Report name and review** page, provide an appropriate name for the report, review your reference sites and target sites. Then select **Finish**.
:::image type="content" source="media/sam-site-policy-comparison/site-policy-comparison-review.png" lightbox="media/sam-site-policy-comparison/site-policy-comparison-review.png" alt-text="Screenshot showing the report naming and review page where administrators can name the report and review selected reference and target sites.":::
:::image type="content" source="media/sam-site-policy-comparison/site-policy-comparison-in-progress.png" alt-text="Screenshot showing the site policy comparison report in progress with status indicating the report is being generated." lightbox="media/sam-site-policy-comparison/site-policy-comparison-in-progress.png":::

    The report is now placed in a queue for processing. For large number of sites, it can take up to 48 hours to finish processing and generate the report.
    :::image type="content" source="media/sam-site-policy-comparison/site-policy-comparison-in-que.png" alt-text="Screenshot showing the site policy comparison report in queue status while waiting to be processed." lightbox="media/sam-site-policy-comparison/site-policy-comparison-in-que.png":::

## How to read the site policy comparison report

Let's use the following sample report to understand the different sections of the site policy comparison report, and what each part means.
:::image type="content" source="media/sam-site-policy-comparison/site-policy-comparison-sample-report.png" alt-text="Screenshot showing a sample site policy comparison report with total sites analyzed, sites with high similarity, and policy mismatches identified." lightbox="media/sam-site-policy-comparison/site-policy-comparison-sample-report.png":::
This report displays sites that have been semantically matched with your reference site or sites and got a "similarity" score of 80% or higher. While the visual report shows the top 100 matched sites, you can download a complete list of all matched sites as a CSV file. 

In this example:
- **Total sites analyzed**: 1,300 sites were included in the comparison scope
- **Sites with high similarity**: 150 sites got a similarity score of 80% or higher
- **Policy mismatches identified**: 60 sites have one or more policy settings that differ from the reference site or sites

## Policies included in the comparison

The report compares five key security policies across your sites:

1. **Sensitivity label**: The [sensitivity label applied to the site](/sharepoint/authentication-context-example#set-a-sensitivity-label-to-apply-the-authentication-context-to-labeled-sites)
2. **External sharing**: Whether external users can access the site
3. **Conditional access**: Access restrictions based on conditions like location or device
4. **Block download**: Whether users are prevented from downloading files
5. **Restricted site access**: Access limited to specific groups or users

The report helps you quickly identify sites with similar content but different security policies. This ensures you can apply consistent policies across your organization. 

To investigate policy differences:

- Look for exclamation marks (!) that highlight policy mismatches
- Select the site name to examine its content and settings
- Navigate to the **[Active sites](/sharepoint/manage-sites-in-new-admin-center)** page in SharePoint admin center for additional management options

## Limitations

- **Maximum sites**: You can include up to 10,000 sites in the target scope for comparison.
- **Site access review**: Currently, you can't initiate a [site access review](site-access-review.md) from this report.
