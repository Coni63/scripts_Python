Bonjour,

Le main code est disponible dans script.py (c'est le fichier a lancer dans la console). Labyrinthe.py ne regroupe que la classe permettant de gérer le robot dans la grille.

Par defaut les cartes doivent etre dans le dossier map situe au meme niveau que script. 
Cependant les fonctions de chargement/sauvegarde/suppression peuvent prendre un path en attribut si vous desirez le changer

Par defaut les sauvegardes seront crees/sauvegardes dans le dossier save situe au meme niveau que le script.
Cela peut aussi etre change.

Concernant les maps, j'ai garde la notation OC avec: 
    "O" pour un mur
    "X" pour le robot
    "." pour une porte
    " " pour du vide 
Une amelioration serait de faire un fichier ini avec les caratères voulu et le script parse les donnees en consequences (c'est assez simple a implementer dans la classe Labyrinthe mais complexifie un peu le code)

Toutes les entrees des utilisateurs sont verifies ainsi que la validite des mouvements.

Pour information, l'attribut classe du labyrinthe ne sauvegarde pas la position du joueur pour eviter d'effacer les portes lorsque je passes dessus. Du coup j'affiche le perso "par dessus" ce qui permet lorsque je bouge de garder le contenu precedent de la cellule.

J'espère que le jeu vous plaira !



