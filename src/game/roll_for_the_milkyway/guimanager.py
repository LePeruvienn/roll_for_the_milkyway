from collections import defaultdict
import math
from src.gui.shapes import (
    Group,
    Rectangle,
    Line,
    Oval,
    Text,
    RegularPolygon,
    RegulareStar,
)

from src.game.roll_for_the_milkyway.roll_for_the_milkyway_referee import (
    NB_OBJECTIVES_PER_CATEGORY,
    PERSONAL_DICES_FACES,
    RESOURCES,
    XMIN,
    XMAX,
    YMIN,
    YMAX,
    NB_SHARED_DICES,
    SHARED_DICES_FACES,
    NB_PERSONAL_DICES,
    DICE_MIN_VALUE,
    DICE_MAX_VALUE,
    OBJECTIVES_CATEGORIES,
    EASY_OBJECTIVE,
    MEDIUM_OBJECTIVE,
    HARD_OBJECTIVE,
)

# Dices constants
DICES_WIDTH = 60
DICES_MARGIN = 20
DICE_POINT_RADIUS = 7
DICE_POINT_FILL_COLOR = (0, 0, 0)
XMIN_DICES = (
    XMIN
    + (XMAX - XMIN) // 2
    + DICES_MARGIN // 2
    - NB_SHARED_DICES // 2 * (DICES_MARGIN + DICES_WIDTH)
)
Y_DICES = YMIN + (YMAX - YMIN) // 2

STARDUST_COORDS_PERCENTS = [
    (43, 47),
    (90, 27),
    (59, 96),
    (27, 21),
    (46, 11),
    (88, 45),
    (46, 7),
    (34, 29),
    (19, 23),
    (72, 44),
    (16, 39),
    (16, 54),
    (39, 36),
    (38, 94),
    (14, 83),
    (39, 51),
    (28, 42),
    (56, 84),
    (35, 74),
    (6, 31),
    (50, 43),
    (78, 23),
    (59, 25),
    (55, 3),
    (3, 41),
    (36, 25),
    (9, 35),
    (55, 55),
    (69, 37),
    (46, 13),
    (62, 2),
    (21, 19),
    (49, 80),
    (10, 54),
    (46, 94),
    (21, 37),
    (78, 53),
    (61, 43),
    (16, 70),
    (85, 50),
    (76, 77),
    (27, 34),
    (27, 89),
    (94, 40),
    (27, 31),
    (92, 55),
    (3, 36),
    (24, 15),
    (64, 8),
    (83, 56),
    (63, 89),
    (67, 58),
    (50, 94),
    (38, 85),
    (66, 77),
    (68, 90),
    (73, 87),
    (45, 56),
    (81, 80),
    (35, 64),
    (74, 73),
    (30, 59),
    (16, 59),
    (0, 54),
    (55, 2),
    (64, 48),
    (61, 82),
    (41, 1),
    (69, 94),
    (10, 76),
]


def percent_to_delta(percentage):
    return (percentage - 50) * DICES_WIDTH // 200


STARDUST_COORDS_DELTA = [
    (percent_to_delta(px), percent_to_delta(py)) for px, py in STARDUST_COORDS_PERCENTS
]

STARDUST_POINT_RADIUS = 1

HELIUM3_PARTICULE_RADIUS = DICES_WIDTH // 8
HELIUM3_PARTICULE_MARGIN = 5
HELIUM3_PROTON_COLOR = (255, 0, 0)
HELIUM3_NEUTRON_COLOR = (255, 0, 255)

ANTIMATTER_PARTICULE_RADIUS = DICES_WIDTH // 6
ANTIMATTER_PARTICULE_MARGIN = 3
ANTIMATTER_STAR_RADIUS = DICES_WIDTH // 4

DARKMATTER_RADIUS = DICES_WIDTH // 3
DARKMATTER_COLOR = (0, 0, 0)

