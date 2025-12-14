from collections import defaultdict
import random

from src.referee.referee import Referee, Player

# Constants

# Referee constants
NB_SHARED_DICES = 4
NB_PERSONAL_DICES = 4
DICE_MIN_VALUE = 1
DICE_MAX_VALUE = 4
NB_ACTIONS = 6
NB_TURNS = 3
NB_OBJECTIVES_PER_CATEGORY = 3

# Messages
LAST_ROLL_MSG = "Last roll reached"
MOVEMENT_COMMAND_ERROR = "The command must be MOVE M where M is -1, 0 or 1."
OBJECTIVE_COMMAND_ERROR = "The command must be PASS or CLAIM OID where OID is one of the objectives ids of the current turn."
ONLY_ONE_SHARED_MOVEMENT_ERROR = (
    "There can be only one movement among the shared dices."
)
NON_EXISTING_OBJECTIVE_ERROR = "Objective id is not an objective of the current turn."
CLAIMED_OBJECTIVE_ERROR = (
    "The claimed objective was already claimed during a previous turn."
)
NON_SATISFIED_OBJECTIVE_ERROR = (
    "You do not satisfy the constraint of the claimed objective."
)
ONE_PLAYER_LEFT = "Last player in game. You won. "
GAME_OVER_MSG = "Game is over."

# Drawing constants
XMIN = 0
XMAX = 1000
YMIN = 0
YMAX = 600


# Resources

STAR_DUST = 1
HELIUM_3 = 2
ANTIMATTER = 3
DARK_MATTER = 4
RESOURCES = [STAR_DUST, HELIUM_3, ANTIMATTER, DARK_MATTER]

# DICES FACES

D1_FACES = (STAR_DUST, ANTIMATTER, DARK_MATTER, ANTIMATTER)
D2_FACES = (STAR_DUST, HELIUM_3, DARK_MATTER, HELIUM_3)
D3_FACES = (STAR_DUST, HELIUM_3, DARK_MATTER, ANTIMATTER)
D4_FACES = (HELIUM_3, DARK_MATTER, ANTIMATTER, DARK_MATTER)
D5_FACES = (STAR_DUST, STAR_DUST, HELIUM_3, HELIUM_3, STAR_DUST)
D6_FACES = (STAR_DUST, HELIUM_3, HELIUM_3, ANTIMATTER, HELIUM_3, HELIUM_3)
D7_FACES = (STAR_DUST, HELIUM_3, ANTIMATTER, ANTIMATTER, HELIUM_3)
D8_FACES = (STAR_DUST, ANTIMATTER, HELIUM_3, DARK_MATTER, ANTIMATTER, HELIUM_3)

SHARED_DICES_FACES = [D1_FACES, D2_FACES, D3_FACES, D4_FACES]
PERSONAL_DICES_FACES = [D5_FACES, D6_FACES, D7_FACES, D8_FACES]

# Objectives constants

EASY_OBJECTIVE = 0
MEDIUM_OBJECTIVE = 1
HARD_OBJECTIVE = 2

OBJECTIVES_CATEGORIES = [EASY_OBJECTIVE, MEDIUM_OBJECTIVE, HARD_OBJECTIVE]

POINTS_PER_OBJETIVE_CATEGORY = {
    EASY_OBJECTIVE: 100,
    MEDIUM_OBJECTIVE: 150,
    HARD_OBJECTIVE: 200,
}

