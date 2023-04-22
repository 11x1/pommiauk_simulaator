import pygame.color

BLOCK_TYPES = {
    'air' : 0,
    'default' : 1
}

BLOCK_COLOR = {
    BLOCK_TYPES[ 'air' ] : pygame.color.Color( 255, 255, 255, 255 ),
    BLOCK_TYPES[ 'default' ] : pygame.color.Color( 100, 100, 100, 255 )
}

class EmptyBlock:
    def __init__( self ):
        self.type = BLOCK_TYPES[ 'air' ]
        self.collision = False

    def __repr__( self ) -> str:
        return f'<{ self.__class__.__name__ }>'

    def get_as_pixel( self ) -> pygame.color.Color:
        return BLOCK_COLOR[ self.type ]

    def is_collideable( self ):
        return self.collision


class BedrockBlock( EmptyBlock ):
    def __init__( self ):
        super( ).__init__( )
        self.type = BLOCK_TYPES[ 'default' ]
        self.collision = True
        self.bounce_factor = 0.8