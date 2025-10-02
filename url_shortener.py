# 
import pyshorteners

url = input("Enter the URL: ")
s = pyshorteners.Shortener()
short_url = s.tinyurl.short(url)

print("Shortened URL:", short_url)
