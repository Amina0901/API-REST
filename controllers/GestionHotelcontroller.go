package controllers

import (
	"github.com/gin-gonic/gin"
	"github.com/API-REST/initializers"
	"github.com/API-REST/models"
)

func HotelCreate (c *gin.Context){
	
	Hotel := models.Hotel{Nom: "Novotel", Telephone: 770002519,Adresse: "Dakar"}

	result := initializers.DB.Create(&Hotel)

	if result.Error != nil{
		c.Status(400)
		return
			}

	c.JSON(200, gin.H{
		"Hotel": Hotel,
	})
}
func ClientCreate (c *gin.Context){
	
	Client := models.Client{Nom: "Diop", Prenom: "Amina",Telephone: 770002519}

	result := initializers.DB.Create(&Client)

	if result.Error != nil{
		c.Status(400)
		return
			}

	c.JSON(200, gin.H{
		"Client": Client,
	})
}
