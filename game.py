import pygame.color

import game_map
from constants import *
from objects import bomb, block

class GameData:
    def __init__( self ):
        self.map = game_map.generate_map( SIZE )

        self.explosives: list[ bomb.Bomb ] = [ ]

    def do_tick( self ):
        print( 'MAP: ', len( self.map[ 0 ] ), len( self.map ) )
        for explosive in self.explosives:
            pos = explosive.get_pos( )
            # find close blocks
            center_x = pos[ 0 ] / BLOCK_SIZE[ 0 ]
            center_y = pos[ 1 ] / BLOCK_SIZE[ 1 ]

            idx_c_x = int( center_x )
            idx_c_y = int( center_y )

            # first check if entity is inside a block
            print( idx_c_x, idx_c_y )
            collision_block = self.map[ idx_c_y ][ idx_c_x ]
            if collision_block.is_collideable( ):
                explosive.set_pos( ( pos[ 0 ], ( idx_c_y - 1 ) * BLOCK_SIZE[ 1 ] ) )
                explosive.bounce_ground( collision_block )

            explosive.simulate_tick( )

    # Return rgba pixel tuples in a matrix to update pygame surface with
    def get_render_data( self ) -> list[ list[ pygame.color.Color ] ]:
        map_pixel_data = [ [ pygame.color.Color( 255, 0, 0, 255 ) for _ in range( SIZE[ 0 ] ) ] for _ in range( SIZE[ 1 ] ) ]

        step = BLOCK_SIZE
        for y_index in range( 0, SIZE[ 1 ], step[ 1 ] ):
            map_y_index = int( y_index / step[ 1 ] )
            for x_index in range( 0, SIZE[ 0 ], step[ 0 ] ):
                map_x_index = int( x_index / step[ 0 ] )
                block_obj = self.map[ map_y_index ][ map_x_index ]

                block_color = block_obj.get_as_pixel( )

                for _y in range( step[ 1 ] ):
                    for _x in range( step[ 0 ] ):
                        map_pixel_data[ y_index + _y ][ x_index + _x ] = block_color

        for explosive in self.explosives:
            pos = explosive.get_pos( )
            radius = explosive.rendering[ 'radius' ]
            diameter = radius * 2
            for y in range( diameter ):
                y_coord = int( pos[ 1 ] + ( radius - y ) )
                if y_coord < 0 or y_coord >= SIZE[ 1 ]:  # out of screen bounds
                    continue

                for x in range( diameter ):
                    x_coord = int( pos[ 0 ] + ( radius - x ) )
                    if x_coord < 0 or x_coord >= SIZE[ 0 ]:  # out of screen bounds
                        continue

                    distance = ( (x-radius) ** 2 + (y-radius) ** 2 ) ** 0.5
                    if distance > radius:
                        continue

                    map_pixel_data[ y_coord ][ x_coord ] = explosive.color

        return map_pixel_data

    def spawn_explosive( self, pos: tuple[ int, int ] = None ):
        self.explosives.append(
            bomb.Bomb( pos )
        )