from spawns.spawn_ground import SpawnGround


class RemoveGround:
    def __init__(self, game):
        self.spawnground = SpawnGround(game)

    def remove_ground(self, ground):
        self.spawnground.all_ground.remove(ground)