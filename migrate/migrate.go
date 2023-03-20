package main

import (

	"github.com/API-REST/initializers"
	"github.com/API-REST/models"
	
)
func init(){
	initializers.LoadEnvVariables()
	initializers.ConnectToDB()
}

func main(){
	initializers.DB.AutoMigrate(&models.Hotel{})
	initializers.DB.AutoMigrate(&models.Client{})
	initializers.DB.AutoMigrate(&models.Chambre{})
	initializers.DB.AutoMigrate(&models.Reservation{})
}