OBJECTIVES = {
    EASY_OBJECTIVE: [
        [1, {STAR_DUST: 2, HELIUM_3: 1, ANTIMATTER: 1, DARK_MATTER: 1}],
        [2, {STAR_DUST: 1, HELIUM_3: 2, ANTIMATTER: 1, DARK_MATTER: 1}],
        [3, {STAR_DUST: 1, HELIUM_3: 1, ANTIMATTER: 2, DARK_MATTER: 1}],
        [4, {STAR_DUST: 1, HELIUM_3: 1, ANTIMATTER: 1, DARK_MATTER: 2}],
        [5, {STAR_DUST: 2, HELIUM_3: 0, ANTIMATTER: 2, DARK_MATTER: 1}],
        [6, {STAR_DUST: 2, HELIUM_3: 2, ANTIMATTER: 0, DARK_MATTER: 1}],
        [7, {STAR_DUST: 0, HELIUM_3: 2, ANTIMATTER: 2, DARK_MATTER: 1}],
        [8, {STAR_DUST: 1, HELIUM_3: 2, ANTIMATTER: 2, DARK_MATTER: 0}],
        [9, {STAR_DUST: 0, HELIUM_3: 4, ANTIMATTER: 0, DARK_MATTER: 0}],
        [10, {STAR_DUST: 0, HELIUM_3: 0, ANTIMATTER: 4, DARK_MATTER: 0}],
    ],
    MEDIUM_OBJECTIVE: [
        [11, {STAR_DUST: 2, HELIUM_3: 2, ANTIMATTER: 1, DARK_MATTER: 1}],
        [12, {STAR_DUST: 2, HELIUM_3: 1, ANTIMATTER: 2, DARK_MATTER: 1}],
        [13, {STAR_DUST: 1, HELIUM_3: 2, ANTIMATTER: 2, DARK_MATTER: 1}],
        [14, {STAR_DUST: 1, HELIUM_3: 5, ANTIMATTER: 0, DARK_MATTER: 0}],
        [15, {STAR_DUST: 1, HELIUM_3: 3, ANTIMATTER: 2, DARK_MATTER: 0}],
        [16, {STAR_DUST: 1, HELIUM_3: 4, ANTIMATTER: 1, DARK_MATTER: 0}],
        [17, {STAR_DUST: 6, HELIUM_3: 0, ANTIMATTER: 0, DARK_MATTER: 0}],
        [18, {STAR_DUST: 0, HELIUM_3: 0, ANTIMATTER: 0, DARK_MATTER: 3}],
        [19, {STAR_DUST: 0, HELIUM_3: 0, ANTIMATTER: 3, DARK_MATTER: 2}],
        [20, {STAR_DUST: 0, HELIUM_3: 3, ANTIMATTER: 0, DARK_MATTER: 2}],
    ],
    HARD_OBJECTIVE: [
        [21, {STAR_DUST: 3, HELIUM_3: 1, ANTIMATTER: 3, DARK_MATTER: 0}],
        [22, {STAR_DUST: 3, HELIUM_3: 3, ANTIMATTER: 1, DARK_MATTER: 0}],
        [23, {STAR_DUST: 1, HELIUM_3: 3, ANTIMATTER: 3, DARK_MATTER: 0}],
        [24, {STAR_DUST: 3, HELIUM_3: 0, ANTIMATTER: 2, DARK_MATTER: 1}],
        [25, {STAR_DUST: 3, HELIUM_3: 2, ANTIMATTER: 0, DARK_MATTER: 1}],
        [26, {STAR_DUST: 1, HELIUM_3: 2, ANTIMATTER: 2, DARK_MATTER: 2}],
        [27, {STAR_DUST: 7, HELIUM_3: 0, ANTIMATTER: 0, DARK_MATTER: 0}],
        [28, {STAR_DUST: 0, HELIUM_3: 6, ANTIMATTER: 0, DARK_MATTER: 0}],
        [29, {STAR_DUST: 0, HELIUM_3: 0, ANTIMATTER: 6, DARK_MATTER: 0}],
        [30, {STAR_DUST: 0, HELIUM_3: 0, ANTIMATTER: 0, DARK_MATTER: 4}],
    ],
}

from src.game.roll_for_the_milkyway.guimanager import GuiManager


def build_objectives():
    objectives = dict()
    for category in OBJECTIVES_CATEGORIES:
        objectives_of_category = []
        objectives[category] = objectives_of_category
        for id, resources_conditions in OBJECTIVES[category]:
            objectives_of_category.append(Objective(id, resources_conditions, category))
    return objectives


class Dice:
    """
    Class for a dice. A dice contains 4, 5 or 6 ordered faces. A face display a resource. From a dice set at a given face, a player can choose to show the next or previous face.
    """

    def __init__(self, index, *faces):
        self._index = index
        self._faces = faces
        self._current_face_index = 0

    @property
    def index(self):
        """The index property."""
        return self._index

    @property
    def current_face(self):
        """The current_face property."""
        return self._faces[self._current_face_index]

    def __add__(self, value):
        self._current_face_index = (self._current_face_index + value) % len(self._faces)
        return self


class Objective:
    """
    Objective of the game, can be claimed by players when the condition is satisfied
    """

    def __init__(self, id, resources_conditions, category):
        self.id = id
        self.claimed = False
        self.claimed_by = []
        self.resources_conditions = resources_conditions
        self.category = category

    def resources_conditions_delta(self, dices):
        values = defaultdict(int)
        for dice in dices:
            values[dice.current_face] += 1
        return {
            resource: values[resource] - nb
            for resource, nb in self.resources_conditions.items()
        }

    def is_satified_by(self, dices):
        return all(x >= 0 for x in self.resources_conditions_delta(dices).values())


