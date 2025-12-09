---
ms.date: 04/02/2025
title: "Migration Manager settings"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: upgrade-and-migration-article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
description: "A complete listing of the Migration Manager basic and advanced settings." 
---

# Migration Manager Settings

The following table details the settings available in the Migration Manager. Only your IT professional should manage the Advanced settings.

**General**
 
|**Setting**                     |**Description**                                                               |
|:-------------------------------|:-----------------------------------------------------------------------------|
|Only perform scanning           |If you wish to scan the files as a preassessment to migration, set to **On**. |
|Preserve file share permissions |Preserve permissions on the files migrated.                                   |

**Users**

|**Setting**            |**Description**|
|:----------------------|:--------------|
|Microsoft Entra lookup |By default, this setting is set to **On**. If no user mapping file is provided by the user, then Microsoft Entra ID is used as the default for user mapping. |
|User mapping file      |By default, *Microsoft Entra lookup* is used to map users when submitting migration jobs. If you want to use your own mapping file, select the file to be used by clicking **Choose file**. </br>If you choose to use a custom user mapping file and want to preserve user permissions, turn off *Microsoft Entra lookup*. By doing so, if a user isn't found in the mapping file, the tool doesn't look them up in Microsoft Entra ID. </br>You can also leave the **Microsoft Entra ID** setting on AND use a custom mapping file. If domain users can't be found in the mapping file, the tool autodetects destination users and its source user’s Security Identifier (SID). |

**Filters**

|**Setting**                                       |**Description**|
|:-------------------------------------------------|:--------------|
|Migrate hidden files                              |If set to **Off**, hidden files are **not** migrated. |
|Migrate files created after                       |Only migrate files created after the selected date. This setting can be used to limit the number of files migrated or to adhere to overall company governance policy regarding file retention. |
|Migrate files modified after                      |Only migrate files modified after the selected date. This setting can be used to limit the number of files migrated or to adhere to overall company governance policy regarding file retention. |
|Don't migrate files with these extensions         |Enter a list of file extensions of file types you don't want to migrate. Separate each extension entered with a colon. Don't include the dot. Example: TXT:EXE:JPEG: </br>**Note**: For files with multiple file extensions, for example, EXT1 or EXT2, add only the last extension, EXT2, to the exclusion list. |
|Migrate files and folders with invalid characters |By default, the setting is set to **On**. This value is the recommended setting. The tool attempts to move all files without filtering on characters. If any file can't be accepted, a failure message is generated for that file.<br/>If set to **Off**, the tool skips any potential special characters. While turning off the setting can improve performance when the source potentially contains a high number of files containing invalid characters, it also has drawbacks. To prevent malicious activities, source packages that generate more than 100 errors to the destination server are blocked. As a result, all valid files in that package are also blocked. |

**Advanced**

|**Setting**                      |**Description** |
|:--------------------------------|:---------------|
|Migration auto rerun             |Upon failure, retry task up to four times.</br></br>**Note:** This setting is scheduled for deprecation. We recommend you set it to **Off**. |
|Migration Manager working folder |A temporary working folder is created named `%appdata%\Microsoft\SPMigration`. </br>Make sure that your working folder has a minimum of 150 GB of free space. It may need more depending on the size of the data you plan to migrate. |
