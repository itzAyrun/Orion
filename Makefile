ruff:
	uv run ruff format .
	uv run ruff check .

run:
	uv run -m src
