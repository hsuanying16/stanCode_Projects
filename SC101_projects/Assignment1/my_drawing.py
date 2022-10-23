"""
File: my_drawing.py
Name: Sharon
----------------------
This file shows a drawing of world map with an airplane
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


# global variable
window = GWindow(1000, 500)


def main():
    """
    use the world map and airplane to express the feeling of people
    wanting to travel after pandemic
    """
    # ocean
    ocean = GRect(1000, 500)
    window.add(ocean)
    ocean.filled = True
    ocean.fill_color = 'lightskyblue'
    ocean.color = 'lightskyblue'
    # right airplane body and line
    plane_body = GOval(500, 100, x=700, y=-20)
    window.add(plane_body)
    plane_body.filled = True
    plane_body.fill_color = 'white'
    plane_body.color = 'white'
    plane_line = GRect(300, 1, x=720, y=50)
    window.add(plane_line)
    # airplane wing
    wing = GPolygon()
    wing.add_vertex((870, 70))
    wing.add_vertex((975, 160))
    wing.add_vertex((990, 160))
    wing.add_vertex((930, 80))
    wing.filled = True
    wing.color = 'white'
    wing.fill_color = 'white'
    window.add(wing)
    wing2 = GPolygon()
    wing2.add_vertex((153, 36))
    wing2.add_vertex((188, 85))
    wing2.add_vertex((175, 85))
    wing2.add_vertex((135, 50))
    wing2.filled = True
    wing2.color = 'white'
    wing2.fill_color = 'white'
    window.add(wing2)
    # left airplane body and line
    plane_back = GOval(500, 100, x=-340, y=-20)
    window.add(plane_back)
    plane_back.filled = True
    plane_back.fill_color = 'white'
    plane_back.color = 'white'
    back_wing = GPolygon()
    back_wing.add_vertex((161, 30))
    back_wing.add_vertex((170, 0))
    back_wing.add_vertex((100, 0))
    window.add(back_wing)
    back_wing.filled = True
    back_wing.fill_color = 'white'
    back_wing.color = 'white'
    plane_line2 = GRect(139, 1, x=0, y=50)
    window.add(plane_line2)
    # airplane front window
    w_front = GRect(30, 10, x=708, y=17)
    window.add(w_front)
    w_front.filled = True
    w_front2 = GPolygon()
    w_front2.add_vertex((708, 17))
    w_front2.add_vertex((705, 20))
    w_front2.add_vertex((704, 21))
    w_front2.add_vertex((703, 22))
    w_front2.add_vertex((701, 24))
    w_front2.add_vertex((700, 25))
    w_front2.add_vertex((700, 27))
    w_front2.add_vertex((708, 27))
    window.add(w_front2)
    w_front2.filled = True
    # airplane window
    w_back1 = GOval(12, 12, x=880, y=18)
    window.add(w_back1)
    w_back1.filled = True
    w_back2 = GOval(12, 12, x=900, y=18)
    window.add(w_back2)
    w_back2.filled = True
    w_back3 = GOval(12, 12, x=920, y=18)
    window.add(w_back3)
    w_back3.filled = True
    w_back4 = GOval(12, 12, x=940, y=18)
    window.add(w_back4)
    w_back4.filled = True
    w_back5 = GOval(12, 12, x=960, y=18)
    window.add(w_back5)
    w_back5.filled = True
    w_back6 = GOval(12, 12, x=980, y=18)
    window.add(w_back6)
    w_back6.filled = True
    w_front1 = GOval(12, 12, x=0, y=18)
    window.add(w_front1)
    w_front1.filled = True
    w_front2 = GOval(12, 12, x=20, y=18)
    window.add(w_front2)
    w_front2.filled = True
    w_front3 = GOval(12, 12, x=40, y=18)
    window.add(w_front3)
    w_front3.filled = True

    # North America
    north_a = GPolygon()
    north_a.add_vertex((100, 170))
    north_a.add_vertex((110, 160))
    north_a.add_vertex((120, 145))
    north_a.add_vertex((130, 135))
    north_a.add_vertex((140, 131))
    north_a.add_vertex((150, 128))
    north_a.add_vertex((160, 126))
    north_a.add_vertex((180, 125))
    north_a.add_vertex((250, 124))
    north_a.add_vertex((265, 125))
    north_a.add_vertex((270, 123))
    north_a.add_vertex((300, 110))
    north_a.add_vertex((310, 108))
    north_a.add_vertex((325, 103))
    north_a.add_vertex((360, 100))
    north_a.add_vertex((390, 103))
    north_a.add_vertex((400, 104))
    north_a.add_vertex((420, 101))
    north_a.add_vertex((440, 98))
    north_a.add_vertex((450, 99))
    north_a.add_vertex((460, 103))
    north_a.add_vertex((462, 105))
    north_a.add_vertex((460, 113))
    north_a.add_vertex((440, 132))
    north_a.add_vertex((430, 135))
    north_a.add_vertex((415, 140))
    north_a.add_vertex((393, 154))
    north_a.add_vertex((390, 156))
    north_a.add_vertex((386, 156))
    north_a.add_vertex((380, 152))
    north_a.add_vertex((382, 126))
    north_a.add_vertex((360, 118))
    north_a.add_vertex((350, 120))
    north_a.add_vertex((350, 126))
    north_a.add_vertex((355, 137))
    north_a.add_vertex((355, 142))
    north_a.add_vertex((350, 153))
    north_a.add_vertex((368, 170))
    north_a.add_vertex((360, 180))
    north_a.add_vertex((350, 190))
    north_a.add_vertex((300, 210))
    north_a.add_vertex((280, 230))
    north_a.add_vertex((270, 238))
    north_a.add_vertex((260, 241))
    north_a.add_vertex((240, 245))
    north_a.add_vertex((230, 253))
    north_a.add_vertex((226, 260))
    north_a.add_vertex((230, 268))
    north_a.add_vertex((240, 265))
    north_a.add_vertex((250, 270))
    north_a.add_vertex((254, 274))
    north_a.add_vertex((262, 276))
    north_a.add_vertex((268, 290))
    north_a.add_vertex((275, 294))
    north_a.add_vertex((270, 305))
    north_a.add_vertex((255, 300))
    north_a.add_vertex((245, 290))
    north_a.add_vertex((240, 280))
    north_a.add_vertex((235, 278))
    north_a.add_vertex((220, 277))
    north_a.add_vertex((210, 275))
    north_a.add_vertex((200, 270))
    north_a.add_vertex((191, 260))
    north_a.add_vertex((185, 240))
    north_a.add_vertex((180, 228))
    north_a.add_vertex((170, 215))
    north_a.add_vertex((168, 210))
    north_a.add_vertex((176, 180))
    north_a.add_vertex((172, 164))
    north_a.add_vertex((165, 160))
    north_a.add_vertex((160, 158))
    north_a.add_vertex((150, 160))
    north_a.add_vertex((110, 173))
    north_a.add_vertex((100, 173))
    window.add(north_a)
    north_a.filled = True
    north_a.color = 'limegreen'
    north_a.fill_color = "limegreen"
    # South America
    south_a = GPolygon()
    south_a.add_vertex((275, 294))
    south_a.add_vertex((295, 291))
    south_a.add_vertex((335, 306))
    south_a.add_vertex((350, 310))
    south_a.add_vertex((360, 326))
    south_a.add_vertex((385, 333))
    south_a.add_vertex((390, 336))
    south_a.add_vertex((394, 343))
    south_a.add_vertex((394, 350))
    south_a.add_vertex((382, 380))
    south_a.add_vertex((375, 393))
    south_a.add_vertex((360, 405))
    south_a.add_vertex((358, 420))
    south_a.add_vertex((348, 431))
    south_a.add_vertex((336, 438))
    south_a.add_vertex((328, 460))
    south_a.add_vertex((334, 475))
    south_a.add_vertex((332, 480))
    south_a.add_vertex((330, 482))
    south_a.add_vertex((325, 482))
    south_a.add_vertex((302, 451))
    south_a.add_vertex((300, 419))
    south_a.add_vertex((295, 380))
    south_a.add_vertex((290, 373))
    south_a.add_vertex((272, 360))
    south_a.add_vertex((268, 353))
    south_a.add_vertex((259, 322))
    south_a.add_vertex((265, 313))
    south_a.add_vertex((273, 313))
    south_a.add_vertex((273, 309))
    south_a.add_vertex((270, 305))
    window.add(south_a)
    south_a.filled = True
    south_a.color = 'greenyellow' #greenyellow/lawngreen
    south_a.fill_color = "greenyellow"
    # Africa
    africa = GPolygon()
    africa.add_vertex((580, 231))
    africa.add_vertex((570, 230))
    africa.add_vertex((540, 230))
    africa.add_vertex((530, 224))
    africa.add_vertex((522, 216))
    africa.add_vertex((505, 215))
    africa.add_vertex((495, 217))
    africa.add_vertex((490, 219))
    africa.add_vertex((480, 225))
    africa.add_vertex((460, 244))
    africa.add_vertex((447, 264))
    africa.add_vertex((444, 272))
    africa.add_vertex((444, 296))
    africa.add_vertex((447, 305))
    africa.add_vertex((455, 310))
    africa.add_vertex((465, 314))
    africa.add_vertex((480, 314))
    africa.add_vertex((510, 313))
    africa.add_vertex((520, 316))
    africa.add_vertex((523, 320))
    africa.add_vertex((524, 337))
    africa.add_vertex((530, 350))
    africa.add_vertex((530, 360))
    africa.add_vertex((527, 380))
    africa.add_vertex((530, 390))
    africa.add_vertex((542, 410))
    africa.add_vertex((542, 421))
    africa.add_vertex((547, 426))
    africa.add_vertex((555, 427))
    africa.add_vertex((570, 418))
    africa.add_vertex((585, 403))
    africa.add_vertex((590, 385))
    africa.add_vertex((605, 370))
    africa.add_vertex((610, 360))
    africa.add_vertex((611, 330))
    africa.add_vertex((620, 320))
    africa.add_vertex((640, 302))
    africa.add_vertex((642, 297))
    africa.add_vertex((640, 293))
    africa.add_vertex((635, 290))
    africa.add_vertex((615, 285))
    africa.add_vertex((605, 279))
    africa.add_vertex((597, 270))
    africa.add_vertex((593, 251))
    africa.add_vertex((580, 231))
    window.add(africa)
    africa.filled = True
    africa.color = 'darkorange'
    africa.fill_color = 'darkorange'
    # Europe
    europe = GPolygon()
    europe.add_vertex((580, 231))
    europe.add_vertex((590, 228))
    europe.add_vertex((590, 222))
    europe.add_vertex((570, 220))
    europe.add_vertex((560, 218))
    europe.add_vertex((550, 214))
    europe.add_vertex((530, 204))
    europe.add_vertex((524, 203))
    europe.add_vertex((520, 204))
    europe.add_vertex((500, 213))
    europe.add_vertex((490, 216))
    europe.add_vertex((480, 216))
    europe.add_vertex((470, 212))
    europe.add_vertex((471, 206))
    europe.add_vertex((475, 201))
    europe.add_vertex((484, 196))
    europe.add_vertex((484, 182))
    europe.add_vertex((490, 177))
    europe.add_vertex((500, 172))
    europe.add_vertex((505, 164))
    europe.add_vertex((505, 150))
    europe.add_vertex((540, 130))
    europe.add_vertex((550, 128))
    europe.add_vertex((580, 132))
    europe.add_vertex((617, 132))
    europe.add_vertex((617, 160))
    europe.add_vertex((620, 168))
    europe.add_vertex((622, 170))
    europe.add_vertex((622, 171))
    europe.add_vertex((614, 180))
    europe.add_vertex((610, 188))
    europe.add_vertex((594, 182))
    europe.add_vertex((588, 184))
    europe.add_vertex((588, 188))
    europe.add_vertex((592, 194))
    europe.add_vertex((586, 200))
    europe.add_vertex((594, 212))
    europe.add_vertex((580, 231))
    window.add(europe)
    europe.filled = True
    europe.color = 'dodgerblue'     #dodgerblue/steelblue
    europe.fill_color = 'dodgerblue'
    # Asia
    asia = GPolygon()
    asia.add_vertex((580, 231))
    asia.add_vertex((594, 212))
    asia.add_vertex((586, 200))
    asia.add_vertex((592, 194))
    asia.add_vertex((588, 188))
    asia.add_vertex((588, 184))
    asia.add_vertex((594, 182))
    asia.add_vertex((610, 188))
    asia.add_vertex((614, 180))
    asia.add_vertex((622, 171))
    asia.add_vertex((622, 170))
    asia.add_vertex((620, 168))
    asia.add_vertex((617, 160))
    asia.add_vertex((617, 132))
    asia.add_vertex((620, 133))
    asia.add_vertex((630, 132))
    asia.add_vertex((670, 122))
    asia.add_vertex((696, 112))
    asia.add_vertex((710, 112))
    asia.add_vertex((730, 120))
    asia.add_vertex((740, 119))
    asia.add_vertex((756, 119))
    asia.add_vertex((780, 128))
    asia.add_vertex((820, 126))
    asia.add_vertex((870, 128))
    asia.add_vertex((895, 138))
    asia.add_vertex((900, 143))
    asia.add_vertex((900, 148))
    asia.add_vertex((895, 150))
    asia.add_vertex((886, 151))
    asia.add_vertex((883, 155))
    asia.add_vertex((883.5, 165))
    asia.add_vertex((886, 175))
    asia.add_vertex((886, 180))
    asia.add_vertex((883, 182))
    asia.add_vertex((880, 183))
    asia.add_vertex((875, 186))
    asia.add_vertex((870, 174))
    asia.add_vertex((860, 158))
    asia.add_vertex((850, 155))
    asia.add_vertex((840, 156))
    asia.add_vertex((824, 162))
    asia.add_vertex((825, 164))
    asia.add_vertex((840, 170))
    asia.add_vertex((850, 178))
    asia.add_vertex((855, 190))
    asia.add_vertex((855, 195))
    asia.add_vertex((850, 206))
    asia.add_vertex((830, 228))
    asia.add_vertex((820, 245))
    asia.add_vertex((812, 262))
    asia.add_vertex((802, 274))
    asia.add_vertex((803, 288))
    asia.add_vertex((802, 292))
    asia.add_vertex((792, 310))
    asia.add_vertex((791, 320))
    asia.add_vertex((800, 332))
    asia.add_vertex((810, 340))
    asia.add_vertex((822, 344))
    asia.add_vertex((830, 348))
    asia.add_vertex((830, 352))
    asia.add_vertex((820, 354))
    asia.add_vertex((810, 352))
    asia.add_vertex((785, 340))
    asia.add_vertex((765, 310))
    asia.add_vertex((762, 300))
    asia.add_vertex((760, 290))
    asia.add_vertex((745, 266))
    asia.add_vertex((740, 264))
    asia.add_vertex((735, 265))
    asia.add_vertex((730, 268))
    asia.add_vertex((725, 275))
    asia.add_vertex((724, 298))
    asia.add_vertex((718, 303))
    asia.add_vertex((710, 298))
    asia.add_vertex((700, 280))
    asia.add_vertex((695, 270))
    asia.add_vertex((690, 264))
    asia.add_vertex((670, 254))
    asia.add_vertex((660, 250))
    asia.add_vertex((654, 252))
    asia.add_vertex((654, 264))
    asia.add_vertex((634, 278))
    asia.add_vertex((628, 280))
    asia.add_vertex((614, 272))
    asia.add_vertex((600, 252))
    window.add(asia)
    asia.filled = True
    asia.color = 'gold'
    asia.fill_color = 'gold'
    # Taiwan
    taiwan = GPolygon()
    taiwan.add_vertex((840, 240))
    taiwan.add_vertex((844, 241))
    taiwan.add_vertex((844, 244))
    taiwan.add_vertex((842, 249))
    taiwan.add_vertex((841, 255))
    taiwan.add_vertex((838, 252))
    taiwan.add_vertex((836, 250))
    taiwan.add_vertex((836, 244))
    window.add(taiwan)
    taiwan.filled = True
    taiwan.color = 'gold'
    taiwan.fill_color = 'gold'
    # Australia
    aus = GPolygon()
    aus.add_vertex((803, 420))
    aus.add_vertex((810, 390))
    aus.add_vertex((820, 382))
    aus.add_vertex((830, 378))
    aus.add_vertex((840, 368))
    aus.add_vertex((850, 360))
    aus.add_vertex((860, 358))
    aus.add_vertex((870, 361))
    aus.add_vertex((880, 366))
    aus.add_vertex((885, 366))
    aus.add_vertex((893, 360))
    aus.add_vertex((897, 360))
    aus.add_vertex((910, 380))
    aus.add_vertex((922, 396))
    aus.add_vertex((922, 408))
    aus.add_vertex((915, 420))
    aus.add_vertex((900, 430))
    aus.add_vertex((890, 434))
    aus.add_vertex((880, 436))
    aus.add_vertex((870, 436))
    aus.add_vertex((860, 432))
    aus.add_vertex((850, 420))
    aus.add_vertex((840, 418))
    aus.add_vertex((815, 424))
    aus.add_vertex((810, 425))
    aus.add_vertex((804, 423))
    window.add(aus)
    aus.filled = True
    aus.color = 'tomato'
    aus.fill_color = 'tomato'

    # Pacific Ocean
    pacific = GLabel('Pacific\nOcean')
    pacific.font = 'Courier-18-italic'
    window.add(pacific, 80, 350)
    pacific2 = GLabel('Pacific\nOcean')
    pacific2.font = 'Courier-18-italic'
    window.add(pacific2, 900, 300)
    # Indian Ocean
    indian = GLabel('Indian\nOcean')
    indian.font = 'Courier-18-italic'
    window.add(indian, 680, 400)
    # Atlantic Ocean
    n_atlantic = GLabel('North\nAtlantic\nOcean')
    n_atlantic.font = 'Courier-18-italic'
    window.add(n_atlantic, 330, 280)
    s_atlantic = GLabel('South\nAtlantic\nOcean')
    s_atlantic.font = 'Courier-18-italic'
    window.add(s_atlantic, 420, 420)
    # Arctic Ocean
    arctic = GLabel('Arctic\nOcean')
    arctic.font = 'Courier-18-italic'
    window.add(arctic, 470, 90)



if __name__ == '__main__':
    main()
