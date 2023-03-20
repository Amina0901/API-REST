package models

import"time"
import"gorm.io/gorm"

type Hotel struct {
	gorm.Model
	Nom string
	Telephone int
	Adresse string
	nombreNiveau int
}  

type Chambre struct {
	gorm.Model
	Nom string
	Classe string
	Etat string
	NumNiveau int
}

type Client struct{
	gorm.Model
	Nom string
	Prenom string
	Telephone int
}

type Reservation struct {
	gorm.Model
	dateEntrée time.Time
	dateSortie time.Time
	nuité int
	tarif int
}
