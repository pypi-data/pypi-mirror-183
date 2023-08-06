"""Yapper module."""
from __future__ import annotations

from typing import TypedDict


class ModuleMap(TypedDict):
    """Typed dict for module maps."""

    module: str
    astro: str


class YapperConfig(TypedDict):
    """Typed dict for yapper config."""

    package_root_relative_path: str
    intro_template: str
    outro_template: str
    module_map: list[ModuleMap]
