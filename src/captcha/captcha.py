import base64
import random
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont


def getRandomPosOnRect(startX,startY,cornerX,cornerY):
    if(startX < cornerX):
        x = random.randint(startX,cornerX)
    else:
        x = random.randint(cornerX,startX)
    if(startY < cornerY):
        y = random.randint(startY,cornerY)
    else:
        y = random.randint(cornerY,startY)
    return (x,y)

def generateImageAndSolution():
    SIZE = 300
    RECT_SIZE = 100

    im = Image.new('RGB', (SIZE, SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    font = ImageFont.truetype(r'Gidole-Regular.ttf', RECT_SIZE)

    number1 = "1"
    number2 = "2"
    number3 = "3"
    number4 = "4"
    numberList = [number1,number2,number3,number4]


    draw.text((10, 10), number1, font = font, align ="left",fill=(0,0,0,255))
    draw.text((SIZE-(RECT_SIZE+10),10), number2, font = font, align ="left",fill=(0,0,0,255))
    draw.text((10,SIZE-(RECT_SIZE-10)), number3, font = font, align ="left",fill=(0,0,0,255))
    draw.text((SIZE-(RECT_SIZE-10),SIZE-(RECT_SIZE-10)), number4, font = font, align ="left",fill=(0,0,0,255))


    options = [0,1,2,3]
    #             from                                   to 
    connection1 = (options.pop(random.randint(0,3)),options.pop(random.randint(0,2)))
    connection2 = (options.pop(random.randint(0,1)),options.pop(random.randint(0,0)))


    rP1 = getRandomPosOnRect(0,0,RECT_SIZE,RECT_SIZE)
    rP2 = getRandomPosOnRect(SIZE,0,SIZE-RECT_SIZE,RECT_SIZE)
    rP3 = getRandomPosOnRect(0,SIZE,RECT_SIZE,SIZE-RECT_SIZE)
    rP4 = getRandomPosOnRect(SIZE,SIZE,SIZE-RECT_SIZE,SIZE-RECT_SIZE)


    rPList = [rP1,rP2,rP3,rP4]

    draw.line((rPList[connection1[0]], rPList[connection1[1]]), fill=(255, 255, 0), width=10)
    draw.line((rPList[connection2[0]], rPList[connection2[1]]), fill=(255, 255, 0), width=10)

    numberConnection1 = (numberList[connection1[0]],numberList[connection1[1]])
    numberConnection2 = (numberList[connection2[0]],numberList[connection2[1]])

    buffered = BytesIO()
    im.save(buffered, format="PNG")
    im_str = base64.b64encode(buffered.getvalue())
    return (im_str,(numberConnection1,numberConnection2))

print(generateImageAndSolution())