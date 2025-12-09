---
ms.date: 05/02/2025
title: "Guidance for retiring Delve in your organization"
ms.reviewer: 
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: overview
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.localizationpriority: medium
ms.custom: admindeeplinkSPO
search.appverid:
- SPO160
- MOE150
- DEL150
- FRP150
- MET150
ms.assetid: 54f87a42-15a4-44b4-9df0-d36287d9531b
description: "With the December 2024 planned retirement of Delve, this article contains information to assist administrators with the Delve offboarding process."

---

# Guidance for retiring Delve in your organization

In December 2024, Delve was retired. This change was first announced in an MC Post available in the [Microsoft 365 Message Center](https://admin.microsoft.com/Adminportal/Home?#/MessageCenter/:/messages/MC698136). There's also an article you can refer to, [Alternatives to Delve in Microsoft 365](https://support.microsoft.com/office/alternatives-to-delve-in-microsoft-365-59e29736-de90-40ce-93ee-0bbe23902a42), that focuses on helping end users find alternatives for their tasks within Microsoft 365. The purpose of this article is to assist administrators with the Delve offboarding process.

## What was retired?

Delve offers many features that are built on top of multiple Microsoft 365 services. When we say we're retiring Delve, it's important to note that we're not changing or retiring anything on the services side. Both documents and people data that are surfaced in Delve continue to be stored and managed as today.

There are a couple of exceptions regarding data storage. Delve stores a limited set of Delve-specific data, such as list of users recently viewed in Delve, Delve favorite documents, Delve favorite tags, and some Delve-specific settings. These are retired together with Delve. You can export this data before December 16, 2024, in Delve by going to **Select settings** > **Feature settings** > **Export data**.

## Where can users view user properties currently surfaced in Delve?

Starting December 2024, properties currently surfaced in Delve, including custom user profile properties, are added to the profile cards available in search experiences on Microsoft365.com, Office.com, and in SharePoint. Eventually, these changes are enabled everywhere the profile card is available. However, for technical reasons, this change takes time. For December 2024, we recommend directing users to Microsoft365.com, Office.com, or SharePoint, which also offer a people search similar to what's offered in the Delve search.

## Direct links to profile cards

The modern search experiences on Microsoft365.com, Office.com, and in SharePoint include profile pages built on the same data as profile cards. They have a unique link and can be used in documentation, email signatures, and other related resources. Starting December 16, we'll handle redirects from Delve profiles to these profile pages on Microsoft365.com. Although there are three URLs that offer the same experience and continue to work for some time, we suggest you start using the new domain, m365.cloud.microsoft.

### Example links

For m365.cloud.microsoft:
`https://m365.cloud.microsoft/search/overview?pp=<User.aadObjectId@TenantId>|UPN`  
`https://m365.cloud.microsoft/search/overview?pp=11111111-1111-4a21-acea-db38b244ac46%4022222222-2222-49c2-99e6-c5c0f6f8ead1%7CAdeleV%40M365x14029536.OnMicrosoft.com`

For Microsoft365.com:  
`https://www.microsoft365.com/search/overview?pp=<User.aadObjectId@TenantId>|UPN`  
`https://www.microsoft365.com/search/overview?pp=11111111-1111-4a21-acea-db38b244ac46%4022222222-2222-49c2-99e6-c5c0f6f8ead1%7CAdeleV%40M365x14029536.OnMicrosoft.com`

For Office.com:  
`https://www.office.com/search/overview? pp=<User.aadObjectId@TenantId>|UPN`  
`https://www.office.com/search/overview?pp=11111111-1111-4a21-acea-db38b244ac46%4022222222-2222-49c2-99e6-c5c0f6f8ead1%7CAdeleV%40M365x14029536.OnMicrosoft.com`

For SharePoint:  
`https://<tenant>.sharepoint.com/_layouts/15/search.aspx/overview? pp=<User.aadObjectId@TenantId>|UPN`  
`https://<tenantname>.sharepoint.com/_layouts/15/search.aspx/overview?pp=11111111-1111-4a21-acea-db38b244ac46%4022222222-2222-49c2-99e6-c5c0f6f8ead1%7CAdeleV%40M365x14029536.OnMicrosoft.com`

## What happens to existing URLs pointing to Delve or SharePoint profiles?

Both Delve URLs and SharePoint profile URLs are redirected to the modern search profile pages on Microsoft365.com. For tenants not using Delve today, there are no change to URLs and their legacy profile experiences in SharePoint. However, they get the extended profile page in modern search and the extended profile cards across Microsoft 365, which include the properties that are visible in Delve.

Below are all the URLs that redirect to modern search profile pages on Microsoft365.com. If you are using a third-party solution with crafted Delve URLs or have internal documentation that for some reason is providing URLs not in this list, these need to be updated. One option is to remove the subdomain and just use the main domain (delve.office.com). Another is to update your solution to support the new profile URLs in modern search. Examples of these URLs can be found at another place on this page.

`https://delve.office.com`<br/>
`https://gcc.delve.office.com`<br/>
`https://delve-gcc.office.com`<br/>
`https://nam.delve.office.com`<br/>
`https://eur.delve.office.com`<br/>
`https://apc.delve.office.com`<br/>
`https://gbr.delve.office.com`<br/>
`https://can.delve.office.com`<br/>
`https://lam.delve.office.com`<br/>
`https://sfeur.delve.office.com`<br/>
`https://sfnam.delve.office.com`

## How can administrators control which custom user profile properties are visible on profile cards?

Administrators can control the visibility of custom user profile properties on the profile card by adjusting the Policy Setting and Display Setting for the specific custom user profile property in the SharePoint admin center. To show a property, ensure the Default Privacy Setting under Policy Setting is set to "Everyone" and select "Show in the profile properties section of the user's profile page" under Display Settings. To hide a property, make sure "Show in the profile properties section of the user's profile page" is not selected. For more details, refer to the article [Add and edit user profile properties in SharePoint](/sharepoint/add-and-edit-user-profile-properties).  
![Screenshot showing the Policy Setting and Display Setting in SharePoint admin center.](media/delve-retirement/image.png)



## Where can users edit properties they used to edit in Delve?

A new edit profile experience, tightly coupled with the profile card, was released in December 2024. It allows users to easily edit their profiles across Microsoft 365. Only properties that were editable in Delve are editable in the new edit profile experience. For some properties, like custom user profile properties, user have to go to the SharePoint edit profile experience. To make this effortless, a link to the SharePoint edit profile experience is part of the new edit profile experience.
For more information on the new edit profile experience, visit [Profile editor in Microsoft 365](https://support.microsoft.com/en-us/office/edit-your-profile-in-microsoft-365-e7056090-56d4-4b81-bb3f-b6af31089ebe).

:::image type="content" source="media/delve-retirement-legacy-edit-experience-in-sharepoint.png" alt-text="Screenshot showing how to access the legacy edit experience in SharePoint.":::
The link to the legacy SharePoint edit profile experience.

:::image type="content" source="media/delve-retirement-edit-profile-in-sharepoint.png" alt-text="Screenshot showing the Edit Details dialog box in SharePoint." lightbox="media/delve-retirement-edit-profile-in-sharepoint.png":::
The SharePoint Edit Details dialog box.

## What do the new edit experience in profile cards look like?

The new edit profile experience is built on top of Microsoft 365 profile cards, and it is presented in an overlay as profile cards are handled today. A most common user pattern is for the user to open their own profile card and select "edit profile." Instead of being redirected to Delve, the edit experience opens in the profile card. Below is an example of what this process looks like.

Please note that if the new edit profile experience isn't yet enabled in the experience where a user is, selecting "edit profile" redirects the user to the modern search profile page on Microsoft365.com.

:::image type="content" source="media/delve-retirement-profile-card-with-update-button.png" alt-text="Screenshot showing an example of a profile card with the Update button.":::

:::image type="content" source="media/delve-retirement-lpe-with-background.png" alt-text="Screenshot showing an example of a profile card and personal data." lightbox="media/delve-retirement-lpe-with-background.png":::

## Where can users search for people and user profile properties that are currently supported in Delve?

Users can search for people in the modern search experience in Microsoft365.com, Office.com, and SharePoint. Classic search continues to work as before and clicks on people results that today link to Delve redirects to the modern search profile page on Microsoft365.com.

Note that people are presented in multiple ways in modern search. Selecting a people result in the "all" vertical takes the user to the modern search profile experience. Selecting on people results in the people vertical opens the large profile card. Both experiences include properties that today are surfaced in Delve.

## Custom people search solutions

If your tenant depends on custom solutions for people search it should continue to work as before. They're built on services powering Delve and not on the Delve experience itself. One common third-party solution in use is the PnP Modern Search app. This particular app allows administrators to create custom search-based experiences based on SharePoint web parts. It's easy to configure people results to support opening profile cards on hover and click. It's also possible to include links to Delve profiles and the legacy SharePoint profile (_person.aspx_/_personimmersive.aspx_). These links continue to work as users are redirected to the modern search profile page in Microsoft365.com.

## Properties not supported by the new edit experience

In general, the new edit experience built on profile cards supports editing properties in the profile card, but there are exceptions. One exception is with properties hosted by Microsoft Entra ID and synced to UPA (SharePoint). By default, these aren't editable in Delve or in the legacy profile edit experience in SharePoint. However, administrators can override the default behavior to make them editable for the user. If administrators make this change, some properties can be edited in Delve, and some can be edited in the legacy edit profile experience in SharePoint.

The new edit profile experience built on profile cards won't support editing these properties. Users can still edit them if administrators have made the setting changes mentioned above, in the legacy edit profile experience, but by default they'll not be visible anywhere and only provide value if you have a custom solution. The following list contains these properties.

### Properties synced from Microsoft Entra ID that aren't editable (by default) in Delve

- UserPrincipalName
- DisplayName
- GivenName
- Sn
- telephoneNumber
- proxyAddresses
- PhysicalDeliveryOfficeName
- Title
- Department
- WWWHomePage
- PreferredLanguage
- msExchHideFromAddressList
- Manager

## When is Delve no longer be available?

Delve was retired on December 16, 2024. The extended profile card experience, the updated profile pages in modern search, and the new edit profile experience are available before Delve was retired. For a limited period, both Delve and the new experiences are available for users. Delve retires when the redirect of Delve URLs is activated.

## What do we recommend administrators do?

- Educate your users about the upcoming changes by updating internal documentation and training material relevant for the Delve retirement.
- Once released, validate that your users can solve their Delve tasks in the new edit profile experience, updated profile pages in modern search, people search in Microsoft365.com, and in the extended profile cards.

## More resources

[Edit your profile in Microsoft 365](https://support.microsoft.com/en-us/office/edit-your-profile-in-microsoft-365-e7056090-56d4-4b81-bb3f-b6af31089ebe)

[Alternatives to Delve in Microsoft 365](https://support.microsoft.com/office/alternatives-to-delve-in-microsoft-365-59e29736-de90-40ce-93ee-0bbe23902a42)

[Add and edit user profile properties in SharePoint](add-and-edit-user-profile-properties.md)

[Tips and tricks on how to search for organizational content more effectively](https://techcommunity.microsoft.com/t5/microsoft-search-blog/tips-and-tricks-on-how-to-search-for-organizational-content-more/ba-p/3838452)

[Profile cards in Microsoft 365](https://support.microsoft.com/en-us/office/profile-cards-in-microsoft-365-e80f931f-5fc4-4a59-ba6e-c1e35a85b501)

[User profile synchronization](user-profile-sync.md)

[Unified cloud.microsoft domain for Microsoft 365 apps](/microsoft-365/enterprise/cloud-microsoft-domain)
