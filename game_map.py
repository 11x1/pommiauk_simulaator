from constants import *
from objects import block
from game_types import vector

# Generates a pixel data matrix to render in simulator.py
def generate_map( size: vector.Vector ) -> list[ list[ block.EmptyBlock | block.BedrockBlock ] ]:
    width = int( size.x / BLOCK_SIZE.x )
    height = int( size.y / BLOCK_SIZE.y )

    empty_map = [
        [ block.EmptyBlock( ) for _x in range( width ) ]
        for _y in range( height )
    ]

    empty_map[ -1 ] = [ block.BedrockBlock( ) for _x in range( width ) ]

    return empty_map