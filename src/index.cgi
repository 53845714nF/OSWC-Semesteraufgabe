#!/usr/bin/python3
'''
Erster Versuch eines CGI Scriptes
'''

print('Content-Type:text/html')
print()

print('''
<!DOCTYPE html>
<tml lang="de">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titel</title>
  </head>
  <body>
''')

for i in range(1, 10):
    print(f'hallo {i} <br>')

print('''
  </body>
</html>
''')
