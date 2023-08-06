# build-in imports
from dataclasses	import dataclass
from time			import sleep
from typing 		import Callable

# external imports
from loguru 	import logger
from requests 	import Response


@logger.catch()
def extra_exception_default(response: Response):
	return False


@dataclass
class AttemptRequests:
	success_codes	: int		= 200
	attempts		: int 		= 3
	waiting_time	: float		= 0.01
	extra_exception : Callable	= extra_exception_default

	def __call__(self, func, *args, **kwargs):
		@logger.catch()
		def inner(*args, attempt=1, **kwargs):
			if not isinstance(self.success_codes, (int, list)):
				raise TypeError('Please pass in a valid success_code, it must be of type int or a list of int')

			if isinstance(self.success_codes, int):
				self.success_codes = [self.success_codes]

			if attempt > self.attempts:
				raise Exception('Function exceeded retries. Check the logs for more information.')

			resp = func(*args, **kwargs)
			if not isinstance(resp, Response):
				raise TypeError('This function does not have a request return, please use this decorator with requests only.')

			logger.debug(f'URL: {resp.url}')
			logger.debug(f'STATUS: {resp.status_code}')
			logger.debug(f'ELAPSED: {resp.elapsed}')
			logger.debug(f'ENCODING: {resp.encoding}')
			logger.debug(f'APPARENT ENCODING: {resp.apparent_encoding}')
			logger.debug(f'HEADERS: {resp.headers}')
			logger.debug(f'COOKIES: {resp.cookies}')
			logger.debug(f'BODY: {resp.content}')

			if (resp.status_code not in self.success_codes) or self.extra_exception(resp):
				logger.error(f"[{attempt}]Attempt: {resp.url} - Failed - [{resp.status_code}]{resp.content}")
				logger.error(f"Wait {self.waiting_time} seconds for the next attempt!!")
				sleep(self.waiting_time)
				inner(*args, attempt=attempt+1, **kwargs)
			else:
				logger.success(f"[{attempt}]Attempt: {func.__name__} - {resp.url}")
				
			return resp
		return inner
