import logging
from typing import Dict, List

from fuel import fuel_sources, get_all_fuels
from interfaces import Fuel

logger = logging.getLogger(__name__)

fuels_cache: Dict[str, List[Fuel]] = {}


def get_fuels() -> Dict[str, List[Fuel]]:
    return fuels_cache


def cache_fuels():
    logger.info("Starting to cache fuels")
    try:
        fuels = get_all_fuels(fuel_sources())
        fuels_cache.clear()
        fuels_cache.update(fuels)
        logger.info(f"Successfully cached {len(fuels)} fuels")
    except Exception as e:
        logger.error(f"Error occurred while caching fuels: {str(e)}", exc_info=True)
