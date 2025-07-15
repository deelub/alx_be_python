def weather_today(feedback):

	match feedback:
	 case "sunny":
	 	return "Wear a t-shirt and sunglasses"
	 case "rainy":
	 	return "Don't forget your umbrella and a raincoat"
	 case "cold":
	 	return "Make sure to wear a warm coat and scarf"
	 case _:
	 	return "Sorry I don't have recommendations for this weather"



weather= input("What's the weather like today? (sunny/rainy/cold").lower()
weather_today(weather)