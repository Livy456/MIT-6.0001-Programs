from PIL import Image, ImageFont, ImageDraw
import numpy

def make_matrix(color):
    """
    Generates a transformation matrix for the specified color.
    Inputs:
        color: string with exactly one of the following values:
               'red', 'blue', 'green', or 'none'
    Returns:
        matrix: a transformation matrix corresponding to
                deficiency in that color
    """
    # You do not need to understand exactly how this function works.
    if color == 'red':
        c = [[.567, .433, 0], [.558, .442, 0], [0, .242, .758]]
    elif color == 'green':
        c = [[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.142, 0.858]]
    elif color == 'blue':
        c = [[.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, .525]]
    elif color == 'none':
        c = [[1, 0., 0], [0, 1, 0.], [0, 0., 1]]
    return c


def matrix_multiply(m1, m2):
    """
    Multiplies the input matrices.
    Inputs:
        m1,m2: the input matrices
    Returns:
        result: matrix product of m1 and m2
        in a list of floats
    """
    product = numpy.matmul(m1, m2)
    if type(product) == numpy.int64:
        return float(product)
    else:
        result = list(product)
        return result

def img_to_pix(filename):
    """
    Takes a filename (must be inputted as a string
    with proper file attachment ex: .jpg, .png)
    and converts to a list of representing pixels.

    For RGB images, each pixel is a tuple containing (R,G,B) values.
    For BW images, each pixel is an integer.

    # Note: Don't worry about determining if an image is RGB or BW.
            The PIL library functions you use will return the 
            correct pixel values for either image mode.

    Returns the list of pixels.

    Inputs:
        filename: string representing an image file, such as 'lenna.jpg'
        returns: list of pixel values 
                 in form (R,G,B) such as [(0,0,0),(255,255,255),(38,29,58)...] for RGB image
                 in form L such as [60,66,72...] for BW image
    """
    # initialization section
    pix = []    
    
    # opens the image and instantiates an image object--> im
    with Image.open(filename) as im:
        # a list of pixels or a list of tuples of pixels 
        pix = list(im.getdata())
    
    # return section
    return pix

def pix_to_img(pixels, size, mode):
    """
    Creates an Image object from a inputted set of RGB tuples.

    Inputs:
        pixels: a list of pixels such as the output of
                img_to_pixels.
        size: a tuple of (width,height) representing
              the dimensions of the desired image. Assume
              that size is a valid input such that
              size[0] * size[1] == len(pixels).
        mode: 'RGB' or 'L' to indicate an RGB image or a 
              BW image, respectively
    returns:
        img: Image object made from list of pixels
    """
    img = Image.new(mode, size) # instantiates an Image Object of either BW or RGB pixels based on mode
    img.putdata(pixels)         # puts list of pixels into Image object
    
    # returns an image object made from list of pixels 
    return img

def filter(pixels, color):
    """
    pixels: a list of pixels in RGB form, such as 
            [(0,0,0),(255,255,255),(38,29,58)...]
    color: 'red', 'blue', 'green', or 'none', must be a string representing 
           the color deficiency that is being simulated.
    returns: list of pixels in same format as earlier functions,
    transformed by matrix multiplication
    """
    # initialization section
    filt_color = []
    color_mat = make_matrix(color)  # makes a matrix of the provided color
    
    # iterates through each RGB pixel
    for pix in pixels:
        # transforms tuple of RGB pixel
        pix = matrix_multiply(color_mat, pix)
        
        # iterates through each RGB value to type cast to integer
        for i in range(len(pix)):
            ele = pix[i]
            pix[i] = int(ele)   # changes float value to int
            
        filt_color.append(tuple(pix))    # adds the tuple of rgb value to filtered list
    
    # returns the transformed list of pixels in RGB form 
    return filt_color
    
def extract_end_bits(num_bits, pixel):
    """
    Extracts the last num_bits bits of each value of a given pixel. 

    example for BW pixel:
        num_bits = 5
        pixel = 214

        214 in binary is 11010110. 
        The last 5 bits of 11010110 are 10110.
                              ^^^^^
        The integer representation of 10110 is 22, so we return 22.

    example for RBG pixel:
        num_bits = 2
        pixel = (214, 17, 8)

        last 3 bits of 214 = 110 --> 6
        last 3 bits of 17 = 001 --> 1
        last 3 bits of 8 = 000 --> 0

        so we return (6,1,0)

    Inputs:
        num_bits: the number of bits to extract
        pixel: an integer between 0 and 255, or a tuple of RGB values between 0 and 255

    Returns:
        The last num_bits bits of pixel, as an integer (BW) or tuple of integers (RGB).
    """
    # initialization section
    pix_int = 0
    rgb_pixel = []
    
    # checks if BW pixels
    if type(pixel) == int:
        """
        Since a binary number will only result in 0 and 1 as digit we
        take 2 to the power of num_bits to get the proper place value 
        in which we are trying to find the LSB
        then when we take the modulos of pixel value it will result in
        the base 10 of the LSB without having to convert from binary to base 10
        """
        # returns the number from the last num_bits of binary representation of BW pixel
        return pixel%(2**num_bits)
    
    # checks if RGB pixels
    elif type(pixel) == tuple:
        # iterates through each element in tuple
        for ele in pixel:
            # coverts each integer in tuple a binary string representation of itself
            rgb_pixel.append(ele%(2**num_bits))
          
        # returns a tuple of the last num_bits of binary representation of RGB pixel
        return tuple(rgb_pixel)

