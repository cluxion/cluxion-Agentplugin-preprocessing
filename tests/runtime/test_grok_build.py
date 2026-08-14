from pathlib import Path

from cluxion_runtime.adapters.grok_build import (
    GROK_COMPOSER_25_FAST,
    build_grok_composer_command,
)


def test_caller_supplies_current_model_and_composer_remains_explicit() -> None:
    default = build_grok_composer_command(
        "inspect", cwd=Path("/repo"), model="fixture-current"
    )
    composer = build_grok_composer_command(
        "inspect", cwd=Path("/repo"), model=GROK_COMPOSER_25_FAST
    )

    assert default[default.index("-m") + 1] == "fixture-current"
    assert composer[composer.index("-m") + 1] == "grok-composer-2.5-fast"
