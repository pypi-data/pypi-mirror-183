from api_utils import Routs, Keys, base_model, FilterData, utils
from api_utils.query import Players
from fastapi import APIRouter
import ast


class PlayersModel(base_model.BaseModel):
    """
    Initiate entities model
    """
    pass


router_players = APIRouter(
    prefix=f"/{Routs.PLAYERS}",
    tags=[Routs.PLAYERS]
)


@router_players.get(path="/overview/{player_id}", summary="Returns player overview")
async def overview(player_id: int):
    """
    Returns player overview by unique player_id
    """
    data = PlayersModel.Meta.database.get_data(query=Players.overview_base(player_id=player_id),
                                               return_data_frame=True)
    response_data = {}
    if len(data) == 1:
        response_data.setdefault(Keys.OVERVIEW, ast.literal_eval(data.overview.values[0]))
        response_data.setdefault(Keys.ACHIEVEMENTS, ast.literal_eval(data.achievements.values[0]))
        response_data.setdefault(Keys.TM_HISTORY, ast.literal_eval(data.transfer_history.values[0]))
        response_data.setdefault(Keys.TM_INJURY, ast.literal_eval(data.injury_history.values[0].replace('nan', 'None')))
        response_data.setdefault(Keys.ATTRIBUTES, ast.literal_eval(data.player_attributes.values[0]))
        mv_data = utils.get_mv_data(data=data)
        return {Keys.DATA_TYPE: Keys.OVERVIEW,
                Keys.BASE_DATA: [response_data],
                Keys.AGE: mv_data.get(Keys.AGE),
                Keys.NATION: mv_data.get(Keys.NATION),
                Keys.MARKET_VALUE: mv_data.get(Keys.MARKET_VALUE),
                Keys.CONTRACT_EXPIRES: mv_data.get(Keys.CONTRACT_EXPIRES),
                Keys.TEAM_ID: int(data.team_id.values[0]),
                Keys.NAME: data.player_name.values[0],
                Keys.POSITION: utils.get_position(PlayersModel.Meta.database,
                                                  Players.position(player_id=player_id)),
                Keys.STATUS_CODE: 200}
    else:
        return {Keys.ERROR: Keys.NOT_FOUND_DATA}


@router_players.post(path="/stats/{player_id}/{id_type}", summary="Returns player stats")
async def stats(player_id: int, id_type: int, required_stats: list = FilterData.DEFAULT_STATS):
    """
    Returns player stays by unique player_id
    """
    if id_type != 1:
        player_id = \
            PlayersModel.Meta.database.get_data(query=Players.get_players_by_ids(players=player_id, one_object=True),
                                                return_data_frame=True).id.values[0]
    return {Keys.DATA_TYPE: Keys.STATS,
            Keys.DATA:
                PlayersModel.Meta.database.get_data(query=Players.stats(player_id=player_id,
                                                                        required_stats=required_stats))[0],
            Keys.COUNT_OF_GAMES:
                PlayersModel.Meta.database.get_data(query=Players.count_of_games(player_id=player_id))[0],
            Keys.STATUS_CODE: 200}


@router_players.get(path="/filter/{data_type}/{object_id}", summary="Returns all players by team or country id")
async def get_players_by_id(object_id: int, data_type: int = 1):
    """
        data_type:
        - current player team id: 1
        - country id: 2

        object_id:
        - the main id, need to be unique.
    """
    return {Keys.DATA_TYPE: Keys.PLAYERS,
            Keys.DATA:
                PlayersModel.Meta.database.get_data(
                    query=Players.players_filter(object_id=object_id, data_type=data_type))[0],
            Keys.STATUS_CODE: 200}


@router_players.get(path="/search/{content}", summary="Returns all players that contain the required content")
async def search(content: str):
    """
        content:
        - need to be string
    """
    return {Keys.DATA_TYPE: Keys.PLAYERS,
            Keys.DATA:
                PlayersModel.Meta.database.get_data(query=Players.search(content=content))[0],
            Keys.STATUS_CODE: 200}


@router_players.get(path="/search_players/{position}", summary="Returns players by specific filter")
async def search_players(position: str, countries: str = None, age_min: int = 18, age_max: int = 35, mv_min: int = 0,
                         mv_max: int = 5000000, place_of_birth: str = None, contract_expires_year: str = None,
                         data_limit: int = 1000):
    data = PlayersModel.Meta.database.get_data(
        query=Players.search_players(position=position, age_min=age_min, age_max=age_max,
                                     mv_min=mv_min, mv_max=mv_max, countries_filter=countries,
                                     place_of_birth=place_of_birth, contract_expires_year=contract_expires_year,
                                     data_limit=data_limit))
    return {Keys.DATA_TYPE: Keys.PLAYERS, Keys.DATA: data[0], Keys.COLUMNS: data[1], Keys.STATUS_CODE: 200}


@router_players.get(path="/filter/{data_type}/{object_id}/{key}",
                    summary="Returns all players by data type and key argument")
async def get_players_by_argument_type(object_id: int, key: str, data_type: int = 1):
    """
        data_type options:
        - current player team id: 1
        - country id: 2
        - position and team id: 3
        - position and country id: 4
        - age, country id and position: 5
        - mv, country id and position: 6
        - mv and position - 7
        object_id:
        - the main id, need to be unique.
    """
    keys = key.split(', ')
    return {Keys.DATA_TYPE: Keys.PLAYERS,
            Keys.DATA:
                PlayersModel.Meta.database.get_data(
                    query=Players.players_filter(object_id=object_id, data_type=data_type, argument=keys))[0],
            Keys.STATUS_CODE: 200}


@router_players.get(path="/similar/{object_id}",
                    summary="Returns all players similar players for object id")
async def get_similar_players(object_id: int):
    """
        object_id:
        - the main id, need to be unique.
    """
    similar_players = None
    player_info = PlayersModel.Meta.database.get_data(
        query=Players.player_basic_info(object_id=object_id))[0]
    if player_info:
        similar_players = PlayersModel.Meta.database.get_data(
            query=Players.rank_similar_players(object_id=object_id, position=player_info[0][2],
                                               player_rank=player_info[0][7]))
    return {Keys.DATA_TYPE: Keys.PLAYERS,
            Keys.DATA: [] if not similar_players else list(similar_players[0]),
            Keys.INFO: [] if not player_info else list(player_info[0]),
            Keys.COLUMNS: [] if not similar_players else list(similar_players[1]),
            Keys.STATUS_CODE: 200}
