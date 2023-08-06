import abc
import inspect
from io import TextIOWrapper
from json import dump, load
from pathlib import Path
from typing import Any, Iterator, Optional

from teddecor import TED, p_value

from .types_default import TypesDefault, Options


def _save_to_file(file: str | Path, data: dict):
    with open(file, "+w", encoding="utf-8") as save_file:
        dump(data, save_file, indent=2)


def _save_to_open_file(file: TextIOWrapper, data: dict):
    dump(data, file, indent=2)


def _path(path: list[str]) -> str:
    """Generate the formatted path to the given variable."""
    return ".".join(f"[@F #eed49f]{TED.escape(val)}[@F]" for val in path)


def _type(val: Any) -> type:
    if not isinstance(val, type):
        return type(val)
    return val


def _all_types(values: Iterator[Any]) -> type:
    types = set()
    for val in values:
        types.add(_type(val))
    return types


def _inherits_config_base(val) -> bool:
    if isinstance(val, type):
        mro = val.mro()
    else:
        mro = type(val).mro()

    return ConfigBase in mro


class ConfigBase:
    """Base class for configuration logic.

    To customize how configs are loaded and saved you may inherit from this class and implement
    `__save__` and `__load__`. `__save__` takes a dict of the data and a file
    as either a str, Path, or TextIOWrapper. `__load__` takes a file as a str, Path, or
    TextIOWrapper and returns the loaded config as a dict. You may change other dunder methods as
    well, but that may break the functionality of the decorator and class.
    """

    def __init__(
        self,
        cls,
        cfg: Optional[dict] = None,
        save: str | Path | None = None,
        load: str | Path | None = None,
        save_defaults: bool = False,
    ):
        self.__tedconfig_attributes__ = {}
        self.__tedconfig_validated__ = []
        self.__classname__ = cls.__name__.lower()
        self.__qualname__ = self.__class__.__qualname__
        self.__tedconfig_save_defaults__ = save_defaults

        if isinstance(cfg, dict):
            self.__tedconfig_config__ = cfg
            self.__tedconfig_load_path__ = load
        elif isinstance(cfg, (str, Path)):
            self.__tedconfig_config__ = {}
            self.__tedconfig_load_path__ = Path(cfg).resolve()
        else:
            self.__tedconfig_config__ = {}
            self.__tedconfig_load_path__ = load

        self.__tedconfig_save_path__ = save

        for i in inspect.getmembers(cls):
            if not i[0].startswith("_"):
                if not inspect.ismethod(i[1]):
                    var, value = i
                    setattr(self, var, self.__get_default__(value))
                    self.__tedconfig_attributes__[var] = value

        if cfg is not None or self.__tedconfig_load_path__ is not None:
            self.__parse__()

        abc.update_abstractmethods(self)

    @classmethod
    def init(cls, cfg: dict | str | Path | None = None):
        """`classmethod`: Initialize the class and run config validation."""

        return cls(cfg)

    def is_default(self, key=None) -> bool:
        """Determine if a specific attribute is the default value."""
        if key is None:
            # Check if entire config object is default
            return all(self.__default__(attr) for attr in self.__tedconfig_attributes__)

        if key in self.__tedconfig_attributes__:
            # Check if specific config attribute is default
            return self.__default__(key)

        raise KeyError(
            f"{key!r} is not a valid attribute on the config {self.__classname__!r}"
        )

    def save(
        self,
        file: str | Path | TextIOWrapper | None = None,
        override: bool = False,
        save_defaults: bool = None,
    ):
        """Save the current configuration to a given save file. Accounts for
        provided save path in the decorator. If a nested config has a save path
        set in the decorator it will be saved to that file instead of the given file.

        Args:
            save_path (str | Path | TextIOWrapper): The path or file to where the config's json
                should written. Defaults to `None`.

            override (bool): If provided, all nested config classes are pulled into the same
                save/location. Otherwise, if a nested config class provides a save location
                then it will be saved there instead.
        """
        file = file or self.__tedconfig_save_path__

        if file is None:
            raise ValueError(
                "Must provide a save path or file in either the config decorator or in the \
save methods arguments"
            )

        self.__save__(self.__build_save_dict__(override, save_defaults), file)

        return self

    @classmethod
    def defaults(cls, file: str | Path | TextIOWrapper = None) -> dict:
        """`classmethod`: Return a dict representation of the configuration defaults.
        If a file is provided then the dict will be saved to that file.

        Returns:
            dict: dict representation of the configuration.
        """
        data = cls().__build_defaults_dict__()

        if file is not None:
            cls.__save__(data, file)
        else:
            return data

    def __iter__(self):
        for key, value in self.__tedconfig_attributes__.items():
            if isinstance(getattr(self, key), ConfigBase):
                yield key, dict(getattr(self, key))
            else:
                if key not in self.__tedconfig_validated__:
                    yield key, self.__get_default__(value)
                else:
                    yield key, getattr(self, key)

    @staticmethod
    def __load__(file: str | Path | TextIOWrapper):
        """Load a config file, convert to a dictionary, and return the result."""

        with open(file, "r", encoding="utf-8") as json:
            return load(json)

    @staticmethod
    def __save__(data: dict, file: str | Path | TextIOWrapper):
        """Save the config as a dict to a specific file."""

        if isinstance(file, TextIOWrapper):
            _save_to_open_file(file, data)
        else:
            _save_to_file(file, data)

    def __parse__(self, cfg: Optional[dict] = None, parent: Optional[list[str]] = None):
        """Parse the values given a configuration in dict form. Sets the given value
        to the attribute on this class. Replaces the typing values with actual values."""

        if cfg is None and self.__tedconfig_load_path__ is not None:
            # Evaluate data after loading it from file

            cfg = self.__load__(self.__tedconfig_load_path__)
        elif cfg is not None or self.__tedconfig_config__ not in [None, {}]:
            # Evaluate data from provided dict
            cfg = cfg or self.__tedconfig_config__
        else:
            # Evaluate as empty config
            cfg = {}

        self.__tedconfig_config__ = cfg
        # Used for error tracing
        parent = parent or []

        for key, value in cfg.items():
            self.__vk_in_object__(key, parent)
            self.__vk_options__(key, value, parent)
            self.__vk_list__(key, value, parent)
            self.__vk_tuple__(key, value, parent)
            self.__vk_dict__(key, value, parent)
            self.__vk_types_default__(key, value, parent)
            self.__vk_generic__(key, value, parent)

            attr = getattr(self, key)
            if _inherits_config_base(attr) and len(attr.__tedconfig_validated__) == 0:
                setattr(
                    self,
                    key,
                    attr.init().__parse__(value, [*parent, self.__classname__]),
                )
                self.__tedconfig_validated__.append(key)
                continue

            self.__tedconfig_validated__.append(key)
            setattr(self, key, value)

        return self

    def __get_default__(self, value) -> Any:
        if isinstance(value, TypesDefault):
            return value.default

        if isinstance(value, Options):
            return value.default

        if isinstance(value, list):
            return list([val for val in value if not isinstance(val, type)])

        if isinstance(value, tuple):
            return tuple([val for val in value if not isinstance(val, type)])

        if isinstance(value, dict):
            return dict(value)

        if isinstance(value, type) and _inherits_config_base(value):
            return value.init().__parse__()

        if isinstance(value, type):
            return value()

        if _inherits_config_base(value):
            return value.__parse__()

        return value

    def __build_save_dict__(
        self, override: bool = False, save_defaults: bool = None
    ) -> Iterator[Any]:
        """Build the dict representation of the config's current state."""
        result = {}

        save_defaults = save_defaults or self.__tedconfig_save_defaults__

        for key, value in self.__tedconfig_attributes__.items():
            if key not in self.__tedconfig_validated__:
                self.__tedconfig_validated__.append(key)
                value = self.__get_default__(value)
            else:
                value = getattr(self, key)

            if _inherits_config_base(value):
                if value.__tedconfig_save_path__ is not None and not override:
                    value.save()
                elif not value.is_default() or save_defaults:
                    result[key] = value.__build_save_dict__(override, save_defaults)
            elif not self.is_default(key) or save_defaults:
                result[key] = value
        return result

    def __build_defaults_dict__(self):
        """Build the default dict representation of the config class."""

        result = {}

        for key, value in self.__tedconfig_attributes__.items():
            if _inherits_config_base(value):
                result[key] = value.defaults()
            else:
                result[key] = self.__get_default__(value)
        return result

    def __default__(self, key):
        """Determine if a single attribute it's default value."""

        attr = getattr(self, key)
        if isinstance(attr, TypesDefault) and getattr(self, key).default == attr:
            return True

        if (
            isinstance(self.__tedconfig_attributes__[key], Options)
            and attr == self.__tedconfig_attributes__[key].default
        ):
            return True

        if isinstance(attr, type) and _inherits_config_base(attr):
            return True

        if (
            isinstance(self.__tedconfig_attributes__[key], type)
            and self.__tedconfig_attributes__[key]() == attr
        ):
            return True

        if _inherits_config_base(getattr(self, key)):
            return getattr(self, key).is_default()

        if getattr(self, key) == self.__tedconfig_attributes__[key]:
            return True

        return False

    def __vk_in_object__(self, key, parent):
        if not hasattr(self, key):
            raise ValueError(
                TED.parse(
                    f"Invalid variable [@F #eed49f]{key}[@F] in \
{_path([*parent, self.__classname__])}"
                )
            )

    def __vk_options__(self, key, value, parent):
        attr = self.__tedconfig_attributes__[key]
        if isinstance(attr, Options):
            if not isinstance(value, attr.types):
                raise TypeError(
                    TED.parse(
                        f"*{_path([*parent, self.__classname__, key])} must be \
any of these types: {', '.join(f'[@F #f5a97f]{val.__name__}[@]' for val in attr.types)}: \
was [@F 210]{_type(value)}"
                    )
                )

            if value not in attr.options:
                raise TypeError(
                    TED.parse(
                        f"*{_path([*parent, self.__classname__, key])} must be one of the \
following values: {', '.join(f'[@F #eed49f]{val!r}[@]' for val in attr.options)}: was [@F 210]{value!r}"
                    )
                )
        self.__tedconfig_validated__.append(key)

    def __vk_list__(self, key, value, parent):
        attr = self.__tedconfig_attributes__[key]
        if isinstance(attr, list) and (
            not isinstance(value, list)
            or any(type(val) not in _all_types(attr) for val in value)
        ):
            invalids = list(filter(lambda val: type(val) not in attr, value))
            if len(invalids) > 0:
                message = f"; contains invalid types \
{', '.join([f'[@F 210]{type(i).__name__}[@]' for i in invalids])}"
            else:
                message = f"; was [@F 210]{type(value)}"

            raise TypeError(
                TED.parse(
                    f"*{_path([*parent, self.__classname__, key])} must be a list containing \
any of these types: {', '.join(f'[@F #f5a97f]{val.__name__}[@]' for val in _all_types(attr))}{message}"
                )
            )

    def __vk_tuple__(self, key, value, parent):
        attr = self.__tedconfig_attributes__[key]
        if isinstance(attr, tuple) and (
            not isinstance(value, tuple)
            or any(type(val) not in _all_types(attr) for val in value)
        ):
            invalids = list(filter(lambda val: type(val) not in attr, value))
            if len(invalids) > 0:
                message = f"; contains invalid types \
{', '.join([f'[@F #f5a97f]{type(i).__name__}[@]' for i in invalids])}"
            else:
                message = f"; was [@F #f5a97f]{type(value)}"
            raise TypeError(
                TED.parse(
                    f"*{_path([*parent, self.__classname__, key])} must be a tuple containing \
any of these types: {', '.join(f'[@F #f5a97f]{val.__name__}[@]' for val in _all_types(attr))}{message}"
                )
            )

    def __vk_dict__(self, key, value, parent):
        attr = self.__tedconfig_attributes__[key]
        if isinstance(attr, dict) and not isinstance(value, dict):
            raise TypeError(
                TED.parse(
                    f"*{_path([*parent, self.__classname__, key])} must be a dict; was \
[@F 210]{type(value).__name__}"
                )
            )

    def __vk_generic__(self, key, value, parent):
        attr = self.__tedconfig_attributes__[key]
        if not isinstance(attr, type):
            attr = type(attr)
        if (
            not _inherits_config_base(attr)
            and key not in self.__tedconfig_validated__
            and not isinstance(value, attr)
        ):
            raise TypeError(
                TED.parse(
                    f"*{_path([*parent, self.__classname__, key])} must be of type \
[@F #f5a97f]{attr.__name__}[@]; was [@F 210]{type(value).__name__}"
                )
            )

    def __vk_types_default__(self, key, value, parent):
        attr = self.__tedconfig_attributes__[key]
        if isinstance(attr, TypesDefault):
            if type(value) not in attr.types:
                raise TypeError(
                    TED.parse(
                        f"*{_path([*parent, self.__classname__, key])} must be one \
of these types ({', '.join(f'[@F #f5a97f]{val.__name__}[@]' for val in attr.types)}); was \
[@F 210]{type(value).__name__}"
                    )
                )
            else:
                self.__tedconfig_validated__.append(key)

            if (
                isinstance(value, (list, tuple))
                and attr.nested_types is not None
                and any(type(val) not in attr.nested_types for val in value)
            ):
                raise ValueError(
                    TED.parse(
                        f"*Values in {_path([*parent, self.__classname__, key])} must be one \
of these types ({', '.join(f'[@F #f5a97f]{val.__name__}[@]' for val in attr.nested_types)})\
; was [@F 210]{type(value).__name__}"
                    )
                )
            else:
                self.__tedconfig_validated__.append(key)

    def __str__(self) -> str:
        return p_value(dict(self), depth=-1)
