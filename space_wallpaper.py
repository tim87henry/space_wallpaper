import ctypes
from random import randint
from selenium import webdriver

""" The openImageWebPage proc is used to open the site and 
navigate to a random image, from the list of images.
It then saves the image to the PC, in the given location.
"""
def openImageWebpage(imageFile):
    # img1 and img2 are random numbers used to pic an image from the list.
    img1=randint(1,6)
    img2=randint(1,10)
    driver=webdriver.Firefox()
    driver.get("http://mydailywallpaper.com/wallcat/space/")
    driver.find_element_by_css_selector("body > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(10) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child("+str(img2)+") > td:nth-child("+str(img1)+") > a:nth-child(1) > img:nth-child(1)").click()
    
    # Select the right image to download (i.e, apart from other ad images on the page)
    list1=driver.find_elements_by_tag_name('img')
    for item in list1:
        if "wallimg" in item.get_attribute("src"):
            item.screenshot(imageFile)
    driver.close()

""" The setWallpaper proc is used to set the downloadimage image,
as the current desktop wallpaper.
"""
def setWallpaper(imageFile):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, imageFile, 0)
    

# Main program starts here

imageFile="C:\\Users\\Tim\\Documents\\geckodriver\\image.png"
openImageWebpage(imageFile)
setWallpaper(imageFile)

