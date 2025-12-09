---
title: "Configure AMSI integration with SharePoint Server"
ms.reviewer: 
ms.author: v-jmathew
author: jitinmathew
manager: serdars
ms.date: 03/06/2025
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: integration
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 763613ac-83f4-424e-99d0-32efd0667bd9
description: "Learn to secure environments and respond to associated threats from the attacks through AMSI."
---

# Configure AMSI integration with SharePoint Server

[!INCLUDE[appliesto-xxx-2016-2019-SUB-xxx-md](../includes/appliesto-xxx-2016-2019-SUB-xxx-md.md)]

## Introduction

The cybersecurity landscape has fundamentally changed, as evidenced by large-scale, complex attacks, and signals that [human-operated ransomware](/security/compass/human-operated-ransomware) are on the rise. More than ever, it's critical to keep your on-premises infrastructure secure and up to date, including SharePoint Servers. 

To help customers secure their environments and respond to associated threats from the attacks, we're introducing integration between SharePoint Server and the Windows
[Antimalware Scan Interface](/windows/win32/amsi/antimalware-scan-interface-portal) (AMSI). AMSI is a versatile standard that allows applications and services to integrate with any AMSI-capable anti-malware product present on a computer. 

The AMSI integration functionality is designed to prevent malicious web requests from reaching SharePoint endpoints. For example, to exploit a security vulnerability in a SharePoint endpoint before the official fix for the security vulnerability has been installed.

Starting with SharePoint Server Subscription Edition (SPSE) Version 25H1, the AMSI extends its scanning capabilities to include the bodies of HTTP requests. This request body scan feature is useful for detecting and mitigating threats that may be embedded in request payloads, providing a more comprehensive security solution.

> [!NOTE]
> The new request body scan feature is available for SharePoint Server Subscription Edition users only. It has been available in the Early Release ring until now and will be included in the Standard ring starting with the SPSE 2025 September PU. Early Release ring users may see "Full Mode" as the default mode for body scan since SPSE 2025 September PU.

## AMSI integration with SharePoint Server

When an AMSI-capable antivirus or anti-malware solution is integrated with SharePoint Server, it can examine `HTTP` and `HTTPS` requests made to the server and prevent SharePoint Server from processing dangerous requests. Any AMSI-capable antivirus or anti-malware program that is installed on the server performs the scan as soon as the server starts to process the request.

The purpose of AMSI integration isn't to replace existing antivirus/anti-malware defenses already installed on the server; it's to provide an extra layer of protection from malicious web requests made to SharePoint endpoints. Customers should still deploy SharePoint-compatible antivirus solutions on their servers to prevent their users from uploading or downloading files with viruses.

## Prerequisites

Before enabling AMSI integration, check the following prerequisites on each SharePoint Server:

- Windows Server 2016 or higher
- SharePoint Server Subscription Edition Version 22H2 or higher
- SharePoint Server 2019 build 16.0.10396.20000 or higher (KB 5002358: March 14, 2023 security update for SharePoint Server 2019)
- SharePoint Server 2016 build 16.0.5391.1000 or higher (KB 5002385: April 11, 2023 security update for SharePoint Server 2016)
- Microsoft Defender with AV engine version at 1.1.18300.4 or higher (alternatively, a compatible AMSI-capable third-party antivirus/antimalware provider)

## Activate/Deactivate AMSI for SharePoint Server

Starting with the September 2023 security updates for SharePoint Server 2016/2019 and the Version 23H2 feature update for SharePoint Server Subscription Edition, AMSI integration with SharePoint Server becomes enabled by default for all web applications within SharePoint Server. This modification aims to enhance the general security of customer environments and mitigate potential security breaches.

To initiate the September 2023 security updates, customers only need to install the update and run the SharePoint Products Configuration Wizard.

> [!NOTE]
> If customers skip installing the September 2023 public update, this change is activated upon their installation of the subsequent public update that includes the September 2023 security updates for SharePoint Server 2016/2019 or the Version 23H2 feature update for SharePoint Server Subscription Edition.
>
> Starting with the September 2025 Public Update, AMSI integration for SharePoint Server Subscription Edition/2016/2019 is a mandatory component and can no longer be deactivated.

If customers prefer not to have AMSI integration enabled automatically within their SharePoint Server farms, they can follow these steps:

1. Install the September 2023 security updates for SharePoint Server 2016/2019 or the Version 23H2 feature update for SharePoint Server Subscription Edition.
1. Run the SharePoint Products Configuration Wizard.
1. Follow the standard steps to disable the AMSI integration feature in your web applications.

If you follow these steps, SharePoint won't attempt to re-enable the feature while installing future public updates.

## Configure AMSI via user interface

