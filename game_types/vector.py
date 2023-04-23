class Vector:
    def __init__( self, x: int = None, y: int = None, z: int = None ):
        if x is None:
            self.x = 0
            self.y = 0
            self.z = 0
        elif y is None:
            self.x = x
            self.y = x
            self.z = x
        elif z is None:
            self.x = x
            self.y = y
            self.z = None

    @property
    def tuple( self ) -> tuple:
        if self.z is None:
            return self.x, self.y
        return self.x, self.y, self.z

    def __add__( self, other ):
        if type( other ) == Vector:
            self.x += other.x
            self.y += other.y
            if self.z is not None and other.z is not None:
                self.z += other.z
        if type( other ) in ( int, float ):
            self.x += other
            self.y += other
            if self.z is not None:
                self.z += other
        return Vector( self.x, self.y, self.z )

    def __sub__( self, other ):
        return self.__add__( other * -1 )

    def __mul__( self, other ):
        if type( other ) == Vector:
            self.x *= other.x
            self.y *= other.y
            if self.z is not None and other.z is not None:
                self.z *= other.z
        if type( other ) in ( int, float ):
            self.x *= other
            self.y *= other
            if self.z is not None:
                self.z *= other
        return Vector( self.x, self.y, self.z )

    def __truediv__( self, other ):
        return self.__mul__( 1 / other )

    def __repr__( self ) -> str:
        return f'<{ self.__class__.__name__ }>({ round( self.x, 2 ) }, { round( self.y, 2 ) }{ ", " + str( round( self.z, 2 ) ) if self.z is not None else "" })'