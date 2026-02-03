# Rapport_Bluetooth_BLE
**Sécurisation et supervision d’un système d’information**
---

![image](https://github.com/user-attachments/assets/724af864-bdb9-4ff2-9d48-731ab769d034)

---

## Introduction
L’objectif de ce TP est d’étudier le fonctionnement du Bluetooth et du Bluetooth Low Energy (BLE) à travers plusieurs manipulations pratiques, incluant : 

- La découverte d’appareils 
- L’appairage entre PC et smartphone 
- L’échange de fichiers 
- La création d’une balise BLE personnalisée 

Ce travail ne se limite pas à une approche théorique, mais que chaque étape démontrer concrètement le bon fonctionnement des outils utilisées. De plus l’ensemble des manipulations a été réalisé sur des postes fonctionnant sous Linux Debian 13. 

---

## Partie 1 — Bluetooth
Cette partie couvre les manipulations pratiques du Bluetooth “classique” : découverte d’appareils, appairage, envoi/réception de fichiers, et collecte d’informations.

### 1) Lister les appareils Bluetooth
Sur Debian Linux, la pile Bluetooth par défaut s’appelle BlueZ. Elle fournit des outils en ligne de commande pour interagir avec des appareils Bluetooth. Les commandes principalement utilisées pour scanner sont bluetoothctl et hcitool.

![image](https://github.com/user-attachments/assets/3f3f26bd-d01c-46de-a6f6-48dc55e1e240)
- scan on : permet de lancer un scan pour détecter tous les appareils Bluetooth dans les environs
- Les appareils trouvés s’affichent avec leurs adresse MAC (ex : 1A:2B:3E:8F:6D:4A) et le nom de l’appareil qu’il diffuse.

![image](https://github.com/user-attachments/assets/79baa3bc-c5d9-4cb5-99d2-34a7686bf14b)
- hcitool scan : liste les appareils Bluetooth visibles autour du poste de travail

### 2) Appairage et Connexion
Pour l’appairage et la connexion, on utilise la commande bluetoothctl :

![image](https://github.com/user-attachments/assets/70bf56f5-8852-4ad4-b601-9b0a6446ccfb)
- agent on : active un agent qui gère le pairing.
- default-agent : définit l’agent en tant qu’agent par défaut
- pair <MAC> : lance l'appairage avec l’appareil Bluetooth.
- trust <MAC> : fait confiance à l’appareil pour faciliter les connexions futures
- connect <MAC> : connecte l’appareil une fois appairé.

Une fois connecté à un appareil, on peut afficher des infos détaillées tels que le nom,
l’addresse MAC, les profils disponibles et parfois le niveau de batterie de l’appareil

![image](https://github.com/user-attachments/assets/b0c7da4a-7cb0-4ed2-bb27-c7f7766921b8)

### 3) Envoi et réception de fichiers
Sur Debian, la gestion de transfert via bluetoothctl n’est pas gérée directement. Dans
ce cas, on peut utiliser la commande obexftp.

![image](https://github.com/user-attachments/assets/491b486f-064f-46f2-8583-bd31a36a7184)

---

## Partie 2 - BLE (Bluetooth Low Energy)
Le BLE est une version de Bluetooth optimisée pour la basse consommation. Les outils changent légèrement par rapport au Bluetooth classique.

### 1) Créer une balise BLE
Pour émettre des messages à partir d’une balise BLE, on peut utiliser des bibliothèques Python comme bleak ou bless.

![image](https://github.com/user-attachments/assets/49278934-c990-4a54-87c6-ae8eba8d73cf)

J’ai utilisé plusieurs scripts pour tenter de créer une balise personnalisée et la seule qui a fonctionné sur mon poste, le script ble_beacon.py. Ce script permet de t transformer un PC Linux en balise Bluetooth Low Energy (BLE) en diffusant un nom et un service via BlueZ.

![image](https://github.com/user-attachments/assets/ba788656-447c-4fc9-beb5-fd7491f29b9e)

- Définit le nom de la balise, l’UUID du service BLE diffusé et l’interface Bluetooth utilisée.

