import pygame as game
import mainlib as lib
import sys

game.init()
frames = game.time.Clock()
human =0
AI = 0
status = -1

while True:
    Board = lib.Game()
    Board.create_board()
    Board.create_boxes()

    #choose turn
    Board.display_msg("Do you want to start first [y/n]")
    response = input()
    Board.surface.fill((255,255,255))

    #set initial turns
    if response == 'y' or response == 'Y':
        human=1
        AI=0
    else:
        human =0
        AI=1;

    #set initial status
    status =- 1

    #draw lines
    Board.draw_lines()

    while True:
        for event in game.event.get():
            if event.type == game.QUIT:
                game.quit()
                sys.exit()

            if  AI == 1:
                Board.AI_turn()
                AI=0
                human=1
                status=Board.check_status()

            elif event.type==game.MOUSEBUTTONUP:
                if human == 1:
                    x,y = event.pos
                    valid=Board.human_turn(x,y)
                    if valid is True:
                        AI = 1
                        human = 0
                        status = Board.check_status()
            if status != -1:
                break
        game.display.update()
        frames.tick(30)
        if status != -1:
            break
    game.mixer.stop()

    if status == 2:
        Board.display_msg('YOU WON THE GAME')
        game.time.delay(4000)

    if status == 1:
        Board.display_msg('YOU LOSE THE GAME')
        game.time.delay(4000)

    if status == 0:
        Board.display_msg("IT'S A TIE")
        game.time.delay(4000)

    Board.surface.fill((255,255,255))
    Board.display_msg('want to play another game [y/n]')
    restart = input()

    if restart=='n' or restart=='N':
        break

