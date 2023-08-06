from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
block_picked = grass_texture

sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')

punch_sound = Audio('assets/punch_sound', loop=False, autoplay=False)

window.fps_counter.enabled = True
window.exit_button.enabled = False


def update():
    global block_picked
    if held_keys['1']:
        block_picked = grass_texture

    if held_keys['2']:
        block_picked = stone_texture

    if held_keys['3']:
        block_picked = brick_texture

    if held_keys['4']:
        block_picked = dirt_texture

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.activate()
    else:
        hand.passive()


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.25,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.lime,
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                Voxel(position=self.position + mouse.normal, texture=block_picked)

            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True
        )


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6)
        )

    def activate(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)


for z in range(25):
    for x in range(25):
        voxel = Voxel((x, -400, z), texture=stone_texture)

for z in range(25):
    for x in range(25):
        voxel = Voxel((x, -300, z), texture=stone_texture)

for z in range(25):
    for x in range(25):
        voxel = Voxel((x, -200, z), texture=stone_texture)

for z in range(25):
    for x in range(25):
        voxel = Voxel((x, -100, z), texture=stone_texture)

for z in range(15):
    for x in range(15):
        for v in range(5):
            voxel = Voxel((x, v, z))

for z in range(15):
    for x in range(15):
        voxel = Voxel((x, 10, z))

voxel = Voxel((0, 5, 0))
for v in range(6):
    h = 5 + v
    for x in range(15):
        voxel = Voxel((x, h, 0))

    for x in range(15):
        voxel = Voxel((x, h, 14))

    for z in range(15):
        voxel = Voxel((14, h, z))

    for z in range(15):
        voxel = Voxel((0, h, z))

for v in range(2):
    h = 10 + v
    for x in range(15):
        voxel = Voxel((x, h, 0), texture=stone_texture)

    for x in range(15):
        voxel = Voxel((x, h, 14), texture=stone_texture)

    for z in range(15):
        voxel = Voxel((14, h, z), texture=stone_texture)

    for z in range(15):
        voxel = Voxel((0, h, z), texture=stone_texture)

player = FirstPersonController()
sky = Sky()
hand = Hand()


def run():
    app.run()
