---
ms.date:     04/07/2025
title:       Use Certificate Based Authentication in migration
description: Describing how to use Certificate Based Authentication in SharePoint migration.
author:      zacsun-ms
ms.author:   zhaosu
manager:     dapodean
ms.reviewer: heidip
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
ms.topic: upgrade-and-migration-article
search.appverid: MET150

---

# Migrate with Certificate Based Authentication

Certificate Based Authentication (CBA) is supported in SPMT (SharePoint Migration Tool) builds newer than v4.1.125.11.

SPMT allows customers to use Azure App Registrations with certificate authentication as the identity model to migrate on-premises content to SharePoint and OneDrive.

## Preparation Steps

### 1. Register an application

Follow [the instructions](/entra/identity-platform/quickstart-register-app?tabs=certificate) to register an application in the Microsoft 365 admin center. Let's name this application 'MigApp'.

### 2. Grant permissions

1. In the Microsoft 365 admin center, go to **Application > App registrations** and select 'MigApp' from the **All applications** tab.
2. Next, grant the necessary API permissions under **API Permissions** page.
3. To limit 'MigApp' to move content into specific SharePoint sites, grant the 'Sites.Selected' permission under the SharePoint and Microsoft Graph API.

- SharePoint API:
  - 'Sites.Selected': Required for REST and CSOM (Client-Side Object Model) calls.
- Microsoft Graph API:
  - 'Sites.Selected': Required for site-related operations.

4. To allow 'MigApp' to move content into all SharePoint sites, grant 'Sites.FullControl.All' permission under the SharePoint and Microsoft Graph API.

- SharePoint API:
  - 'Sites.FullControl.All': Required for full control of all site collections.
- Microsoft Graph API:
  - 'Sites.FullControl.All': Required for full control of all site collections.

5. Grant more permissions

- Microsoft Graph API:
  - 'User.Read.All': Required for resolving user mapping.
  - 'Group.Read.All': Required for resolving user mapping.
  - 'Organization.Read.All': Required for sending telemetry to the correct Geo location.
- SharePoint API:
  - 'TermStore.ReadWrite.All': Required for reading and writing managed metadata (necessary for SharePoint term store migration).
- Dynamic CRM API:
  - 'user_impersonation': Required for accessing Common Data Service as organization users (necessary for migrating SharePoint workflows to Power Automate).

### 3. Upload certificate

Go to the **Certificates & secrets** page, and select the **Certificates** tab.
- Upload the public key of your X.509 certificate issued by the Enterprise Public Key Infrastructure (PKI).
- Copy the value in 'Thumbprint' for future use.

## Grant destination site access permission

If you set the SharePoint **Sites.Selected** permission for 'MigApp' you need to grant the application **FullControl** permissions for all the migration destination sites before the migration starts.

You can use either the Microsoft Graph API or PowerShell PnP to grant these permissions:

- Microsoft Graph API: Grant the **Owner** permission role on the sites. You can find detailed instructions in [Create permission - Microsoft Graph v1.0](/graph/api/site-post-permissions?view=graph-rest-1.0&preserve-view=true&tabs=http).
- PowerShell PnP: Use “Grant-PnPAzureADAppSitePermission” command to set the **FullControl** permission. Detailed instructions are available on the [Grant-PnPAzureADAppSitePermission page](https://pnp.github.io/powershell/cmdlets/Grant-PnPAzureADAppSitePermission.html).

## Using CBA with SPMT

On the workstation that SPMT is installed, install your X.509 certificate at Windows certificate management store 'Current User' path. You can launch the certificate management application by typing the command `certmgr.msc`.

Prepare a configuration file named **CertificateConfig.json** with following content:

```json
{
    "Thumbprint":"thumbprint for the cert",
    "TenantId":"Tenant ID",
    "ClientId":"App registration Id"
}
```

Copy **CertificateConfig.json** under %appdata%\Microsoft\MigrationToolStorage. If the folder doesn't exist, create it manually. Then, launch SPMT.

- If the **CertificateConfig.json** file contains the correct attributes, SPMT starts without prompting for SharePoint admin credentials.
- If the file is incorrectly formatted or contains incorrect attribute values, SPMT displays the message "The application will exit because of sign-in failure" followed by an error message explaining the reason for the failure.
- If the file isn't provided, SPMT prompts you to enter SharePoint admin credentials.

Additionally, if 'MigApp' doesn't have sufficient permissions, all migrations fail with one of the following error messages:
- "Sorry, you can’t create this site. Enter a different SharePoint Online site URL or contact your administrator" if the target site doesn't exist.
- "Invalid site URL" if the target site already exists.

## Setup for Workflow migration

To enable 'MigApp' to migrate SharePoint workflows to Power Automate, you need to do extra configuration.

**Make 'MigApp' a Service Principal for the Power Platform**

Use PowerShell to register 'MigApp' with Microsoft Power Platform ([learn more](/power-platform/admin/powershell-create-service-principal)).

```powershell
Install-Module -Name Microsoft.PowerApps.Administration.PowerShell
Import-Module -Name Microsoft.PowerApps.Administration.PowerShell
Add-PowerAppsAccount [-Endpoint 
New-PowerAppManagementApp -ApplicationId $appId]
```

For a detailed explanation of `Add-PowerAppsAccount`, refer to [link](/powershell/module/microsoft.powerapps.administration.powershell/add-powerappsaccount?view=pa-ps-latest&preserve-view=true).

**Grant 'MigApp' Access to the Power Platform Environment**

Follow [the instruction](/power-platform/admin/manage-application-users) to create an application user. Make sure you select 'MigApp' after you select **'+ Add an app'** in step 6. Assign the 'System Administrator' role to the new application user.
