import cv2

# Load an image from a file
image = cv2.imread("sample.jpg")
if image is None:
    print("Error: Image not found")
else:
    # Display the loaded image
    cv2.imshow("Loaded Image", image)
    cv2.waitKey(0)

    # Save the image to a new file
    cv2.imwrite("output_image.jpg", image)

if image is not None:
    resized_image = cv2.resize(image, (300, 300))  # Resize to 300x300
    cv2.imshow("Resized Image", resized_image)
    cv2.waitKey(0)

    # Crop the image using slicing
    cropped_image = image[50:200, 100:300]  # Crop a region of the image
    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(0)

    # Rotate the image by 90 degrees clockwise
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Rotated Image", rotated_image)
    cv2.waitKey(0)

    # Flip the image horizontally
    flipped_image = cv2.flip(image, 1)  # 1 for horizontal flipping
    cv2.imshow("Flipped Image", flipped_image)
    cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
