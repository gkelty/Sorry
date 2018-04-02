import pygame
import pygame.locals as pl
import os.path
pygame.font.init()
screen = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
BLACK = (0, 0, 0)


class TextInputBox:
    # Modified from https://github.com/Nearoo/pygame-text-input/blob/master/pygame_textinput.py
    # Github, pygame_textinput, posted Nov. 28, 2017, updated Feb. 8, 2018 by user Nearoo
    # and from  https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame
    # StackOverflow, How to Create a Text Input Box with Pygame, posted Sept. 24, 2017, edited Nov. 29, 2017
    # by user skrx
    """
    This class lets the user input a piece of text within a box at a blinking cursor.
    Position within the text can be moved using the arrow-keys. Delete, backspace, home and end work as well.
    """
    def __init__(self, x, y, w, h,
                        font_family="",
                        font_size=25,
                        antialias=True,
                        text_color=BLACK,
                        cursor_color=BLACK,
                        repeat_keys_initial_ms=400,
                        repeat_keys_interval_ms=35):
        """
        Args:
            font_family: Name or path of the font that should be used. Default is pygame-font
            font_size: Size of the font in pixels
            antialias: (bool) Determines if antialias is used on fonts or not
            text_color: Color of the text
            cursor_color: Color of the cursor
            repeat_keys_initial_ms: ms until the keydowns get repeated when a key is not released
            repeat_keys_interval_ms: ms between to keydown-repeats if key is not released
        """

        #Box related vars:
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.active = False

        # Text related vars:
        self.antialias = antialias
        self.text_color = text_color
        self.font_size = font_size
        self.input_string = "" # Inputted text
        if not os.path.isfile(font_family): font_family = pygame.font.match_font(font_family)
        self.font_object = pygame.font.Font(font_family, font_size)

        # Text-surface will be created during the first update call:
        self.surface = self.font_object.render(self.input_string, True, self.color)
        self.surface.set_alpha(0)

        # Vars to make keydowns repeat after user pressed a key for some time:
        self.keyrepeat_counters = {} # {event.key: (counter_int, event.unicode)} (look for "***")
        self.keyrepeat_intial_interval_ms = repeat_keys_initial_ms
        self.keyrepeat_interval_ms = repeat_keys_interval_ms

        # Things cursor:
        self.cursor_surface = pygame.Surface((int(self.font_size/20+1), self.font_size))
        self.cursor_surface.fill(cursor_color)
        self.cursor_position = 0 # Inside text
        self.cursor_visible = False # Switches every self.cursor_switch_ms ms
        self.cursor_switch_ms = 500 # /|\
        self.cursor_ms_counter = 0

        self.clock = pygame.time.Clock()

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if self.rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.active = not self.active
                else:
                    self.active = False
                # Change the current color of the input box.
                if self.active:
                    self.color = COLOR_ACTIVE
                    self.cursor_visible = True

            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print(self.input_string)
                        self.input_string = ''
                    # If none exist, create counter for that key:
                    if not event.key in self.keyrepeat_counters:
                        self.keyrepeat_counters[event.key] = [0, event.unicode]

                    if event.key == pl.K_BACKSPACE: # FIXME: Delete at beginning of line?
                        self.input_string = self.input_string[:max(self.cursor_position - 1, 0)] + \
                                        self.input_string[self.cursor_position:]

                        # Subtract one from cursor_pos, but do not go below zero:
                        self.cursor_position = max(self.cursor_position - 1, 0)
                    elif event.key == pl.K_DELETE:
                        self.input_string = self.input_string[:self.cursor_position] + \
                                            self.input_string[self.cursor_position + 1:]

                    elif event.key == pl.K_RETURN:
                        return True

                    elif event.key == pl.K_RIGHT:
                        # Add one to cursor_pos, but do not exceed len(input_string)
                        self.cursor_position = min(self.cursor_position + 1, len(self.input_string))

                    elif event.key == pl.K_LEFT:
                        # Subtract one from cursor_pos, but do not go below zero:
                        self.cursor_position = max(self.cursor_position - 1, 0)

                    elif event.key == pl.K_END:
                        self.cursor_position = len(self.input_string)

                    elif event.key == pl.K_HOME:
                        self.cursor_position = 0

                    else:
                        # If no special key is pressed, add unicode of key to input_string
                        self.input_string = self.input_string[:self.cursor_position] + \
                                            event.unicode + \
                                            self.input_string[self.cursor_position:]
                        self.cursor_position += len(event.unicode) # Some are empty, e.g. K_UP

            elif event.type == pl.KEYUP:
                # *** Because KEYUP doesn't include event.unicode, this dict is stored in such a weird way
                if event.key in self.keyrepeat_counters:
                    del self.keyrepeat_counters[event.key]

        # Update key counters:
        for key in self.keyrepeat_counters :
            self.keyrepeat_counters[key][0] += self.clock.get_time() # Update clock
            # Generate new key events if enough time has passed:
            if self.keyrepeat_counters[key][0] >= self.keyrepeat_intial_interval_ms:
                self.keyrepeat_counters[key][0] = self.keyrepeat_intial_interval_ms - \
                                                    self.keyrepeat_interval_ms

                event_key, event_unicode = key, self.keyrepeat_counters[key][1]
                pygame.event.post(pygame.event.Event(pl.KEYDOWN, key=event_key, unicode=event_unicode))

        # Resize the box if the text is too long.
        width = max(200, self.surface.get_width() + 10)
        self.rect.w = width
                
        # Rerender text surface:
        self.surface = self.font_object.render(self.input_string, self.antialias, self.text_color)

        # Update self.cursor_visible
        if self.active:
            self.cursor_ms_counter += self.clock.get_time()
            if self.cursor_ms_counter >= self.cursor_switch_ms:
                self.cursor_ms_counter %= self.cursor_switch_ms
                self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            cursor_y_pos = self.font_object.size(self.input_string[:self.cursor_position])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if self.cursor_position > 0:
                cursor_y_pos -= self.cursor_surface.get_width()
            self.surface.blit(self.cursor_surface, (cursor_y_pos, 0))

        self.clock.tick()
        return False

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def get_surface(self):
        return self.surface

    def get_text(self):
        return self.input_string

    def get_cursor_position(self):
        return self.cursor_position

    def set_text_color(self, color):
        self.text_color = color

    def set_cursor_color(self, color):
        self.cursor_surface.fill(color)

    def clear_text(self):
        self.input_string = ""

# Create TextInput-object
textinput = TextInputBox(100, 100, 140, 22)

screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()

while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    textinput.draw(screen)

    pygame.display.flip()
    clock.tick(30)