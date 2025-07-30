# import cv2 

# image = cv2.imread("Leo.jpg")
# # start point of line
# start_point = (0,0)
# #end point of line
# end_point = (300,300)
# # line color
# color = (159,10,215)
# #line thickness
# thickness = 7

# # cv2.line( is used to draw a line on an image)
# image = cv2.line(image,start_point,end_point,color,thickness)
# image2 = cv2.rectangle(image,start_point,end_point,color,thickness)
# # showing the line
# cv2.imshow("Line on the image",image)
# cv2.imshow("rectangle on the image",image2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2 

image = cv2.imread("Leo.jpg")
# start point of line
centre_point = (100,100)
#end point of line
radius = 100
# line color
color = (159,10,215)
#line thickness
thickness = 7

# cv2.line( is used to draw a line on an image)
image2 = cv2.circle(image,centre_point,radius,color,thickness)
# showing the line
cv2.imshow("Circle on the image",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()