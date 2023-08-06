"""The config module of the application"""
from common.config import Config, ConfigEntry, CliEntry
from common.logger import get_level_choices, get_format_choices

APP_NAME = "minimum"
APP_DESCRIPTION = "The bare-minimum application"

config_entries = [
    ConfigEntry(
        name="NUM_PRODUCERS",
        help_text="The number of producers",
        default=1,
        cli=CliEntry(
            short_flag="-p", name="--num-producers", entry_type=int, action="store"
        ),
    ),
    ConfigEntry(
        name="NUM_CONSUMERS",
        help_text="The number of consumers",
        default=1,
        cli=CliEntry(
            short_flag="-c", name="--num-consumers", entry_type=int, action="store"
        ),
    ),
    ConfigEntry(
        name="LOG_LEVEL",
        help_text=f"Log level {get_level_choices()}",
        default="info",
        cli=CliEntry(short_flag="-l", name="--log-level", choices=get_level_choices()),
    ),
    ConfigEntry(
        name="LOG_FORMAT",
        help_text=f"The format of the log messages {get_format_choices()}",
        default="text",
        cli=CliEntry(
            short_flag="-f", name="--log-format", choices=get_format_choices()
        ),
    ),
    ConfigEntry(
        name="DUMP_CONFIG",
        help_text="Dump the actual configuration parameters of the application",
        default=False,
        cli=CliEntry(
            short_flag="-d", name="--dump-config", entry_type=bool, action="store_true"
        ),
    ),
    ConfigEntry(
        name="HEALTH_CHECK",
        help_text="Enable to run health check web service with '/health' endpoint",
        default=True,
        cli=CliEntry(
            short_flag="-hc",
            name="--health-check",
            entry_type=bool,
            action="store_true",
        ),
    ),
    ConfigEntry(
        name="HEALTH_CHECK_HOST",
        help_text="Host for health check web service",
        default="127.0.0.1",
        cli=CliEntry(
            short_flag="-hh",
            name="--health-check-host",
            entry_type=str,
        ),
    ),
    ConfigEntry(
        name="HEALTH_CHECK_PORT",
        help_text="Port number for health check web service",
        default=8008,
        cli=CliEntry(
            short_flag="-hp",
            name="--health-check-port",
            entry_type=int,
        ),
    ),
]

application_config = Config(APP_NAME, APP_DESCRIPTION, config_entries)
