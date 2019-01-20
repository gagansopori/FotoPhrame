from tkinter import *
from PIL import Image, ImageTk
import urllib.request, json
import requests
import random


# Instagram Updates using the Instagram API
class InstagramUpdate:

	access_token = 'get your own @ api.instagram.com'		


	def getUserInfo(user):
		
		user_url = 'https://api.instagram.com/v1/users/self/?access_token=%s' %(user.access_token)
		req = urllib.request.urlopen(user_url)
		response = req.read().decode('utf-8')
		query = json.loads(response)
		req.close()

		return query['data']['counts']['media']


	def getRecentMedia(media, media_count):

		media_url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token=%s' %(media.access_token)

		req = urllib.request.urlopen(media_url)
		response = req.read().decode('utf-8')
		query = json.loads(response)
		req.close()

		
		for i in range(0,media_count):
			
			postLink = query['data'][i]['images']['standard_resolution']['url']
			img = urllib.request.urlretrieve(postLink,"D:/Python3/PlayMirror/pf/%s.jpg" %(i))

			image = Image.open("..//your directory goes here/%s.jpg" %(i))
			# image = image.resize((400,400), Image.ANTIALIAS)
			image.save("..//your directory goes here/ig_%s.png" %(media_count-i))



	def showPhoto(photoCanvas, pCanvas):
		
		# to generate photos randomly
		number = random.randint(61,79)		# using this to fetch images saved in line 42

		# loading the image element to be displayed on the canvas
		photo = PhotoImage(file = '..//your directory goes here/ig_%d.png' %(number))

		# Loading the image onto the canvas
		pCanvas.create_image(0,0, image = photo, anchor = 'nw')
		pCanvas.image = photo
		
		# Recursive call
		pCanvas.after(10000, photoCanvas.showPhoto, pCanvas)



root=Tk()

# creating object for the class
I_Up = InstagramUpdate()

# getting the total no. of posts by the user
media_count = I_Up.getUserInfo()
# getting the most recent posts
I_Up.getRecentMedia(media_count)

# Initializing the Canvas onto which the image will be loaded
pCanvas = Canvas(background = 'black', width = 640, height = 640)			# the dimensions can be edited as per the user requirements.
pCanvas.pack(fill = 'both', expand = True)

# displaying the Photo
I_Up.showPhoto(pCanvas)

root.mainloop()
