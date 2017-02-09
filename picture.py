from PIL import Image

#find the median function
def medianOdd(myList):
    # Store list length in the variable listLength
    listLength = len(myList)
    # Sort the list
    sortedValues = sorted(myList)
    # Location of middle value. Subtract one because of zero index
    middleIndex = ((listLength + 1)/2) - 1
    # Return the object located at that index
    return sortedValues[middleIndex]
    
#create image array of source pictures to be used in creation of the new image
img1 = Image.open('1.png')
img2 = Image.open('2.png')
img3 = Image.open('3.png')
img4 = Image.open('4.png')
img5 = Image.open('5.png')
img6 = Image.open('6.png')
img7 = Image.open('7.png')
img8 = Image.open('8.png')
img9 = Image.open('9.png')
pictures = [img1,img2,img3,img4,img5,img6,img7,img8,img9]

#definitions / initalizations
redMedianPixel = 0
greenMedianPixel = 0
blueMedianPixel = 0
rList = []
bList = []
gList = []
width, height = pictures[0].size
newPhoto = Image.new("RGBA", (width,height), "white")
newPhoto.save('finalImage.jpg')

#loop through pictures to find RGB values and insert them into new image
for x in range(0,width):
    for y in range(0,height):
        for i in pictures:
            #cycle through array of pictures to get pixel data from each photo
            r,b,g = i.getpixel((x,y))
            rList.append(r)
            gList.append(g)
            bList.append(b)
    #find the median values of the pixel list
    redMedianPixel = medianOdd(rList)
    greenMedianPixel = medianOdd(gList)
    blueMedianPixel = medianOdd(bList)
    #insert correct pixel into space and clear pixel lists for next median values
    newPhoto.putpixel((x,y), (redMedianPixel,greenMedianPixel,blueMedianPixel))
    newPhoto.save('finalImage.jpg')
    r = []
    g = []
    b = []