If you're using versions earlier than the September 2025 Public Update for SharePoint Server 2016 and 2019 or earlier versions of SharePoint Server Subscription Edition Version 25H1, follow these steps to manually deactivate or activate the AMSI integration for each web application:

1. Open **SharePoint Central Administration**, and select **Application Management**.
2. Under **Web Applications**, select **Manage web applications**.
3. Select the web application for which you want to enable the AMSI integration, and select **Manage Features** in the toolbar.
4. On the **SharePoint Server Antimalware Scanning** screen, select **Deactivate** to switch off AMSI integration, or select **Activate** to switch on AMSI integration.

If you installed the SharePoint Server Subscription Edition Version 25H1 feature update, follow these steps to activate or deactivate and configure the AMSI integration settings:

1. Open **SharePoint Central Administration**.

2. Go to the **Security section**.

3. Select **AMSI Configuration**.

4. On the AMSI Scan Configuration page, select the desired web application.

5. Next, you can choose to enable or disable the AMSI scan feature by selecting the appropriate option.

    - To enable the AMSI scan, select the **Enable AMSI scan feature** button. This ensures all HTTP request headers are scanned.
    - To disable the scan, select the **Disable AMSI scan feature fully** button.

6. After enabling, select the Request Body Scan mode for scanning the request body according to your specific requirements from the following available options:

    - **Off**: Disables body scanning. This won't affect the existing header scanning feature.
    - **Balanced Mode**: Scans request bodies that are sent to system-predefined sensitive endpoints and other endpoints that are specified to be included in the body scan.
    - **Full Mode**: Scans request bodies that are sent to all endpoints except those explicitly excluded, to improve performance while maintaining fair security assurance.

7. Specify the endpoints that should be included or excluded from the body scan as per the mode you selected and click **Add**.

    Ensure that the endpoints contain the whole request URI path. For example, include `/SitePages/Home.aspx`, so it can scan URLs like `http://test.contoso.com/SitePages/Home.aspx`, and `http://test.contoso.com/sites/marketing/SitePages/Home.aspx`. To understand the syntax structure of URI, refer to [Uniform Resource Identifier - Wikipedia](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier).

    :::image type="content" source="../media/amsi-configuration-body-scan-page.png" alt-text="Screenshot of the AMSI Scan Configuration page with different modes." lightbox="../media/amsi-configuration-body-scan-page.png":::

8. After making the necessary changes, select **OK** to apply them effectively.

> [!NOTE]
>
> - Each web application must be configured for AMSI independently, and the specified endpoints list applies only to that web application.
> - The new body scan feature will remain disabled after the upgrade if the AMSI is disabled for a web application.
> - Body scanning can't be enabled without enabling header scanning.
> - The default configuration for body scan is the Balanced Mode. After upgrading to SPSE Version 25H1, any web application that had AMSI enabled will also have body scanning enabled in the Balanced Mode.

## Configure AMSI using PowerShell

Alternatively, you can activate/deactivate AMSI integration for a web application using PowerShell commands.

To deactivate, run the following PowerShell command:

```powershell
Disable-SPFeature -Identity 4cf046f3-38c7-495f-a7da-a1292d32e8e9 -Url <web application URL>  
```

To activate, run the following PowerShell command:

```powershell
Enable-SPFeature -Identity 4cf046f3-38c7-495f-a7da-a1292d32e8e9 -Url <web application URL> 
```

After upgrading to SharePoint Server Subscription Edition Version 25H1 build, you can also configure the body scan settings using PowerShell. To set the body scan mode, run the following command:

```powershell

$webAppUrl = "http://spwfe"

$webApp = Get-SPWebApplication -Identity $webAppUrl

$webApp.AMSIBodyScanMode = 1 # 0 = Off, 1 = Balanced, 2 = Full

$webApp.Update() # To save changes

# Iisreset # restarting the IIS service or recycling the app pool may be required when switching modes
```

To set the body scan mode to Balanced Mode with targeted endpoints, run the following command:

```powershell
# Get current list of targeted endpoints

$webApp.AMSITargetedEndpoints

# Add a targeted endpoint

$webApp.AddAMSITargetedEndpoints('/test/page123', 1)

# Get a certain targeted endpoint

$webApp.GetAMSITargetedEndpoint('/test/page123')

# Remove a targeted endpoint

$webApp.RemoveAMSITargetedEndpoints('/test/page123')

# Update the web app object to save changes

$webApp.Update()
```

To set the body scan mode to Full Mode with excluded endpoints, run the following command:

