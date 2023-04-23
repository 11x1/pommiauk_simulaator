import pygame

from constants import *
import game

pygame.init( )
screen = pygame.display.set_mode( ( SIZE.x * 2, SIZE.y * 2 ) )
surface = pygame.Surface( SIZE.tuple )

clock = pygame.time.Clock( )

simulator_game = game.GameData( )

for _ in range( 10 ):
    simulator_game.spawn_explosive( )

while True:
    for event in pygame.event.get( ):
        if event.type == pygame.QUIT:
            pygame.quit( )
            break

    screen.fill( ( 0, 0, 0 ) )

    simulator_game.do_tick( )
    pixels_data = simulator_game.get_render_data( )

    for ( idx_y, row ) in enumerate( pixels_data ):
        for ( idx_x, pixel_data ) in enumerate( row ):
            surface.set_at( ( idx_x, idx_y ), pixel_data )

    screen.blit( surface, WINDOW_START.tuple )

    pygame.display.update( )

    clock.tick( FPS )

