package initializers

import (
	"log"
	"os"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

// DB est une variable globale pour stocker une instance de *gorm.DB
var DB *gorm.DB

// ConnectToDB initialise une connexion de base de données avec Gorm
func ConnectToDB() {
	dsn := os.Getenv("DB_URL") // Récupérer la valeur de l'URL de la base de données depuis une variable d'environnement
	var err error
	DB, err = gorm.Open(mysql.Open(dsn), &gorm.Config{
		SkipDefaultTransaction: true,
	}) // Ouvrir une connexion de base de données MySQL avec Gorm
	if err != nil {
		
		log.Fatalf("Failed to connect to database: %v", err) // Si la connexion échoue, afficher un message d'erreur et arrêter le programme
	
	}
}

