import cv2
  
# Save image in set directory
# Read RGB image
img = cv2.imread('cat.jpg') 
  
# Output img with window name as 'image'
cv2.imshow('image', img) 
  
# Maintain output window utill
# user presses a key
cv2.waitKey(6000)        
  
# Destroying present windows on screen
cv2.destroyAllWindows() 
