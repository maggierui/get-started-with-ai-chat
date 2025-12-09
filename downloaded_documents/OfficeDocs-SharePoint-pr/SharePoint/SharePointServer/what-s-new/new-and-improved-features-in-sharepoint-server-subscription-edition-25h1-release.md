---
ms.date: 04/02/2025
title: "New and improved features in SharePoint Server Subscription Edition Version 25H1"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: overview
ms.service: sharepoint-server-itpro
ms.localizationpriority: high
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition Version 25H1."
---

# New and improved features in SharePoint Server Subscription Edition Version 25H1

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn about the new features and updates introduced in the SharePoint Server Subscription Edition Version 25H1 feature update. 

## Summary of the features

The following table provides a summary of the new features introduced in the SharePoint Server Subscription Edition Version 25H1 feature update.

|**Feature**|**Release ring**|**More information**|
|:-----|:-----|:-----|
| **Support for RSA public key in OIDC authentication configuration**   |Standard release   |For more information, see [Support for RSA public key in OIDC authentication configuration](new-and-improved-features-in-sharepoint-server-subscription-edition-24h2-release.md#support-for-rsa-public-key-in-oidc-authentication-configuration).<p> This was part of Early release in the Version 24H2 feature update.<p>**Note:** This feature is still in Early ring for technical issues, and will roll out to Standard ring after resolution.|
| **Support for automatic machine key rotation**  |  Early release   | For more information, see [Support for automatic machine key rotation](#support-for-automatic-machine-key-rotation).|
| **Dynamic customer survey by One Customer Voice**  | Early release  | For more information, see [Dynamic customer survey by One Customer Voice](#dynamic-customer-survey-by-one-customer-voice). |
| **Create new Office files in client apps**   |Early release   |For more information, see [Create new Office files in client apps](#create-new-office-files-in-client-apps).|
| **Support for request body scan in AMSI**   |Early release   |For more information, see [Support for request body scan in AMSI](#support-for-request-body-scan-in-amsi).|
| **Cloud Hybrid Search upgrade**   |Early release   |For more information, see [Cloud Hybrid Search upgrade](#cloud-hybrid-search-upgrade).|
| **New database connectivity layer with TDS 8.0 and TLS 1.3 support**   |Standard release   |For more information, see [New database connectivity layer with TDS 8.0 and TLS 1.3 support](#new-database-connectivity-layer-with-tds-80-and-tls-13-support).|
| **Support for Microsoft Graph connector**   |Standard release   |For more information, see [Support for Microsoft Graph connector](#support-for-microsoft-graph-connector).|

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition Version 25H1.

> [!NOTE]
> Features previously introduced in the Version 24H2 feature update won't be described here. For more information on Version 24H2, see [New and improved features in SharePoint Server Subscription Edition Version 24H2](new-and-improved-features-in-sharepoint-server-subscription-edition-24h2-release.md). 

### Support for automatic machine key rotation

The objective of automatic machine key rotation is to enhance security by regularly updating machine keys without manual intervention, thus reducing the risk of key compromise. This feature ensures seamless and automatic rotation of machine keys while maintaining high availability and reliability of SharePoint services during key rotation.

The feature incorporates a Key Management Service that handles storage, retrieval, and distribution of machine keys using a timer job called Machine Key Rotation Job. The timer job is configured to run automatically on the last Sunday of every month by default.

For more information, see [Improved ASP.NET view state security and key management](../security-for-sharepoint-server/improved-asp-net-view-state-security-key-management.md).

### Dynamic customer survey by One Customer Voice

[One Customer Voice (OCV)](new-and-improved-features-in-sharepoint-server-subscription-edition-24h1-release.md#customer-feedback-experience-in-central-administration) was introduced in SharePoint Server Version 24H1 for gathering feedback from farm administrators. When enabled, it prompts administrators with a Net Promoter Score (NPS) survey via a dialog box on the Central Administration page, collecting data like NPS score, reason for the score (optional), contact email (optional), farm ID, and SharePoint Server version. The initial prompt appears two weeks after the administrator first opens Central Administration page and every six months. If dismissed, the dialog box reappears after two weeks and administrators can disable or enable this feature via PowerShell.

To further enhance the flexibility and effectiveness of the OCV feature, the SharePoint Server now introduces the new Dynamic Survey functionality. This feature allows us to configure and display surveys dynamically to gather administrator feedback based on current needs. It offers flexibility to configure the survey type, rating questions, survey rating scale and options, comment question, and whether to collect user emails. Additionally, the frequency of survey prompts can be configured at both the user and survey levels.

> [!NOTE]
> This feature overwrites the OCV feature released in Version 24H1. Therefore, the popup rule from the first iteration of this feature will no longer be triggered.

For more information, see [Configure feedback for SharePoint Server](../administration/configure-ocv.md).

### Create new Office files in client apps

This feature enhances the user experience by allowing the creation of new Office documents in a SharePoint Server farm, even when [Office Online Server (OOS)](/officeonlineserver/office-online-server), also known as Web Access Components (WAC) or Office Web Apps, isn't configured or unavailable.

Previously, if OOS was unavailable, new Office documents couldn't be created from the document library in the browser. Additionally, even if Content Types were enabled for the library without OOS/WAC, a new file would be created without a file extension but couldn't be opened in a browser or client app.

Now, new Office document creation can be initiated in the browser and completed in the client-side application. The **New** button in the library toolbar launches the new document within the client-side Office application. Also, if Content Types are enabled for the library without OOS/WAC, they're shown in the **New** drop-down. Selecting one creates a new file of that type and opens it in the appropriate client application. For example, selecting **Word document** under the **New** menu creates a new docx file in the library and opens it in the Word client application.

> [!NOTE]
> If OOS is unavailable and the client machine doesn't have the Office installed, then selecting an Office file type from the **New** drop-down creates an empty file in the library. This mirrors the old behavior but the file will have the correct extension.

:::image type="content" source="../media/create-new-office-file-spse.png" alt-text="Screenshot displaying the New button with file extensions in the browser of SharePoint library.":::

### Support for request body scan in AMSI

The Antimalware Scanning Interface (AMSI) feature now has the ability to scan the body of web requests. The request body scan feature enhances the existing anti-malware scan capabilities in SharePoint Server Subscription Edition by extending its reach to include the bodies of HTTP requests.

This is useful for detecting and mitigating threats that might be embedded in request payloads, providing a more comprehensive security solution. Users can also choose from the available modes such as Balanced and Full mode for scanning request body.

For more information, see [Configure AMSI integration with SharePoint Server](../security-for-sharepoint-server/configure-amsi-integration.md).

### Cloud Hybrid Search upgrade

Search Content Service (SCS), an internal component of Cloud Hybrid Search in SharePoint in Microsoft 365 will be retired starting June 30, 2025. To continue using Cloud Hybrid Search, it's necessary to upgrade your SharePoint Server farm to SharePoint Server Subscription Edition Version 25H1 for improved scalability and security. Without this upgrade, previous versions of SharePoint Server can only search on-premises and Microsoft 365 content separately using Hybrid Federated Search. 

This update requires patching for SharePoint Server and reonboarding the Hybrid Search Service Application (Cloud SSA) in the on-premises farm using a PowerShell script. 

For more information on upgrading an existing Cloud SSA, see [Configure cloud hybrid search - roadmap](../hybrid/configure-cloud-hybrid-searchroadmap.md#connect-your-cloud-search-service-application-to-your-microsoft-365-organization).

### New database connectivity layer with TDS 8.0 and TLS 1.3 support

The SharePoint Server Subscription Edition Version 25H1 build introduces a new database connectivity layer called [Microsoft.Data.SqlClient](/sql/connect/ado-net/overview-sqlclient-driver?view=sql-server-ver16&preserve-view=true) for .NET-based applications. This new database connectivity layer supports advanced security capabilities such as TLS 1.3 that couldn't be supported in our previous database connectivity layer, that is, [System.Data.SqlClient](/dotnet/framework/data/adonet/sql/) library. It also enables SharePoint Server to take advantage of other new SQL capabilities, such as SQL Server and Azure SQL features.

The following are the capabilities of the new Microsoft.Data.SqlClient library:

- **Support for Tabular Data Stream (TDS) Version 8.0**: The new TDS version 8.0 is secure by default, requiring encrypted connections and supporting newer encryption protocols like TLS 1.3. This also ensures compatibility with older TLS versions while enhancing security.
- **Support for Transport Layer Security (TLS) Version 1.3**: This new build update provides support for connecting to SQL databases using TLS 1.3 connection encryption, addressing design concerns of previous versions. This enables better database connections, ensuring even backward compatibility with older SQL Server versions.

For more information, see [Transport Layer Security (TLS) 1.3 Support](../security-for-sharepoint-server/tls-support-1.3.md).

### Support for Microsoft Graph connector: 

Starting from Version [16.0.17928.20238](https://support.microsoft.com/topic/description-of-the-security-update-for-sharepoint-server-subscription-edition-november-12-2024-kb5002651-0e3d5086-13f2-4bc2-b42b-88d45a9377c3) released in November 2024, SharePoint Server Subscription Edition supports Microsoft Graph connector. With [Microsoft Graph connectors](/microsoftsearch/connectors-overview), Microsoft Search or Microsoft 365 Copilot in your organizations can index and leverage data stored in SharePoint Server. Microsoft Graph connector respects the source permissions configured in SharePoint Server, ensuring users access only authorized content.<p>
For more information, see [SharePoint Server Microsoft Graph connector](/microsoftsearch/sharepoint-server-connector).
