from kaybee_bulma.run_livereload import get_server
from livereload import shell

sphinx = "venv/Scripts/python3.exe venv/scripts/sphinx-build -E -b html doc doc/_build"

server = get_server()
server.watch('doc/**', shell(sphinx),
ignore=lambda s: '_build' in s)
# server.watch('kaybee_bulma/**/*.html', shell(sphinx))
# server.watch('kaybee_bulma/**.py', shell(sphinx))
server.serve(root='doc/_build', live_css=False)