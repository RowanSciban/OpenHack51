def pad_image(img_path):

    # Read image as a numpy array
    img = im.imread(img_path)

    # Get the difference between the height and width of the image
    diff = img.shape[0] - img.shape[1]

    # If the difference is non-zero, proceed with padding
    if (diff != 0):
        #if diff is positive, pad width or else pad height
        if (diff > 0):
            # Divide by two to get value that can be used to pad on both sides to center image
            bordersize = diff//2
            # Arguments = Image, top border, bottom border, left border, right border, cv2.BORDER_CONSTANT means same color uniformly for border, value = white
            border=cv2.copyMakeBorder(img, top=0, bottom=0, left=bordersize, right=bordersize, borderType= cv2.BORDER_CONSTANT, value=[255,255,255] )
        else:
            bordersize = abs(diff)//2
            border=cv2.copyMakeBorder(img, top=bordersize, bottom=bordersize, left=0, right=0, borderType= cv2.BORDER_CONSTANT, value=[255,255,255] )
    
    # If the image is already a square, copy it over as is
    else:
        border=img
    
    return border
