from PIL import ImageGrab

def screenshot(speicherort, format='png', bereich=None):

    if bereich:
        bild = ImageGrab.grab(bbox=bereich)
    else:
        bild = ImageGrab.grab(all_screens=True)

    bild.save(speicherort, format.upper())

#screenshot("mein_screenshot.png")  
#screenshot("screenshot2.png", bereich=(100, 100, 500, 500))  
#screenshot("screenshot3.jpg", format='jpeg') 
