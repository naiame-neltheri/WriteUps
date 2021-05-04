class WordFilter:
	def __init__(self, words: List[str]):
		self.words = words
		self.history = []

	def search(self, prefix: str, suffix: str) -> int:
		