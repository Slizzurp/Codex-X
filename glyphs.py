class Glyph:
    def __init__(self, name, symbol, role, status, sync_depth):
        self.name = name
        self.symbol = symbol
        self.role = role
        self.status = status
        self.sync_depth = sync_depth
        self.echoes = []