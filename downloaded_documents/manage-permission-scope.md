---
ms.date: 02/11/2025
title: "Manage Permission Scopes in SharePoint"
ms.reviewer: dilucesr
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: concept-article
ms.service: sharepoint-online
ms.collection:  
- Strat_SP_modern
- M365-collaboration
- essentials-security
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid:
- SPO160
- MET150
ms.localizationpriority: high
description: "In this article, you learn about effectively managing permission scopes in SharePoint, including key concepts, best practices, and the implications of breaking inheritance to maintain optimal performance and security"
---
# Manage Permission Scopes in SharePoint

Effectively managing permissions in SharePoint is essential for security and proper user access. As the number of documents in SharePoint sites increases, poor design and implementation can quickly lead to permission scope limits, negatively affecting performance. This article explains permission scopes and access control mechanisms, offering best practices for designing and managing permission scopes efficiently within SharePoint.
First, let’s review some key components related to permission scopes. 

## Key concepts and components

- Access Control List—An Access Control List (ACL) is composed of a set of Access Control Entries (ACEs). 
- Access Control Entry—An Access Control Entry (ACE) in SharePoint is a combination of a principal and a rights mask (read, read/write). 
- Principal—A principal can be an individual user or a [group](/microsoft-365/admin/create-groups/compare-groups). If a group is present in an ACE within an ACL, all members of that group are granted the permission level specified by the ACE. 
- Permission scope—A permission scope is a uniquely secured object. This means that its ACL can be set differently from its parent. Files and folders can have the same permissions if they're all part of the same directory tree. You can have up to 50,000 unique ACLs within a document library, but for best performance it’s recommended that you keep it under 5,000. 
- Permission inheritance—By default, a site collection contains multiple sites. Each site can have one or more lists and document libraries, all of which inherit their permissions from the site collection. Similarly, folders, lists, and documents inherit permissions from the parent object that contains them. For more information, see [Customize permissions for a SharePoint list or library](https://support.microsoft.com/office/customize-permissions-for-a-sharepoint-list-or-library-02d770f3-59eb-4910-a608-5f84cc297782). 
- Unique permissions—By default, a file or folder inherits the permissions of the library or folder that contains it. When a file is assigned "unique permissions," it stops inheriting permissions from its parent and can have its permissions set independently. This means that the file or folder now has its own permission scope. 

## Permission scope and permission inheritance

In SharePoint, ACLs are used to manage permissions for objects (files and folders). Each ACL consists of multiple ACEs, which specify the permissions for a principal. 

When a document library is created, it has a single permission scope, meaning all files and folders within the document library [inherit their ACL](https://support.microsoft.com/office/customize-permissions-for-a-sharepoint-list-or-library-02d770f3-59eb-4910-a608-5f84cc297782#bkmk-permission) from the root of the document library and share the same permissions. The initial scope count is 1. 

### Breaking inheritance 

Breaking inheritance on a file or folder creates a new permission scope, increasing the scope count by 1. 

You can break the inheritance using two methods:

- You can [break inheritance manually](https://support.microsoft.com/office/customize-permissions-for-a-sharepoint-list-or-library-02d770f3-59eb-4910-a608-5f84cc297782#bkmk-break-inheritance) by going to the settings of the library.  
- If you share a file or folder, this action breaks permission inheritance on the file or folder, allowing its ACL (and the content within the folder) to differ from its parent. 

This article discusses the implications of breaking inheritance using the second method and outlines best practices for minimizing the addition of excessive scope counts in a library.

For example, if you create a document library, then make a folder, share the folder (which breaks inheritance), and upload 75,000 files to the folder, the document library's scope count is 2. This is because all 75,000 files in the folder share the folder's permission scope and therefore its ACL. There are only two unique ACLs in the document library: the ACL at the root and the ACL on the folder. If you create multiple files and share each one individually with a user, you add a scope count each time. To avoid this, put all the files in the same folder and share the folder instead. 

### Sharing folders with large item counts 

A folder can only break its inheritance if it has 100,000 or fewer items. If a folder exceeds this limit and isn't uniquely shared, it can't be uniquely shared later. Therefore, share large folders before they hit 100,000 items. Ideally, share a folder when it contains zero items if you know it needs unique sharing. 

### Shared ACLs for files with inherited permissions 

If two files have the equivalent ACL because they both inherit from the parent folder, then they share an ACL. Only the parent folder counts. However, if two files have the same ACL because they were shared separately with the same principals, they'll have two permission scopes with identical permissions. 

### Impact of breaking inheritance on scope count 

If a folder has two files in it and you share them both with a user, that will cost you three scopes: one for the parent folder and one for each of the files that was shared individually. It doesn't matter that you shared both files with the user and the ACLs of the files are identical. Once you break the inheritance of a file or folder from its parent, you create a unique scope. 

### Efficient sharing to avoid exceeding scope limits 

If you have 10,000 files that you want to share with a user and you share each file individually, that will cost 10,000 scopes, degrading performance as you have exceeded the recommended 5,000 limit. However, if you make a folder, share the folder with the user, and then move all 10,000 files into that folder, it will only cost you one additional scope (for the folder). If you had previously shared each of those 10,000 files individually, one by one, and move them to a common folder that has an identical ACL, you would have still exceeded the limit (the system doesn't "clean up" these permissions on your behalf by restoring permission inheritance). 

### Understanding the scope limit 

The [recommended 5,000 limit](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits#unique-security-scopes-per-list-or-library) for ACLs means you can have up to 5,000 unique ACLs. It doesn't mean you can only have 5,000 files or folders with ACLs. If two files inherit the same ACL from their parent folder, they share that ACL. In this case, only the parent folder's ACL counts towards the limit. However, if two files have the same ACL, but it's explicitly set, not via inheritance from their parent folder, each file’s ACL, plus the parent folder’s ACL, counts towards the limit. 
Actual performance can vary depending on factors like the size of the ACLs. If the ACLs are small (fewer than 10 ACEs per ACL), you can exceed 5,000 scopes without encountering issues. However, with larger ACLs (up to 5,000 ACEs), you might experience performance problems before reaching the limit. 

## Example scenarios 

### Scenario: Sharing files 

Sharing two files in a folder with a single user uses three scopes: one for the parent folder and one for each of the two files. Even though both files are shared with the same user and have the same ACL, breaking inheritance from the parent folder creates unique scopes. Therefore, if you have 10,000 files to share with the user and share each one individually, it requires 10,000 additional scopes. However, if you place all the files into a single folder, share that folder with the user, and then move the files into the folder, it will only require one additional scope for the folder. 
One important point to consider is co-authoring. If a user is working on a file in Microsoft Word and wants to co-author with someone, they can still invite them if the file is in SharePoint. Doing so uses one of the remaining ACLs available. This is an additional factor to consider. 

### Scenario: Moving files

Imagine a situation where 10,000 files have been shared with an individual one by one. If these files are later moved into a single folder, the system doesn't automatically consolidate the permission entries to apply only the folder's permissions. Instead, the permissions remain cluttered unless the user manually corrects them. This is because automatic restoration of the permission hierarchy isn't implemented due to security concerns. 
In this scenario, before the files are moved, the recipient can view each of the 10,000 files individually shared with them. After moving the files into a folder, the recipient can still see the 10,000 files along with the containing folder, which changes the access structure. This means that without manual cleanup, extensive sharing from one's OneDrive could lead to performance issues or even operational failure once the limit of 50,000 items is reached. 
However, careful management, where files are organized into folders with matching ACLs, can help mitigate these issues. It's also important to note that exposing the actual folder hierarchy to users might be undesirable, especially when using metadata to represent everything instead of traditional folders. 

### Scenario: Creating a document library with minimal scopes
 
You create a document library that has a single permission scope, meaning that all items within it initially share the same access control settings. Next, you add a folder to this document library. To share this folder with specific individuals or groups, you break the inheritance of permissions from the document library. This action creates a new, unique permission scope for the folder, allowing you to set different access controls than those applied to the document library. 
With the folder's permissions set, you proceed to upload 75,000 files into this folder. Each of these files inherits the folder's ACL, ensuring that they all have the same permissions as the folder itself. 
As a result, the document library now has two unique permission scopes: one for the root of the document library and another for the folder. This setup allows for more granular control over who can access the files within the folder, while maintaining a simpler permission structure for the rest of the document library. 

### Scenario: Managing permissions for multiple folders

To efficiently map categories to folders, you decide to create 20 folders within each document library. Each of these folders is designated for a specific type of document, such as contracts or invoices, allowing for better organization and easier access. 
To ensure that each folder has its own unique permissions, you set up individual ACL settings for each one. This results in a total of 21 unique permission scopes within the  document library: one for the root of the document library and one for each of the 20 folders. By doing this, you can control who has access to each category of files, providing a more secure and organized structure. 
To avoid performance issues and stay within the system's limits, you minimize the number of individual files with unique permissions. This means that the majority of files inherit the permissions of their respective folders, keeping the total number of unique permission entries well within the 5,000 limit.  

## Tips for managing permission scopes 

To effectively manage permission scopes in SharePoint, follow these recommendations:

- Minimize the number of unique permission scopes by leveraging inheritance. 
- Share folders instead of individual files to reduce the number of unique scopes. 
- Ensure folders that need unique permissions are shared before they exceed 100,000 items. 
- For developers, regularly review and minimize unique permission scopes, use groups, and monitor performance to maintain optimal SharePoint performance. 
- For end users, use default permission groups, review access requests, and conduct regular audits to keep SharePoint permissions clean and efficient. 
- Use [SharePoint groups](/sharepoint/dev/general-development/authorization-users-groups-and-the-object-model-in-sharepoint#users-groups-and-principals) and [Microsoft Entra](/entra/fundamentals/what-is-entra) for managing user references and permissions efficiently. 

## Resources

- [SharePoint Limits - Service Descriptions](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits)