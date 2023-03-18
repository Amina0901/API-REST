package models

import"gorm.io/gorm"

type Hotel struct{
	gorm.model
	Nom string
	Telephone int
	Adresse string
	nombreNiveau int
}