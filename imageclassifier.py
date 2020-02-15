# importing google_images_download module 
from google_images_download import google_images_download 

# creating object 
response = google_images_download.googleimagesdownload() 

search_queries = ['isometric 3d shop.','helicopter.','laptop.','ball.','3d coffee shop isometric.','3d helmet sport.'] 


def downloadimages(query): 
	arguments = {"keywords": query,
                # "format": "jpg",
                "limit":20,
                "print_urls":True
                # "size": "medium",
                # "aspect_ratio": "panoramic"
                }
	try: 
		response.download(arguments) 
	
	except FileNotFoundError: 
		arguments = {"keywords": query, 
					# "format": "jpg", 
					"limit":20, 
					"print_urls":True 
					# "size": "medium"
                    } 
					
		try:
			response.download(arguments) 
		except: 
			pass

# Driver Code 
for query in search_queries: 
	downloadimages(query) 
	print() 

