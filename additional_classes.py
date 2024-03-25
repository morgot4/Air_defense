import pygame as p

class EffectsSprites:

    def __init__(self, path, count, window, pos ,set_color, flip):
        self.path = path
        self.count = count
        self.anim_base = []
        self.frame = 0
        self.window = window
        self.pos = list(pos)
        self.flip = flip
        im = p.image.load(self.path + '-' + '0' + '.png').convert_alpha()
        im = p.transform.flip(im, self.flip, False)
        self.pos[0] = self.pos[0] + im.get_width()
        self.set_color = set_color
        
    def load(self):
        for i in range(self.count):
            i = str(i)
            im = p.image.load(self.path + '-' + i + '.png').convert_alpha()
            im = p.transform.flip(im, self.flip, False)
            im.set_colorkey(self.set_color)
            self.anim_base.append(im)
        

    def change_frame(self, amount):
        self.frame += amount
        if self.frame >= len(self.anim_base)-1:
            self.frame = 0

    def draw(self):
        self.window.blit(self.anim_base[self.frame], self.pos)

class HealthBar():
    def __init__(self,screen,max_health,bar_len,speed,x,y,width,height) -> None:
        self.current_health = max_health
        self.max_health = max_health
        self.screen = screen
        self.health_bar_lenght = bar_len
        self.target_health = max_health
        self.health_ration = self.max_health / self.health_bar_lenght
        self.speed = speed
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def get_damage(self,amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health <= 0:
            self.target_health = 0

    def get_health(self,amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health >= self.max_health:
            self.target_health = self.max_health

    def basic_health(self,):
        p.draw.rect(self.screen, (255,0,0),(self.x,self.y,self.target_health/self.health_ration,40))
        p.draw.rect(self.screen, (255,255,255),(self.x,self.y,self.health_bar_lenght,40),4)

    def advanced_health(self):
        transition_width = 0
        transition_color = (255,0,0)
        damage = False
        if self.current_health < self.target_health:
            self.current_health += self.speed * 2
            transition_width = int((self.target_health - self.current_health)/self.health_ration)
            transition_color = (0,255,0)
            damage = False
        if self.current_health > self.target_health:
            self.current_health -= self.speed
            transition_width = int((self.current_health - self.target_health)/self.health_ration)
            transition_color = (255,255,0)
            damage = True

        health_bar_width = int(self.current_health/self.health_ration)
        health_bar = p.Rect(self.x,self.y,health_bar_width,self.height)
        if damage:
            transition_bar = p.Rect(health_bar.right-transition_width,self.y,transition_width,self.height)
        else:
            transition_bar = p.Rect(health_bar.right,self.y,transition_width,self.height)
        
        p.draw.rect(self.screen, (66, 42, 56),(self.x,self.y,self.health_bar_lenght,self.height),self.width)
        p.draw.rect(self.screen, (255,0,0),health_bar)
        p.draw.rect(self.screen, transition_color, transition_bar)
        
class Font():
    def __init__(self, path,color, sizes):
        self.spacing = 1
        self.character_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']
        font_img = p.image.load(path).convert_alpha()
        current_char_width = 0
        self.characters = {}
        character_count = 0
        for x in range(font_img.get_width()):
            c = font_img.get_at((x, 0))
            if c[0] == 127:
                char_img = self.clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
                char_img.set_colorkey((0,0,0))
                
                char_img = p.transform.scale(char_img, (sizes['radar_terminal']['char'][0],sizes['radar_terminal']['char'][1]))
                char_img = self.set_color(char_img, color)
                self.characters[self.character_order[character_count]] = char_img.copy()
                character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        self.space_width = self.characters['A'].get_width()

    def render(self, surf, text, loc):
        x_offset = 0
        for char in text:
            if char != ' ':
                surf.blit(self.characters[char], (loc[0] + x_offset, loc[1]))
                x_offset += self.characters[char].get_width() + self.spacing
            else:
                x_offset += self.space_width + self.spacing

    def clip(self,surf,x,y,x_size,y_size):
        handle_surf = surf.copy()
        clipR = p.Rect(x,y,x_size,y_size)
        handle_surf.set_clip(clipR)
        image = surf.subsurface(handle_surf.get_clip())
        return image.copy()

    def set_color(self,img, color):
        for x in range(img.get_width()):
            for y in range(img.get_height()):
                if img.get_at((x,y)) == (0,0,0):
                    continue
                else:
                    img.set_at((x, y), color)
        return img

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = p.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		pos = p.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if p.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
		if p.mouse.get_pressed()[0] == 0:
			self.clicked = False
		surface.blit(self.image, (self.rect.x, self.rect.y))
		return action
