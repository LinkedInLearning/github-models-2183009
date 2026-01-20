# Découvrir GitHub Models

Ce dossier repository est lié au cours `Découvrir GitHub Models`. Le cours entier est disponible sur [LinkedIn Learning][lil-course-url].

![Découvrir Les Modèles Github][lil-thumbnail-url] 

Guidé par Sandy Ludosky, ce cours permet de découvrir comment exploiter la puissance des modèles d’IA directement depuis GitHub. À travers des démonstrations concrètes, vous apprendrez à utiliser le catalogue de modèles (OpenAI, Meta, Mistral…), à tester leurs performances dans le Playground, à rédiger des prompts efficaces et à effectuer des appels API. Vous intégrerez ensuite ces modèles dans votre environnement de développement pour créer vos propres applications et assistants IA. Accessible aux débutants, cette formation allie clarté et bonnes pratiques pour une utilisation responsable de l’intelligence artificielle.

## Instructions

Ce dossier repository a des branches pour chacune des vidéos du cours. Vous pouvez utiliser le menu des Branches sur GitHub afin d’accéder aux passages qui vous intéressent. Vous pouvez également rajouter `/tree/BRANCH_NAME` à l’URL afin d’accéder à la branche qui vous intéresse. 

## Branches

Les branches sont structurées de manière à correspondre aux vidéos du cours. La convention de nommage est : `CHAPITRE#_VIDEO#`. Par exemple, la branche nommée`02_03` correspond au second chapitre, et à la troisième vidéo de ce chapitre. Certaines branches ont un état de départ et de fin.  
La branche `02_03_d` correspond au code du début de la vidéo.  
La branche `02_03_f` correspond au code à la fin de la vidéo.  
La branche master correspond au code à la fin de la formation. 

Lorsque vous passez d’une branche des fichiers d’exercice à une autre après avoir fait des modifications, il est possible que vous ayez un message d’erreur similaire à : 

	error: Your local changes to the following files would be overwritten by checkout:        [files]
	Please commit your changes or stash them before you switch branches.
	Aborting

Afin de résoudre ce souci, vous devez :

	Rajouter les changements au git en utilisant la commande : git add .
	Enregistrer les changements avec la commande : git commit -m "message de votre choix"

## Installation

1. Pour utiliser ces fichiers d’exercice, vous avez besoin de : 
   * [Visual Studio Code](https://code.visualstudio.com/)
   * [Git - version control system](https://git-scm.com/)
2. Clonez ce dossier repository sur votre machine locale (Mac), CMD (Windows), ou sur un outil GUI tel que SourceTree

## Démarrage rapide avec GitHub Models 
[**Quickstart**](https://docs.github.com/fr/github-models/quickstart)

* Un compte personnel GitHub - [Se connecter avec ses identifiants GitHub](https://github.com/login)
* Une clé d’accès GitHub (Personal Access Token ou Fine-grained PAT)

## Liens & ressources
- [Guide de démarrage](https://docs.github.com/fr/github-models/quickstart)
- [Playground](https://docs.github.com/fr/github-models/quickstart)
- [Marketplace (catalogue de modèles de langage)](https://github.com/marketplace/models)
- [Référence API- Github Models](https://docs.github.com/fr/rest/models/inference?apiVersion=2022-11-28)

### Formateur

**Sandy Ludosky** 

Retrouvez mes autres formations sur [LinkedIn Learning][lil-URL-trainer].

[0]: # (Replace these placeholder URLs with actual course URLs)
[lil-course-url]: https://www.linkedin.com
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4E0DAQGmfdPvoSB1tw/learning-public-crop_675_1200/B4EZvGsT_8HIAg-/0/1768565064022?e=2147483647&v=beta&t=momk4zwYAbz-PW2R91KDB_vZvs86EuBdA0OTAG5cQ3Y
[lil-URL-trainer]: https://www.linkedin.com/learning/instructors/sandy-ludosky

[1]: # (End of FR-Instruction ###############################################################################################)
