Title: Créer un service Thrift
NavOrder: 3
## Interface Definition Langage

Interface description language (appelé aussi interface definition language), est un langage voué à la définition de l'interface de composants logiciels, laquelle permet de faire communiquer des modules implémentés dans des langages différents, ou déployés à travers un réseau sur des systèmes hétérogènes (Windows, Linux, Mac OS X, VMS, etc.) dans la perspective d'architecture distribuée.

Proche de l'annotation C

- types (de base, structures, containers, exceptions, services)
- namespaces
- enum
- constante
- includes
- typedef
- commentaires

Extension « `.thrift` »

Génération de code
- `thrift --gen <language> <Thrift filename>`
- « `gen-<langage>/` »

## Thrift Types
### Types
Les types de base ont été choisis dans le but de simplicité et de clarté plutôt que l'abondance, en se concentrant sur les principaux types disponibles dans tous les langages de programmation.

| Type | Valeur |
|:-----:|-----|
| bool | booléen |
| byte | 8-bit signed integer |
| i16 | 16-bit signed integer |
| i32 | 32-bit signed integer |
| i64 | 64-bit signed integer |
| double | 64-bit floating point number |
| string | chaîne de caratères encodé en UTF-8 |
| binary | séquence d'octets non-encodé |

### Structures
Les structures Thrift définissent un objet commun - ils sont équivalents aux classes dans les langages de programmation orientée objet, mais sans héritage. Une structure est un ensemble de champs fortement typées, chacune avec un identifiant de nom unique. Les champs peuvent avoir diverses annotations qui sont décrits dans le Thrift IDL.

    struct <name> {
        <id>: <required | optional> <type> <field>;
    }

    struct Example {
        1:i32 number=10;
        2:i64 bigNumber;
        3:double decimals;
        4:string name="thrifty"
    }

### Containers
Les Thrift Containers sont fortement typés et correspondent aux collections couramment disponibles dans la plupart des langages de programmation.

Il y a trois types de conteneurs:

- `list<type>` : Une liste ordonnée d'éléments. Se traduit par un STL vecteur, Java ArrayList, tableaux natif dans les langages de script, etc.

- `set<type>` : Un ensemble non ordonné d'éléments uniques. Se traduit par un STL set, Java HashSet, set en Python, etc. Note: PHP ne supporte pas les sets, il est traité comme une liste

- `map<type 1,type 2>` : Une map de valeurs à clé unique. Traduit par une STL map, Java HashMap, PHP tableau associatif, dictionnaire Python / Ruby, etc. Les valeurs par défaut sont fournies, les mappages de type ne sont pas explicitement fixés.

Les conteneurs peuvent être de tout les types valides de Thrift.

### Exceptions
Les exceptions utilise la même syntaxe que les structures.

    exception <name> {
        <id>: <type> <field>;
    }

    exception MyException {
        1:string message;
    }

### Services
Les services sont définis en utilisant des types de Trift. Définir un service est sémantiquement équivalent à définir une interface (ou une classe abstraite virtuelle pure) dans la programmation orientée objet. Le compilateur Thrift génère un client et un serveur entièrement fonctionnels qui implémentent l'interface.

Un service se compose d'un ensemble de fonctions nommées, chacun avec une liste de paramètres et un type de retour.

A noter que vide est un type valide pour un retour de la fonction, en plus de tous les autres types que Thrift définies.
En outre, un mot-clé modificateur oneway peut être ajouté à une fonction de vide, qui va générer du code qui n'attend pas une réponse.
A noter aussi qu'une fonction vide pur renvoie une réponse au client qui garantit que l'opération est terminée du côté du serveur. Avec l'appelle d'une méthode oneway le client  aura seulement comme garantie que la demande a réussi à la couche de transport.

L'héritage de services est possible : `extends <service>`

    service <name> {
        <returntype> <name>(<id>:<argument>...)
            [throws (<exceptions>)]
            ...
    }

    service StringCache {
        void set(1:i32 key, 2:string value);
        string get(1:i32 key) throws (1:KeyNotFound knf);
        void delete(1:i32 key)
    }

### Enum

    enum TweetType {
        TWEET,
        RETWEET = 2,
        DM = 0xa,
        REPLY
    }  

### Includes
Il est possible, pour des raisons de lisibilité et d'organisation, d'inclure d'autres fichiers .thrift.

    include "tweet.thrift"

    struct Tweet {
        1:list<tweet.Tweet> tweets;
    }

### Namespaces
Les namespaces permettent de packager le code généré. Du fait que les notions (nommage, organisation) de package ou de namespace sont différents selon les langages, la création d'un namespace se fait au cas par cas.

    namespace cpp com.example.project
    namespace java com.example.project

    struct Example {
        1:i32 number=10;
        ...

- C++ : `namespace com { namespace example { namespace project {`
- Java : `package com.example.project`

### Constantes

    const i32 INT_CONST = 1234;
    const map<string,string> MAP_CONST = {"hello": "world", "goodnigth": "moon"};

    struct Example {
        1:i32 number=INT_CONST;

### Typesdef

    typedef i64 UserId

    struct Example {
        1:UserId bigNumber;
        ...

Dans certains langages, tel que le Java, la notion de typedef n'existe pas. Il est quand même possible de l'utiliser puisque chaque occurrence du type redéfini sera remplacé par sa vératible valeur.

## Versioning

Apache Thrift permet la rétrocompatibilité entre chaque version d'une IDL. Pour se faire il est important de bien renseigner et ne pas modifier les index des champs des fonctions, structures et exception

- Ajout d’un nouveau champ
    - Nouveau Client, ancien Serveur
le serveur ignore le nouveau champ, il ne le connaît pas.
    - Ancien Client, nouveau Serveur
le serveur ne trouve pas le champ attendu, laisse le champ inchangé.

- Suppression d’un champ
    - Nouveau Client, ancien Serveur
le serveur ne trouve pas le champ attendu, laisse le champ inchangé.
    - Ancien Client, nouveau Serveur
le client envoi un champ déprécié, le serveur l’ignore.
