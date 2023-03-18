package main

import (

	"github.com/API-REST/initializers"
	"github.com/API-REST/models"
	
)
func init(){
	initializers.LoadEnvVariables()
	initializers.ConnectToDatabase()
}

func main(){
	initializers.DB.AutoMigrate(&models.Post{})

}