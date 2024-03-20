# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
#
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the
# pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
# of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the
# same color), and so on. Replace the color of all of the aforementioned pixels with color.
#
# Return the modified image after performing the flood fill.
#
# Constraints:
#   • m == image.length
#   • n == image[i].length
#   • 1 <= m, n <= 50
#   • 0 <= image[i][j], color < 216
#   • 0 <= sr < m
#   • 0 <= sc < n


def floodFill(image, sr, sc, color):
    # Keep the old color for comparisons
    old_color = image[sr][sc]

    # Recursive function
    # Handles if the inputs are incorrect and the 4-directional checks to the first few pixels
    def flood(sr, sc):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        if image[sr][sc] == color or image[sr][sc] != old_color:
            return

        # Colors the pixel if the pixel passes checks
        image[sr][sc] = color

        # Colors pixels surrounding (sr, sc)
        flood(sr - 1, sc)
        flood(sr + 1, sc)
        flood(sr, sc + 1)
        flood(sr, sc - 1)

    # Gets the blood flow going
    flood(sr, sc)

    return print(image)


image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1
sc = 1

floodFill(image, sr, sc, 2)