def get_img_size(filename):
    """
    Gets the size of the image
    Inputs:
        filename: string, input of BW or RGB file to be processed
    Returns:
        size of BW or RGB image
    """
    # opens the image object from the filename
    with Image.open(filename) as im:
        size = im.size # gets the size of the image object
    
    # returns the size of the BW or RGB image object
    return size
    
def reveal_bw_image(filename):
    """
    Extracts the single LSB for each pixel in the BW input image. 
    Inputs:
        filename: string, input BW file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    # initialization section
    hidden_pixels = []
    
    # gets the list of BW pixels
    pixels = img_to_pix(filename)
    
    # iterates through each BW pixels
    for pix in pixels:
        # BW pixel values only between 0(black) and 1(white)
        # white value is 255
        # black value is 0
        # must multiply by 255 to get either white or black value
       end_bit = extract_end_bits(1, pix)*255 
       hidden_pixels.append(end_bit) # adds the LSBS for each tuple of BW pixels
    
    # helper function to get size of image object
    size = get_img_size(filename) 
    
    # returns image object of hidden image
    return pix_to_img(hidden_pixels, size, 'L')

def reveal_color_image(filename):
    """
    Extracts the 3 LSBs for each pixel in the RGB input image. 
    Inputs:
        filename: string, input RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    # initialization section
    hidden_pixels = []
    
    # gets the list of tuples of RGB pixels
    pixels = img_to_pix(filename)
    
    # iterates through each tuple of RGB pixels
    for pix in pixels:
        # list of the end bits of the RGB values
        end_bit = list(extract_end_bits(3, pix))
        scal_bit = [] # resets the list of scaled values
        
        # iterates through red, gree, and blue 
        for ele in end_bit:
            # to get an 8 bit RGB pixel must be divided by 7
            # then must get into the 0, 255 range 
            # and make sure result is an int
            scaled = int((ele/7)*255)
            scal_bit.append(scaled) # adds the scaled bit to list of RGB scaled pixel values
        hidden_pixels.append(tuple(scal_bit)) # adds each tuple of scaled   RGB pixels
    
    # helper function to get image object size
    size = get_img_size(filename)
    
    # returns image object of hidden image
    return pix_to_img(hidden_pixels, size, "RGB")

def reveal_image(filename):
    """
    Extracts the single LSB (for a BW image) or the 3 LSBs (for a 
    color image) for each pixel in the input image. Hint: you can
    use a function to determine the mode of the input image (BW or
    RGB) and then use this mode to determine how to process the image.
    Inputs:
        filename: string, input BW or RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    im = Image.open(filename)
    if im.mode == '1' or im.mode == 'L':
        return(reveal_bw_image(filename))
    elif im.mode == 'RGB':
        return(reveal_color_image(filename))
    else:
        raise Exception("Invalid mode %s" % im.mode)


def draw_kerb(filename, kerb):
    """
    Draws the text "kerb" onto the image located at "filename" and returns a PDF.
    Inputs:
        filename: string, input BW or RGB file
        kerb: string, your kerberos
    Output:
        Saves output image to "filename_kerb.xxx"
    """
    im = Image.open(filename)
    font = ImageFont.truetype("noto-sans-mono.ttf", 40)
    draw = ImageDraw.Draw(im)
    draw.text((0, 0), kerb, "white", font=font)
    idx = filename.find(".")
    new_filename = filename[:idx] + "_kerb" + filename[idx:]
    im.save(new_filename)
    return

def main():
    pass

    # # Uncomment the following lines to test part 1

    # #small_bw_image.png is a 6x2 image which spans from 0 to 253
    #small_bw_pixels = img_to_pix('small_bw_image.png')
    # # small_rgb_pixels.png is a 6x2 image which spans from (0,0,0) to (0,253,253)
    #small_rgb_pixels = img_to_pix('small_rgb_image.png')
    #print('small_bw_pixels: ', small_bw_pixels)
    #print('small_rgb_pixels: ', small_rgb_pixels)
"""
    im = Image.open('image_15.png')
    width, height = im.size
    pixels = img_to_pix('image_15.png')

    #non_filtered_pixels = filter(pixels, 'none')
    #im = pix_to_img(non_filtered_pixels, (width, height), 'RGB')
    #im.show()

    red_filtered_pixels = filter(pixels, 'red')
    im2 = pix_to_img(red_filtered_pixels, (width, height), 'RGB')
    im2.copy().save("Filtered image_15.png") # saves a copy of im2 image object as filtered image15
    #im2.show()

    # # Uncomment the following lines to test part 2
    
    im3 = reveal_image('hidden1.bmp')
    im3.copy().save("Unhidden hidden1.bmp") # saves a copy of im3 image object as unhidden image1
    #im3.show()

    im4 = reveal_image('hidden2.bmp')
    im4.copy().save("Unhidden hidden2.bmp") # saves a copy of im4 image object as unhidden image2
    #im4.show()

    # drawing my kerbos over the three images
    draw_kerb("Filtered image_15.png", "omdias77@mit.edu")
    draw_kerb("Unhidden hidden1.bmp", "omdias77@mit.edu")
    draw_kerb("Unhidden hidden2.bmp", "omdias77@mit.edu")
"""
if __name__ == '__main__':
    main()
