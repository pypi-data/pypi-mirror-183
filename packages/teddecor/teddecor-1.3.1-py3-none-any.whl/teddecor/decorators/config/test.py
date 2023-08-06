from dataclasses import dataclass
from teddecor.decorators import config, Options


@config.yaml
class Cache:
    size = 1000
    timeout = 10000


@config.yaml(save="test.yaml", defaults=True)
class AppConfig:
    background = "black"
    cache = Cache


@config.json(save="test.json")
class Config:
    extensions = ["today", "junior", int, float]
    validate = [int, "junior", "day"]
    app = AppConfig
    day = Options("m", "t", "w", "th", "f", "sat", "sun", default="f")


cfg = Config.init({"extensions": ["tomorrow", "senior"], "day": "th"})
print(cfg)
cfg.save()
