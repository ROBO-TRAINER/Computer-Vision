import cv2

# Load an image from file
image = cv2.imread('image.jpg')  # replace 'image.jpg' with the path to your image file

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original image
cv2.imshow('Original Image', image)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()

