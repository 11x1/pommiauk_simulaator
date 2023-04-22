import random
import pygame.color

from constants import *
from objects import block

class Bomb:
    def __init__( self, pos: tuple[ int, int ] ):
        self.pos = list( pos ) \
            if not pos is None else \
            [
                int( WIDTH * random.random( ) ),
                int( HEIGHT * random.random( ) )
            ]

        self.velocity = [ 0, 0 ]
        self.color = pygame.color.Color( 255, 0, 0, 255 )

        self.mass = 1
        self.air_deacceleration = 0.8

        self.rendering = {
            'radius' : 4
        }

    def get_pos( self ) -> tuple[ int, int ]:
        return self.pos[ 0 ], self.pos[ 1 ]

    def set_pos( self, new_pos: tuple[ int, int ] ) -> None:
        self.pos[ 0 ] = new_pos[ 0 ]
        self.pos[ 1 ] = new_pos[ 1 ]

    def get_as_pixel( self ) -> pygame.color.Color:
        return self.color

    def simulate_tick( self ):
        acceleration = GRAVITY # self.mass * GRAVITY / self.mass

        self.velocity[ 0 ] *= self.air_deacceleration
        self.velocity[ 1 ] += acceleration * self.air_deacceleration

        self.pos[ 0 ] += self.velocity[ 0 ]
        self.pos[ 1 ] += self.velocity[ 1 ]

    def bounce_ground( self, bounced_block: block.BedrockBlock ):
        self.velocity[ 1 ] *= -bounced_block.bounce_factor