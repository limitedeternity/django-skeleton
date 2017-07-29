from split_settings.tools import include

include(
    # Load environment settings
    'base/env.py',

    # Here we should have the order because of dependencies
    'base/paths.py',
    'base/apps.py',
    'base/middleware.py',

    # Load all other settings
    'base/*.py',

)
