from pathlib import Path

from PySide6.QtCore import QStandardPaths
APP_NAME = "PepperChat3"
def _add_dir(path:Path):
    path.mkdir(parents=True, exist_ok=True)
    return path
APP_DIR = _add_dir(Path(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation)) / APP_NAME)
LOG_DIR = _add_dir(APP_DIR / "logs")
SYSLOG_DIR = _add_dir(APP_DIR / "syslogs")