package main

import (

 "github.com/gin-gonic/gin"
 "github.com/API-REST/initializers"
 "github.com/API-REST/controllers"
)
	
func init(){
	initializers.LoadEnvVariables()
	initializers.ConnectToDB()
}



func main(){
	r := gin.Default()
	r.POST("/Hotel", controllers.HotelCreate)
	r.Run() // listen and serve on 0.0.0.0:8080
}