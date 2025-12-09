---
ms.date: 11/21/2025
title: "Initiate site access reviews for Data access governance reports"
description: "Learn about how to initiate site access reviews as a remedial action for data access governance for SharePoint sites."
recommendations: true
audience: Admin
customer-intent: As a SharePoint administrator, I want to initiate site access reviews for data access governance reports.
f1.keywords: NOCSH
ms.topic: how-to
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
ms.reviewer: pullabhk
ms.author: ruihu
author: maggierui
manager: dansimp
search.appverid:

---

# Initiate site access reviews for Data access governance reports

Site access reviews in the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219) allow [IT administrators](/microsoft-365/admin/add-users/assign-admin-roles) to delegate the process of reviewing data access governance reports to site owners of overshared sites.

This review process is crucial because:

- IT administrators can't access file-level or item-level details due to compliance reasons.
- Site owners are best positioned to review and address oversharing issues for their own sites.

> [!NOTE]
> Site access review is supported only for SharePoint sites. It's currently not supported for OneDrive accounts.

## What do you need to initiate a site access review?

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

In addition, before initiating a site access review, ensure that you meet the following requirements:

- A nongovernment cloud tenant environment or GCC-Moderate government cloud environment. Site access reviews aren't supported in government cloud environments (GCCH, DoD, Gallatin).
- Admin credentials for accessing the SharePoint admin center.
- Site owners, who are available to respond to review requests, take necessary actions, and complete the review.

## How site access review works

