"""
Created on Mar 15, 2014

@author: tjoneslo
"""
from pypdflite.pdflite import PDFLite
from pypdflite.pdfobjects.pdfcolor import PDFColor
from pypdflite.pdfobjects.pdfcursor import PDFCursor


def ArcTest():
    """
    Functional test for drawing eclipses
    """
    # Create PDFLite object
    writer = PDFLite("generated/ArcTest.pdf")

    # Set compression defaults to False
    writer.set_compression(False)

    # Set document metadata
    writer.set_information(title="Testing Arcs")  # set optional information

    # Get document object
    document = writer.get_document()
    black = PDFColor()

    center = PDFCursor(300, 300)
    radius = 30
    document.draw_circle(center, radius, black)


    red = PDFColor(name='red')
    starting_angle = 45
    arc_angle = 90

    document.draw_arc(center, radius, starting_angle, arc_angle, inverted=False, border_color=red)

    blue = PDFColor(name="blue")
    document.set_draw_color(blue)
    document.draw_line(306.049, 270.61622, 286.40641373, 268.5761)

    # Close Document
    writer.close()


if __name__ == '__main__':
    CircleTest()