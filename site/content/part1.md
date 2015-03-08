Title: Apache Thrift
NavOrder: 2
## Historique
Développé par Facebook en interne pour répondre à un besoin d'interconnection de différents programmes de plus en plus nombreux, Thrift a été légué à la Fondation Apache en 2007 dans le but d'enrichir les fonctionnalités du projet par l'intermédiaire d'une communauté active.

Aujourd'hui Apache Thrift est utilisé par dans différents programmes et projets comme Evernote, reCaptcha, Hypertable et bien entendu Facebook.

Points cléfs :

- Framework RPC (cross-language)
- Indépendant du langage
- Inclus : protocoles de transport, de sérialisation / déserialisation et création de serveurs
- Projet initié par Facebook (2006)
- Projet Apache depuis 2007
- Licence Apache (2.0)
- Version stable 0.9.2 (07-11-2014)

## Remote Procedure Call
RPC (Remote Procedure Call) est un protocole réseau permettant de faire des appels de procédures sur un ordinateur distant à l'aide d'un serveur d'applications. Ce protocole est utilisé dans le modèle client-serveur pour assurer la communication entre le client, le serveur et des éventuels intermédiaires.

<div style="text-align:center"><img src ="img/rpc.png" alt="Remote Procedure Call (RPC)"/></div>

## Richesse
### Langages
- C / C++ / C#
- Java
- JavaScript
- Objective-C
- Python
- PHP …
- … Perl / Ruby / Smalltalk / OCami  / Go / Haskell

### Plate-formes
Windows, Linux, OS X, IOS et Android

### Architecture
x86 et x64

## Pile de protocoles
<div style="text-align:center"><img src ="img/protocoles.png" alt="Pile de protocoles"/></div>

### Protocoles (sérialisation)
Un protocole spécifie comment les types de données utilisent le transport sous-jacent pour coder / décoder. Ainsi, la mise en œuvre du protocole régit le schéma de codage et est responsable de la (de)sérialisation. Quelques exemples de protocoles possibles JSON, XML, texte brut, binaire compact etc.

- TBinaryProtocol
- TCompactProtocol
- TDenseProtocol
- TJSONProtocol
- TSimpleJSONProtocol
- TDebugProtocol

### Transport (interface I/O)
La couche de transport fournit une abstraction simple pour la lecture / écriture de / vers le réseau. Cela permet à Thrift de découpler le transport sous-jacent du reste du système (sérialisation / désérialisation, par exemple).

- TSocket
- TFramedTransport
- TFileTransport
- TMemoryTransport
- TZlibTransport

### Serveurs
- TSimpleServer
- TThreadPoolServer
- TNonblockingServer

## Performance
<div style="text-align:center"><img src ="img/perf1.png" alt="Performance données"/></div>
<div style="text-align:center"><img src ="img/perf2.png" alt="Performance CPU"/></div>

## Applications

- Streaming

Communications caractérisées par un flux continu d'octets à partir d'un serveur vers un ou plusieurs clients.

- Messaging

Transmission de messages de façon asynchrone, souvent en file d'attente, les communications sont faiblement liées.

- Remote Procedure Calls (RPC)

Remote Procedure Call permet l’appel de fonctions entre processus sur différentes machines.

## Principe
<div style="text-align:center"><img src ="img/principe.png" alt="Principe"/></div>
