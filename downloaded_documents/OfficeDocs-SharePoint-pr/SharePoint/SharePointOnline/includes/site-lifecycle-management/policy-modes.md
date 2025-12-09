---
author: maggierui
manager: dansimp
ms.author: ruihu
ms.service: sharepoint-online
ms.topic: include
ms.date: 11/10/2025
---
### Policy modes

When setting up a site lifecycle policy, you can choose between a simulation policy and an active policy. 

#### Simulation mode

The simulation policy runs once and generates a report based on the set parameters. If it fails, you need to delete it and create a new one. Once you validate a simulation policy, you can convert it to an active policy.

> [!NOTE]
> Site lifecycle policies in simulation mode are now available in GCCH and DoD environments as of November 17, 2005.

#### Active mode

The active policy runs monthly, generating reports and sending notifications to site owners to confirm the site's status. If it fails during a particular month, it will run again on the next schedule. The policy enforces actions on sites that remain uncertified or unattested by the site owner or admin, provided you configured it to take enforcement actions.