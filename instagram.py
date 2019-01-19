from tkinter import *
from PIL import Image, ImageTk
import urllib.request, json
import requests




# Instagram Updates using the Instagram API
class InstagramUpdate():

	# client_id = 'get your own by registering for it'
	# redirect_url = 'yourwebsite from where you can access Access token using Oauth 2.0/'
	access_token = 'get your own from instagram'

	
	# def __init__(self, parent, *args, **kwargs):

	# 	Frame.__init__(self, parent, bg = 'black')

	# 	self.frame = Frame(self, bg = 'black')				#create the frame
	# 	self.frame.pack(side = TOP, anchor = W)				#pack the frame

		
	# 	#photo
	# 	self.photoLabel = Label(self.frame, bg = 'black', height = 400, width = 400)
	# 	self.photoLabel.pack(side = LEFT, anchor = N, padx = 10)	
	


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

			image = Image.open("D:/Python3/PlayMirror/pf/%s.jpg" %(i))
			# image = image.resize((400,400), Image.ANTIALIAS)
			image.save("../add your path here/ig_%s.png" %(i))



root=Tk()

# creating object for the class
I_Up = InstagramUpdate()

# getting the total no. of posts by the user
media_count = I_Up.getUserInfo()

# getting the most recent posts
I_Up.getRecentMedia(media_count)

root.mainloop()
