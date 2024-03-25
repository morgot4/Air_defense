from additional_classes import Font, HealthBar, EffectsSprites, Button
import pygame as p
import sys
import random
import math
import time
p.init()
WINDOW_SIZE = (p.display.Info().current_w,p.display.Info().current_h)
window = p.display.set_mode(WINDOW_SIZE)

if WINDOW_SIZE[0] / WINDOW_SIZE[1] == 16/9 or WINDOW_SIZE[0] / WINDOW_SIZE[1] == 16/10:
    sizes = {
    'gun': [WINDOW_SIZE[0]*0.2,WINDOW_SIZE[1] * 0.03],
    'base': [WINDOW_SIZE[0] * 0.1,WINDOW_SIZE[1] * 0.1],
    'radar': 
        {'max_distance':[WINDOW_SIZE[0] // 3, WINDOW_SIZE[1]//1.5],
        'size': p.rect.Rect(WINDOW_SIZE[0]* 0.34,WINDOW_SIZE[1]*0.87, WINDOW_SIZE[0] * 0.09,  WINDOW_SIZE[1] * 0.18)},
    'rocket': 
        {'speed':round(WINDOW_SIZE[0]*0.06),
         'size':[WINDOW_SIZE[0] * 0.07,WINDOW_SIZE[1] * 0.07]},
    'bullet': 
        {'size':WINDOW_SIZE[0] * 0.014,
         'speed':round(WINDOW_SIZE[1]*0.18)},
    'cool_down': 
        {'rect': p.rect.Rect(10,WINDOW_SIZE[1] - WINDOW_SIZE[1] * 0.9, WINDOW_SIZE[0] * 0.11,WINDOW_SIZE[1] *0.03),
         'speed':   WINDOW_SIZE[0] * 0.0018},
    'radar_terminal': 
        {'rect': p.rect.Rect(WINDOW_SIZE[0] * 0.79,WINDOW_SIZE[1]-WINDOW_SIZE[1] * 0.138, WINDOW_SIZE[0] * 0.23, WINDOW_SIZE[1] * 0.138),
        'font_xy':  [WINDOW_SIZE[0]*0.8,WINDOW_SIZE[1]*0.875],
        'char': [round(WINDOW_SIZE[0] * 0.009), round(WINDOW_SIZE[1] * 0.08)]},
    'target':
    {'size': p.rect.Rect(WINDOW_SIZE[0] * 0.46,WINDOW_SIZE[1],WINDOW_SIZE[0]*0.2,WINDOW_SIZE[1]*0.2)},
    'fire':
    {'locations':[WINDOW_SIZE[0] * 0.15, WINDOW_SIZE[0] * 0.2, WINDOW_SIZE[0] * 0.19]},
    'tymbler':  p.rect.Rect(WINDOW_SIZE[0] * 0.9,WINDOW_SIZE[1] * 0.7, WINDOW_SIZE[0]*0.1, WINDOW_SIZE[1]*0.16)}
elif WINDOW_SIZE[0] / WINDOW_SIZE[1] == 43/18:
    sizes = {
    'gun': [WINDOW_SIZE[0]*0.18,WINDOW_SIZE[1] * 0.04],
    'base': [WINDOW_SIZE[0] * 0.1,WINDOW_SIZE[1] * 0.1],
    'radar': 
        {'max_distance':[WINDOW_SIZE[0] // 3, WINDOW_SIZE[1]//1.5],
        'size':p.rect.Rect(WINDOW_SIZE[0]* 0.35,WINDOW_SIZE[1]*0.83, WINDOW_SIZE[0] * 0.09,  WINDOW_SIZE[1] * 0.2)},
    'rocket': 
        {'speed': round(WINDOW_SIZE[0]*0.09),
         'size':[WINDOW_SIZE[0] * 0.06,WINDOW_SIZE[1] * 0.06]},
    'bullet': 
        {'size':WINDOW_SIZE[0] * 0.01,
         'speed':round(WINDOW_SIZE[1]*0.4)},
    'cool_down': 
        {'rect': p.rect.Rect(10,WINDOW_SIZE[1] - WINDOW_SIZE[1] // 1.1, WINDOW_SIZE[0] * 0.11,WINDOW_SIZE[1] *0.03),
         'speed':  WINDOW_SIZE[0] * 0.004},
    'radar_terminal': {
        'rect': p.rect.Rect(WINDOW_SIZE[0]-WINDOW_SIZE[0] * 0.17,WINDOW_SIZE[1]-WINDOW_SIZE[1] * 0.138, WINDOW_SIZE[0] * 0.17, WINDOW_SIZE[1] * 0.138),
        'font_xy':  [WINDOW_SIZE[0]*0.843,WINDOW_SIZE[1]*0.9],
        'char': [round(WINDOW_SIZE[0] * 0.007), round(WINDOW_SIZE[1] * 0.06)]},
    'target':
    {'size': p.rect.Rect(WINDOW_SIZE[0] * 0.46,WINDOW_SIZE[1],WINDOW_SIZE[0]*0.25,WINDOW_SIZE[1]*0.25)},
    'fire':
    {'locations':[WINDOW_SIZE[0] * 0.3, WINDOW_SIZE[0] * 0.36, WINDOW_SIZE[0] * 0.42]},
    'tymbler':  p.rect.Rect(WINDOW_SIZE[0] * 0.9,WINDOW_SIZE[1] * 0.7, WINDOW_SIZE[0]*0.1, WINDOW_SIZE[1]*0.16)
    }
elif WINDOW_SIZE[0] / WINDOW_SIZE[1] == 4/3:
    sizes = {
    'gun': [WINDOW_SIZE[0]*0.28,WINDOW_SIZE[1] * 0.05],
    'base': [WINDOW_SIZE[0] * 0.18,WINDOW_SIZE[1] * 0.15],
    'radar': 
        {'max_distance':[WINDOW_SIZE[0] // 3, WINDOW_SIZE[1]//1.5],
        'size':[WINDOW_SIZE[0] * 0.15, WINDOW_SIZE[1] * 0.27]},
    'rocket': 
        {'speed':round(WINDOW_SIZE[0]*0.0019),
         'size':[WINDOW_SIZE[0] * 0.06,WINDOW_SIZE[1] * 0.06]},
    'bullet': 
        {'size':WINDOW_SIZE[0] * 0.014,
         'speed':round(WINDOW_SIZE[1]*0.14)},
    'cool_down': 
        {'rect': p.rect.Rect(10,WINDOW_SIZE[1] - WINDOW_SIZE[1] // 6, WINDOW_SIZE[0] * 0.11,WINDOW_SIZE[1] *0.03),
         'speed':   WINDOW_SIZE[0] * 0.0018},
    'radar_terminal': 
        {'rect': p.rect.Rect(WINDOW_SIZE[0] * 0.79,WINDOW_SIZE[1]-WINDOW_SIZE[1] * 0.138, WINDOW_SIZE[0] * 0.23, WINDOW_SIZE[1] * 0.138),
        'font_xy':  [WINDOW_SIZE[0]*0.8,WINDOW_SIZE[1]*0.875],
        'char': [round(WINDOW_SIZE[0] * 0.009), round(WINDOW_SIZE[1] * 0.08)]},
    'fire':
    {'locations':[WINDOW_SIZE[0] * 0.3, WINDOW_SIZE[0] * 0.36, WINDOW_SIZE[0] * 0.42]},
    'tymbler':  p.rect.Rect(WINDOW_SIZE[0] * 0.9,WINDOW_SIZE[1] * 0.7, WINDOW_SIZE[0]*0.1, WINDOW_SIZE[1]*0.16)}

framerate = 60
clock = p.time.Clock()
class PVO:
    def __init__(self):
        self.image_gun = p.image.load('images/gun.png').convert_alpha()
        self.image_base = p.image.load('images/osnovanie.png').convert_alpha()
        self.image_base = p.transform.scale(self.image_base, (sizes['base']))
        self.image_gun = p.transform.scale(self.image_gun, (sizes['gun']))
        self.image_base.set_colorkey((123,192,67))
        self.image_gun.set_colorkey((123,192,67))
        self.rect = self.image_gun.get_rect()
        self.base_x = WINDOW_SIZE[0]*0.2
        self.base_y = WINDOW_SIZE[1]-self.image_base.get_height()
        self.rect.centerx = self.base_x + (self.image_base.get_width()/2)
        self.rect.centery = self.base_y + (self.image_base.get_height()/1.2)
        self.rect1 = None
        self.angle = 0
        self.current_target = None
        tymb1 = p.image.load('images/off_tymbler.png').convert_alpha();tymb2 = p.image.load('images/on_tymbler.png').convert_alpha()
        tymb1 = p.transform.scale(tymb1, (sizes['tymbler'].width, sizes['tymbler'].height))
        tymb2 = p.transform.scale(tymb2, (sizes['tymbler'].width, sizes['tymbler'].height))
        tymb1.set_colorkey((123,192,67)); tymb2.set_colorkey((123,192,67))
        self.tymbler_images = [tymb1, tymb2]
        self.left = False
        self.right = False
        self.cool_down_rect = sizes['cool_down']['rect']
        self.cool_down_rect_width = 0
        self.gun_to_blit = self.image_gun
        self.auto = False
        self.bullet_spawn = [self.rect.x + self.rect.width-20 , self.rect.y]
        self.future_angle = 0

    def update(self): 
        if self.angle != 0:   
            self.bullet_spawn = [self.rect1.x + self.rect1.width-20, self.rect1.y]
        if self.angle <= 0:
            self.angle = 0
        if self.angle >= 90:
            self.bullet_spawn = [self.rect1.x, self.rect1.y-40]
        if self.angle >= 180:
            self.angle = 180
        if self.left:
            self.angle += 1
        if self.right:
            self.angle -= 1
        self.gun_to_blit = p.transform.rotate(self.image_gun,self.angle)
        self.rect1 = self.gun_to_blit.get_rect()
        self.gun_to_blit.set_colorkey((123,192,67))
        self.rect1.center = self.rect.center

    def auto_update(self):
        katetx = self.current_target.rect.x - self.rect.x
        katety = self.current_target.rect.y - self.rect.y
        self.future_angle = -math.atan(katety/katetx)
        self.future_angle = round(math.degrees(self.future_angle))
        if self.angle != 0:   
            self.bullet_spawn = [self.rect1.x + self.rect1.width-20, self.rect1.y]
        if self.angle <= 0:
            self.angle = 0
        if self.angle >= 90:
            self.bullet_spawn = [self.rect1.x, self.rect1.y-40]
        if self.angle >= 180:
            self.angle = 180
        if  self.future_angle > self.angle:
            self.angle += 1
        if self.future_angle < self.angle:
            self.angle -= 1
        if self.future_angle == self.angle and attack:
            objects.add(Bullet(pvo.bullet_spawn[0], pvo.bullet_spawn[1],'bullet', sizes['bullet']['speed'], pvo.angle, pvo.bullet_spawn, False))
            pvo.cool_down_rect_width = 0
            
        self.gun_to_blit = p.transform.rotate(self.image_gun,self.angle)
        self.rect1 = self.gun_to_blit.get_rect()
        self.gun_to_blit.set_colorkey((123,192,67))
        self.rect1.center = self.rect.center

    def cool_down(self,):
        global attack
        stage = sizes['cool_down']['speed']
        current_rect = p.rect.Rect(sizes['cool_down']['rect'].x, sizes['cool_down']['rect'].y, self.cool_down_rect_width,self.cool_down_rect.height)
        if self.cool_down_rect_width < self.cool_down_rect.width:
            attack = False
            self.cool_down_rect_width += stage
        else:
            self.cool_down_rect_width = self.cool_down_rect.width
            attack = True
            p.draw.rect(window, (23,245,245), (current_rect.x-10,current_rect.y-10, current_rect.width + 20,current_rect.height + 20,), 5)
            p.draw.rect(window, (23,244,14), (current_rect.x-10,current_rect.y-10, current_rect.width + 20,current_rect.height + 20,), 5)
        p.draw.rect(window, (255,255,255), self.cool_down_rect)
        p.draw.rect(window, (0,123,14), current_rect)

    
    def draw(self):
        if self.auto:
            window.blit(self.tymbler_images[1], sizes['tymbler'])
        else:
            window.blit(self.tymbler_images[0], sizes['tymbler'])
        window.blit(self.gun_to_blit, self.rect1)
        window.blit(self.image_base, (self.base_x, self.base_y))

class Radar:
    def __init__(self):
        self.image = p.image.load('images/Radar.png').convert_alpha()
        self.image = p.transform.scale(self.image, (sizes['radar']['size'].width, sizes['radar']['size'].height))
        self.rect = sizes['radar']['size']
        self.image.set_colorkey((123,192,67))
        self.max_distance = sizes['radar']['max_distance']
        self.zone = p.image.load('images/bullet.png').convert()
        self.zone = p.transform.scale(self.zone, (WINDOW_SIZE[0] * 0.8,WINDOW_SIZE[0] * 0.8))
        self.zone.set_colorkey((123,192,67))
        self.zone_rect = self.zone.get_rect()
        self.zone_rect.centery = self.rect.centery
        self.zone_rect.centerx = self.rect.centerx + WINDOW_SIZE[0] * 0.1
        self.zone_mask = p.mask.from_surface(self.zone)

    def scan(self, rocket):
        overlap_mask = self.zone_mask.overlap_mask(rocket.mask, (rocket.rect.x - self.zone_rect.x, rocket.rect.y - self.zone_rect.y))
        if overlap_mask.count() > 5:
            rocket.scaned = True
            angle = round((180/math.pi) * rocket.angle)
            if angle <= 0:
                angle = -(90+angle)
            katetx =  rocket.rect.centerx - self.rect.x
            katety = self.rect.y - rocket.rect.y
            distance = round((katetx**2 + katety **2) ** 0.5)
            if distance < 100:
                distance = 'BOOM'
            text = f'Scaning: {rocket.index}, {angle}, {distance}'
            return text 
        else:
            text = 'Scaning: . . .'
            return text
    
        
        
    def draw(self):
        
        window.blit(self.image, (self.rect.x,self.rect.y-40))

class Target:
    def __init__(self):
        self.image = p.image.load('images/farm.png').convert_alpha()
        self.image = p.transform.scale(self.image, (sizes['target']['size'].width,sizes['target']['size'].height))
        self.image.set_colorkey((123,192,67))
        self.health_bar = HealthBar(window, 1000, 600, 2, 12, WINDOW_SIZE[1]*0.04, 350, 50)
        self.rect = sizes['target']['size']
        self.rect.y = WINDOW_SIZE[1] - self.rect.height
        self.health_scripts = [False, False, False]

class MovingObject(p.sprite.Sprite):
    def __init__(self,x,y,type):
        p.sprite.Sprite.__init__(self)
        self.rect = p.rect.Rect(x,y,sizes['bullet']['size']*2,sizes['bullet']['size']*2)
        self.type = type
        self.died = False
    def screen_check(self):
        if self.rect.x + 50 >= WINDOW_SIZE[0] or self.rect.y+50 >= WINDOW_SIZE[1]:
            self.died = True

class Rocket(MovingObject):
    def __init__(self,velocity, angle, pos,type, index):
        super().__init__(0,0,type=type)
        self.angle = angle
        self.index = index
        self.scaned = False
        self.sprite = [p.image.load("images/rocket_0.png").convert(), p.image.load("images/rocket_1.png").convert(), p.image.load("images/rocket_2.png").convert()]
        self.anim_base = []
        for image in self.sprite:
            image = p.transform.scale(image, (sizes['rocket']['size']))
            if self.angle > 0:
                image = p.transform.flip(image, True, False)
            image = p.transform.rotate(image, 180 - ((180/math.pi) * self.angle))
            for j in range(0,13):
                self.anim_base.append(image)
        self.frame = 0
        self.image =  self.anim_base[self.frame]
        self.image.set_colorkey((123,192,67))
        self.x0 = pos[0]
        self.y0 = pos[1]
        self.rect = self.image.get_rect()
        self.rect.center = self.x0, self.y0
        self.vx = velocity[0] * math.cos(velocity[1])
        self.vy = -velocity[0] * math.sin(velocity[1])
        self.t = 0
        self.acceleration = (0, 0)
        self.mask = p.mask.from_surface(self.image)
        self.mask_2 = p.mask.from_surface(p.image.load('images/bullet.png').convert())

                
    def change_frame(self, amount):
        self.frame += amount
        if self.frame >= len(self.anim_base)-1:
            self.frame = 0
    def update(self, dt,) -> None:
        self.t += dt / 250.0
        self.image = self.anim_base[self.frame]
        self.image.set_colorkey((123,192,67))
        self.rect = self.image.get_rect()
        self.rect.width -= 20
        self.rect.height -= 50
        self.rect.center = (self.x0+100, self.y0)
        if self.x0 > target.rect.centerx:
            self.rect.centerx = self.x0 - self.vx * self.t + self.acceleration[0] * self.t ** 2 / 2
            self.rect.centery = self.y0 + self.vy * self.t + self.acceleration[1] * self.t ** 2 / 2
        else:
            self.rect.centerx = self.x0 + self.vx * self.t + self.acceleration[0] * self.t ** 2 / 2
            self.rect.centery = self.y0 - self.vy * self.t + self.acceleration[1] * self.t ** 2 / 2
  
    def moving_collision(self):
        global boom
        for object in objects:
            if object.type != 'rocket':
                overlap_mask = self.mask.overlap_mask(self.mask_2, (object.rect.x - self.rect.x, object.rect.y - self.rect.y))
                if overlap_mask.count() > 5:
                    self.died = True
                    object.kill()                   
                    boom = True
                    
                
    def draw(self):
        window.blit(self.image, self.rect)

def particles_draw(particl):
    global particles
    if particl != []:
        for partic in particl:
            partic[0][0] += partic[1][0]
            partic[0][1] += partic[1][1]
            partic[2] -= 0.1
            partic[1][1] += 0.1
            p.draw.circle(window, (random.randint(200,254), random.randint(0,200), 40), [int(partic[0][0]), int(partic[0][1])], int(partic[2])*10)
            if partic[2] <= 0:
                particl.remove(partic)
            particles = particl
def particles_spawn(x,y):
    particles = []
    for i in range(100):
        particle = [[x,y], [random.randint(0, 5), random.randint(1,5)], random.randint(4, 6)]
            
        speed_chancey = random.randint(1,2)
        speed_chancex = random.randint(1,2)
            
        if speed_chancey == 1:
            particle[1][1] = -particle[1][1]
        if speed_chancex == 2:
            particle[1][0] = -particle[1][0]
        particles.append(particle)
    return particles

class Bullet(MovingObject):
    def __init__(self,x,y,type,speed,angle, pos, auto):
        super().__init__(x,y,type=type)
        self.v0 = speed
        self.gravity = -10
        self.angle = angle
        self.pos = pos
        self.launched = True
        self.t = 0
        self.s = self.pos 
        self.v = (0, 0) 
        self.vm = speed #s
        self.auto = auto
        self.image = p.image.load('images/bullet.png').convert()
        self.image = p.transform.scale(self.image, (WINDOW_SIZE[0] * 0.03,WINDOW_SIZE[1] * 0.06))
        self.image.set_colorkey((123,192,67))
        self.a = (-1.0, 15.0)
        self.v0 = (self.vm*math.cos(math.radians(self.angle)), -self.vm*math.sin(math.radians(self.angle)))
        
    def update(self,dt):
        if self.launched:
            self.t = self.t + dt/250.0
            self.v =  (self.v0[0] + self.a[0]*self.t, self.v0[1] + self.a[1]*self.t)
            self.vm = math.sqrt(self.v[0]*self.v[0] + self.v[1]*self.v[1])
            self.s0 = self.pos
            self.s = (self.s0[0] + self.v0[0]*self.t + self.a[0]*self.t*self.t/2, self.s0[1] + self.v0[1]*self.t + self.a[1]*self.t*self.t/2)
            if self.s[1] >= WINDOW_SIZE[1]:
                self.launched = False
                self.kill()

    def auto_update(self,dt):
        if self.launched:
            self.t += dt/250
            self.v =  (self.v0[0] + self.a[0]*self.t, self.v0[1] + self.a[1]*self.t)
            self.vm = math.sqrt(self.v[0]*self.v[0] + self.v[1]*self.v[1])
            self.s0 = self.pos
            self.s = (self.s0[0] + self.v0[0]*self.t + self.a[0]*self.t*self.t/2, self.s0[1] + self.v0[1]*self.t + self.a[1]*self.t*self.t/2)
            if self.s[1] >= WINDOW_SIZE[1]:
                self.launched = False
                self.kill()
        
    def draw(self):
        self.rect.x = self.s[0]
        self.rect.y = self.s[1]
        window.blit(self.image, self.rect)
       


def check_health():
    if target.health_bar.current_health <= 600 and target.health_bar.current_health >= 400:
        target.health_scripts[0] = True
    elif target.health_bar.current_health <= 400 and target.health_bar.current_health >= 200:
        target.health_scripts[1] = True
    elif target.health_bar.current_health <= 200 and target.health_bar.current_health >= 0:
        target.health_scripts[2] = True

def die_func():
    global isLive
    
    if exit_button.draw(window):
        p.quit()
        sys.exit()
    if restart_button.draw(window):
        isLive = True

def main_game(pvo, radar, target, objects):
    global isLive, attack, boom, particles
    rockets = []
    particles = []
    num = 1
    boom_sound = p.mixer.Sound('boom.wav')
    p.mixer.Sound.set_volume(boom_sound, 0.01)
    attack = False
    bg = p.image.load('images/bg2.png').convert_alpha()
    bg = p.transform.scale(bg, (WINDOW_SIZE[0],WINDOW_SIZE[1]))
    t0 = time.time()
    terminal_font = Font('images/large_font.png', (0,255,0), sizes)
    die = Font('images/large_font.png', (255,20,20), sizes)
    text = 'Scaning: . . .'
    fires = []
    flip = False
    boom = False
    
    for i in range(len(target.health_scripts)):
        k = random.randint(1,2)
        if k == 1:
            flip = True
        else:
            flip = False
        fire = EffectsSprites('images/fire1/Pixel art fire effects', 120, window, (sizes['fire']['locations'][i],WINDOW_SIZE[1]-290), (16,12,33), flip)
        fires.append(fire)
    for fire in fires:
        fire.load()
    while True:
        current_t = time.time()
        window.blit(bg, (0,0))
        window.blit(target.image, target.rect)
        target.health_bar.advanced_health()
        if not isLive:
            die_func()
            text = 'You Died'
            die.render(window,text,sizes['radar_terminal']['font_xy'])
            if isLive:
                num = 1
                for i in range(3):
                    target.health_scripts[i] = False
                t0 = time.time()
                for object in objects:
                    object.kill()
        
        for i in range(3):
            if target.health_scripts[i]:
                fires[i].draw()
                fires[i].change_frame(1)
        dt = clock.tick(60)
        particles_draw(particles)
        if isLive:
            check_health()
            if current_t - t0 >= 3:
                t0 = time.time()
                rx = random.randint(0,  WINDOW_SIZE[0])
                ry = random.randint(-200, 0)
                rocket_angle = math.atan((ry - target.rect.centery)/(rx - target.rect.centerx))
                rocket = Rocket(velocity=(sizes['rocket']['speed']/2, rocket_angle),angle=rocket_angle, pos=(rx, ry), type='rocket', index=num, )
                objects.add(rocket)
                rockets.append(rocket)
                num += 1
            objects.update(dt)
            if not pvo.auto:
                pvo.update()
            for object in objects:
                if object.type == 'rocket':
                    if object.scaned and pvo.auto:
                        print('a')
                        pvo.current_target = object
                        pvo.auto_update()
                    if object.rect.colliderect(target.rect):
                        target.health_bar.get_damage(100)
                        boom = True
                        object.died = True
                    if not object.scaned:
                        text = radar.scan(object)
                    object.moving_collision()
                    if boom:
                        particles = particles_spawn(object.rect.centerx,object.rect.centery)
                        boom_sound.play()
                        boom = False
                    
                    if object.died == True:
                        rockets.remove(object)
                        object.kill()
                        text = 'Scaning: . . .'
                    object.change_frame(1)
                object.draw()
                object.screen_check()
        pvo.cool_down()
        pvo.draw()
        radar.draw()
        p.draw.rect(window, (0,0,0), sizes['radar_terminal']['rect'])
        terminal_font.render(window,text,sizes['radar_terminal']['font_xy'])
        if target.health_bar.current_health <= 0:
            isLive = False
            target.health_bar.get_health(1000)

        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN and event.button == 1:
                pos = p.mouse.get_pos()
                
                if sizes['tymbler'].collidepoint(pos):
                    if pvo.auto:
                        pvo.auto = False
                    else:
                        pvo.auto = True
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    p.quit()
                    sys.exit()
                if event.key == p.K_LEFT:
                    pvo.left = True
                if event.key == p.K_SPACE:
                    if attack and isLive:
                        objects.add(Bullet(pvo.bullet_spawn[0], pvo.bullet_spawn[1],'bullet', sizes['bullet']['speed'], pvo.angle, pvo.bullet_spawn, False))
                        pvo.cool_down_rect_width = 0
                if event.key == p.K_RIGHT:
                    pvo.right = True
            if event.type == p.KEYUP:
                if event.key == p.K_LEFT:
                    pvo.left = False
                if event.key == p.K_RIGHT:
                    pvo.right = False
        p.display.update()

exit_button = Button(WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2, p.image.load('images/exit_button.png').convert_alpha(), 3)
restart_button = Button(WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/4, p.image.load('images/restart_button.png').convert_alpha(), 3)


pvo = PVO()
radar = Radar()
objects = p.sprite.Group()
target = Target()
isLive = True
main_game(pvo,radar,target,objects)