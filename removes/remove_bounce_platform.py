from spawns.spawn_bounce_platform import SpawnBouncePlatform


class RemoveBouncePlatform:
    def __init__(self, game):
        self.spawnbounceplatform = SpawnBouncePlatform(game)

    def remove_bounce_platform(self, bounce_platform):
        self.spawnbounceplatform.all_bounce_platforms.remove(bounce_platform)
        