CENTER_COORDS_DELTA = (0, 0)
ABOVE_LEFT_COORDS_DELTA = (
    -DICES_WIDTH // 3.5,
    -DICES_WIDTH // 3.5,
)
ABOVE_RIGHT_COORDS_DELTA = (
    DICES_WIDTH // 3.5,
    -DICES_WIDTH // 3.5,
)
BELOW_LEFT_COORDS_DELTA = (
    -DICES_WIDTH // 3.5,
    DICES_WIDTH // 3.5,
)
BELOW_RIGHT_COORDS_DELTA = (
    DICES_WIDTH // 3.5,
    DICES_WIDTH // 3.5,
)
CENTER_LEFT_COORDS_DELTA = (-DICES_WIDTH // 3.5, 0)
CENTER_RIGHT_COORDS_DELTA = (DICES_WIDTH // 3.5, 0)

# Players names constants
PLAYERS_NAME_MARGIN = 10
PLAYERS_NAME_WIDTH = 300
PLAYERS_NAME_HEIGHT = 60
PLAYERS_NAME_RECT_STROKE_WIDTH = 5
PLAYERS_NAME_RECT_RADIUS = 10
PLAYERS_NAME_PADDING = 10
PLAYERS_NAME_MAX_CHAR = 12

PLAYERS_DICES_Y_DELTA = [
    PLAYERS_NAME_HEIGHT * 1.5,
    PLAYERS_NAME_HEIGHT * 1.5,
    -PLAYERS_NAME_HEIGHT * 0.5 - DICES_WIDTH,
    -PLAYERS_NAME_HEIGHT * 0.5 - DICES_WIDTH,
]

# Left abscissa for players names rectangles
PLAYERS_NAME_RECT_LEFTS = [
    XMIN + PLAYERS_NAME_MARGIN,
    XMAX - PLAYERS_NAME_WIDTH - PLAYERS_NAME_MARGIN,
    XMIN + PLAYERS_NAME_MARGIN,
    XMAX - PLAYERS_NAME_WIDTH - PLAYERS_NAME_MARGIN,
]
# Top ordinates for players names rectangles
PLAYERS_NAME_RECT_TOPS = [
    YMIN + PLAYERS_NAME_MARGIN,
    YMIN + PLAYERS_NAME_MARGIN,
    YMAX - PLAYERS_NAME_HEIGHT - PLAYERS_NAME_MARGIN,
    YMAX - PLAYERS_NAME_HEIGHT - PLAYERS_NAME_MARGIN,
]

# Colors of the four players
PLAYERS_COLORS = [(213, 94, 0), (204, 121, 167), (0, 114, 178), (0, 158, 115)]

# Move constants

MOVE_SCALE = 1.25
MOVE_HEIGHT = DICES_WIDTH // 2.5

PERSONNAL_MOVE_Y_DELTA = [
    DICES_WIDTH * 1.20 - MOVE_HEIGHT * 1 / 3,
    DICES_WIDTH * 1.20 - MOVE_HEIGHT * 1 / 3,
    -DICES_WIDTH * 0.20 - MOVE_HEIGHT * 2 / 3,
    -DICES_WIDTH * 0.20 - MOVE_HEIGHT * 2 / 3,
]

SHARED_MOVE_X_DELTA = [
    -DICES_WIDTH * 0.25,
    DICES_WIDTH * 0.25,
    -DICES_WIDTH * 0.25,
    DICES_WIDTH * 0.25,
]

SHARED_MOVE_Y_DELTA = [
    -DICES_WIDTH * 0.75 - MOVE_HEIGHT * 2 / 3,
    -DICES_WIDTH * 0.75 - MOVE_HEIGHT * 2 / 3,
    DICES_WIDTH * 0.75 - MOVE_HEIGHT * 1 / 3,
    DICES_WIDTH * 0.75 - MOVE_HEIGHT * 1 / 3,
]

# Objectives

OBJECTIVE_RESOURCE_MARGIN = 5
OBJECTIVE_HEIGHT = 50
OBJECTIVES_COLUMN_WIDTH = 50

OBJECTIVE_X = {
    EASY_OBJECTIVE: (XMAX + XMIN) // 2 - OBJECTIVES_COLUMN_WIDTH * 2.5,
    MEDIUM_OBJECTIVE: PLAYERS_NAME_RECT_LEFTS[0]
    + PLAYERS_NAME_WIDTH // 2
    - OBJECTIVES_COLUMN_WIDTH * 2.5,
    HARD_OBJECTIVE: PLAYERS_NAME_RECT_LEFTS[1]
    + PLAYERS_NAME_WIDTH // 2
    - OBJECTIVES_COLUMN_WIDTH * 2.5,
}

OBJECTIVE_Y = {
    EASY_OBJECTIVE: PLAYERS_NAME_RECT_TOPS[0]
    + PLAYERS_DICES_Y_DELTA[0]
    + DICES_WIDTH // 4
    - 2 * OBJECTIVE_HEIGHT,
    MEDIUM_OBJECTIVE: (YMAX + YMIN) // 2 - 2 * OBJECTIVE_HEIGHT,
    HARD_OBJECTIVE: (YMAX + YMIN) // 2 - 2 * OBJECTIVE_HEIGHT,
}


# Claim box

CLAIM_BOX_WIDTH = PLAYERS_NAME_HEIGHT
CLAIM_BOX_HEIGHT = PLAYERS_NAME_HEIGHT
CLAIM_MARGIN = PLAYERS_NAME_MARGIN
CLAIM_BOX_X = [
    PLAYERS_NAME_RECT_LEFTS[0] - PLAYERS_NAME_MARGIN - CLAIM_BOX_WIDTH,
    PLAYERS_NAME_RECT_LEFTS[1] + PLAYERS_NAME_MARGIN + PLAYERS_NAME_WIDTH,
    PLAYERS_NAME_RECT_LEFTS[2] - PLAYERS_NAME_MARGIN - CLAIM_BOX_WIDTH,
    PLAYERS_NAME_RECT_LEFTS[3] + PLAYERS_NAME_MARGIN + PLAYERS_NAME_WIDTH,
]
CLAIM_BOX_Y = [
    PLAYERS_NAME_RECT_TOPS[0],
    PLAYERS_NAME_RECT_TOPS[1],
    PLAYERS_NAME_RECT_TOPS[2],
    PLAYERS_NAME_RECT_TOPS[3],
]
CLAIM_TEXT_Y = [
    CLAIM_BOX_Y[0] + CLAIM_BOX_HEIGHT + CLAIM_MARGIN,
    CLAIM_BOX_Y[1] + CLAIM_BOX_HEIGHT + CLAIM_MARGIN,
    CLAIM_BOX_Y[2] - CLAIM_MARGIN,
    CLAIM_BOX_Y[3] - CLAIM_MARGIN,
]

# Timings
DICE_VALUE_SAVE_TIME = 0.5
DICE_VALUE_UPDATE_TIME = 0.8

MOVE_VALUE_SAVE_TIME = 0.2
MOVE_VALUE_UPDATE_TIME = 0.5

OBJECTIVES_INFOS_SAVE_TIME = 0.2
OBJECTIVES_INFOS_UPDATE_TIME = 0.5

OBJECTIVES_SUBRECTS_SAVE_TIME = 0.5
OBJECTIVES_SUBRECTS_UPDATE_TIME = 0.8

OBJECTIVES_CLAIM_SAVE_TIME = 0.5
OBJECTIVES_CLAIM_UPDATE_TIME = 0.8

SCORES_SAVE_TIME = 0.8
SCORES_UPDATE_TIME = 0.9


class GuiManager:
    _inst = None

    @staticmethod
    def get_gui_manager():
        return GuiManager._inst

    def __init__(self, referee):
        self._referee = referee
        GuiManager._inst = self

        self._players_colors = dict()
        self._players_scores_texts = dict()

        self._dices_points = []
        self._personnal_dices_points = defaultdict(list)
        self._players_personnal_moves = defaultdict(list)
        self._players_shared_moves = defaultdict(list)
        self._objectives_infos = defaultdict(list)
        self._objectives_subrects = defaultdict(list)
        self._claimed_objective_id_texts = dict()

    def clear(self):
        self._players_colors.clear()
        self._players_scores_texts.clear()
        del self._dices_points[:]
        self._personnal_dices_points.clear()
        self._players_personnal_moves.clear()
        self._players_shared_moves.clear()
        self._objectives_infos.clear()
        self._objectives_subrects.clear()
        self._claimed_objective_id_texts.clear()

    def build_graphics(self):
        self._build_shared_dices()
        self._build_shared_dices_moves()
        self._build_personnal_dices()
        self._build_personnal_dices_moves()
        self._build_players_names()
        self._build_scores()
        self._build_objectives()
        self._build_claim_boxes()

    def _stardust_group(self, x, y):
        g = Group("stardust-group")
        for dpx, dpy in STARDUST_COORDS_DELTA:
            g.add_child(
                Oval(
                    "stardust_point",
                    x + dpx,
                    y + dpy,
                    STARDUST_POINT_RADIUS,
                    STARDUST_POINT_RADIUS,
                )
            )
            g.fill_color = DICE_POINT_FILL_COLOR
        return g

    def _helium_3_group(self, x, y):
        g = Group("helium-3-group")

        for angle, name, color in [
            (0, "proton", HELIUM3_PROTON_COLOR),
            (2 * math.pi / 3, "proton", HELIUM3_PROTON_COLOR),
            (2 * math.pi / 3 * 2, "neutron", HELIUM3_NEUTRON_COLOR),
        ]:
            o = Oval(
                name,
                x
                + (HELIUM3_PARTICULE_RADIUS + HELIUM3_PARTICULE_MARGIN)
                * math.cos(angle),
                y
                + (HELIUM3_PARTICULE_RADIUS + HELIUM3_PARTICULE_RADIUS)
                * math.sin(angle),
                HELIUM3_PARTICULE_RADIUS,
                HELIUM3_PARTICULE_RADIUS,
            )
            o.fill_color = color
            g.add_child(o)

        return g

    def _antimatter_group(self, x, y):
        g = Group("antimatter-group")
        g.add_children(
            [
                Oval(
                    "antimatter_positive_circle",
                    x - ANTIMATTER_PARTICULE_RADIUS - ANTIMATTER_PARTICULE_MARGIN,
                    y,
                    ANTIMATTER_PARTICULE_RADIUS,
                    ANTIMATTER_PARTICULE_RADIUS,
                ),
                Oval(
                    "antimatter_negative_circle",
                    x + ANTIMATTER_PARTICULE_RADIUS + ANTIMATTER_PARTICULE_MARGIN,
                    y,
                    ANTIMATTER_PARTICULE_RADIUS,
                    ANTIMATTER_PARTICULE_RADIUS,
                ),
                Line(
                    "antimatter_positive_symbol_line",
                    x - 2 * ANTIMATTER_PARTICULE_RADIUS,
                    y,
                    x - 2 * ANTIMATTER_PARTICULE_MARGIN,
                    y,
                ),
                Line(
                    "antimatter_positive_symbol_line",
                    x - ANTIMATTER_PARTICULE_RADIUS - ANTIMATTER_PARTICULE_MARGIN,
                    y - ANTIMATTER_PARTICULE_RADIUS + ANTIMATTER_PARTICULE_MARGIN,
                    x - ANTIMATTER_PARTICULE_RADIUS - ANTIMATTER_PARTICULE_MARGIN,
                    y + ANTIMATTER_PARTICULE_RADIUS - ANTIMATTER_PARTICULE_MARGIN,
                ),
                Line(
                    "antimatter_negative_symbol_line",
                    x + 2 * ANTIMATTER_PARTICULE_RADIUS,
                    y,
                    x + 2 * ANTIMATTER_PARTICULE_MARGIN,
                    y,
                ),
                RegulareStar(
                    "antimatter_star",
                    x,
                    y,
                    ANTIMATTER_STAR_RADIUS * 2 // 3,
                    ANTIMATTER_STAR_RADIUS,
                    10,
                ),
            ]
        )
        return g

    def _darkmatter_group(self, x, y):
        g = Group("darkmatter-group")

        g.add_child(
            Oval("dark-matter-circle", x, y, DARKMATTER_RADIUS, DARKMATTER_RADIUS)
        )
        g.fill_color = DARKMATTER_COLOR
        return g

    def _build_dices_points(self, dice_x, dice_y, player=None):
        dice_center_x = dice_x + DICES_WIDTH // 2
        dice_center_y = dice_y + DICES_WIDTH // 2

        dice_points = [
            self._stardust_group(dice_center_x, dice_center_y),
            self._helium_3_group(dice_center_x, dice_center_y),
            self._antimatter_group(dice_center_x, dice_center_y),
            self._darkmatter_group(dice_center_x, dice_center_y),
        ]

        if player is None:
            self._dices_points.append(dice_points)
        else:
            self._personnal_dices_points[player].append(dice_points)
        for dice_points_x in dice_points:
            dice_points_x.opacity = 0
            dice_points_x.save_state(1)

        self._referee.add_graphics(dice_points)

    def _build_shared_dices(self):
        for i in range(NB_SHARED_DICES):
            dice_x = XMIN_DICES + i * (DICES_MARGIN + DICES_WIDTH)
            dice_y = Y_DICES - DICES_WIDTH // 2
            rect = Rectangle(
                "dice-rectangle",
                dice_x,
                dice_y,
                DICES_WIDTH,
                DICES_WIDTH,
            )
            self._referee.add_graphic(rect)

            self._build_dices_points(dice_x, dice_y)

            first_face = SHARED_DICES_FACES[i][0]
            dp = self._dices_points[i][first_face - 1]
            dp.opacity = 1
            dp.save_state(1)

    def _build_shared_dices_moves(self):
        for i in range(NB_SHARED_DICES):
            dice_x = XMIN_DICES + i * (DICES_MARGIN + DICES_WIDTH) + DICES_WIDTH // 2
            dice_y = Y_DICES
            for j, player in enumerate(self._referee.players):
                move_x = dice_x + SHARED_MOVE_X_DELTA[j]
                move_y = dice_y + SHARED_MOVE_Y_DELTA[j]

                reg = RegularPolygon(
                    "shared_move",
                    0,
                    0,
                    MOVE_HEIGHT // 2,
                    3,
                )
                reg.translate_x = move_x
                reg.translate_y = move_y + MOVE_HEIGHT // 2
                reg.fill_color = PLAYERS_COLORS[j]
                reg.scale_y = MOVE_SCALE
                reg.rotate_z = 90
                reg.opacity = 0
                self._referee.add_graphic(reg)
                self._players_shared_moves[player].append(reg)

    def _build_players_names(self):
        for i, player in enumerate(self._referee.players):
            group = Group("player-name-group")

            x = PLAYERS_NAME_RECT_LEFTS[i]
            y = PLAYERS_NAME_RECT_TOPS[i]

            rect = Rectangle(
                "player-name-rectangle", x, y, PLAYERS_NAME_WIDTH, PLAYERS_NAME_HEIGHT
            )
            rect.stroke_width = PLAYERS_NAME_RECT_STROKE_WIDTH
            rect.rx = PLAYERS_NAME_RECT_RADIUS
            rect.ry = PLAYERS_NAME_RECT_RADIUS
            rect.stroke_color = PLAYERS_COLORS[i]
            rect.fill_color = PLAYERS_COLORS[i]

            text = Text(
                "player-name-text",
                x + PLAYERS_NAME_PADDING,
                y + PLAYERS_NAME_HEIGHT / 2,
                text=player.name[:PLAYERS_NAME_MAX_CHAR],
                font_size=25,
                font_family="Arial",
            )
            text.set_horizontal_left_align()
            text.set_vertical_center_align()

            group.add_children([rect, text])
            self._referee.add_graphic(group)

    def _build_personnal_dices(self):
        for j, player in enumerate(self._referee.players):
            x = PLAYERS_NAME_RECT_LEFTS[j]
            y = PLAYERS_NAME_RECT_TOPS[j] + PLAYERS_DICES_Y_DELTA[j]

            for i in range(NB_PERSONAL_DICES):
                dice_x = x + i * (DICES_MARGIN + DICES_WIDTH)
                dice_y = y
                rect = Rectangle(
                    "dice-rectangle",
                    dice_x,
                    dice_y,
                    DICES_WIDTH,
                    DICES_WIDTH,
                )
                self._referee.add_graphic(rect)

                self._build_dices_points(dice_x, dice_y, player)

                first_face = PERSONAL_DICES_FACES[i][0]
                dp = self._personnal_dices_points[player][i][first_face - 1]
                dp.opacity = 1
                dp.save_state(1)

    def _build_personnal_dices_moves(self):
        for j, player in enumerate(self._referee.players):
            x = PLAYERS_NAME_RECT_LEFTS[j] + DICES_WIDTH // 2
            y = (
                PLAYERS_NAME_RECT_TOPS[j]
                + PLAYERS_DICES_Y_DELTA[j]
                + PERSONNAL_MOVE_Y_DELTA[j]
            )
            for i in range(NB_PERSONAL_DICES):
                move_x = x + i * (DICES_MARGIN + DICES_WIDTH)
                move_y = y

                reg = RegularPolygon(
                    "personnal_move",
                    0,
                    0,
                    MOVE_HEIGHT // 2,
                    3,
                )
                reg.translate_x = move_x
                reg.translate_y = move_y + MOVE_HEIGHT // 2
                reg.fill_color = PLAYERS_COLORS[j]
                reg.scale_y = MOVE_SCALE
                reg.rotate_z = 90
                reg.opacity = 0
                self._referee.add_graphic(reg)
                self._players_personnal_moves[player].append(reg)

    def _build_scores(self):
        for i, player in enumerate(self._referee.players):
            x = PLAYERS_NAME_RECT_LEFTS[i]
            y = PLAYERS_NAME_RECT_TOPS[i]
            t = Text(
                "player-score",
                x + PLAYERS_NAME_WIDTH - PLAYERS_NAME_PADDING,
                y + PLAYERS_NAME_HEIGHT / 2,
                text="0",
                font_size=25,
                font_family="Arial",
            )

            t.set_horizontal_right_align()
            t.set_vertical_center_align()

            self._referee.add_graphic(t)
            self._players_scores_texts[player] = t

    def _build_objectives(self):
        for category in OBJECTIVES_CATEGORIES:
            x = OBJECTIVE_X[category]
            y = OBJECTIVE_Y[category]

            rect = Rectangle(
                "objective-title-rect",
                x,
                y,
                5 * OBJECTIVES_COLUMN_WIDTH,
                OBJECTIVE_HEIGHT,
                rx=5,
                ry=5,
            )
            tid = Text(
                "objective-title-id",
                x + OBJECTIVES_COLUMN_WIDTH // 2,
                y + OBJECTIVE_HEIGHT // 2,
                text="Id",
                font_size=25,
                font_family="Arial",
            )
            self._referee.add_graphics([rect, tid])
            for i, gf in enumerate(
                [
                    self._stardust_group,
                    self._helium_3_group,
                    self._antimatter_group,
                    self._darkmatter_group,
                ]
            ):
                g = gf(0, 0)
                g.translate_x = x + OBJECTIVES_COLUMN_WIDTH * (i + 1.5)
                g.translate_y = y + OBJECTIVE_HEIGHT // 2
                g.scale_x = 0.8
                g.scale_y = 0.8
                self._referee.add_graphic(g)

            for i in range(NB_OBJECTIVES_PER_CATEGORY):
                rect = Rectangle(
                    "objective-rect",
                    x,
                    y + (i + 1) * OBJECTIVE_HEIGHT,
                    5 * OBJECTIVES_COLUMN_WIDTH,
                    OBJECTIVE_HEIGHT,
                    rx=5,
                    ry=5,
                )
                self._referee.add_graphic(rect)
                infos = []
                self._objectives_infos[category].append(infos)
                for j in range(5):
                    t = Text(
                        "objective-info",
                        x + (j + 0.5) * OBJECTIVES_COLUMN_WIDTH,
                        y + (i + 1.5) * OBJECTIVE_HEIGHT,
                        text="",
                        font_size=25,
                        font_family="Arial",
                    )
                    infos.append(t)
                    self._referee.add_graphic(t)

                subrects = []  # Small Rectangles indicating if a resource of the i-th objective belong to a player
                self._objectives_subrects[category].append(subrects)
                for r in range(len(RESOURCES)):  # For each resource
                    subrects_of_ressources = dict()  # Small rectangles restricted to hte r-th resource of the ith objective
                    subrects.append(subrects_of_ressources)
                    nbplayers = len(self._referee.players)
                    width = (
                        OBJECTIVES_COLUMN_WIDTH - OBJECTIVE_RESOURCE_MARGIN
                    ) / nbplayers
                    for j, player in enumerate(self._referee.players):
                        ressource_rect = Rectangle(
                            "ressource-rect",
                            -width // 2,
                            -OBJECTIVE_HEIGHT,
                            width,
                            OBJECTIVE_HEIGHT,
                        )
                        ressource_rect.translate_x = (
                            width // 2
                            + x
                            + (1 + r) * OBJECTIVES_COLUMN_WIDTH
                            + OBJECTIVE_RESOURCE_MARGIN // 2
                            + j * width
                        )
                        ressource_rect.translate_y = y + (i + 2) * OBJECTIVE_HEIGHT
                        ressource_rect.fill_color = PLAYERS_COLORS[j]
                        ressource_rect.stroke_width = 0
                        ressource_rect.scale_y = 0
                        ressource_rect.opacity = 0.5
                        self._referee.add_graphic(ressource_rect)
                        subrects_of_ressources[player] = ressource_rect

    def _build_claim_boxes(self):
        for j, player in enumerate(self._referee.players):
            x = CLAIM_BOX_X[j]
            y = CLAIM_BOX_Y[j]
            rect = Rectangle("claim-box-rect", x, y, CLAIM_BOX_WIDTH, CLAIM_BOX_HEIGHT)
            text = Text(
                "claim-box-text",
                x + CLAIM_BOX_WIDTH // 2,
                CLAIM_TEXT_Y[j],
                text="Claim",
                font_size=20,
                font_family="Arial",
            )
            if j < 2:
                text.set_vertical_top_align()
            else:
                text.set_vertical_bottom_align()

            claimed_objective_id = Text(
                "claimed-objective-id-text",
                x + CLAIM_BOX_WIDTH // 2,
                y + CLAIM_BOX_HEIGHT // 2,
                text="",
                font_size=25,
                font_family="Arial",
            )

            self._referee.add_graphics([rect, text, claimed_objective_id])
            self._claimed_objective_id_texts[player] = claimed_objective_id

    def update_shared_dice(self, turn, dice_index, value):
        for v in range(DICE_MIN_VALUE, DICE_MAX_VALUE + 1):
            dp = self._dices_points[dice_index - 1][v - 1]
            dp.save_state(turn + DICE_VALUE_SAVE_TIME)
            dp.opacity = 1 if v == value else 0
            dp.save_state(turn + DICE_VALUE_UPDATE_TIME)

    def update_move_shared_dice(self, turn, player, dice_index, value):
        angle = 90 - value * 90
        reg = self._players_shared_moves[player][dice_index - 1]
        reg.save_state(turn + MOVE_VALUE_SAVE_TIME)
        reg.rotate_z = angle
        reg.opacity = 0 if value == 0 else 1
        reg.translate_y += 3 * value
        reg.save_state(turn + MOVE_VALUE_UPDATE_TIME)
        reg.translate_y -= 3 * value

    def update_personnal_dice(self, turn, player, dice_index, value):
        for v in range(DICE_MIN_VALUE, DICE_MAX_VALUE + 1):
            dp = self._personnal_dices_points[player][dice_index - NB_SHARED_DICES - 1][
                v - 1
            ]
            dp.save_state(turn + DICE_VALUE_SAVE_TIME)
            dp.opacity = 1 if v == value else 0
            dp.save_state(turn + DICE_VALUE_UPDATE_TIME)

    def update_move_personnal_dice(self, turn, player, dice_index, value):
        angle = 90 - value * 90
        reg = self._players_personnal_moves[player][dice_index - NB_SHARED_DICES - 1]
        reg.save_state(turn + MOVE_VALUE_SAVE_TIME)
        reg.rotate_z = angle
        reg.opacity = 0 if value == 0 else 1
        reg.translate_y += 3 * value
        reg.save_state(turn + MOVE_VALUE_UPDATE_TIME)
        reg.translate_y -= 3 * value

    def update_objective(self, turn, objective_index, objective):
        category = objective.category
        objective_index = objective_index % 3
        for r in range(len(RESOURCES)):
            for player in self._referee.players:
                rect = self._objectives_subrects[category][objective_index][r][player]
                rect.save_state(turn + OBJECTIVES_CLAIM_SAVE_TIME)
                rect.opacity = 0.5
                rect.save_state(turn + OBJECTIVES_CLAIM_SAVE_TIME)

        infos = self._objectives_infos[category][objective_index]
        for info, objective_info in zip(
            infos,
            [objective.id] + [objective.resources_conditions[r] for r in RESOURCES],
        ):
            info.save_state(turn + OBJECTIVES_INFOS_SAVE_TIME)
            info.text = str(objective_info)
            info.opacity = 1
            info.save_state(turn + OBJECTIVES_INFOS_UPDATE_TIME)

        for player in self._referee.players:
            claimed_objective_id = self._claimed_objective_id_texts[player]
            claimed_objective_id.save_state(turn + OBJECTIVES_INFOS_SAVE_TIME)
            claimed_objective_id.text = ""
            claimed_objective_id.save_state(turn + OBJECTIVES_INFOS_UPDATE_TIME)

    def update_objective_condition_satisfaction(
        self, turn, objective_index, objective, resource_index, player, percentage
    ):
        category = objective.category
        objective_index = objective_index % 3
        rect = self._objectives_subrects[category][objective_index][resource_index][
            player
        ]
        rect.save_state(turn + OBJECTIVES_SUBRECTS_SAVE_TIME)
        rect.scale_y = percentage
        rect.save_state(turn + OBJECTIVES_SUBRECTS_UPDATE_TIME)

    def update_claim_objective(self, turn, objective_index, objective, players):
        category = objective.category
        objective_index = objective_index % 3
        for r in range(len(RESOURCES)):
            for player in self._referee.players:
                rect = self._objectives_subrects[category][objective_index][r][player]
                rect.save_state(turn + OBJECTIVES_CLAIM_SAVE_TIME)
                rect.opacity = 0.33
                rect.save_state(turn + OBJECTIVES_CLAIM_SAVE_TIME)
        for info in self._objectives_infos[category][objective_index]:
            info.save_state(turn + OBJECTIVES_CLAIM_SAVE_TIME)
            info.opacity = 0.33
            info.save_state(turn + OBJECTIVES_CLAIM_SAVE_TIME)
        for player in players:
            claimed_objective_id = self._claimed_objective_id_texts[player]
            claimed_objective_id.save_state(turn + OBJECTIVES_CLAIM_SAVE_TIME)
            claimed_objective_id.text = str(objective.id)
            claimed_objective_id.save_state(turn + OBJECTIVES_CLAIM_UPDATE_TIME)

    def edit_score(self, turn, player, score):
        t = self._players_scores_texts[player]
        t.save_state(turn + SCORES_SAVE_TIME)
        t.text = str(score)
        t.save_state(turn + SCORES_UPDATE_TIME)
