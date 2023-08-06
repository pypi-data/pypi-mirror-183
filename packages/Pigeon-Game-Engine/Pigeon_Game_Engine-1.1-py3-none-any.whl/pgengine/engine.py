import random
from tkinter import Tk, Canvas
from PIL import Image as Image_, ImageTk
from time import sleep, time, localtime
from keyboard import is_pressed
import keyboard
import pgengine.matrix as matrix
from math import hypot, radians, degrees, sqrt, atan2, sin, cos
from copy import copy



def _empty(*args, **kwargs):
    pass
def sign(n) -> int:
    if n == 0:
        return 1
    return n / abs(n)
def dec2hex(num, length = 1):
    num = hex(num)
    num2 = ''
    for i, n in enumerate(num):
        if n == "x" or (n == "0" and num[i+1:i+2] == "x"):
            continue
        num2 += n
    while len(num2) < length:
        num2 = "0" + num2
    return num2
def hex2dec(num):
    returned = 0
    for i, s in enumerate(num):
        returned += Color.hex_table[s] * 16 ** (len(num)-i-1)
    return returned

class Color:
    BLACK = '#000'
    WHITE = '#fff'
    GRAY = '#888'
    RED = '#f00'
    GREEN = '#0f0'
    BLUE = '#00f'
    YELLOW = '#ff0'
    ORANGE = '#f80'
    VIOLET = '#f0f'
    LIGHTBLUE = '#0ff'
    EMPTY = ''
    hex_table = {
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }
    for i in range(10):
        hex_table[str(i)] = i
    def __init__(self, color):
        self.color = color
    def rainbow_color(color, change = 1):
        d = False
        count = color.count(255)
        index255 = color.index(255)
        if count != 1:
            color2 = copy(color)
            color2[index255] = 0
            if color2.index(255) - index255 == 1: index255 = color2.index(255)
        
        if count == 2 or (color[index255] > color[index255-1] and color[index255-1]!=0): d = True
        
        if d: color[index255-1] -= change; color[index255-1] = max(color[index255-1], 0)
        else: color[(index255+1)%3] += change; color[(index255+1)%3] = min(color[(index255+1)%3], 255)
        return color
    def rgb2hex(color):
        if type(color) == Color:
            color = color.color
        r, g, b = color
        red = dec2hex(r, 2)
        green = dec2hex(g, 2)
        blue = dec2hex(b, 2)
        return "#" + red + green + blue
    def hex2rgb(color):
        if type(color) == Color:
            color = color.color
        color = color[1:]
        r, g, b = color[:2], color[2:4], color[4:]
        red, green, blue = hex2dec(r), hex2dec(g), hex2dec(b)
        return [red, green, blue]

class scene:
    '''
    This is scene class. It contains all information about:
    -window(window width and height, that you can change)
    -all entities on the scene
    -FPS
    -etc.
    '''
    def __init__(self):
        self.running = True
        
        self.all_entities = []
        self.ui = []

        self.FPS = 500
        self.unit = 50
        
        self.main_camera = None
        
        self.g = 9.8
        self.defaultCollider = False
        self.width, self.height = 1000, 800
        
        self.def_width, self.def_height = self.width, self.height
        
        self.tk = Tk()
        self.tk.title('Window')
        self.tk.geometry(f"{self.width}x{self.height}")
        
        self.canvas = Canvas(width = self.width, height = self.height, bg = Color.BLACK, highlightthickness=0)
        self.canvas.pack()
    def engine_update(self, update):
        time1 = time()

        for entity in self.all_entities:
            if entity.usable:
                entity.update()
        for entity in self.ui:
            if entity.usable:
                entity.update()
        
        width, height = self.getWindowSize(True)
        window_bounds.verticies = [Vector(x, y) for x in [-width/2, width/2] for y in [-height/2, height/2]]
        window_bounds.verticies[2], window_bounds.verticies[3] = window_bounds.verticies[3], window_bounds.verticies[2]
        
        # Calling given update function
        update()
        
        # time2 = time()
        # self.tick(time1, time2, self.FPS)
                
        try:
            self.update_window()
            self.refresh()
        except:
            self.running = False
        
        time3 = time()
        delta = time3 - time1
        if delta:
            Time.delta = delta * 100
    def background(self, color):
        self.canvas.configure(bg = color)
    def title(self, name):
        self.tk.title(name)
    def tick(self, time1, time2, FPS):
        sleep(time2-time1+1/FPS)
    def cursor(self, name):
        self.tk.configure(cursor=name)
    def fullscreen(self, state:bool = True):
        '''
        Enter or exit fullscreen mode.

        :param state: Enter or exit fullscreen variable.
        :type state: bool
        '''
        if state:
            self.tk.attributes('-fullscreen', True)
            screen_width, screen_height = self.getScreenSize()
            self.setSize(screen_width, screen_height, defValue = False)
        else:
            self.tk.attributes('-fullscreen', False)
            self.setSize(self.def_width, self.def_height)
    def resizable(self, state=True):
        self.tk.resizable(state, state)
    def run(self, update = _empty):
        while self.running:
            if Time.running() > 0.01:
                self.canvas.configure(width=self.tk.winfo_width(), height=self.tk.winfo_height())
                self.width, self.height = self.canvas.winfo_width(), self.canvas.winfo_height()
            self.engine_update(update)
    def refresh(self):
        for entity in self.all_entities:
            if entity.drawable and type(entity) != Image:
                for id in entity.ids:
                    self.canvas.delete(id)
        for entity in self.ui:
            if entity.drawable and type(entity) != Image:
                for id in entity.ids:
                    self.canvas.delete(id)
        # self.canvas.delete('all')
    def update_window(self):
        self.tk.update_idletasks()
        self.tk.update()
    def setSize(self, width: int, height: int, units = False, defValue: bool = True):
        '''
        Seting a size of window to specified width and height

        :type width: int
        :type height: int
        '''
        if defValue:
            self.def_width, self.def_height = width, height
        if units:
            width /= self.unit
            height /= self.unit
        self.width, self.height = width, height
        self.canvas.configure(width = width, height = height)
        self.tk.geometry(f"{width}x{height}")
    def getScreenSize(self, units=False, vector=False):
        if units:
            return self.tk.winfo_screenwidth()/self.unit, self.tk.winfo_screenheight()/self.unit
        elif vector:
            return Vector(self.tk.winfo_screenwidth()/self.unit, self.tk.winfo_screenheight()/self.unit)
        return self.tk.winfo_screenwidth(), self.tk.winfo_screenheight()
    def getWindowSize(self, units=False, vector=False):
        if units:
            return self.width/self.unit, self.height/self.unit
        elif vector:
            return Vector(self.width/self.unit, self.height/self.unit)
        return self.width, self.height