- You can initiate site access reviews for up to 100 sites directly from the web view of data access governance reports. 
- If you need to review a larger number of sites, use [PowerShell](/sharepoint/powershell-for-data-access-governance#initiate-site-access-review-using-powershell) to initiate reviews.
- When a review is initiated, the site owner receives an email tailored to the specific oversharing issue identified in the selected report. For example, if the review is for the "Content shared with 'Everyone except external users'" category, the email will focus only on sharing concerns related to that report.

## Supported reports

Site access reviews are available for the following reports:

- Sharing link reports (Anyone, PeopleInYourOrg, Specific People shared externally)
- "Content shared with 'Everyone except external users'" reports
- Oversharing baseline report using permissions

## How to initiate a site access review

1. Sign in to the SharePoint admin center with your admin credentials.
1. Expand the **Reports** section and select **Data access governance**.
1. Select **View reports** for any one of the [supported reports](#supported-reports).
1. Choose a report and select the sites you want to review.

   :::image type="content" source="./media/data-access-governance/initiate-site-access-review.png" alt-text="Screenshot that shows Initiate site access review for sites listed within DAG report" lightbox="./media/data-access-governance/initiate-site-access-review.png":::

1. Select **Initiate site access review**.
2. Select **Customize and preview email** to customize the email contents for site owners.

    :::image type="content" source="media/data-access-governance/customize-email-initiate-site-access-review.png" alt-text="Customize the email to be sent to site owners":::

3. Customize the message to site owners as described in the [email customization section](#customize-email-to-site-owners).
4. Select **Send** to initiate the review request.

Site access reviews can also be initiated using [PowerShell commands](powershell-for-data-access-governance.md#initiate-site-access-review-using-powershell).

> [!IMPORTANT]
> The number of Site access reviews that can be initiated from 'Site permissions across your organization' report is limited to 1000 per calendar month. The limit resets when the month changes.

## Track site access reviews

To track all initiated site access reviews, go to the **My review requests** tab on the Data access governance landing page.

:::image type="content" source="./media/data-access-governance/my-review-requests.png" alt-text="Screenshot that shows track all reviews initiated from a central page" lightbox="./media/data-access-governance/my-review-requests.png":::

Once a review is initiated, its status remains "pending" until the site owner completes it. After completion, the review status and comments will be updated with the reviewer's name and the date and time of completion. If a review fails (for example, due to an invalid email for the site owner), it's marked as failed.

You can track reviews using this [PowerShell command](powershell-for-data-access-governance.md#track-site-access-reviews-using-powershell) as well.

## Site access review process for site owners

When you initiate a review, site owners receive an email containing:

- A relevant title.
- Your comments (if any).
- A request to review site permissions.
- A link to a detailed access review page, specific to the identified issue in the data access governance report.

Here are examples of the different emails a site owner might receive:

- Content shared with 'Everyone except external users' report for the past 28 days:

    :::image type="content" source="./media/data-access-governance/email-eeeu-files-folders-lists.png" alt-text="Screenshot that shows email received by site owners for oversharing via EEEU" lightbox="./media/data-access-governance/email-eeeu-files-folders-lists.png":::

- Sharing links report for the past 28 days:

  :::image type="content" source="./media/site-access-review/3-email-sharing-links.png" alt-text="Screenshot that shows the detailed oversharing permissions reports email notification." lightbox="./media/site-access-review/3-email-sharing-links.png":::

- Oversharing baseline report using permissions:
  :::image type="content" source="./media/site-access-review/2-email-permissions-report.png" alt-text="Screenshot that shows the sharing links within the last 28 days report email notification." lightbox="./media/site-access-review/2-email-permissions-report.png":::

### Review 'Everyone Except External Users' site access requests

Site owners can review and manage access in two main areas:

- **SharePoint groups:**
  - View which groups contain 'Everyone except external users.'
  - See when and by whom the group was added.
  - Remove 'Everyone except external users' from groups if necessary:
    1. Open the SharePoint group membership page.
    2. Select **Everyone except external users**, select **Actions**, and select **Remove users from group**.

        :::image type="content" source="./media/data-access-governance/manage-sharepoint-group-membership.png" alt-text="Screenshot that shows displays sharepoint group members" lightbox="./media/data-access-governance/manage-sharepoint-group-membership.png":::

- **Individual items (files/folders/lists):**
  - View items shared with 'Everyone except external users' in the last 28 days.
  - See sharing details (who shared and when).
  - Manage access and remove permissions as needed:
    1. Select **Manage access**.
    1. Under the 'Everyone except external users' group in the **Groups** tab, select the group and select **Remove access**. See [Stop sharing OneDrive or SharePoint files or folders, or change permissions](https://support.microsoft.com/office/stop-sharing-onedrive-or-sharepoint-files-or-folders-or-change-permissions-0a36470f-d7fe-40a0-bd74-0ac6c1e13323) for more information.

        :::image type="content" source="./media/data-access-governance/site-owner-view-foreeeu-files.png" alt-text="Screenshot that shows view for site owner regarding items shared with eeeu." lightbox="./media/data-access-governance/site-owner-view-foreeeu-files.png":::

### Review 'Sharing link' reports

Once the site owner opens the email, they're redirected to a detailed sharing links report. This report shows:

- Files for which links were generated, with the date and the user who created the link.
- The **Manage access** button allows site owners to remove or modify permissions.

The following screenshot shows the detailed sharing links report:

:::image type="content" source="./media/site-access-review/6-detailed-sharing-links.png" alt-text="Screenshot that shows the detailed sharing links report." lightbox="./media/site-access-review/6-detailed-sharing-links.png":::

### Review 'Oversharing baseline using permissions' reports

When site owners select the email, they're redirected to the site access review page, where they can see the oversharing baseline using permissions report. This report helps site owners identify items with excessive permissions and take necessary actions.

:::image type="content" source="./media/site-access-review/5-detailed-permissions-report.png" alt-text="Screenshot that shows the oversharing baseline using permission reports email notification." lightbox="./media/site-access-review/5-detailed-permissions-report.png":::

The SharePoint admin views the number of users with permissions to a site in the Data access governance report. Site owners can see this number, along with how permissions are distributed across different site items. Items with the highest number of permissioned users are shown first, allowing the site owner to address the most exposed items.

### Understanding the permissions report

#### Number of permissioned users

This column shows the total number of users who have permissions to a specific scope (Site, List, Folder, or File). It reflects the exposure of that item compared to others. However, it's important to note that this number isn't unique—if the same user has both direct and indirect permissions, they're counted multiple times.

**Example**:

Imagine a folder "F" with the following permissions:

- 40 users from Group “A”
- 10 users with direct permissions
- 20 users with permissions via sharing links

The total number of permissioned users for folder "F" would be 80 (40 from Group “A” + 10 direct + 20 via sharing links). No deduplication is applied, so if the same user is in both Group “A” and has access via a sharing link, they're counted twice.

Additionally, the total number of permissioned users across all scopes might exceed the number of users shown in the email or Data Access Governance report. This happens because users can have permissions on multiple items. While a user might be counted once at the site level, they're counted separately for each item they have access to.

#### Number of groups

This column shows how many groups have permissions to a specific item or scope. Often, a large portion of exposure comes from permissions granted to groups, especially those with many members. Reducing exposure can be achieved by adjusting group memberships or removing unnecessary groups from permissions.

Select the **Group number** to see the membership count of each group. This helps you identify which groups to target for reducing permissions.

:::image type="content" source="./media/site-access-review/4-group-membership-details.png" alt-text="Screenshot that shows a specific group and its member count." lightbox="./media/site-access-review/4-group-membership-details.png":::

#### Links and EEEU/Everyone

This section displays:

- The number of links (for example, "Anyone" or "People in your organization") that have been shared for the scope.
- Whether the item is exposed to Everyone or EEEU (Everyone Except External Users).

If the number of links is high or the EEEU/Everyone column says "Yes," this is an immediate indicator that the item has broad exposure, and the site owner should focus on reducing permissions for that item.

#### Manage Access

The Manage Access button provides a way for the site owner to take action by:

- Removing individual users
- Modifying group memberships
- Deleting links
- Adjusting permissions

For a SharePoint site, selecting this button redirects to the **SharePoint group management** page. For individual items, it opens the **Manage Access** interface, allowing for more granular control over permissions.

### Complete site access reviews

Once the site owner makes necessary changes (like modifying or removing permissions), they should:

1. Select **Complete review**.
2. Add any relevant comments.
3. Submit the review.

Comments are sent back to the IT administrator, and the review will be marked as completed.

### Manage multiple site access reviews

Site owners can receive and handle multiple site access review requests simultaneously. To track all review requests:

 :::image type="content" source="./media/data-access-governance/site-review-master-page.png" alt-text="Screenshot that shows Master page to track all site review for a site." lightbox="./media/data-access-governance/site-review-master-page.png":::

1. Go to the **Site reviews** page via:
    - The link in the review email.
    - The gear icon on the site home page:
      1. Select **Site settings**.
      1. Select **Site reviews**.
   
          :::image type="content" source="./media/data-access-governance/site-review-from-gear-icon.png" alt-text="Screenshot that shows path to site review page from site home page under gear icon." lightbox="./media/data-access-governance/site-review-from-gear-icon.png":::
      1. View all pending site access reviews.
      1. Complete reviews as necessary.

## Customize email to site owners

Now you can customize the email sent to site owners to increase the probability that site owners treat the email as a genuine request from SharePoint admins and not treat it as a suspicious email. The following values are new/available for customization:

1. From address: This is automatically fetched from the custom username, as specified in Microsoft 365 admin center [under organizational profile](/microsoft-365/admin/email/select-domain-to-use-for-email-from-microsoft-365-products).
2. Title of the email
3. Message to the site owner that usually describes the scenario
4. Any additional comments related to the ask to review
5. A link to any SharePoint page or document that list details or further instructions

:::image type="content" source="media/data-access-governance/email-customization-dag.png" alt-text="customize message, comments and add links to SharePoint pages in emails to site owners":::

Select **Save** to save your customizations for this report type. This overrides any previous changes and will be fetched automatically for the subsequent site reviews from that report type. In other words, you can save a customized version for each report type, as shown in the Data Access Governance landing page. Select **Reset** to revert all customizations to product defined defaults.


