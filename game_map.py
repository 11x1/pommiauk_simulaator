from constants import *
from objects import block

# Generates a pixel data matrix to render in simulator.py
def generate_map( size: tuple[ int, int ] ) -> list[ list[ block.EmptyBlock | block.BedrockBlock ] ]:
    width = int( size[ 0 ] / BLOCK_SIZE[ 0 ] )
    height = int( size[ 1 ] / BLOCK_SIZE[ 1 ] )

    empty_map = [
        [ block.EmptyBlock( ) for _x in range( width ) ]
        for _y in range( height )
    ]

    empty_map[ -1 ] = [ block.BedrockBlock( ) for _x in range( width ) ]

    return empty_map