from PIL import Image

#ASCII character used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";",":",",","."]

#resize the image according to a new width
def resize_image(image, new_width = 100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resize_image = image.resize((new_width, new_height))
    return (resize_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return (characters)

def test(new_width=100,path='Mina2.jpg'):
    #attempt to open image from user-iput
    # path = input("Enter a valid pathname to an image:\n")
    imgpath = f'resources\imgs\{path}'
    try:
        image = Image.open(imgpath)
    except:
        print(imgpath, "is not a valid pathname to an image")
    #convert image to ASCII
    new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width)))

    #format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0,pixel_count,new_width))

    # #print result
    # print(ascii_image)
    return ascii_image
