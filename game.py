import pygame.color

import game_map
from constants import *
from objects import bomb, block

from game_types import vector

class GameData:
    def __init__( self ):
        self.map = game_map.generate_map( SIZE )

        self.explosives: list[ bomb.Bomb ] = [ ]

    def do_tick( self ):
        for explosive in self.explosives:
            next_tick_data = explosive.get_next_tick( )
            pos = next_tick_data[ 'pos' ]

            pos += next_tick_data[ 'velocity' ]

            pos.y += explosive.rendering[ 'radius' ]

            center_x = pos.x / BLOCK_SIZE.x
            center_y = pos.y / BLOCK_SIZE.y

            idx_c_x = int( center_x )
            idx_c_y = int( center_y )

            idx_c_x = max( 0, min( int( SIZE.x / BLOCK_SIZE.x ) - 1, idx_c_x ) )
            idx_c_y = max( 0, min( int( SIZE.y / BLOCK_SIZE.y ) - 1, idx_c_y ) )

            # first check if entity is inside a block
            should_resimulate = False
            collision_block = self.map[ idx_c_y ][ idx_c_x ]
            if collision_block.is_collideable( ):
                explosive.set_pos(
                    vector.Vector( pos.x, idx_c_y * BLOCK_SIZE.y - BLOCK_SIZE.y * 0.1 )
                )
                explosive.bounce_ground( collision_block )
                should_resimulate = True

            explosive.simulate_tick( resimulate=should_resimulate )

    # Return rgba pixel tuples in a matrix to update pygame surface with
    def get_render_data( self ) -> list[ list[ pygame.color.Color ] ]:
        map_pixel_data = [ [ 0 for _ in range( SIZE.x ) ] for _ in range( SIZE.y ) ]

        step = BLOCK_SIZE
        for y_index in range( 0, SIZE.y, step.y ):
            map_y_index = int( y_index / step.y )
            for x_index in range( 0, SIZE.x, step.x ):
                map_x_index = int( x_index / step.x )
                block_obj = self.map[ map_y_index ][ map_x_index ]

                block_color = block_obj.get_as_pixel( )

                # Block size has to be colored according to the block's color
                for _y in range( BLOCK_SIZE.y ):
                    for _x in range( BLOCK_SIZE.x ):
                        map_pixel_data[ y_index + _y ][ x_index + _x ] = block_color

        for explosive in self.explosives:
            explosive.render( map_pixel_data )

        return map_pixel_data

    def spawn_explosive( self, pos: vector.Vector = None ):
        self.explosives.append(
            bomb.Bomb( pos )
        )