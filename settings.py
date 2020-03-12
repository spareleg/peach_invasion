class Settings:
    """ Stores game settings """

    def __init__(self):
        # Player
        self.player_image = 'images/player.bmp'
        self.player_speed = 4.5

        # Bullets
        self.bullet_image = 'images/bullet.bmp'
        self.bullet_speed = 6.5

        # Enemy
        self.enemy_image = 'images/enemy.bmp'
        self.enemy_speed = 1.5

        # Ammo
        self.ammo_image = 'images/ammo.bmp'
        self.ammo_limit = 2

        # Health
        self.health_image = 'images/health.bmp'
        self.health_limit = 3

        # Background
        self.bg_color = (20, 60, 30)
        self.bg_grass_image = 'images/grass.bmp'
        self.bg_grass_number = 35

        # Scoreboard
        self.scoreboard_txt_color = (210, 240, 220)
        self.scoreboard_font_size = 42
        self.scoreboard_margin = 10

        # Button
        self.btn_size = (250, 70)
        self.btn_color = (210, 240, 220)
        self.btn_txt_color = (20, 60, 30)
        self.btn_font_size = 64

        # Gameplay
        self.speedup_rate = 1.1
