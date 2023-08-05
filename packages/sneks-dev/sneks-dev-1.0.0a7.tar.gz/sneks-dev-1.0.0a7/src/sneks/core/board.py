"""
This holds the current game state. The board is in a grid shape with 0-based
row and column indices represented by (row, column) Cells:

(0, 0), (0, 1), (0, 2), ..., (0, COLUMNS - 1)
(1, 0), (1, 1), (1, 2), ..., (1, COLUMNS - 1)
...
(ROWS - 1, 0), (ROWS - 1, 1), ..., (ROWS - 1, COLUMNS - 1)
"""

from sneks.config.config import config

ROWS = config.game.rows
COLUMNS = config.game.columns
