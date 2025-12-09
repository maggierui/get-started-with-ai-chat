---
title: Certificate Based Authentication for migration
description: How to use Certificate Based Authentication in SharePoint migration in Microsoft 365.
author:      zacsun-ms # GitHub alias
ms.author: zhaosu
ms.reviewer: heidip
ms.service: microsoft-365-admin
audience: ITPro
ms.topic: upgrade-and-migration-article
mscollection: 
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.date:     04/03/2025
manager: dapodean
ms.localizationpriority: medium
search.appverid: MET150
---

# Migration Manager with Certificate Based Authentication

Migration Manager allows customers to use Azure App Registrations with certificate authentication as the identity model to migrate network file share to SharePoint and OneDrive.

## Preparation Steps

### 1. Register an application

Follow [the instructions](/entra/identity-platform/quickstart-register-app?tabs=certificate) to register an application in the Microsoft Entra admin center. Let's name this application **MigApp**.

### 2. Grant permissions

In the Microsoft Entra admin center, go to **Application > App registrations** and select 'MigApp' from the **All applications** tab.

Next, grant the necessary API permissions on the **API Permissions** page.

To limit 'MigApp' to move content into specific SharePoint sites, grant the 'Sites.Selected' permission under the SharePoint and Microsoft Graph API.

- SharePoint API:
  - 'Sites.Selected': Required for REST and CSOM (Client-Side Object Model) calls.
   - Microsoft Graph API:
      - 'Sites.Selected': Required for site-related operations.
      
To allow 'MigApp' to move content into all SharePoint sites, grant ‘Sites.FullControl.All’ permission under the SharePoint and Microsoft Graph API.

- SharePoint API:
  - 'Sites.FullControl.All': Required for full control of all site collections.
  - Microsoft Graph API:
     - 'Sites.FullControl.All': Required for full control of all site collections.
     
Grant more permissions

- Microsoft Graph API:
  - 'User.Read.All': Required for resolving user mapping.
  - 'Group.Read.All': Required for resolving user mapping.
  - 'Organization.Read.All': Required for sending telemetry to the correct Geo location.

### 3. Upload the certificate

Go to the **Certificates & secrets** page and select the **Certificates** tab.

- Upload the public key of your X.509 certificate issued by the Enterprise Public Key Infrastructure (PKI).
- Copy the value in 'Thumbprint' for future use.

## Grant destination site access permission

If you set the SharePoint **Sites.Selected** permission for 'MigApp', you need to grant the application **FullControl** permissions for **all the migration destination sites** before the migration starts.

## Grant the SharePoint Admin site Read permission

You also need to grant the application **Read** permissions for **SharePoint Admin site** before the migration starts.

## Install agent

On the agent workstation, install your X.509 certificate, issued by the Enterprise Public Key Infrastructure (PKI), at Windows certificate management store 'Current User' path. You can launch the certificate management application by typing the command `certmgr.msc`.

Prepare a configuration Json file with the following content:

```json
{
    "Thumbprint":"The client credential certificate thumbprint",
    "TenantId":"Tenant ID",
    "ClientId":"App registration Id",
    "AdminUrl": "The SharePoint Admin site URL, example https://contoso-admin.sharepoint.com",
}
```

Install an agent by following [the instructions](/sharepointmigration/mm-setup-clients). In the agent setup Welcome page, select the "Certificate Authentication" option and load the certificate auth config file, which is prepared in the previous step. Then complete the rest installation steps.

- If the file contains incorrect attribute values, the agent displays an error message to explain the reason and disables the next button.
- If 'MigApp' doesn't have sufficient permissions, the agent displays an error message reminding you to grant necessary permissions to the app.

After the agents are launched successfully, you can start migrating your content on Migration Manager.

## Steps to grant permission to a site

### Use Graph API to grant permission to a site

Follow the steps to grant permissions to a given site using Microsoft Graph API.

1. Obtain the site ID by calling [Get Site API](/graph/api/site-get).
- To retrieve the site ID of the admin site, call GET /sites/contoso-admin.sharepoint.com
- To retrieve the site ID of root site, call GET /sites/contoso.sharepoint.com.
- To retrieve the site ID of other sites, call GET /sites/contoso.sharepoint.com:/sites/{site relative url} or GET /sites/contoso.sharepoint.com:/teams/{site relative url}.

The **ID property** in the response body contains three parts separated by commas; ensure you copy the entire string.

2. Assign permissions to the site by calling [Create Permission API](/graph/api/site-post-permissions). Using the string copied from Step 1, call POST /sites/{**siteId**}/permissions with the request body.
- For assigning permissions to the admin site, set the roles as **read**.
- For any other site, set the roles as **owner**.

```json
    {
      "roles": ["read/write/owner"],
      "grantedToIdentities": [{
        "application": {
          "id": "IdOfYourEntraApp",
          "displayName": "NameOfYourEntraApp"
        }
      }]
    }
```

### Use PowerShell PnP to grant permission to a site

Follow the steps to grant permission to a site using [PowerShell PnP](https://pnp.github.io/powershell/cmdlets/Grant-PnPAzureADAppSitePermission.html).

1. Install Powershell7 and import required modules with the command:

`Install-Module PnP.PowerShell -Force and Import-Module PnP.PowerShell`

2. Run the command to create an app that plays as a proxy of PnP-PowerShell for granting permissions. Copy the client ID from the execution result.

`Register-PnPEntraIDAppForInteractiveLogin -ApplicationName "PnP PowerShell" -Tenant yourtenant.onmicrosoft.com -Interactive`

3. Set a variable PnPClientId with the client ID retrieved in the previous step.

`$PnPClientId = <The client ID from the step above>`

4. Run the command to Connect SharePoint Admin site. The admin URL is in the format `https://contoso-admin.sharepoint.com`.

`Connect-PnPOnline –interactive  –Url <AdminSiteUrl>  -ClientId <PnPClientId>`

5. Grant your app the SharePoint Admin site access permission. The 'ClientId' is your entra app client ID.

`Grant-PnPAzureADAppSitePermission -AppId <ClientId> -DisplayName <App name or a random name> -Permissions ``<Permission> -Site <DestinationSiteUrl>`

- To grant your app the SharePoint Admin site Read permission, the command is:

`Grant-PnPAzureADAppSitePermission -AppId <ClientId> -DisplayName <App name or a random name> -Permissions `**`Read`** `-Site <`**`AdminSiteUrl`**`>`

- To grant your app FullControl permission for the destination site, the command is:

`Grant-PnPAzureADAppSitePermission -AppId <ClientId> -DisplayName < App name or a random name > -Permissions `**`FullControl`** `-Site <`**`DestinationSiteUrl`**`>`
