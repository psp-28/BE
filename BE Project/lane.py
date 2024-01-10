import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt


def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1 * (3 / 4.3))
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, int(y1), x2, y2])


def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    try:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            # print(parameters)
            slope = parameters[0]
            intercept = parameters[1]

            if slope < 0:
                left_fit.append((slope, intercept))
                # left_fit_average = np.average(left_fit, axis=0)
                # left_line = make_coordinates(image, left_fit_average)
            else:
                right_fit.append((slope, intercept))
                # right_fit_average = np.average(right_fit, axis=0)
                # right_line = make_coordinates(image, right_fit_average)

        print(left_fit)
        print(right_fit)
        left_fit_average = np.average(left_fit, axis=0)
        right_fit_average = np.average(right_fit, axis=0)
        print(left_fit_average)
        print(right_fit_average)

        left_line = make_coordinates(image, left_fit_average)
        right_line = make_coordinates(image, right_fit_average)
        return np.array([left_line, right_line])
    except:
        return None


def canny(image):
    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        canny_edge = cv2.Canny(blur, 50, 150)
        return canny_edge


def region_of_interest(image):
    height = image.shape[0]
    width = image.shape[1]
    polygons = np.array([
        [(100, width), (650, height), (430, 340)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


def display_lines(image, lines):
    line_image = np.zeros_like(image)
    # before detecting the lines we will check if the array is not empty because if the lines are not present then it will not display

    if lines is not None:
        for x1, y1, x2, y2 in lines:
            print(x2)
            if x1 > 9999:
                x1 = 1045
            if x2 > 9999:
                x2 = 750
            # we will convert 2D array into 1D array by reshaping
            #
            cv2.line(line_image, (int(x1 * 1.01), int(y1 * 1.01)), (int(x2 * 1.01), int(y2 * 1.01)), (0, 0, 255), 5)
            # cv2.line(image, first point ofthe line segment, second point of the line segment, BGR color we want, thickness)
    return line_image


##/// For image use below commented code
# image = cv2.imread('roadpic.jpg')
# image = imutils.resize(image, width=800)
# lane_image = np.copy(image)
# canny_image = canny(lane_image)
# cropped_image = region_of_interest(canny_image)
# lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)     #(image, precision of 2 pixel, with 1 degree precision i.e. in radians, threshold- no. of intersection for precision, placeholder array)
# # cv2.HoughLinesP(rho(precision in hough space), theta(angle between points of intersection), threshold(no. of intersections), placeholder array, length of a line in pixel that we will accept in input)
# averaged_lines = average_slope_intercept(lane_image, lines)
# line_image = display_lines(lane_image, averaged_lines)
#
# #our image is in black background , we want it to show drawn lines on our color image.
# combined_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)
# #plt.imshow(region_of_interest(canny))
# #plt.show()
#
# cv2.imshow('Result', combined_image)
# cv2.waitKey(0)


cap = cv2.VideoCapture('./inputs/test8.mp4')
while (cap.isOpened()):
    _, frame = cap.read()  # when while is true it return boolean value that we don't want so we use _
    if _== True:
        frame = cv2.resize(frame, (720,640))

        canny_image = canny(frame)
        cropped_image = region_of_interest(canny_image)
        lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180, 100, np.array([]), minLineLength=50,
                                maxLineGap=10)  # (image, precision of 2 pixel, with 1 degree precision i.e. in radians, threshold- no. of intersection for precision, placeholder array)
        # cv2.HoughLinesP(rho(precision in hough space), theta(angle between points of intersection), threshold(no. of intersections), placeholder array, length of a line in pixel that we will accept in input)
        averaged_lines = average_slope_intercept(frame, lines)
        line_image = display_lines(frame, averaged_lines)

    # our image is in black background , we want it to show drawn lines on our color image.
        combined_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
        cv2.imshow('Lane Detection System', combined_image)
        cv2.waitKey(1)
    else:
        cap.release()
        cv2.destroyAllWindows()
    # plt.imshow(combined_image)
    # plt.show()
    # except:
    #     if frame is not None:
    #         cv2.imshow('Lane Detection System',frame)
    #         cv2.waitKey(1)