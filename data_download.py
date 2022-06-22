import requests
from PIL import Image


response = requests.get("https://i.imgur.com/ExdKOOz.png")

file = open("sample_image.png", "wb")
file.write(response.content)
file.close()

im1 = Image.open("sample_image.png")


#show images
im1.show()



print("Job Completed of downloading the image!!!")