class RollForTheMilkywayReferee(Referee):
    """
    The game consists in a dice roll optimization game.
    2, 3 or 4 players.

    The players have each 4 dices and share 4 dices during 3 turns. A turn consists in six actions, each action consists in two phases. During the first phase, each player may change each of his dices faces by selecting the next or previous face. He can then do the same with one of the shared dices. The face of each dice at the beginning of the turn is the first face. The second phase consists in claiming an achieved objective , each objective rewards the claiming player with some points. Each objective consists in having a tuple of given faces among the personal and shared dices (for instance, there must be, amond those 8 dices, 6 STAR_DUST faces).

    During the movement phase, the player must send 8 times the following command:
    - MOVE M where M is -1 0 or 1 in order to change the current face of the dice respectively to the previous, same or next face. The i-th command changes the face of the i-th dice. The four first dices are the sharded dices.

    During the objective phase, the player must send either the command PASS or CLAIM OID where OID is the id of an achieved objective. Note that only one objective can be claimed at a time and it is not possible to claim an already claimed objective.

    A player looses
    - if she does not send the command in time,
    - if she does send an incorrect command,
    - if she choose to change the face of more than one shared dice
    - if she claims a not achieved objective or an objective that does not exists.
    The score of the player is then -1.

    A player win if she does not lose before the end of the game or if all the other players lose the game. The score of the player is the number of earned points by the achieved objectives.

    """

    def __init__(self):
        super().__init__()

        # List of all objetives
        self.all_objectives = []

        # DIct associating objective_ids to objectives for every objective of current turn
        self.objectives = dict()

        # Dictionnary, List of dices associated with each player or shared
        self.dices = dict()

        # Score of each player
        self.scores = dict()

        # Current turn in the game (distinct from the turns of the referee)
        self.current_roll_turn = 0

        # Current actions in current turn
        self.current_action = 0

        # Last movement of each player:
        self.last_movements = dict()

        # Last claimed objective of eac player
        self.last_claimed_objective = dict()

        # True if the next phase is a moving phase
        self.moving = False

        # Build instance to manage the shapes of the game
        GuiManager(self)

    @staticmethod
    def get_author():
        return "Dimitri Watel"

    @staticmethod
    def get_description():
        return "A game where dices are rolled and objectives are achieved."

    @staticmethod
    def get_date():
        return "9 Janvier 2026"

    @staticmethod
    def allowed_number_of_players():
        return [2, 3, 4]

    def _init(self):
        gm = GuiManager.get_gui_manager()
        gm.clear()
        self.dices = {
            None: [Dice(i + 1, *faces) for i, faces in enumerate(SHARED_DICES_FACES)]
        }
        self.dices.update(
            {
                player: [
                    Dice(i + NB_SHARED_DICES + 1, *faces)
                    for i, faces in enumerate(PERSONAL_DICES_FACES)
                ]
                for player in self.players
            }
        )
        self.scores = {player: 0 for player in self.players}
        self.last_movements = {player: [] for player in self.players}
        self.last_claimed_objective = {player: None for player in self.players}

        self.current_roll_turn = 0
        self.current_action = 0

        self.all_objectives = build_objectives()
        for objectives_of_category in self.all_objectives.values():
            random.shuffle(objectives_of_category)
        self.objectives = dict()

        for i, player in enumerate(self.players):
            player.send_input_line_nl(input_msg=[len(self.players), i + 1])

        gm.build_graphics()

    def _end(self):
        """
        Nothing is done at the end of this referee
        :return:
        """
        pass

    def destroy(self, turn, player, message):
        if message.strip() != "":
            player.send_game_infos(message)
        player.loose()

    def end_all_players(self, msg):
        for player in self.players:
            if not player.is_playing:
                continue

            player.send_game_infos(msg)
            player.win(self.scores[player])

    def update_roll_turn(self, turn):
        if self.current_action == 0:
            # gm = GuiManager.get_gui_manager()
            # gm.remove_locks(turn)

            self.current_roll_turn += 1
            self.current_action += 1
            if not self.check_last_roll_turn():
                self.update_objectives(turn)
            self.moving = True
            return True
        return False

    def update_objectives(self, turn):
        self.objectives.clear()

        gm = GuiManager.get_gui_manager()
        # Reset
        for category in OBJECTIVES_CATEGORIES:
            objectives = []
            for j in range(NB_OBJECTIVES_PER_CATEGORY):
                objective = self.all_objectives[category].pop()
                self.objectives[objective.id] = objective
                objectives.append(objective)
            objectives.sort(key=lambda o: o.id)
            for j, objective in enumerate(objectives):
                gm.update_objective(turn, j, objective)

    def check_last_roll_turn(self):
        if self.current_roll_turn <= NB_TURNS:
            return False

        self.end_all_players(GAME_OVER_MSG)
        return True

    def read_player_movement_output(self, turn, player, player_output, dice):
        """
        Read the player output and move a dice accordingly.
        If the output is malformed, the player loose
        """
        gm = GuiManager.get_gui_manager()
        outputs = player_output.strip()

        outputs = outputs.split()
        if len(outputs) != 2:
            self.destroy(turn, player, MOVEMENT_COMMAND_ERROR)
            return None
        if outputs[0] != "MOVE":
            self.destroy(turn, player, MOVEMENT_COMMAND_ERROR)
            return None
        try:
            delta = int(outputs[1])
            if delta < -1 or delta > 1:
                self.destroy(turn, player, MOVEMENT_COMMAND_ERROR)
                return None
            dice += delta
            if dice.index <= NB_SHARED_DICES:
                gm.update_move_shared_dice(turn, player, dice.index, delta)
            else:
                gm.update_move_personnal_dice(turn, player, dice.index, delta)
            self.last_movements[player].append(delta)
            return delta != 0
        except ValueError:
            self.destroy(turn, player, MOVEMENT_COMMAND_ERROR)
            return None

    def read_player_objective_output(self, turn, player, player_output):
        """
        Read the player output and claim an objective accordingly.
        If the output is malformed, the player loose
        """
        # gm = GuiManager.get_gui_manager()
        outputs = player_output.strip()

        if outputs == "PASS":
            return

        outputs = outputs.split()
        if len(outputs) != 2:
            self.destroy(turn, player, OBJECTIVE_COMMAND_ERROR)
            return None
        if outputs[0] != "CLAIM":
            self.destroy(turn, player, OBJECTIVE_COMMAND_ERROR)
            return None
        try:
            objective_id = int(outputs[1])

            objective = self.objectives[objective_id]

            if objective.claimed:
                self.destroy(turn, player, CLAIMED_OBJECTIVE_ERROR)
                return None
            if not objective.is_satified_by(self.dices[None] + self.dices[player]):
                self.destroy(turn, player, NON_SATISFIED_OBJECTIVE_ERROR)
                return None
            objective.claimed_by.append(player)
            # gm.update_lock(turn, dice_index, player)
        except ValueError:
            self.destroy(turn, player, OBJECTIVE_COMMAND_ERROR)
            return None
        except KeyError:
            self.destroy(turn, player, NON_EXISTING_OBJECTIVE_ERROR)
            return None

    def send_begin_turn_input_to_players(self, turn):
        # Send, for each player, the number of the player, FALSE if the player has lost and TRUE otherwise, and
        # the score of the player
        # If a player has lost, send -1
        for player in self.players:
            Player.send_input_line_nl_to_all_players(
                players=self.players,
                input_msg=[player.id + 1, player.is_playing, self.scores[player]],
            )

        # Send objective of the turn to players
        objectives = sorted(
            [
                (objective_id, objective)
                for objective_id, objective in self.objectives.items()
            ]
        )
        for objective_id, objective in objectives:
            Player.send_input_line_nl_to_all_players(
                players=self.players,
                input_msg=[objective_id]
                + [objective.resources_conditions[resource] for resource in RESOURCES],
            )

    def send_movements_input_to_players(self, turn):
        for player in self.players:
            if player.is_playing:
                last_movements = self.last_movements[player]
            else:
                last_movements = [0] * (NB_PERSONAL_DICES + NB_SHARED_DICES)
            Player.send_input_line_nl_to_all_players(
                players=self.players,
                input_msg=[player.id + 1] + last_movements,
            )

    def send_claiming_input_to_players(self, turn):
        for player in self.players:
            if player.is_playing and self.last_claimed_objective[player] is not None:
                last_claimed_objective = self.last_claimed_objective[player].id
            else:
                last_claimed_objective = -1
            Player.send_input_line_nl_to_all_players(
                players=self.players,
                input_msg=[player.id + 1, last_claimed_objective],
            )

    def reinit_last_movements(self, turn):
        for player in self.players:
            del self.last_movements[player][:]

    def reinit_last_claimed_objective(self, turn):
        for player in self.players:
            self.last_claimed_objective[player] = None

    def end_of_current_roll_turn(self, turn):
        return self.current_action > NB_ACTIONS

    def check_claimed_objectives(self, turn):
        gm = GuiManager.get_gui_manager()

        for category in OBJECTIVES_CATEGORIES:
            objectives = [
                objective
                for objective in self.objectives.values()
                if objective.category == category
            ]
            objectives.sort(key=lambda o: o.id)

            for i, objective in enumerate(objectives):
                if objective.claimed:
                    continue
                for player in objective.claimed_by:
                    if not player.is_playing:
                        continue
                    objective.claimed = True
                    self.scores[player] += POINTS_PER_OBJETIVE_CATEGORY[
                        objective.category
                    ]
                    self.last_claimed_objective[player] = objective
                    gm.edit_score(turn, player, self.scores[player])
                if objective.claimed:
                    gm.update_claim_objective(turn, i, objective, objective.claimed_by)

    def read_movement_output_from_players(self, turn):
        """
        Read the movement outputs of all the players
        """
        for player in self.players:
            if not player.is_playing:
                continue

            moved_shared_dice = False

            for i, dice in enumerate(self.dices[None] + self.dices[player]):
                player_output = player.get_output_line()
                # If player returned no output
                if player_output is None:
                    break

                moved = self.read_player_movement_output(
                    turn, player, player_output, dice
                )
                if i < NB_SHARED_DICES and moved:
                    if moved_shared_dice:
                        self.destroy(turn, player, ONLY_ONE_SHARED_MOVEMENT_ERROR)
                    else:
                        moved_shared_dice = True

        gm = GuiManager.get_gui_manager()
        for i, dice in enumerate(self.dices[None]):
            gm.update_shared_dice(turn, dice.index, dice.current_face)
        for player in self.players:
            for i, dice in enumerate(self.dices[player]):
                gm.update_personnal_dice(turn, player, dice.index, dice.current_face)

        for category in OBJECTIVES_CATEGORIES:
            objectives = [
                objective
                for objective in self.objectives.values()
                if objective.category == category
            ]
            objectives.sort(key=lambda o: o.id)
            for i, objective in enumerate(objectives):
                for player in self.players:
                    fcd = objective.resources_conditions_delta(
                        self.dices[None] + self.dices[player]
                    )
                    for r, resource in enumerate(RESOURCES):
                        resource_condition = objective.resources_conditions[resource]
                        delta = fcd[resource]
                        if resource_condition == 0:
                            percentage = 0
                        elif delta >= 0:
                            percentage = 1
                        else:
                            percentage = (
                                resource_condition + delta
                            ) / resource_condition
                        gm.update_objective_condition_satisfaction(
                            turn, i, objective, r, player, percentage
                        )

    def read_objective_output_from_players(self, turn):
        """
        Read the claiming outputs of all the players
        """
        for player in self.players:
            if not player.is_playing:
                continue

            player_output = player.get_output_line()
            # If player returned no output
            if player_output is None:
                break

            self.read_player_objective_output(turn, player, player_output)

    def init_next_action(self, turn):
        self.current_action += 1
        if self.end_of_current_roll_turn(turn):
            self.current_action = 0
        self.moving = True

    def _game_turn(self, turn):
        # Check next roll
        # new_turn is true if a new turn has started. In that case, we end the
        # turn to pause the gui for one turn (so that the gui has time to update)
        # New objectives are given to the players
        # Also, check if this is the last turn, in which case all players stop.
        new_turn = self.update_roll_turn(turn)

        if new_turn:
            return

        # The following is done only at the beginning of the current_roll_turn, that is when current_roll is 1.
        if self.moving and self.current_action == 1:
            final_players = [player for player in self.players if player.is_playing]
            if len(final_players) == 1:
                final_players[0].send_game_infos(ONE_PLAYER_LEFT)
                final_players[0].win(self.scores[final_players[0]])
                return

            # Send first part of the input to the players
            self.send_begin_turn_input_to_players(turn)

        if self.moving:
            # Reinit the last movement of each player
            self.reinit_last_movements(turn)

            # Read the output of all the players, change dices faces accordingly
            self.read_movement_output_from_players(turn)

            # Send frozen dices to the players
            self.send_movements_input_to_players(turn)
            self.moving = False
            return

        if not self.moving:
            # The following is done only at the end of the turns
            # Increase the counter associated with the current roll
            # and reroll the dices
            self.reinit_last_claimed_objective(turn)

            self.read_objective_output_from_players(turn)

            self.check_claimed_objectives(turn)

            self.send_claiming_input_to_players(turn)

            self.init_next_action(turn)

    def _get_x_max(self):
        return XMAX

    def _get_y_max(self):
        return YMAX
