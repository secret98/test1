import pygame as pg
pg.init()

scr_width, scr_height = 500, 500
win = pg.display.set_mode((scr_width, scr_height))
pg.display.set_caption('Stickman')

x,y = 50, 425
height, width = 60, 40
vel = 5
is_jump = False
jump_count = 10
run = True
while run:
    pg.time.delay(100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x > vel:
        x -= vel

    if keys[pg.K_RIGHT] and x < scr_width - width:
        x += vel
    if not is_jump:
        if keys[pg.K_DOWN] and y < scr_height - height:
            y += vel

        if keys[pg.K_UP] and y > vel:
            y -= vel

        if keys[pg.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg # * 0.5 == / 2
            jump_count -= 1
        else:
            is_jump = False 
            jump_count = 10


    win.fill((255,255,255))
    pg.draw.rect(win, (255, 0, 0), (x,y,width,height))
    pg.display.update()

pg.quit()
