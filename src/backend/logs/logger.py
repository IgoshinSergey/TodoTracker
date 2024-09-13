from functools import wraps
import logging


logger = logging.getLogger()

formatter = logging.Formatter(
    fmt='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

file_handler = logging.FileHandler('logs/logs.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def log_decorator(level=logging.INFO):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            logger.log(level, f"Starting {func.__name__}")
            result = await func(*args, **kwargs)
            logger.log(level, f'Function: {func.__name__} returned: {result}')
            return result
        return wrapper
    return decorator