```powershell
# Get current list of excluded endpoints

$webApp.AMSIExcludedEndpoints

# Add an excluded endpoint

$webApp.AddAMSIExcludedEndpoints('/test/page123', 1)

# Get a certain excluded endpoint

$webApp.GetAMSIExcludedEndpoint('/test/page123')

# Remove an excluded endpoint

$webApp.RemoveAMSIExcludedEndpoints('test123456')

# Update the web app object to save changes

$webApp.Update()
```

## Test and verify AMSI integration with SharePoint Server

You can test the Antimalware Scan Interface (AMSI) feature to verify that it's working correctly. This involves sending a request to SharePoint Server with a special test string that Microsoft Defender recognizes is for testing purposes. This test string isn't dangerous, but Microsoft Defender treats it as if it's malicious so you can confirm how it behaves when it encounters malicious requests.

If AMSI integration is enabled in SharePoint Server and is using Microsoft Defender as its malware detection engine, the presence of this test string results in the request being blocked by AMSI instead of being processed by SharePoint.

The test string is similar to the [EICAR test file](https://www.eicar.org/download-anti-malware-testfile/) but differs slightly to avoid URL encoding confusion.

You can test AMSI integration by adding the test string as either a query string or an HTTP header in your request to SharePoint Server.

### Use a query string to test AMSI integration

```
amsiscantest:x5opap4pzx54p7cc7$eicar-standard-antivirus-test-fileh+h*
```

**For example**: send a request to https://servername/sites/sitename?amsiscantest:x5opap4pzx54p7cc7$eicar-standard-antivirus-test-fileh+h*

```powershell
Invoke-WebRequest -Uri "https://servername/sites/sitename?amsiscantest:x5opap4pzx54p7cc7$eicar-standard-antivirus-test-fileh+h*" -Method GET
```

### Use an HTTP header to test AMSI integration

```
amsiscantest: x5opap4pzx54p7cc7$eicar-standard-antivirus-test-fileh+h*
```

**For example**: send a request that looks like the following.

```
GET /sites/sitename HTTP/1.1
Host: servername
amsiscantest: x5opap4pzx54p7cc7$eicar-standard-antivirus-test-fileh+h*
```

Microsoft Defender detects this as the following exploit:

```
Exploit:Script/SharePointEicar.A
```

> [!NOTE]
> If you're using a malware detection engine other than Microsoft Defender, then you should check with your malware detection engine vendor to determine the best way to test its integration with the AMSI feature in SharePoint Server.

## Other references

### Performance effects of using Microsoft Defender as the primary AMSI solution

By default, [Microsoft Defender Antivirus](https://support.microsoft.com/windows/stay-protected-with-windows-security-2ae0363d-0ada-c064-8b56-6a39afb6a963) (MDAV), an AMSI-capable solution, is automatically enabled and installed on endpoints and devices that are running Windows 10, Windows Server 2016, and later. If you haven't installed an antivirus/anti-malware application, SharePoint Server AMSI integration works with MDAV. If you install and enable another antivirus/anti-malware application, MDAV automatically turns off. If you uninstall the other app, MDAV automatically turns back on, and the SharePoint Server integration will work with MDAV.

The benefits of using MDAV on SharePoint Server include:

- MDAV fetches signatures that match malicious content. If Microsoft learns about an exploit that can be blocked, a new MDAV signature can be deployed to block the exploit from affecting SharePoint.
- Using existing technology to add signatures for the malicious content.
- Using the expertise of Microsoft's malware research team for adding signatures.
- Using best practices that MDAV already applies for adding other signatures.

There might be a performance impact on the web application because AMSI scanning uses CPU resources. There's no distinct performance impact observed from AMSI scanning when tested with MDAV and no changes to be made to the existing documented SharePoint Server antivirus exclusions. Each antivirus provider develops their own definitions that utilize AMSI technology. Therefore, your level of protection remains dependent on how quickly your specific solution can be updated to detect the latest threats.

### Microsoft Defender version via the command line

> [!NOTE]
> If you're using Microsoft Defender, you can use the command line and ensure to update the signatures with the latest version.

1. Launch `Command Prompt` as an Administrator.
2. Navigate to `%ProgramData%\Microsoft\Windows Defender\Platform\<antimalware platform version>`.
3. Run `mpcmdrun.exe -SignatureUpdate`.

These steps determine your current engine version, check for updated definitions, and report.  

```powershell
Copyright (C) Microsoft Corporation. All rights reserved.
C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2105.5-0>MpCmdRun.exe -SignatureUpdate
Signature update started . . .
Service Version: 4.18.2106.6
Engine Version: 1.1.18300.4 
AntiSpyware Signature Version: 1.343.1364.0
AntiVirus Signature Version: 1.343.1364.0
Signature update finished. No updates needed
C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2105.5-0>
```

