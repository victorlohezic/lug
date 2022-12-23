# Lug 

Ce projet permet d'envoyer automatiquement des mails en passant en pièce jointe un document pdf.
Il m'est utile en tant que chef de projet pour faciliter l'envoi des compte rendus de réunion. Un champ permet de choisir entre le client et le responsable pédagogique en fonction du cadre de la réunion. On envoie le mail ainsi à la bonne personne. Il utilise PyQT6. 

Les variables suivantes d'environnement sont à définir dans `~/.bashrc` : 
```bash
export LUG_PASSWORD="mdp_mail_expediteur"
export LUG_CUSTOMER="adresse_mail_du_client"
export LUG_EDUCATIONAL_MANAGER="adresse_mail_du_responsable_pedagogique"
export LUG_SENDER="adresse_mail_de_l_expediteur"
```

![logo](logo.png)

> Anecdote : Le projet se nomme Lug en hommage au dieu gaulois protecteur des marchands et des voyageurs, inventeur et praticien de tous les arts. Il a pour emblème une harpe.