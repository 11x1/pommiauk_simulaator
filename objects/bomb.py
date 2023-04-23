import random
from typing import Dict

import pygame.color

from constants import *
from objects import block
from game_types import vector

class Bomb:
    def __init__( self, pos: vector.Vector = None ):
        self.pos = pos \
            if not pos is None else \
            vector.Vector(
                int( WIDTH * random.random( ) ),
                int( HEIGHT * random.random( ) )
            )

        self.velocity = Vector( 0, 0 )
        self.color = pygame.color.Color( 255, 0, 0, 255 )

        self.mass = int( random.random( ) * 10 )
        self.air_deacceleration = 0.8

        self.rendering = {
            'radius' : 4
        }

    def get_pos( self ) -> vector.Vector:
        return self.pos

    def set_pos( self, new_pos: vector.Vector ) -> None:
        self.pos = new_pos

    def get_as_pixel( self ) -> pygame.color.Color:
        return self.color

    def get_next_tick( self ) -> Dict[ str, vector.Vector ]:
        acceleration = GRAVITY * self.mass  # self.mass * GRAVITY / self.mass

        velocity = self.velocity
        pos = self.pos

        velocity.x *= self.air_deacceleration
        velocity.y += acceleration * self.air_deacceleration

        pos += velocity

        return {
            'pos': pos,
            'velocity': velocity
        }

    def simulate_tick( self, resimulate: bool = False ):
        if resimulate:
            acceleration = GRAVITY * self.mass # self.mass * GRAVITY / self.mass

            self.velocity.x *= self.air_deacceleration
            self.velocity.y += acceleration * self.air_deacceleration

            self.pos += self.velocity
        else:
            next_tick_data = self.get_next_tick( )

            self.pos = next_tick_data[ 'pos' ]
            self.velocity = next_tick_data[ 'velocity' ]

    def bounce_ground( self, bounced_block: block.BedrockBlock ):
        random_variation = 1 - random.random( ) * 0.2
        self.velocity.y *= -bounced_block.bounce_factor * random_variation

    def render( self, pixel_matrix: list[ list[ pygame.color.Color ] ] ):
        pos = self.get_pos( )
        radius = self.rendering[ 'radius' ]
        diameter = radius * 2
        for y in range( diameter ):
            y_coord = int( pos.y + (radius - y) )
            if y_coord < 0 or y_coord >= SIZE.y:  # out of screen bounds
                continue

            for x in range( diameter ):
                x_coord = int( pos.x + (radius - x) )
                if x_coord < 0 or x_coord >= SIZE.x:  # out of screen bounds
                    continue

                distance = ((x - radius) ** 2 + (y - radius) ** 2) ** 0.5
                if distance > radius:
                    continue

                pixel_matrix[ y_coord ][ x_coord ] = self.color