Scene = scene()

class InputManager:
    left_down = False
    right_down = False
    def initialisate():
        Scene.canvas.bind("<Button-1>", InputManager.left_go_down)
        Scene.canvas.bind("<ButtonRelease-1>", InputManager.left_go_up)
        Scene.canvas.bind("<Button-3>", InputManager.right_go_down)
        Scene.canvas.bind("<ButtonRelease-3>", InputManager.right_go_up)
    def left_go_down(evt):
        InputManager.left_down = True
    def left_go_up(evt):
        InputManager.left_down = False
    def right_go_down(evt):
        InputManager.right_down = True
    def right_go_up(evt):
        InputManager.right_down = False
    def getMouseButton(btn = 0):
        if btn == 0:
            return InputManager.left_down
        elif btn == 1:
            return InputManager.right_down
    def keyDown(key):
        '''
        :return: is key pressed
        '''
        return is_pressed(key)
    def mousePos(vector = True):
        '''
        :return: mouse position
        '''
        mouse_x = (Scene.tk.winfo_pointerx() - Scene.tk.winfo_rootx() - Scene.width//2) / Scene.unit
        mouse_y = (Scene.tk.winfo_pointery() - Scene.tk.winfo_rooty() - Scene.height//2) / Scene.unit
        if not vector:
            return mouse_x, mouse_y
        return Vector(mouse_x, mouse_y)
class Random:
    def vector(v1, v2, digits=10):
        minX, minY = v1.x, v1.y
        maxX, maxY = v2.x, v2.y
        return Vector(Random.float(minX, maxX, digits=digits), Random.float(minY, maxY, digits=digits))
    def int(min, max):
        return random.randint(min, max)
    def float(min, max, digits=100):
        return random.randint(min*digits, max*digits)/digits
    def percent(multiplier = 1):
        return random.random() * multiplier
    def shuffle(list):
        return random.shuffle(list)
    def seed(seed):
        return random.seed(seed)
class Time:
    start = time()
    delta = 0.005
    def running():
        """returns time passed since start of program"""
        return time() - Time.start
    def time():
        """returns current hour, minute and second"""
        return localtime()[3:6]

class Vector:
    def __init__(self, x  = 0, y = 0):
        self.x = x
        self.y = y
    def normalise(self):
        '''
        This method normalising vector
        '''
        max_n = max(abs(self.x), abs(self.y))
        if max_n != 0:
            self.x, self.y = self.x / max_n, self.y / max_n
        return self
    def normalised(self):
        '''
        This method normalising vector
        '''
        max_n = max(abs(self.x), abs(self.y))
        if max_n != 0:
            return Vector(self.x / max_n, self.y / max_n)
        return self
    def getMatrixPosition(self):
        '''
        :return: vector position in matrix style
        '''
        return (self.x, ), (self.y, )
    def distance(a, b):
        c = a - b
        return hypot(c.x, c.y)
    def set(self, x, y):
        self.x = x
        self.y = y
    def angle(self):
        return atan2(self.y, self.x) + radians(90)
    def __add__(self, other):
        if type(other) == Vector:
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)
        elif type(other) in [int, float]:
            x = self.x + other
            y = self.y + other
            return Vector(x, y)
    def __radd__(self, other):
        return self.__add__(other)
    def __repr__(self) -> tuple:
        return (self.x, self.y)
    def __mul__(self, other):
        if type(other) == Vector:
            x = self.x * other.x
            y = self.y * other.y
            return Vector(x, y)
        if type(other) in [int, float]:
            x = self.x * other
            y = self.y * other
            return Vector(x, y)
    def __rmul__(self, other):
        return self.__mul__(other)
    def __truediv__(self, other):
        if type(other) == Vector:
            x = self.x / other.x
            y = self.y / other.y
            return Vector(x, y)
        if type(other) in [int, float]:
            x = self.x / other
            y = self.y / other
            return Vector(x, y)
    def __rtruediv__(self, other):
        if type(other) == Vector:
            x = other.x / self.x
            y = other.y / self.y
            return Vector(x, y)
        if type(other) in [int, float]:
            x = other / self.x
            y = other / self.y
            return Vector(x, y)
    def __sub__(self, other):
        if type(other) == Vector:
            x = self.x - other.x
            y = self.y - other.y
            return Vector(x, y)
        elif type(other) in [int, float]:
            x = self.x - other
            y = self.y - other
            return Vector(x, y)
    def __rsub__(self, other):
        if type(other) == Vector:
            x = -self.x + other.x
            y = -self.y + other.y
            return Vector(x, y)
        elif type(other) in [int, float]:
            x = -self.x + other
            y = -self.y + other
            return Vector(x, y)
    def __neg__(self):
        return Vector(-self.x, -self.y)
    def __str__(self):
        return "Vector(" + str(self.x) + ', ' + str(self.y) + ")"
class Entity:
    def __init__(self, pos = copy(Vector(0, 0)), rot = 0, tag = None, mass = 5, drawable = True, usable = True, on_scene=True, entity_update = _empty, entity_class = None, static = False, ui = False):
        if type(pos) == tuple:
            pos = Vector(pos[0], pos[1])
        self.position = pos
        self.rotation = rot
        self.last_rotation = 0

        self.drawable = drawable
        self.usable = usable
        self.static = static

        self.collider_shape = None
        self.tag = tag
        
        self.entity_update = entity_update
        self.entity_class = entity_class

        self.orientation = Vector(0, 1)
        self.forward = self.orientation
        self.left = Vector(-1, 0)
        self.right = Vector(1, 0)
        self.back = Vector(0, -1)
        # Scene.width//2 = anchorX
        # Scene.height//2 = anchorY
        # rotated = matrix.multiply(matrix.rotation(self.rotation), self.forward.getMatrixPosition())
        # self.forward.x, self.forward.y = rotated[0][0], rotated[1][0]
        # self.last_rotation = self.rotation

        self.collider = Scene.defaultCollider
        self.rigidbody = False
        self.collided = False
        self.colliding_objects = 'all'

        self.accX = 0
        self.accY = 0
        self.velX = 0
        self.velY = 0

        self.move_y = None

        self.have_gravity = False

        self.mass = mass
        
        self.ids = []
        
        if ui: on_scene = False
        self.on_scene = on_scene
        self.ui = ui
        if on_scene:
            Scene.all_entities.append(self)
        elif ui:
            Scene.ui.append(self)
    def look_at(self, target, extra_angle = 0):
        self.rotation = (target - self.position).angle() + extra_angle
    def destroy(self):
        Scene.all_entities.pop(Scene.all_entities.index(self))
        for id in self.ids:
            Scene.canvas.delete(id)
    def create_rect_collider(self, scale):
        self.collider_shape = 'polygon'
        self.collider_verticies = [Vector(x, y) for x in [-scale.x/2, scale.x/2] for y in [-scale.y/2, scale.y/2]]
    def class_update(self): pass
    def draw(self): pass
    def update(self):
        if not self.static:
            try:
                if self.collider and self.colliding_objects == 'all':
                    for _entity in Scene.all_entities:
                        if _entity != self and _entity.collider and self.collision(_entity):
                            self.collided = True
                            break
                        self.collided = False
            except: pass
            if self.have_gravity:
                if not self.collided:
                    self.gravity()
            
            self.velX += self.accX
            self.velY += self.accY

            self.position.x += self.velX * Time.delta
            self.position.y += self.velY * Time.delta

            self.accX = 0
            self.accY = 0
            
            try:
                if self.collider and self.colliding_objects == 'all':
                    for _entity in Scene.all_entities:
                        if _entity != self and _entity.collider and self.collision(_entity):
                            self.collided = True
                            break
                        self.collided = False
            except: pass

            if self.collided and self.move_y != None:
                self.position.y = self.move_y
                self.move_y = None
            
            if type(self) == Polygon:
                for v in self.verticies:
                    rotated = matrix.multiply(matrix.rotation(self.rotation - self.last_rotation), v.getMatrixPosition())
                    v.x, v.y = rotated[0][0], rotated[1][0]
            rotated = matrix.multiply(matrix.rotation(self.rotation - self.last_rotation), self.orientation.getMatrixPosition())
            self.orientation.x, self.orientation.y = rotated[0][0], rotated[1][0]
            self.last_rotation = self.rotation

            self.forward = -self.orientation
            self.back.set(-self.forward.x, -self.forward.y)
            self.left.set(self.forward.y, -self.forward.x)
            self.right.set(-self.left.x, -self.left.y)
            
            self.class_update()
            self.entity_update(self)
        
        if self.drawable:
            in_view = False
            window_size = Scene.getWindowSize(True)
            window_bounds_copy = copy(window_bounds)
            window_bounds_copy.position += Scene.main_camera.position
            # if type(self) == Polygon: 
                # print(-window_size[0]/2 < self.position.x - Scene.main_camera.position.x < window_size[0]/2, -window_size[1]/2 < self.position.y - Scene.main_camera.position.y < window_size[1]/2, self.collision(window_bounds))
            if self.ui or type(self) == Image or ((-window_size[0]/2 < self.position.x - Scene.main_camera.position.x < window_size[0]/2 and -window_size[1]/2 < self.position.y - Scene.main_camera.position.y < window_size[1]/2) or self.collision(window_bounds_copy)):
                        in_view = True
            if in_view: self.ids = []; self.draw()
    def gravity(self):
        if not self.collided:
            self.force((0, self.mass / 1000 * Scene.g))
    def force(self, pos):
        if type(pos) == tuple:
            x, y = pos
        if type(pos) == Vector:
            x, y = pos.x, pos.y
        
        fX = x / Scene.unit * Scene.main_camera.FOV
        fY = y / Scene.unit * Scene.main_camera.FOV
        self.accX += fX
        self.accY += fY
    def circle_line_collision(circle, line):
        A = line[0]
        B = line[1]

        linePt = None
    
        x1 = A.x
        y1 = -A.y
        x2 = B.x
        y2 = -B.y

        direct = (B - A)
        for direction in [direct, -1 * direct]:
            direction.x, direction.y = direction.y, direction.x

            x3 = circle.position.x 
            y3 = -circle.position.y
            x4 = (circle.position.x + direction.x)
            y4 = (-circle.position.y + direction.y)

            den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if (den == 0):
                continue
            
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
            u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
            if 1 > t > 0 and 1 > u > 0:
                linePt = Vector()
                linePt.x = (x1 + t * (x2 - x1))
                linePt.y = (y1 + t * (y2 - y1))
            
            if linePt == None:
                distA = sqrt((x1 - circle.position.x) ** 2 + (y1 + circle.position.y) ** 2)
                distB = sqrt((x2 - circle.position.x) ** 2 + (y2 + circle.position.y) ** 2)
                if distA <= circle.radius or distB <= circle.radius:
                    return True
                continue

            pt = linePt
            
            if hypot(pt.x - circle.position.x, pt.y + circle.position.y) <= circle.radius:
                return True
    def circle_polygon_collision(circle, polygon):
        for i, v in enumerate(polygon.collider_verticies):
            A = v
            B = copy(polygon.collider_verticies[(i+1) % len(polygon.collider_verticies)])

            linePt = None
        
            x1 = (A.x + polygon.position.x)
            y1 = (-A.y - polygon.position.y)
            x2 = (B.x + polygon.position.x)
            y2 = (-B.y - polygon.position.y)

            direct = B - A
            for direction in [direct, -direct]:
                direction.x, direction.y = direction.y, direction.x

                x3 = circle.position.x 
                y3 = -circle.position.y
                x4 = (circle.position.x + direction.x)
                y4 = (-circle.position.y + direction.y)

                den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
                if den == 0:
                    continue
                
                t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
                u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
                if 1 > t > 0 and 1 > u > 0:
                    linePt = Vector()
                    linePt.x = (x1 + t * (x2 - x1))
                    linePt.y = (y1 + t * (y2 - y1))
                
                if linePt == None:
                    distA = sqrt((x1 - circle.position.x) ** 2 + (y1 + circle.position.y) ** 2)
                    distB = sqrt((x2 - circle.position.x) ** 2 + (y2 + circle.position.y) ** 2)
                    if distA <= circle.radius or distB <= circle.radius:
                        return True
                    continue

                pt = linePt
                
                if hypot(pt.x - circle.position.x, pt.y + circle.position.y) <= circle.radius:
                    return True
    def collisions(self, entities):
        for entity in entities:
            collision = self.collision(entity)
            if collision:
                return entity
        return False
    def collision(self, other):
        if self.collider_shape == 'line':
            if other.collider_shape == 'line':
                pass
            elif other.collider_shape == "circle":
                return Entity.circle_line_collision(other, (self.start, self.end))
        elif self.collider_shape == 'polygon':
            if other.collider_shape == 'polygon':
                for i, v1 in enumerate(other.collider_verticies):
                    x1 = (-v1.x + other.position.x)
                    y1 = v1.y + other.position.y
                    x2 = (-other.collider_verticies[(i+1) % 4].x + other.position.x)
                    y2 = other.collider_verticies[(i+1) % 4].y + other.position.y

                    for j, v2 in enumerate(self.collider_verticies):
                        x3 = -v2.x + self.position.x
                        y3 = v2.y + self.position.y
                        x4 = -self.collider_verticies[(j+1) % 4].x + self.position.x
                        y4 = self.collider_verticies[(j+1) % 4].y + self.position.y

                        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
                        if (den == 0):
                            continue

                        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den;
                        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den;
                        if 1 > t > 0 and 1 > u > 0:
                            pt = Vector()
                            pt.x = x1 + t * (x2 - x1)
                            pt.y = y1 + t * (y2 - y1)
                            if self.rigidbody:
                                normal = Vector(y2 - y1, -(x2 - x1))
                                normal.normalise()
                                
                                vert = copy(v2)
                                vert.y *= -1
                                # vert.x *= -1
                                vert += self.position
                                pt = vert
                                # Scene.canvas.create_oval(pt.x * Scene.unit - 5 + Scene.width//2, pt.y * Scene.unit - 5 + Scene.height//2, pt.x * Scene.unit + 5 + Scene.width//2, pt.y * Scene.unit + 5 + Scene.height//2, fill = 'yellow')
                                
                                hit = raycaster.ray(vert, normal, [other])
                                if sign(self.velX) == -sign(normal.x):
                                    self.velX = 0
                                if sign(self.velY) == -sign(normal.y):
                                    self.velY = 0
                                
                                if hit:
                                    # hit.x *= -1
                                    self.position += hit - vert
                                # print(hit, vert)
                                # if normal.x and normal.y:
                                #     self.position += Vector(1 / Scene.unit * abs(normal.x) / normal.x, 1 / Scene.unit * abs(normal.y) / normal.y)
                                # elif not normal.x:
                                #     self.position += Vector(1 / Scene.unit * normal.x, 1 / Scene.unit * abs(normal.y) / normal.y)
                                # elif not normal.y:
                                #     self.position += Vector(1 / Scene.unit * abs(normal.x) / normal.x, 1 / Scene.unit * normal.y)
                            return True
            elif other.collider_shape == 'circle':
                return Entity.circle_polygon_collision(other, self)
        elif self.collider_shape == 'circle':
            if other.collider_shape == 'line':
                return self.circle_line_collision((other.start, other.end))
            elif other.collider_shape == 'circle':
                dist = Vector.distance(self.position, other.position)
                if dist <= other.radius + self.radius:
                    return True
            elif other.collider_shape == 'polygon':
                return self.circle_polygon_collision(other)

class Camera(Entity):
    def __init__(self, pos=copy(Vector(0, 0))):
        super().__init__(pos=pos, rot=0, drawable=False)
        self.FOV = 1
        self.min_FOV = 0.1
    def update(self):
        self.min_FOV = abs(self.min_FOV)
        self.FOV = max(self.min_FOV, self.FOV)
camera = Camera()
Scene.main_camera = camera

class Polygon(Entity):
    def __init__(self, pos = copy(Vector(0, 0)), rot = 0, scale = None, color: str = Color.WHITE, outline_color = '', outline_width = 1, tag = None, mass = 5, drawable = True, usable = True, on_scene = True, entity_update = _empty, entity_class = None, static = False):
        super().__init__(pos, rot, tag, mass, drawable, usable, on_scene, entity_update, entity_class, static)
        if not scale:
            scale = Vector(1, 1)
        elif type(scale) == tuple:
            scale = Vector(scale[0], scale[1])
        self.scale = scale
        self.color = color
        self.outline_color = outline_color
        self.outline_width = outline_width
        self.collider_shape = 'polygon'

        self.verticies = [Vector(x, y) for x in [-scale.x/2, scale.x/2] for y in [-scale.y/2, scale.y/2]]
        self.verticies[2], self.verticies[3] = self.verticies[3], self.verticies[2]
        self.collider_verticies = self.verticies
    def draw(self):
        camera_ = Scene.main_camera
        draw_verticies = [pos2 for pos in self.verticies for pos2 in pos.__repr__()]
        camera_offset = Vector()
        if self.on_scene:
            camera_offset = camera_.position
        for i in range(len(draw_verticies)):
            if i % 2:
                draw_verticies[i] += self.position.y - camera_offset.y
            else:
                draw_verticies[i] += self.position.x - camera_offset.x
            draw_verticies[i] *= Scene.unit / camera_.FOV
            if i % 2:
                draw_verticies[i] += Scene.height//2
            else:
                draw_verticies[i] += Scene.width//2
        self.ids.append(Scene.canvas.create_polygon(draw_verticies, fill = self.color, outline=self.outline_color, width=self.outline_width))
class Circle(Entity):
    def __init__(self, pos = copy(Vector(0, 0)), rot = 0, radius = 0.5, color: str = Color.WHITE, tag = None, mass = 5, drawable = True, usable=True, on_scene=True, entity_update = _empty, entity_class = None, static = False):
        super().__init__(pos, rot, tag, mass, drawable, usable, on_scene, entity_update, entity_class, static)
        self.radius = radius
        self.color = color
        self.collider_shape = 'circle'
    def draw(self):
        mult = Scene.unit / Scene.main_camera.FOV
        camera_ = Scene.main_camera
        camera_offset = Vector()
        if self.on_scene:
            camera_offset = camera_.position
        x1, y1 = (self.position.x - self.radius - camera_offset.x) * mult + Scene.width//2, (self.position.y - self.radius - camera_offset.y) * mult + Scene.height//2
        x2, y2 = (self.position.x + self.radius - camera_offset.x) * mult + Scene.width//2, (self.position.y + self.radius - camera_offset.y) * mult + Scene.height//2
        self.ids.append(Scene.canvas.create_oval(x1, y1, x2, y2, fill = self.color, outline = ''))
class Line(Entity):
    def __init__(self, start = copy(Vector(0, 0)), end=copy(Vector(0, 0)), rot=0, color: str = Color.WHITE, tag=None, mass=5, drawable=True, usable=True, on_scene=True, entity_update = _empty, entity_class = None, static = False, width = 3):
        if type(start) == tuple:
            start = Vector(start[0], start[1])
        if type(end) == tuple:
            end = Vector(end[0], end[1])
        super().__init__(start - end, rot, tag, mass, drawable, usable, on_scene, entity_update, entity_class, static)
        self.start = start
        self.end = end
        self.color = color
        self.width = width
        self.collider_shape = 'line'
    def draw(self):
        mult = Scene.unit / Scene.main_camera.FOV
        camera_ = Scene.main_camera
        camera_offset = Vector()
        if self.on_scene:
            camera_offset = camera_.position
        x1, y1 = (self.start.x - camera_offset.x) * mult + Scene.width//2, (self.start.y - camera_offset.y) * mult + Scene.height//2
        x2, y2 = (self.end.x - camera_offset.x) * mult + Scene.width//2, (self.end.y - camera_offset.y) * mult + Scene.height//2
        self.ids.append(Scene.canvas.create_line(x1, y1, x2, y2, width = self.width, fill = self.color))

class Image(Entity):
    def __init__(self, pos=copy(Vector(0, 0)), scale = None, rot=0, image="", tag=None, mass=5, drawable=True, usable=True, on_scene=True, entity_update = _empty, entity_class = None, static = False):
        # if type(pos) == tuple:
        #     pos = Vector(pos[0], pos[1])
        if not scale: scale = Vector(1, 1)
        elif type(scale) == tuple:
            scale = Vector(scale[0], scale[1])
        super().__init__(pos, rot, tag, mass, drawable, usable, on_scene, entity_update, entity_class, static)
        self.image = image
        self.scale = scale
        self.last_scale = None
        self.last_image = None
        self.read()
        self.draw()
    def read(self):
        self.read_image = Image_.open(self.image)
    def draw(self):
        mult = Scene.unit / Scene.main_camera.FOV
        if int(self.scale.x * mult) and int(self.scale.y * mult):
            if self.last_scale == None:
                drawing_image = self.read_image
                if int(self.scale.x * mult) < 0: drawing_image = drawing_image.transpose(Image_.FLIP_LEFT_RIGHT)
                if int(self.scale.y * mult) < 0: drawing_image = drawing_image.transpose(Image_.FLIP_TOP_BOTTOM)
                
                # if self.scale != self.last_scale:
                #     self.drawing_image = self.drawing_image.resize((abs(int(self.scale.x * Scene.unit)), abs(int(self.scale.y * Scene.unit))), 0)
                # if self.rotation != self.last_rotation:
                #     self.drawing_image = self.drawing_image.rotate(degrees(self.rotation), expand=True)
                    
                drawing_image = drawing_image.resize((abs(int(self.scale.x * mult)), abs(int(self.scale.y * mult))), 0)
                drawing_image = drawing_image.rotate(-degrees(self.rotation), expand=True)
                self.drawing_image = ImageTk.PhotoImage(drawing_image)
                
                camera_ = Scene.main_camera
                camera_offset = Vector()
                if self.on_scene:
                    camera_offset = camera_.position
                
                self.ids = [Scene.canvas.create_image((self.position.x - camera_offset.x) * mult + Scene.width//2, (self.position.y - camera_offset.y) * mult + Scene.height//2, image = self.drawing_image)]
            # elif not (self.last_rotation == self.rotation and self.last_scale == self.scale and self.image == self.last_image): # and self.last_position.__repr__() == self.position.__repr__()
            else:            
                if int(self.scale.x * mult) < 0: self.drawing_image = self.read_image.transpose(Image_.FLIP_LEFT_RIGHT)
                if int(self.scale.y * mult) < 0: self.drawing_image = self.read_image.transpose(Image_.FLIP_TOP_BOTTOM)
                    
                self.drawing_image = self.drawing_image.resize((abs(int(self.scale.x * mult)), abs(int(self.scale.y * mult))), 0)
                self.drawing_image = self.drawing_image.rotate(-degrees(self.rotation), expand=True)
                self.drawing_image = ImageTk.PhotoImage(self.drawing_image)
                
                Scene.canvas.itemconfig(self.id, image=self.drawing_image)
                # if self.last_position.__repr__() != self.position.__repr__():
                camera_ = Scene.main_camera
                camera_offset = Vector()
                if self.on_scene:
                    camera_offset = camera_.position
                # print((self.position.x - camera_offset.x) * mult + Scene.width//2, (self.position.y - camera_offset.y) * mult + Scene.height//2,\
                # (self.last_position.x - camera_offset.x) * mult + Scene.width//2, (self.last_position.y - camera_offset.y) * mult + Scene.height//2)
                Scene.canvas.moveto(self.ids[0], (self.position.x - camera_offset.x) * mult + Scene.width//2, (self.position.y - camera_offset.y) * mult + Scene.height//2)
            # self.last_scale = self.scale
            # # self.last_position = self.position
            # self.last_image = self.image
class Text(Entity):
    def __init__(self, pos = copy(Vector(0, 0)), size = 1, rot = 0, text = '', color = Color.BLACK, parent = None, tag = None, mass = 5, drawable = True, usable = True, on_scene = True, entity_update = _empty, entity_class = None, static = False, ui=False):
        if type(pos) == tuple:
            pos = Vector(pos[0], pos[1])
        super().__init__(pos, rot, tag, mass, drawable, usable, on_scene, entity_update, entity_class, static, ui)
        # self.position = pos
        self.text = text
        self.color = color
        self.size = size
        self.parent = parent
        
    def draw(self):
        mult = Scene.unit / Scene.main_camera.FOV
        camera_ = Scene.main_camera
        camera_offset = Vector()
        if self.on_scene and not self in Scene.ui:
            camera_offset = camera_.position
        x, y = (self.position.x - camera_offset.x) * mult + Scene.width//2, (self.position.y - camera_offset.y) * mult + Scene.height//2
        self.ids.append(Scene.canvas.create_text(x, y, text = self.text, fill = self.color, font = ('Comic Sans MS', int(self.size * Scene.unit/10))))
class Button(Entity):
    def __init__(self, pos = copy(Vector(0, 0)), scale = copy(Vector(1, 1)), rot = 0, text = '', text_color = Color.BLACK, color = Color.WHITE, outline_color = '', outline_width = 1, highlight_color = 'white', onclick = _empty, onrelease = _empty, whileclicked = _empty, tag = None, mass = 5, drawable = True, usable = True, on_scene = True, entity_update = _empty, entity_class = None, static = False, ui=False):
        if type(pos) == tuple:
            pos = Vector(pos[0], pos[1])
        if type(scale) == tuple:
            scale = Vector(scale[0], scale[1])
        super().__init__(pos, rot, tag, mass, drawable, usable, on_scene, entity_update, entity_class, static, ui)
        # self.position = pos
        self.text = text
        self.color = color
        self.outline_color = outline_color
        self.outline_width = outline_width
        self.highlight_color = highlight_color
        self.text_color = text_color
        self.scale = scale
        self.onclick = onclick
        self.onrelease = onrelease
        self.whileclicked = whileclicked
        self.clicked = False
    def draw(self):
        color = self.color
        mouse_x, mouse_y = InputManager.mousePos(False)
        if self.clicked and self.position.x - self.scale.x/2 < mouse_x < self.position.x + self.scale.x/2 and self.position.y - self.scale.y/2 < mouse_y < self.position.y + self.scale.y/2:
            color = self.highlight_color
        
        mult = Scene.unit / Scene.main_camera.FOV
        camera_ = Scene.main_camera
        camera_offset = Vector()
        if self.on_scene and not self in Scene.ui:
            print(not self in Scene.ui)
            camera_offset = camera_.position
        
        x1, y1 = (self.position.x - self.scale.x/2 - camera_offset.x) * mult + Scene.width//2, (self.position.y - self.scale.y/2 - camera_offset.y) * mult + Scene.height//2
        x2, y2 = (self.position.x + self.scale.x/2 - camera_offset.x) * mult + Scene.width//2, (self.position.y + self.scale.y/2 - camera_offset.y) * mult + Scene.height//2
        self.ids.append(Scene.canvas.create_rectangle(x1, y1, x2, y2, fill = color, outline = self.outline_color, width = self.outline_width))
        x, y = (self.position.x - camera_offset.x) * mult + Scene.width//2, (self.position.y - camera_offset.y) * mult + Scene.height//2
        self.ids.append(Scene.canvas.create_text(x, y, text = self.text, fill = self.text_color, font = ('Times', int(0.35 * Scene.unit))))
    def class_update(self):
        mouse_x, mouse_y = InputManager.mousePos(False)
        if InputManager.getMouseButton(0):
            if self.clicked:
                self.whileclicked(self)
            else:
                if self.position.x - self.scale.x/2 < mouse_x < self.position.x + self.scale.x/2 and self.position.y - self.scale.y/2 < mouse_y < self.position.y + self.scale.y/2:
                # self.whileclicked()
                # if not self.clicked:
                    self.onclick(self)
                self.clicked = True
        else:
            if self.clicked and self.position.x - self.scale.x/2 < mouse_x < self.position.x + self.scale.x/2 and self.position.y - self.scale.y/2 < mouse_y < self.position.y + self.scale.y/2:
                self.onrelease(self)
            self.clicked = False
class InputField(Entity):
    def __init__(self, pos = copy(Vector(0, 0)), scale = copy(Vector(1, 1)), rot = 0, text = '', text_color = Color.BLACK, color = Color.WHITE, outline_color = '', outline_width = 1, tag = None, mass = 5, drawable = True, usable = True, on_scene = True, entity_update = _empty, entity_class = None, static = False):
        if type(pos) == tuple:
            pos = Vector(pos[0], pos[1])
        if type(scale) == tuple:
            scale = Vector(scale[0], scale[1])
        super().__init__(pos, rot, tag, mass, drawable, usable, on_scene, entity_update, entity_class, static)
        self.scale = scale
        self.color = color
        self.outline_color = outline_color
        self.text = text
        self.text_color = text_color
        self.cursor = 0
        self.selected = False
    def draw(self):
        color = self.color
        text = self.text
        if self.selected:
            text = self.text[:self.cursor] + "|" + self.text[self.cursor:]
        # mouse_x, mouse_y = InputManager.mousePos()
        # if self.clicked and self.position.x - self.scale.x/2 < mouse_x < self.position.x + self.scale.x/2 and self.position.y - self.scale.y/2 < mouse_y < self.position.y + self.scale.y/2:
        #     color = self.highlight_color
        
        mult = Scene.unit / Scene.main_camera.FOV
        camera_ = Scene.main_camera
        camera_offset = Vector()
        if self.on_scene:
            camera_offset = camera_.position
        
        x1, y1 = (self.position.x - self.scale.x/2 - camera_offset.x) * mult + Scene.width//2, (self.position.y - self.scale.y/2 - camera_offset.y) * mult + Scene.height//2
        x2, y2 = (self.position.x + self.scale.x/2 - camera_offset.x) * mult + Scene.width//2, (self.position.y + self.scale.y/2 - camera_offset.y) * mult + Scene.height//2
        self.ids.append(Scene.canvas.create_rectangle(x1, y1, x2, y2, fill = color, outline = self.outline_color))
        x, y = (self.position.x - camera_offset.x) * mult + Scene.width//2, (self.position.y - camera_offset.y) * mult + Scene.height//2
        self.ids.append(Scene.canvas.create_text(x, y, text = text, fill = self.text_color, font = ('Times', int(0.35 * Scene.unit))))
        
        # Scene.canvas.create_rectangle((self.position.x - self.scale.x/2) * Scene.unit + Scene.width//2, (self.position.y - self.scale.y/2) * Scene.unit + Scene.height//2, (self.position.x + self.scale.x/2) * Scene.unit + Scene.width//2, (self.position.y + self.scale.y/2) * Scene.unit + Scene.height//2, fill = color, outline = self.outline_color)#, width = self.outline_width
        # Scene.canvas.create_text(self.position.x * Scene.unit + Scene.width//2, self.position.y * Scene.unit + Scene.height//2, text = text, fill = self.text_color, font = ('Times', int(0.35 * Scene.unit)))
    def pressed(self, key):
        if self.selected:
            if key.name == "space":
                key.name = " "
            elif key.name == "backspace":
                self.text = self.text[:self.cursor-1] + self.text[self.cursor:]
                self.cursor = max(self.cursor-1, 0)
            elif key.name == "delete":
                self.text = self.text[:self.cursor] + self.text[self.cursor+1:]
            elif key.name == "left":
                self.cursor = max(self.cursor-1, 0)
            elif key.name == "right":
                self.cursor = min(self.cursor+1, len(self.text))
            elif key.name == "enter":
                self.selected = False
            elif len(key.name) == 1:
                # self.text += key.name
                self.text = self.text[:self.cursor] + key.name + self.text[self.cursor:]
                self.cursor+=1
    def class_update(self):
        mouse_x, mouse_y = InputManager.mousePos(False)
        if InputManager.getMouseButton(0):
            if self.position.x - self.scale.x/2 < mouse_x < self.position.x + self.scale.x/2 and self.position.y - self.scale.y/2 < mouse_y < self.position.y + self.scale.y/2:
                self.selected = True
            else: self.selected = False                
        if self.selected:
            keyboard.on_press(self.pressed, suppress=True)
    def get_text(self, to_cursor = False):
        if to_cursor: return self.text[:self.cursor]
        return self.text

class ParticleSystem(Entity):
    def __init__(self, pos=copy(Vector(0, 0)), rot=0, particle_color = Color.WHITE, spawn_range = 1, spawn_angle = radians(360), spawn_num = [5, 10], particle_size = 0.1, force = [1, 2], lifetime = [5, 10], particle_update = _empty, tag=None, mass=5, drawable=True, usable=True, on_scene=True, entity_update = _empty, entity_class = None, static = False):
        super().__init__(pos, rot, tag, mass, drawable, usable, on_scene, entity_update, entity_class, static)
        self.particle_color = particle_color
        self.particle_size = particle_size
        self.spawn_range = spawn_range
        self.spawn_angle = spawn_angle
        self.spawn_num = spawn_num
        self.particle_force = force
        self.lifetime = lifetime
        self.particle_update = particle_update
        
        self.particles = []
    def class_update(self):
        for particle in self.particles:
            if time() - particle.lifestart >= particle.lifetime or not particle in Scene.all_entities:
                self.particles.pop(self.particles.index(particle))
                if particle in Scene.all_entities:
                    particle.destroy()
                continue
            self.particle_update(particle)
    def clear(self):
        for particle in self.particles:
            particle.destroy()
            self.particles = []
    def generate(self):
        size = self.particle_size
        spawn_range = self.spawn_range
        spawn_num = self.spawn_num
        if type(spawn_num) in [tuple, list]:
            spawn_num = Random.int(spawn_num[0], spawn_num[1])
        color = self.particle_color
        for i in range(spawn_num):
            angle = Random.percent(self.spawn_angle) - self.spawn_angle/2 - self.rotation
            dist = Random.percent(spawn_range)
            pos = self.position + Vector(dist * sin(angle), dist * cos(angle))
            particle = Circle(pos=pos, radius=size, color=color)
            random_force = self.particle_force
            if type(random_force) in [tuple, list]:
                random_force = Random.float(self.particle_force[0], self.particle_force[1])
            particle.lifestart = time()
            particle.lifetime = self.lifetime
            if type(particle.lifetime) in [tuple, list]:
                particle.lifetime = Random.float(self.lifetime[0], self.lifetime[1])
            particle.force(Vector(random_force * sin(angle), random_force * cos(angle)))
            self.particles.append(particle)

class Raycast:
    def ray(self, start_point: Vector, dir: Vector, objects = Scene.all_entities):
        '''
        :return: ray hit point
        '''
        dir.normalise()
        x3 = -start_point.x
        y3 = start_point.y
        x4 = -start_point.x - dir.x
        y4 = start_point.y + dir.y

        last_pt = None

        for other in objects:
            if other.collider_shape == 'polygon':
                for i, v1 in enumerate(other.verticies):
                    x1 = -(v1.x + other.position.x)
                    y1 = v1.y + other.position.y
                    x2 = -(other.verticies[(i+1) % len(other.verticies)].x + other.position.x)
                    y2 = other.verticies[(i+1) % len(other.verticies)].y + other.position.y


                    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
                    if (den == 0):
                        continue

                    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
                    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
                    if 1 > t > 0 and u > 0:
                        pt = Vector()
                        pt.x = x1 + t * (x2 - x1)
                        pt.y = y1 + t * (y2 - y1)

                        # dist = hypot(pt.x - x3, pt.y - y3)
                        # if not last_pt:
                        #     last_pt = pt
                        #     last_dist = dist
                        # elif dist < last_dist:
                        #     last_dist = dist
                        #     last_pt = pt
            elif other.collider_shape == "line":
                x1 = -other.start.x
                y1 = other.start.y
                x2 = -other.end.x
                y2 = other.end.y
                den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
                if (den == 0):
                    continue

                t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
                u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
                if 1 > t > 0 and u > 0:
                    pt = Vector(x1 + t * (x2 - x1), y1 + t * (y2 - y1))
                    # pt.x = 
                    # pt.y = 

            elif other.collider_shape == 'circle':
                dir2 = Vector(sign(dir.x)*dir.y, -sign(dir.x)*(dir.x))
                line = Line(start=other.position - dir2*other.radius, end=other.position + dir2*other.radius, on_scene=True, color=Color.GREEN)
                pt = raycaster.ray(start_point, dir, [line])
                # print(line.start, line.end)
                if pt:
                    angle = atan2(start_point.y - other.position.y, other.position.x - start_point.x)
                    distance = sqrt(abs(other.radius**2 - Vector.distance(other.position, pt)**2))
                    pt = Vector(-1 * dir * distance, -1 * dir * distance)
                # if hypot(other.position.x - start_point.x, other.position.y - start_point.y) <= other.radius:
                #     angle = atan2(start_point.y - other.position.y, start_point.x - other.position.x)
                #     pt = Vector(-cos(angle) * other.radius + other.position.x, -sin(angle) * other.radius + other.position.y)
            
            try:
                dist = hypot(pt.x - x3, pt.y - y3)
                if not last_pt:
                    last_pt = pt
                    last_dist = dist
                elif dist < last_dist:
                    last_dist = dist
                    last_pt = pt
            except: pass
        if last_pt:
            last_pt.x *= -1
            # pt = last_pt
            # Scene.canvas.create_oval(pt.x * Scene.unit - 5 + Scene.width//2, pt.y * Scene.unit - 5 + Scene.height//2, pt.x * Scene.unit + 5 + Scene.width//2, pt.y * Scene.unit + 5 + Scene.height//2, fill = 'yellow')
        
        return last_pt

window_bounds = Polygon(scale=Scene.getWindowSize(True), on_scene=False, static=True)
raycaster = Raycast()
InputManager.initialisate()

left = Vector(-1, 0)
right = Vector(1, 0)
up = Vector(0, -1)
down = Vector(0, 1)